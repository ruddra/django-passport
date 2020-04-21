from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import JWTTokenBlackListSerializer


class JWTTokenBlackList(generics.GenericAPIView):
    """
    To blacklist own's refresh token. Works as logout as well.
    User who has generated the refresh token can blacklist himself.
    Superuser can use this API as well, also can do that from adminsite.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = JWTTokenBlackListSerializer

    def get_refresh_token(self, data):
        try:
            token = data['refresh']
            return str.encode(token)
        except (KeyError, IndexError):
            return b''

    def blacklist_token(self, request, token):
        if request.user.is_superuser or token.payload.get('user_id') == request.user.pk:
            token.blacklist()
        else:
            raise Exception('Invalid token')

    def post(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            base64_encoded_token_string = self.get_refresh_token(serializer.data)
            try:
                token = RefreshToken(base64_encoded_token_string)
                self.blacklist_token(request, token)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except:
                return Response(
                    {
                        'detail': "Invalid refresh token",
                        "code": "token_not_valid"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
