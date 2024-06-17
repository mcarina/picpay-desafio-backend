from rest_framework import generics
from rest_framework.generics import get_object_or_404
from .models import *
from .serializer import *

class TipoUsuarioListCreate(generics.ListCreateAPIView):
    queryset = TipoUsuario.objects.all()
    serializer_class = TipoUsuarioSerializer

class TipoUsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoUsuario.objects.all()
    serializer_class = TipoUsuarioSerializer

#============================================

class AutorizacaoListCreate(generics.ListCreateAPIView):
    queryset = Autorizacao.objects.all()
    serializer_class = AutorizacaoSerializer

class AutorizacaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autorizacao.objects.all()
    serializer_class = AutorizacaoSerializer

#============================================

class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

#============================================

class UsuarioAutorizacaoListCreate(generics.ListCreateAPIView):
    queryset = UsuarioAutorizacao.objects.all()
    serializer_class = UsuarioAutorizacaoSerializer

class UsuarioAutorizacaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsuarioAutorizacao.objects.all()
    serializer_class = UsuarioAutorizacaoSerializer

    def get_object(self):
        if self.kwargs.get('usuario_pk'):
            return get_object_or_404(self.get_queryset(), curso_id = self.kwargs.get('usuario_pk'), pk = self.kwargs.get('usuario_pk'))
        return get_object_or_404(self.get_queryset(), pk = self.kwargs.get('usuario_pk'))