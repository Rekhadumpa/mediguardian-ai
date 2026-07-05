from google.adk.agents import Agent
from google.adk.models import Gemini
from google.genai import types
from .app_utils.disease_loader import search_by_symptoms
def find_possible_diseases(user_input: str) -> str:
    matches = search_by_symptoms(user_input)

    if not matches:
        return (
            "No matching disease was found in the knowledge base.\n"
            "Please consult a healthcare professional."
        )

    response = "Possible Conditions Based on Your Symptoms:\n\n"

    # Top possible diseases
    for disease in matches:
        response += f"• {disease['name']}\n"

    # Best matching disease
    best = matches[0]

    response += "\n\n----------------------------------"
    response += f"\nMost Likely Match: {best['name']}"

    # Foods
    response += "\n\n🥗 Recommended Foods:\n"
    for food in best["foods"]:
        response += f"✓ {food}\n"

    # Avoid
    response += "\n🚫 Foods to Avoid:\n"
    for item in best["avoid"]:
        response += f"✗ {item}\n"

    # Precautions
    response += "\n🩺 Precautions:\n"
    for precaution in best["precautions"]:
        response += f"• {precaution}\n"

    # General symptom-based advice
    text = user_input.lower()

    response += "\n💡 General Advice:\n"

    if "fever" in text:
        response += "• Drink plenty of water.\n"
        response += "• Take adequate rest.\n"

    if "headache" in text:
        response += "• Rest in a quiet room.\n"

    if "body pain" in text or "joint pain" in text:
        response += "• Avoid heavy exercise until you recover.\n"

    if "cough" in text:
        response += "• Drink warm fluids.\n"

    if "vomiting" in text or "diarrhea" in text:
        response += "• Drink ORS or electrolyte-rich fluids.\n"

    response += (
        "\n\n⚠ This is NOT a diagnosis."
        "\nPlease consult a qualified healthcare professional."
    )

    return response

symptoms_agent = Agent(
    name="symptoms_agent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="""
You are MediGuardian AI.

When a user provides symptoms,
ALWAYS use the find_possible_diseases tool.

Do not guess diseases from your own knowledge.

Use the tool results.

Never diagnose.

Always remind the user that this is not medical advice.
""",
    tools=[find_possible_diseases],
)