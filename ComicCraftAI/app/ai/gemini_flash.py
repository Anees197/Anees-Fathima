import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key) if api_key else None


def generate_outline(request):
    if not client:
        raise Exception("GEMINI_API_KEY is not configured in .env")

    prompt = f"""
Create a five-panel comic outline.

Story:
{request.story_prompt}

Main character:
{request.character_name}

Setting:
{request.setting}

Tone:
{request.tone}

Art style:
{request.art_style}

Create exactly 5 different story scenes.
Each panel must have:
- title
- scene
- action
- character expression

The same main character must continue through all five panels.
Make the expressions match what happens in each scene.
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text