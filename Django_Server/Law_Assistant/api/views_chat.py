from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import StreamingHttpResponse
from django.utils import timezone
from django.apps import apps
from Django_Server.config import *
from Law_Assistant.services import RAGService
from pathlib import Path

from Law_Assistant.models import Conversation, Message


class RAGAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        text = request.data.get('text')
        if not text:
            return Response({"error": "No question provided"}, status=400)

        c_id = self.store_message(request.data)

        appcfg = apps.get_app_config('Law_Assistant')
        rag_service = appcfg.rag_service
        if rag_service is None:
            # Lazy init once embeddings exist
            if not Path(VECTORDB_PATH).exists():
                return Response({"error": "Embeddings not found. Please run re-embed first."}, status=503)
            rag_service = RAGService(key_path=KEY_PATH,
                                     law_docs_path=LAW_DOCS_PATH,
                                     model_path=MODEL_PATH,
                                     vectordb_path=VECTORDB_PATH,
                                     truncate_dim=TRUNCATE_DIM,
                                     top_k=TOP_K,
                                     openai_model=OPENAI_MODEL,
                                     device=DEVICE)
            appcfg.rag_service = rag_service
        openai_stream = rag_service.send_message(text)

        response_buffer = []

        def stream_response(response_stream, conversation_id):
            for chunk in response_stream:
                response_buffer.append(chunk.choices[0].delta.content)
                yield chunk.choices[0].delta.content

            full_response = ""
            for chunk in response_buffer:
                if chunk:
                    full_response += chunk
            bot_data = request.data
            bot_data["sender"] = "bot"
            bot_data["text"] = full_response
            bot_data["conversation_id"] = conversation_id
            self.store_message(bot_data)

        response = StreamingHttpResponse(stream_response(openai_stream, c_id), content_type='text/plain')
        response["conversation_id"] = c_id
        return response

    def store_message(self, data):
        conversation_id = data["conversation_id"]
        if conversation_id == "new_conversation":
            new_conversation = Conversation.objects.create(
                user_id=data["user_id"],
                create_date=timezone.now(),
                conversation_name=data["conversation_name"][:100],
            )
            new_conversation.save()
            conversation_id = new_conversation.id
            new_message = Message.objects.create(
                conversation_id=conversation_id,
                text=data["text"],
                sender=data["sender"],
                create_date=timezone.now(),
            )
            new_message.save()
        else:
            new_message = Message.objects.create(
                conversation_id=data["conversation_id"],
                text=data["text"],
                sender=data["sender"],
                create_date=timezone.now(),
            )
            new_message.save()
        return conversation_id


class AdminReEmbedAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request):
        from django.core.management import call_command
        docs = request.data.get('docs', None)
        out = request.data.get('out', None)
        device = request.data.get('device', 'cpu')
        kwargs = {k: v for k, v in [('docs', docs), ('out', out), ('device', device)] if v}
        try:
            call_command('reembed_documents', **kwargs)
            return Response({"message": "Re-embedding started and completed."})
        except Exception as e:
            return Response({"error": str(e)}, status=400)


