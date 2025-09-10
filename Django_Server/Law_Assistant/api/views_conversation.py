from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import JsonResponse

from Law_Assistant.models import Conversation, Message


class ConversationHistoryAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user_id = request.query_params.get('user_id')
        queryset = Conversation.objects.filter(user_id__exact=user_id).order_by('create_date').reverse()
        try:
            return JsonResponse(list(queryset.values()), safe=False)
        except Exception:
            return Response("Error", status=status.HTTP_400_BAD_REQUEST)


class ConversationAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        c_id = request.query_params.get('conversation_id')
        queryset = Message.objects.filter(conversation_id__exact=c_id).order_by('create_date')
        try:
            return JsonResponse(list(queryset.values()), safe=False)
        except Exception:
            return Response("Error", status=status.HTTP_400_BAD_REQUEST)


