from rest_framework.serializers import ModelSerializer
from .models import Word
from cloudinary.templatetags import cloudinary

class WordSerializer(ModelSerializer):
    class Meta:
        model = Word
        fields = ["word", "description", "url", "image", "category"]
