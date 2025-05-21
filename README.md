# 🇸🇪 Scandinavian Name Correction Service

**Fix Scandinavian names with Hybrid AI + Frequency + Transliteration Lookup.**  
This service corrects and suggests the most likely authentic names for leads from Sweden, Norway, Denmark, Finland and Iceland — even when the input is poorly transliterated or misspelled.

---

## Setup

**1. Create a virtual environment**

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

text

**2. Install dependencies**

pip install -r requirements.txt

text

**3. Run migrations**

python manage.py migrate

text

**4. Start the server**

python manage.py runserver

text

**Or, run with Docker:**

docker build -t scandi-name-corrector .
docker run -p 8000:8000 scandi-name-corrector

text

---

## Test the API

curl -X POST http://localhost:8000/api/suggest/
-H 'Content-Type: application/json'
-d '{"name": "Naeik", "country": "Sweden"}'

text

**Example response:**

{
"original_name": "Naeik",
"country": "Sweden",
"suggestions": ["Nöik", "Nöke"]
}

text

---

## Assumptions

- Frequency data for only common names is available for each Scandinavian country.
- Transliteration rules are based on common patterns (e.g., `ae` → `ä`, `ö`, `æ`).
- The service uses a hybrid of transliteration, fuzzy matching and fastText for better results.
- For demo, this uses a minimal dataset for speed and clarity.

---

## Room for Improvement

- **Expand name frequency lists**: Use official national registries for higher accuracy.
- **Improve transliteration rules**: Add more context aware and phonetic mappings.
- **Better ML models**: Train fastText or similar embeddings on a much larger datasets of real names.
- **Multilingual support**: Add support for more countries or regions.
- **User feedback loop**: Improving model tuning with users' feedback loops.

---

## Production Considerations

- **Security**: Add authentication and rate limiting for public APIs.
- **Scalability**: Using production ready database and caching frequent queries.
- **Monitoring**: Log requests and monitor performance.
- **Testing**: Add automated and integration tests for multiple query scenarios.

---