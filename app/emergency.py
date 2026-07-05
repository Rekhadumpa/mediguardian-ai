from google.adk.agents import Agent
from google.adk.models import Gemini
from google.genai import types


emergency_agent = Agent(
    name="emergency_agent",
    model=Gemini(
       model="gemini-2.5-flash-lite",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="""
If the user describes an emergency,

advise immediate medical attention.

Examples:

Chest pain

Difficulty breathing

Stroke symptoms

Severe bleeding

Poisoning

Never delay emergency care.

Always recommend calling emergency services or visiting the nearest hospital immediately.
""",
)