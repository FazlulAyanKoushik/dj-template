from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import User
from .serializers import UserSerializer, UserRegistrationSerializer, LoginSerializer
from core.utils.message import Message


class RegisterView(generics.CreateAPIView):
    """
    User registration endpoint.
    """
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer

    @swagger_auto_schema(
        operation_description="Register a new user",
        responses={
            201: openapi.Response('User created successfully', UserSerializer),
            400: 'Bad Request'
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            message = Message(resource="User")
            return Response({
                'message': message.created_success(),
                'data': UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': Message(resource="User").created_failed(),
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='post',
    operation_description="Login endpoint",
    request_body=LoginSerializer,
    responses={
        200: openapi.Response('Login successful'),
        400: 'Bad Request',
        401: 'Unauthorized'
    }
)
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """
    User login endpoint.
    """
    serializer = LoginSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)

        return Response({
            'message': Message.login_success(),
            'data': {
                'user': UserSerializer(user).data,
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            }
        }, status=status.HTTP_200_OK)

    return Response({
        'message': Message.login_failed(),
        'errors': serializer.errors
    }, status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(
    method='post',
    operation_description="Logout endpoint",
    responses={
        200: openapi.Response('Logout successful'),
        401: 'Unauthorized'
    }
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    """
    User logout endpoint.
    """
    try:
        refresh_token = request.data.get('refresh_token')
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()
        return Response({
            'message': Message.logout()
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'message': Message.logout(),
            'error': str(e)
        }, status=status.HTTP_200_OK)
