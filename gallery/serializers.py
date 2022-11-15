from rest_framework import serializers
from .models import GDSC_Gallery
class GallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = GDSC_Gallery
        fields = ['thumbnail','caption','description']