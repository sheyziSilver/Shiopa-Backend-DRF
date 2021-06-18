from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.product.models import Category, Product
from apps.product.serializers import CategorySerializer


class CategoryList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
