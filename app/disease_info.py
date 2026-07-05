from google.adk.agents import Agent
from google.adk.models import Gemini
from google.genai import types

from .app_utils.disease_loader import get_disease_info


def disease_information(name: str) -> str:
    """Returns detailed information about a disease."""

    disease = get_disease_info(name)

    if disease is None:
        return (
            "Disease not found in the MediGuardian knowledge base. "
            "Please consult a healthcare professional."
        )

    return f"""
Disease: {disease['name']}

Causes:
{disease['causes']}

Symptoms:
{", ".join(disease['symptoms'])}

Recommended Foods:
{", ".join(disease['foods'])}

Foods to Avoid:
{", ".join(disease['avoid'])}

Precautions:
{", ".join(disease['precautions'])}
"""


disease_info_agent = Agent(
    name="disease_info_agent",

    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),

    instruction="""
You are the Disease Information Specialist for MediGuardian AI.

Your ONLY responsibility is answering questions about diseases.

For EVERY disease-related question, ALWAYS call the
disease_information tool FIRST.

Never answer using your own medical knowledge if the tool
can answer.

Examples:

- Tell me about Dengue.
- What is Malaria?
- Foods for Diabetes.
- Causes of Asthma.
- Prevention of Typhoid.
- Symptoms of Influenza.

After receiving the tool result:

• Present it clearly.
• Preserve all information from the tool.
• Do not invent facts.
• Do not remove any precautions.
• Never diagnose.

Always end with:

"This information is for educational purposes only.
Please consult a qualified healthcare professional."
""",

    tools=[
        disease_information,
    ],
)

