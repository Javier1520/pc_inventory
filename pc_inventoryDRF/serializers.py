from rest_framework import serializers
from .models import Category, Brand, Component
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
import bleach

class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(
        validators = [UniqueValidator(queryset=Category.objects.all())],
    )

    def validate(self, attrs):
        attrs['title'] = bleach.clean(attrs['title'])
        return super().validate(attrs)

    class Meta:
        model = Category
        fields = ('id', 'slug', 'title')

class BrandSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(
        validators = [UniqueValidator(queryset=Brand.objects.all())],
    )

    def validate(self, attrs):
        attrs['title'] = bleach.clean(attrs['title'])
        return super().validate(attrs)

    class Meta:
        model = Brand
        fields = ('id', 'slug', 'title')

class ComponentSerializer(serializers.ModelSerializer):
    date_creation = serializers.DateTimeField(format="%d/%m/%Y - %H:%M", read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    brand = BrandSerializer(read_only=True)
    brand_id = serializers.IntegerField(write_only=True)
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    # user = serializers.PrimaryKeyRelatedField(
    #     read_only=True,
    #     # queryset=User.objects.all(),
    #     default=serializers.CurrentUserDefault(),
    # )

    def validate(self, attrs):
        attrs['name'] = bleach.clean(attrs['name'])

        if attrs['price'] <= 0:
            raise serializers.ValidationError('Price must be greater than 0')
        if attrs['stock'] <= 0:
            raise serializers.ValidationError('Stock must be greater than 0')
        return super().validate(attrs)

    class Meta:
        model = Component
        fields = ('id','price','stock','name','date_creation','category','category_id','brand','brand_id','user')
        validators = [UniqueTogetherValidator(
                        queryset=Component.objects.all(),
                        fields=('user','name', 'brand_id'),
                    )
        ]