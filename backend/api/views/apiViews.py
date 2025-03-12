from rest_framework import viewsets , status
from django.contrib.auth import authenticate,login
from api.models import *
from api.serializers import *
from rest_framework.views import APIView
from rest_framework.views import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class Login(APIView):
    def post(self,request):
        nome = request.data.get("nome")
        senha = request.data.get("senha")

        usuario = authenticate(username = nome,pasword=senha)

        if (usuario):
            login(request, usuario)
            return Response({"status": status.HTTP_200_OK })
        
        else:
            return Response({"mensagem":"Usuario não encontrado", "status": status.HTTP_401_UNAUTHORIZED })
        
        


