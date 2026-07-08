from rest_framework import serializers
from .models import ShortURL


class ShortURLSerializer(serializers.ModelSerializer):
    shortCode = serializers.CharField(source="short_code", read_only=True)
    createdAt = serializers.DateTimeField(source="created_at", read_only=True)
    updatedAt = serializers.DateTimeField(source="updated_at", read_only=True)

    class Meta:
        model = ShortURL
        fields = [
            "id",
            "url",
            "shortCode",
            "createdAt",
            "updatedAt",
        ]


class ShortURLStatsSerializer(ShortURLSerializer):
    accessCount = serializers.IntegerField(source="access_count", read_only=True)

    class Meta(ShortURLSerializer.Meta):
        fields = ShortURLSerializer.Meta.fields + ["accessCount"]
