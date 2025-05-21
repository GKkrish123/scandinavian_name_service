import requests
import json

API_URL = "http://localhost:8000/api/suggest/"

test_cases = [
    {
        "payload": {"name": "Ake", "country": "Sweden"},
        "expected": {"suggestions": ["Åke"]}
    },
    {
        "payload": {"name": "Gosta", "country": "Sweden"},
        "expected": {"suggestions": ["Gösta"]}
    },
    {
        "payload": {"name": "Naeik", "country": "Sweden"},
        "expected": {"suggestions": ["Nöik", "Nöke"]}
    },
    {
        "payload": {"name": "Soeren", "country": "Denmark"},
        "expected": {"suggestions": ["Søren"]}
    },
    {
        "payload": {"name": "Haakon", "country": "Norway"},
        "expected": {"suggestions": ["Håkon"]}
    },
    {
        "payload": {"name": "Oskar", "country": "Iceland"},
        "expected": {"suggestions": ["Óskar"]}
    },
    {
        "payload": {"name": "Tord", "country": "Iceland"},
        "expected": {"suggestions": ["Þord"]}
    },
    {
        "payload": {"name": "Aesa", "country": "Iceland"},
        "expected": {"suggestions": ["Æsa"]}
    },
    {
        "payload": {"name": "Moose", "country": "Denmark"},
        "expected": {"suggestions": ["Møse"]}
    },
    {
        "payload": {"name": "Jukka", "country": "Finland"},
        "expected": {"suggestions": []}
    },
    {
        "payload": {"name": "Ake", "country": "Germany"},
        "expected": {"error": "Country must be one of sweden, norway, denmark, finland, iceland"}
    },
    {
        "payload": {"country": "Sweden"},
        "expected": {"error": "Both name and country are required."}
    },
    {
        "payload": {"name": "Ake"},
        "expected": {"error": "Both name and country are required."}
    },
    {
        "payload": {"name": "Gosta", "country": "Finland"},
        "expected": {"suggestions": ["Gösta"]}
    },
]

def compare_suggestions(expected, actual):
    if "suggestions" in expected:
        return set(expected["suggestions"]) == set(actual.get("suggestions", []))
    else:
        return expected.get("error") == actual.get("error")

def main():
    for idx, case in enumerate(test_cases, 1):
        print(f"\nTest Case {idx}:")
        print("Payload:", case["payload"])
        try:
            resp = requests.post(API_URL, json=case["payload"], timeout=10)
            resp_json = resp.json()
            print("Response:", json.dumps(resp_json, ensure_ascii=False))
            if compare_suggestions(case["expected"], resp_json):
                print("✅ Test Passed")
            else:
                print("❌ Test Failed")
                print("Expected:", case["expected"])
        except Exception as e:
            print("❌ Exception occurred:", e)

if __name__ == "__main__":
    main()
