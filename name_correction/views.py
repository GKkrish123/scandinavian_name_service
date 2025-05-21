from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.name_correction_service import NameCorrectionService

class NameCorrectionAPIView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = NameCorrectionService()

    def post(self, request, format=None):
        name = request.data.get('name')
        country = request.data.get('country') or ""
        if not name or not country:
            return Response({'error': 'Both name and country are required.'}, status=status.HTTP_400_BAD_REQUEST)
        if country.lower() not in ['sweden', 'norway', 'denmark', 'finland', 'iceland']:
            return Response({'error': 'Country must be one of sweden, norway, denmark, finland, iceland'}, status=status.HTTP_400_BAD_REQUEST)
        suggestions = self.service.get_name_suggestions(name, country)
        return Response({
            'original_name': name,
            'country': country,
            'suggestions': suggestions
        })
