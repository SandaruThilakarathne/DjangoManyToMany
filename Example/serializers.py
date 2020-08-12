from rest_framework import serializers
from .models import Colors, ColorTemplate


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        models = Colors
        fields = '__all__'


class ColorTemplateViewSerializer(serializers.ModelSerializer):
    color = serializers.PrimaryKeyRelatedField(queryset=Colors.objects.all(), many=True)

    class Meta:
        model = ColorTemplate
        fields = ['id', 'template_name', 'color']


class ColorPalletValidationSerializer(serializers.Serializer):
    template_name = serializers.CharField(required=True)
    colors = serializers.ListField(required=True)

    def validate(self, attrs):
        colors = attrs.get('colors')
        if len(colors) == 0:
            raise Exception("At least on color is required")
        return attrs
