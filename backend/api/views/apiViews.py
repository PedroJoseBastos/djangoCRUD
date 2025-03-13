from rest_framework import viewsets , status
from django.contrib.auth import authenticate,login
from api.models import *
from api.serializers import *
from rest_framework.views import APIView
from rest_framework.views import Response
from django.shortcuts import get_object_or_404
# class UserViewSet(viewsets.ModelViewSet):
    # queryset = CustomUser.objects.all()
    # serializer_class = UserSerializer
class User(APIView):
    def get(self, request,id=None):
        
        if id:
            usuarios = get_object_or_404(CustomUser, id=id)
            serializers = UserSerializer(usuarios)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        
        usuarios = CustomUser.objects.all()
        serializers = UserSerializer(usuarios, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)




class Login(APIView):
    def post(self,request):
        nome = request.data.get("nome")
        senha = request.data.get("senha")

        usuario = authenticate(username = nome, password = senha)

        if (usuario):
            login(request, usuario)
            return Response({"status": status.HTTP_200_OK })
        
        else:
            return Response({"mensagem":"Usuario não encontrado", "status": status.HTTP_401_UNAUTHORIZED })
        
        


