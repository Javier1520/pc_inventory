from django.urls import path
from . import views

urlpatterns = [
    path('categories', views.category_detail, name='categories'),
    path('categories/<slug:slug>', views.SingleCategoryView.as_view(), name='single_category'),
    path('brands', views.BrandView.as_view(), name='brands'),
    path('brands/<slug:slug>', views.SingleBrandView.as_view(), name='single_brand'),
    path('components', views.ComponentView.as_view(), name='components'),
    path('components/<int:pk>', views.SingleComponentView.as_view(), name='single_component'),
]