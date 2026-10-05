import os
from pathlib import Path

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
HF_IMAGE_MODEL = os.getenv(
    "HF_IMAGE_MODEL",
    "stabilityai/stable-diffusion-xl-base-1.0"
)

OUTPUT_DIR = (
    Path(__file__).resolve().parent.parent.parent
    / "outputs"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

client = (
    InferenceClient(
        provider="hf-inference",
        api_key=HF_TOKEN
    )
    if HF_TOKEN and HF_TOKEN != "your_huggingface_token_here"
    else None
)


def generate_image(
    prompt: str,
    panel_number: int
):

    if not client:
        raise Exception(
            "HF_TOKEN is not configured in .env"
        )

    image = client.text_to_image(
        prompt=prompt,
        model=HF_IMAGE_MODEL
    )

    output_path = (
        OUTPUT_DIR
        / f"panel_{panel_number}.png"
    )

    image.save(output_path)

    return output_path