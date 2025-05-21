class FrequencyService:
    def __init__(self):
        self.name_frequencies = {
            'sweden': {'Åke': 100, 'Gösta': 80, 'Nöik': 20, 'Nöke': 50},
            'norway': {'Håkon': 90, 'Søren': 70, 'Nøik': 15, 'Nøke': 8},
            'denmark': {'Søren': 95, 'Møse': 10, 'Æsa': 5},
            'finland': {'Åke': 60, 'Gösta': 30},
            'iceland': {'Óskar': 50, 'Þord': 20, 'Æsa': 10},
        }

    def get_most_frequent_names(self, names, country, limit=5):
        freq = self.name_frequencies.get(country.lower(), {})
        scored = [(n, freq.get(n, 0)) for n in names]
        scored.sort(key=lambda x: x[1], reverse=True)
        return [n for n, s in scored[:limit] if s > 0]

    def get_all_names(self, country):
        return list(self.name_frequencies.get(country.lower(), {}).keys())
