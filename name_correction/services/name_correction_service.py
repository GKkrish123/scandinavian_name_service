from ..models import NameVerification
from .transliteration_service import TransliterationService
from .frequency_service import FrequencyService
from .ai_service import AIService

class NameCorrectionService:
    def __init__(self):
        self.freq_service = FrequencyService()
        self.translit_service = TransliterationService()
        self.ai_service = AIService(self.freq_service)

    def get_name_suggestions(self, name, country, max_suggestions=5):
        verified_qs = NameVerification.objects.filter(
            input_name=name,
            country=country,
            is_correct=True
        ).order_by('-verified_at')
        verified_suggestions = [v.suggested_name for v in verified_qs]
        if verified_suggestions:
            ranked = self.freq_service.get_most_frequent_names(
                verified_suggestions, country, limit=max_suggestions
            )
            return ranked

        suggestions = set()
        suggestions.update(self.translit_service.generate_transliteration_suggestions(name, country))
        suggestions.update(self.ai_service.generate_ai_suggestions(name, country))
        ranked = self.freq_service.get_most_frequent_names(list(suggestions), country, limit=max_suggestions)
        return ranked
