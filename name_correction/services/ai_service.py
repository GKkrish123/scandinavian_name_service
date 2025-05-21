from fuzzywuzzy import fuzz, process
import fasttext
import os

class AIService:
    def __init__(self, frequency_service):
        self.frequency_service = frequency_service
        self.model_path = os.path.join(os.path.dirname(__file__), 'cc_names.bin')
        if not os.path.exists(self.model_path):
            self._train_minimal_model()
        self.ft_model = fasttext.load_model(self.model_path)

    def _train_minimal_model(self):
        names = set()
        for country in self.frequency_service.name_frequencies:
            names.update(self.frequency_service.name_frequencies[country].keys())
        with open(self.model_path + '.txt', 'w', encoding='utf-8') as f:
            for n in names:
                f.write(n + '\n')
        fasttext.train_unsupervised(self.model_path + '.txt', model='skipgram', minn=1, maxn=3, dim=25).save_model(self.model_path)

    def fuzzywuzzy_suggestions(self, name, country, threshold=70):
        candidates = self.frequency_service.get_all_names(country)
        results = process.extract(name, candidates, scorer=fuzz.partial_token_sort_ratio, limit=5)
        return [n for n, score in results if score >= threshold]
    
    def fasttext_suggestions(self, name, country, threshold=0.7):
        candidates = self.frequency_service.get_all_names(country)
        name_vec = self.ft_model.get_word_vector(name)
        scored = []
        for cand in candidates:
            cand_vec = self.ft_model.get_word_vector(cand)
            sim = self._cosine_similarity(name_vec, cand_vec)
            scored.append((cand, sim))
        # Sort and filter by threshold
        scored.sort(key=lambda x: x[1], reverse=True)
        return [n for n, sim in scored if sim >= threshold]

    def _cosine_similarity(self, v1, v2):
        dot = sum(a*b for a, b in zip(v1, v2))
        norm1 = sum(a*a for a in v1) ** 0.5
        norm2 = sum(a*a for a in v2) ** 0.5
        return dot / (norm1 * norm2 + 1e-8)

    def generate_ai_suggestions(self, name, country):
        fuzzy = self.fuzzywuzzy_suggestions(name, country)
        ft = self.fasttext_suggestions(name, country)
        return list(set(fuzzy + ft))
