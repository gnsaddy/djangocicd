from django.contrib import auth
from django.contrib.auth.models import update_last_login
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser, StudentModel, FacultyModel
from rest_framework import serializers, status
from django.contrib.auth import password_validation
from rest_framework.decorators import authentication_classes, permission_classes


class StudentSerializers(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = StudentModel
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

        fields = ('id', 'sid', 'first_name', 'last_name', 'email', 'password', 'student_phone',
                  'picture', 'gender', 'student_grade', 'student_school', 'student_college', 'student_city',
                  'student_state', 'student_country', 'student_parent_name', 'student_parent_email',
                  'student_parent_phone', 'created_at', 'student_date_joined', 'student'
                  )


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['email'] = user.email

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        data['email'] = self.user.email
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class LogoutSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': 'Token is expired or invalid'
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')
