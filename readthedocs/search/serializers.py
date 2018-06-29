from rest_framework import serializers


class PageSearchSerializer(serializers.Serializer):
    project = serializers.CharField()
    version = serializers.CharField()
    title = serializers.CharField()
    path = serializers.CharField()
    highlight = serializers.SerializerMethodField()

    def get_highlight(self, obj):
        highlight = getattr(obj.meta, 'highlight', None)
        if highlight:
            return highlight.to_dict()
