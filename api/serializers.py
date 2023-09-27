from rest_framework import serializers
from rest_framework.response import Response

from .models import Slide, TextBlock, Photo, Contact, Header, Footer


class TextBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextBlock
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class SlideSerializer(serializers.ModelSerializer):
    text_blocks = TextBlockSerializer(many=True, read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Slide
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class LayoutDataSerializer(serializers.Serializer):
    header = serializers.SerializerMethodField()
    footer = serializers.SerializerMethodField()

    def get_header(self):
        header = Header.objects.first()
        icons_data = []
        for icon in header.icons.all():
            icons_data.append({
                'image_url': icon.image.url,
                'link': icon.link,
            })
        return {
            'company_name': header.company_name,
            'email': header.email,
            'phone_number': header.phone_number,
            'icons': icons_data,
        }

    def get_footer(self):
        footer = Footer.objects.first()
        if footer:
            icons_data = []
            for icon in footer.icons.all():
                icons_data.append({
                    'image_url': icon.image.url,
                    'link': icon.link,
                })
            return {
                'company_name': footer.company_name,
                'user_agreement': footer.user_agreement.url if footer.user_agreement else None,
                'company_description': footer.company_description,
                'icons': icons_data,
            }

