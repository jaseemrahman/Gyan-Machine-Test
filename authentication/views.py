from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


        
class LoginView(APIView):
    def post(self, request):
        print("req", request.POST)
        username = request.POST['username']
        password = request.POST['password']
        existing_user = User.objects.filter(username=username).first()
        print("existing_user", existing_user)
        
        if existing_user:
            user = authenticate(request, username=username, password=password)
            if user:
                token = Token.objects.get_or_create(user=user)
                serializer = UserSerializer(user)
                response_data = {
                    'token': token.key,
                    'userid': serializer.data['id'],
                    'username': serializer.data['username']
                }
                return Response(response_data)
            else:
                return Response({'error': 'Invalid credentials'})
        else:
            user = User.objects.create(username=username)
            user.set_password(password)
            token = Token.objects.get_or_create(user=user)
            serializer = UserSerializer(user)
            response_data = {
                'token': token.key,
                'userid': serializer.data['id'],
                'username': serializer.data['username']
            }
            return Response(response_data)