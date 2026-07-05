from google.adk.agents import Agent
from google.adk.models import Gemini
from google.genai import types

from .prompts import ROUTER_PROMPT


router_agent = Agent(
    name="router_agent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=ROUTER_PROMPT,
)