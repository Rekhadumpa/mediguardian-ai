# ruff: noqa
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.adk.apps import App
import os
import google.auth

from .router import router_agent
from .symptoms import symptoms_agent
from .disease_info import disease_info_agent
from .emergency import emergency_agent
from .safety import safety_agent

from google.adk.agents import Agent
from google.adk.models import Gemini
from google.genai import types

from dotenv import load_dotenv, find_dotenv
import os

dotenv_path = find_dotenv()
print("Loaded .env file at:", dotenv_path)

load_dotenv(dotenv_path, override=True)

print("API KEY:", os.getenv("GOOGLE_API_KEY"))


root_agent = Agent(
    name="MediGuardianAI",

    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),

    instruction="""
You are MediGuardian AI.

Delegate every user request to the most appropriate specialist agent.

Available agents:

1. symptoms_agent
- User describes symptoms.

Examples:
I have fever.
I have cough and headache.

2. disease_info_agent
- User asks about diseases.

Examples:
Tell me about dengue.
Foods for diabetes.
What causes malaria?

3. emergency_agent
- User has emergency symptoms.

Examples:
Chest pain.
Difficulty breathing.
Heavy bleeding.
Stroke symptoms.

Always delegate to ONLY ONE agent.

Never diagnose.
Always remind users to consult a healthcare professional.
""",

    sub_agents=[
        symptoms_agent,
        disease_info_agent,
        emergency_agent,
    ],
)

app = App(
    root_agent=root_agent,
    name="app",
)
