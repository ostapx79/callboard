from rest_framework import serializers

from backend.gallery.serializers import GallerySer
from .models import *


class CategorySer(serializers.ModelSerializer):
    """Для вывода категрий"""

    class Meta:
        model = Category
        fields = ("name", )


class FilterAdvertSer(serializers.ModelSerializer):
    """Для вывода фильтров"""

    class Meta:
        model = FilterAdvert
        fields = ("name", )


class AdvertListSer(serializers.ModelSerializer):
    """Для вывода списока объявлений"""

    category = CategorySer()
    filters = FilterAdvertSer()
    images = GallerySer(read_only=True)

    class Meta:
        model = Advert
        fields = (
            "id",
            "category",
            "filters",
            "subject",
            "images",
            "price",
            "created",
            "slug"
        )


class AdvertDetailSer(serializers.ModelSerializer):
    """Для вывода полного объявления"""

    category = CategorySer()
    filters = FilterAdvertSer()
    images = GallerySer(read_only=True)

    class Meta:
        model = Advert
        fields = (
            "category",
            "filters",
            "subject",
            "description",
            "images",
            "file",
            "price",
            "created",
            "user"
        )


class AdvertCreateSer(serializers.ModelSerializer):
    """Добавление объявления"""

    class Meta:
        model = Advert
        fields = (
            "category",
            "filters",
            "date",
            "subject",
            "description",
            "price"
        )

    def create(self, request):
        request["user"] = self.context['request'].user
        advert = Advert.objects.create(**request)
        return advert
