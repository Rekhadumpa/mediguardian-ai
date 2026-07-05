import json
import os

DATA_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "diseases.json",
)


def load_diseases():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def search_by_symptoms(user_symptoms):
    diseases = load_diseases()

    # Convert input into individual words
    words = user_symptoms.lower().replace(",", " ").split()

    matches = []

    for disease in diseases:
        score = 0

        for symptom in disease["symptoms"]:

            symptom_words = symptom.lower().split()

            # Every word of the symptom should be present
            if all(word in words for word in symptom_words):
                score += 1

        if score > 0:
            matches.append((score, disease))

    # Highest score first
    matches.sort(key=lambda x: x[0], reverse=True)

    # Return only top 3 diseases
    return [disease for score, disease in matches[:3]]

def get_disease_info(name):
    diseases = load_diseases()

    for disease in diseases:
        if disease["name"].lower() == name.lower():
            return disease

    return None