from rest_framework import viewsets
from django.shortcuts import render
from django.http import HttpResponse, request
from .models import FileUpload
from .serializers import FileUploadSerializer
from rest_framework.renderers import JSONRenderer
from .serializers import UserSerializer,SignupSerializer
from rest_framework import response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


def login(request):
    return render(request,"loginPanel.html")

def signup(request):
    return render(request,"signup.html")


class FileViewSet(viewsets.ModelViewSet):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer


class SignupAPI(APIView):
     def post(self, request):
        try:
            data = request.data
            # print(data)
            serializer = SignupSerializer(data = data)
            # print(serializer,serializer.is_valid())
            if serializer.is_valid():
                serializer.save()
                return response.Response(
                    {
                        'status':200,
                        'message': 'User Registration Successfully! verify email',
                        'data':serializer.data
                    }
                )
            return response.Response({
                'status' : 400,
                'message': 'something went wrong!',
                'data': serializer.error
            })
        except Exception as e:
            print(e)


class LoginAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            email = data.get('Email')
            password = data.get('Password')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response(
                    {
                        'status': 200,
                        'message': 'Login Successful',
                        'token': token.key,
                        'user_id': user.pk,
                        'Email': user.email
                    }
                )
            else:
                # Authentication failed
                return Response(
                    {
                        'status': 401,
                        'message': 'Invalid credentials'
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )

        except Exception as e:
            print(e)
            return Response(
                {
                    'status': 500,
                    'message': 'Internal Server Error'
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

