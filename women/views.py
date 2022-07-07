from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women, Category
from .serializers import WomenSerializer

#
# class WomenApiView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# class WomenViewSet(ModelViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#     @action(methods=['get'], detail=False)
#     def category(self, request):
#         cats = Category.objects.all()
#         return Response({'cats': [c.name for c in cats]})

class WomenApiList(ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenApiUpdate(RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenApiDestroy(RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# class WomenApiView(APIView):
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid()
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         try:
#             Women.objects.get(pk=pk).delete()
#         except:
#             return Response({"error": "Object does not exist"})
#
#         return Response({"post": "delete post " + str(pk)})

