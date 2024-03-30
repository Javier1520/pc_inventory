from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Category, Brand, Component
from .serializers import CategorySerializer, BrandSerializer, ComponentSerializer

# Create your views here.
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def category_detail(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serialized_categories = CategorySerializer(categories, many=True)
        return Response(serialized_categories.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        deserialized_category = CategorySerializer(data=request.data)
        deserialized_category.is_valid(raise_exception=True)
        deserialized_category.save()
        return Response(deserialized_category.data, status=status.HTTP_201_CREATED)

class SingleCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]

    # def get_permissions(self):
    #     if self.request.method in ['DELETE', 'PUT', 'PATCH']:
    #         return [IsAuthenticated()]
    #     return super().get_permissions()

class BrandView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticated]

    # def get_permissions(self):
    #     if self.request.method in ['POST']:
    #         return [IsAuthenticated()]
    #     return super().get_permissions()

class SingleBrandView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]

    # def get_permissions(self):
    #     if self.request.method in ['DELETE', 'PUT', 'PATCH']:
    #         return [IsAuthenticated()]
    #     return super().get_permissions()

class ComponentView(generics.ListCreateAPIView):
    # queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Component.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def get_permissions(self):
    #     if self.request.method in ['POST']:
    #         return [IsAuthenticated()]
    #     return super().get_permissions()

class SingleComponentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    permission_classes = [IsAuthenticated]

    # def get_permissions(self):
    #     if self.request.method in ['DELETE', 'PUT', 'PATCH']:
    #         return [IsAuthenticated()]
    #     return super().get_permissions()