from rest_framework.serializers import Serializer, CharField, ValidationError


class JWTTokenBlackListSerializer(Serializer):
    """
    Serializer for Tokens
    """
    current_password = CharField(
        style={
            'input_type': 'password',
            'placeholder': 'Password'
        }
    )
    refresh = CharField()

    def validate_current_password(self, data):
        request = self.context['request']
        if not request.user.check_password(data):
            raise ValidationError("Password does not match")
        return data
