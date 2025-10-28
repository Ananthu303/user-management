from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser
from .serializers import (
    ChangePasswordSerializer,
    LoginSerializer,
    LogoutSerializer,
    RegisterSerializer,
    TokenRefreshSerializer,
    TokenSerializer,
    UserDetailSerializer,
)
from .services import AuthUtil


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter(user_type=CustomUser.UserType.USER).order_by("id")
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def get_instance(self):
        return self.request.user

    def get_serializer_class(self):
        if self.action == "register":
            return RegisterSerializer
        elif self.action == "login":
            return LoginSerializer
        elif self.action == "logout":
            return LogoutSerializer
        elif self.action == "me":
            return UserDetailSerializer
        elif self.action == "change_password":
            return ChangePasswordSerializer
        elif self.action == "refresh_token":
            return TokenRefreshSerializer

        return super().get_serializer_class()

    @action(detail=False, methods=["post"], url_path="register")
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            self.get_serializer(instance=user).data,
            status=status.HTTP_201_CREATED,
        )

    @action(detail=False, methods=["post"], url_path="login")
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token_pair = AuthUtil.generate_token_pair(user)
        token_serializer = TokenSerializer(token_pair)
        return Response(
            {"message": "Login successful", **token_serializer.data},
            status=status.HTTP_200_OK,
        )

    @action(detail=False, methods=["post"])
    def logout(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        refresh_token = serializer.validated_data["refresh"]
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"message": "Logout successful."},
                status=status.HTTP_200_OK,
            )
        except Exception:
            return Response(
                {"error": "Invalid or expired token."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @action(
        methods=["get", "put", "patch", "delete"],
        detail=False,
        url_path="me",
        permission_classes=[IsAuthenticated],
    )
    def me(self, request, *args, **kwargs):
        self.get_object = self.get_instance
        if request.method == "GET":
            return self.retrieve(request, *args, **kwargs)
        elif request.method == "PUT":
            return self.update(request, *args, **kwargs)
        elif request.method == "PATCH":
            return self.partial_update(request, *args, **kwargs)
        elif request.method == "DELETE":
            return self.destroy(request, *args, **kwargs)

    @action(
        detail=False, methods=["put", "patch"], permission_classes=[IsAuthenticated]
    )
    def change_password(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        new_password = serializer.validated_data["new_password_1"]
        user.set_password(new_password)
        user.save()
        return Response(
            {"message": "Password updated successfully."},
            status=status.HTTP_200_OK,
        )

    @action(detail=False, methods=["post"], url_path="token/refresh")
    def refresh_token(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            {"access": serializer.validated_data["access"]},
            status=status.HTTP_200_OK,
        )
