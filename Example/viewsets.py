from rest_framework.viewsets import ModelViewSet
from Example.models import Colors, ColorTemplate
from Example import serializers as ser
from rest_framework.response import Response


class ColorPalletViewsets(ModelViewSet):
    queryset = ColorTemplate.objects.all().order_by("-id")
    serializer_class = ser.ColorTemplateViewSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.serializer_class(self.queryset, many=True).data
        for item in queryset:
            color_item = item.get('color', [])
            if len(color_item) > 0:
                item['color'] = [Colors.objects.filter(id=color_id).first().color_code
                                 for color_id in item.get('color')]
            else:
                item['color'] = []

        return Response(queryset)

    def create(self, request, *args, **kwargs):
        serialzer = ser.ColorPalletValidationSerializer(data=request.data)
        if not serialzer.is_valid():
            return Response(serialzer.errors)

        color_template = ColorTemplate.objects.create(
            template_name=serialzer.validated_data.get('template_name'))
        for item in serialzer.validated_data.get('colors'):
            color = Colors.objects.create(color_code=item)
            color_template.color.add(color)
        return Response(color_template.id)
