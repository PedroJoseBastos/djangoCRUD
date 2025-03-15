from rest_framework import viewsets , status
from django.contrib.auth import authenticate,login
from api.models import *
from api.serializers import *
from rest_framework.views import APIView
from rest_framework.views import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password


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
    
    def post(self, request):
        nome = request.data.get("nome")
        senha = request.data.get("senha")   
        
        if not nome or not senha:
            return Response({"status": status.HTTP_400_BAD_REQUEST})
        
        usuario = CustomUser.objects.create(
            username = nome,
            password=make_password(senha),
            is_active = True,
            is_aluno = True
        )

        return Response({"messagem":"Usuario criado com sucesso", "id": usuario.id}, status=status.HTTP_201_CREATED)
    
    def put(self, request,id):
        usuario = get_object_or_404(CustomUser, pk=id)
        serializer = UserSerializer(instance=usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)    
    
    def delete(self, request,id=None):
        usuario = get_object_or_404(CustomUser, id=id)
        if usuario:
            usuario.delete()
            return Response({"status": status.HTTP_200_OK})
        else:
            return Response({"status": status.HTTP_404_NOT_FOUND})

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
        
        


