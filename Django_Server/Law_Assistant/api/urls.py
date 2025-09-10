from django.urls import path
from .views_auth import LoginAPIView, SignUpAPIView, TokenRefreshAPIView, LogoutAPIView
from .views_chat import RAGAPIView, AdminReEmbedAPIView
from .views_conversation import ConversationHistoryAPIView, ConversationAPIView

urlpatterns = [
    path('chat/',  RAGAPIView.as_view(), name='rag-api'),
    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('history/', ConversationHistoryAPIView.as_view(), name='history'),
    path('conversation/', ConversationAPIView.as_view(), name='conversation'),
    path('admin/reembed/', AdminReEmbedAPIView.as_view(), name='admin-reembed'),
    path('api/token/refresh/', TokenRefreshAPIView.as_view(), name='token-refresh'),
    path('api/logout/', LogoutAPIView.as_view(), name='logout'),
]


