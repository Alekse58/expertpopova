from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Slide, Contact
from .serializers import SlideSerializer, ContactSerializer, LayoutDataSerializer


class LayoutDataView(APIView):
    def get(self, request):
        serializer = LayoutDataSerializer(context={'request': request})
        header_data = serializer.get_header()  # Вызываем метод get_header без аргументов
        footer_data = serializer.get_footer()
        data = {
            'header': header_data,
            'footer': footer_data,
        }
        return Response(data, status=status.HTTP_200_OK)


class AllSlides(APIView):
    def get(self, request, format=None):
        slides = Slide.objects.all()
        serializer = SlideSerializer(slides, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ContactRetrieveView(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
