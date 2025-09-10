from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from Law_Assistant.components.signup_form import SignUpForm
from Law_Assistant.models import User


class SignUpAPIView(APIView):
    def post(self, request):
        form = SignUpForm(request.data)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            gender = form.cleaned_data['gender']
            date_of_birth = form.cleaned_data['date_of_birth']
            address = form.cleaned_data['address']
            phone_number = form.cleaned_data['phone_number']

            user = User(
                email=email,
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                date_of_birth=date_of_birth,
                address=address,
                phone_number=phone_number,
            )
            user.set_password(password)
            user.save()

            data = {"message": "Sign up successfully"}
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {"message": "Error occurred", "error": form.errors}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, username=email, password=password)
        
        if user:
            refresh = TokenObtainPairSerializer.get_token(user)
            payload = {
                'message': f"Log in successfully - Welcome {user.email}",
                'access_token': str(refresh.access_token),
                'user_id': user.id
            }
            
            response = Response(payload, status=status.HTTP_200_OK)

            response.set_cookie(
                'refresh_token',
                str(refresh),
                max_age=settings.SIMPLE_JWT.get('REFRESH_TOKEN_LIFETIME').total_seconds(),
                httponly=True,
                secure=True,  
                samesite='Strict' 
            )
            
            return response
            
        return Response(
            {'message': 'Log in unsuccessfully - email or password is incorrect'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

class TokenRefreshAPIView(APIView):
    """
    Refresh access token using HTTP-only refresh cookie
    """
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        
        if not refresh_token:
            return Response(
                {'error': 'Refresh token not found'}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)
            
            return Response({
                'access_token': access_token,
                'message': 'Token refreshed successfully'
            })
        except TokenError:
            return Response(
                {'error': 'Invalid refresh token'}, 
                status=status.HTTP_401_UNAUTHORIZED
            )

class LogoutAPIView(APIView):
    """
    Logout user and clear refresh cookie
    """
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        
        if refresh_token:
            try:
                # Blacklist the refresh token
                refresh = RefreshToken(refresh_token)
                refresh.blacklist()
            except TokenError:
                pass  # Token already invalid
        
        response = Response({
            'message': 'Logged out successfully'
        }, status=status.HTTP_200_OK)
        
        # Clear the refresh token cookie
        response.delete_cookie('refresh_token')
        
        return response

# Don't forget to add these to your urls.py:
# path('api/token/refresh/', TokenRefreshAPIView.as_view(), name='token_refresh'),
# path('api/logout/', LogoutAPIView.as_view(), name='logout'),