from .frequency_service import FrequencyService
from collections import defaultdict

class TransliterationService:
    def __init__(self):
        self.frequency_service = FrequencyService()
        self.translit_map = [
            ('ae', ['æ', 'ä', 'ö']),
            ('oe', ['ø', 'ö']),
            ('aa', ['å']),
            ('AE', ['Æ']),
            ('OE', ['Ø']),
            ('AA', ['Å']),
            ('a', ['å', 'ä']),
            ('o', ['ö', 'ø']),
            ('th', ['þ']),
            ('d', ['ð']),
            ('A', ['Å']),
            ('O', ['Ö']),
            ('oo', ['ø']),
            ('ik', ['ke']),
            ('ke', ['ik']),
        ]
        self.variant_to_canonicals = defaultdict(set)
        self._build_variant_map()

    def _build_variant_map(self):
        all_countries = self.frequency_service.name_frequencies.keys()
        for country in all_countries:
            for name in self.frequency_service.get_all_names(country):
                variants = self.generate_all_transliteration_variants(name)
                for variant in variants:
                    self.variant_to_canonicals[variant].add(name)

    def generate_all_transliteration_variants(self, name):
        variants = set([name])
        for ascii_seq, scandi_chars in self.translit_map:
            new_variants = set()
            for v in variants:
                if ascii_seq in v:
                    for scandi_char in scandi_chars:
                        new_variants.add(v.replace(ascii_seq, scandi_char))
            variants.update(new_variants)
        return variants

    def generate_transliteration_suggestions(self, name, country=None):
        variants = self.generate_all_transliteration_variants(name)
        matches = set()
        for v in variants:
            matches.update(self.variant_to_canonicals.get(v, []))
        if country:
            country_names = set(self.frequency_service.get_all_names(country))
            matches = matches & country_names
        return list(matches)
