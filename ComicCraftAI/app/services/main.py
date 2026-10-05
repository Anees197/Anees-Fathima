from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from pathlib import Path
import base64
import html

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
HTML_FILE = BASE_DIR / "templates" / "index.html"


def make_comic_image(panel_number, prompt):
    titles = [
        "The Beginning",
        "The Discovery",
        "The Adventure",
        "The Mystery",
        "Happy Ending"
    ]

    title = titles[panel_number - 1]

    svg = f"""
    <svg xmlns="http://www.w3.org/2000/svg"
         width="800" height="600" viewBox="0 0 800 600">

      <rect width="800" height="600" fill="#dff3d8"/>

      <rect x="0" y="0" width="800" height="90"
            fill="#222"/>

      <text x="400" y="55"
            text-anchor="middle"
            font-size="32"
            font-family="Arial"
            fill="white"
            font-weight="bold">
        PANEL {panel_number} - {html.escape(title)}
      </text>

      <!-- Forest -->
      <rect x="0" y="90" width="800" height="510"
            fill="#a8d08d"/>

      <circle cx="120" cy="180" r="80" fill="#4f8a45"/>
      <circle cx="250" cy="150" r="90" fill="#5d984f"/>
      <circle cx="680" cy="170" r="100" fill="#4f8a45"/>
      <circle cx="540" cy="140" r="75" fill="#6ba85b"/>

      <rect x="110" y="220" width="25" height="250"
            fill="#795548"/>
      <rect x="660" y="220" width="25" height="250"
            fill="#795548"/>

      <!-- Ground -->
      <rect x="0" y="470" width="800" height="130"
            fill="#75a957"/>

      <!-- Fox body -->
      <ellipse cx="400" cy="420" rx="120" ry="70"
               fill="#d96b32"/>

      <!-- Fox head -->
      <ellipse cx="400" cy="330" rx="85" ry="75"
               fill="#e47735"/>

      <!-- Ears -->
      <polygon points="335,285 350,205 385,285"
               fill="#c85c2c"/>
      <polygon points="415,285 450,205 465,285"
               fill="#c85c2c"/>

      <!-- White face -->
      <ellipse cx="400" cy="350" rx="48" ry="42"
               fill="#fff1dc"/>

      <!-- Eyes -->
      <circle cx="370" cy="325" r="8" fill="#111"/>
      <circle cx="430" cy="325" r="8" fill="#111"/>

      <!-- Nose -->
      <circle cx="400" cy="355" r="10" fill="#222"/>

      <!-- Tail -->
      <path d="M500 420 Q680 350 650 470 Q590 530 500 455"
            fill="#d96b32"/>

      <path d="M620 435 Q650 440 650 470 Q625 495 600 480"
            fill="white"/>

      <!-- Mystery object -->
      <circle cx="560" cy="420" r="28"
              fill="#fff176"
              stroke="#ff9800"
              stroke-width="6"/>

      <!-- Speech box -->
      <rect x="35" y="105" width="300" height="90"
            rx="18" fill="white"
            stroke="#222" stroke-width="3"/>

      <text x="55" y="140"
            font-size="20"
            font-family="Arial"
            fill="#222">
        Filo's Comic Adventure
      </text>

      <text x="55" y="170"
            font-size="16"
            font-family="Arial"
            fill="#555">
        Panel {panel_number}
      </text>

    </svg>
    """

    encoded = base64.b64encode(
        svg.encode("utf-8")
    ).decode("utf-8")

    return "data:image/svg+xml;base64," + encoded


@app.get("/", response_class=HTMLResponse)
def home():
    return HTML_FILE.read_text(encoding="utf-8")


@app.post("/generate")
def generate_comic(
    prompt: str = Form(...)
):

    images = []

    for i in range(1, 6):
        images.append({
            "panel": i,
            "title": f"Panel {i}",
            "image": make_comic_image(i, prompt)
        })

    return {
        "success": True,
        "images": images
    }