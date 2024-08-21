from django.contrib.auth.models import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator






User = get_user_model

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    password_1 =serializers.CharField(required=True)
    password_2 = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = (
                  'email','username', 'password_1', 
                  'password_2','first_name','last_name'
                  )
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},

        }
    def validate(self, attrs):
        if attrs['password_1'] is None == attrs['password_2']:
            raise serializers.ValidationError({
                'password': 'Password did not match.'
            })
        return attrs
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name',''),
            last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password_1'])
        user.save()

    
    