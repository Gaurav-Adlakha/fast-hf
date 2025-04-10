from fasthtml_hf import setup_hf_backup
from fasthtml import FastHTML
from monsterui.core import Theme
from fasthtml.common import *
import os, uvicorn
from starlette.responses import FileResponse
from starlette.datastructures import UploadFile
from fastai.vision.all import *


theme = Theme.blue
app, rt = fast_app(hdrs=theme.headers())

os.makedirs("uploads", exist_ok=True)

def classify(image_path): 
    im = PILImage.create(image_path)
    learn = load_learner("model.pkl")
    cls,idx,probs = learn.predict(im)
    return cls,probs[idx]
 

@app.get("/")
def home():
    return Title("German Bread Classification"), Main(
        H1("German Bread Classification App"),
        Form(
            Input(type="file", name="image", accept="image/*", required=True),
            Button("Classify"),
            enctype="multipart/form-data",
            hx_post="/classify",
            hx_target="#result"
        ),
        Br(), Div(id="result"),
        cls="container"
    )

@app.post("/classify")
async def handle_classify(image:UploadFile):
    
    image_path = f"uploads/{image.filename}"
    with open(image_path, "wb") as f:
        f.write(await image.read())
    
    result = classify(image_path)
    
    return Div(
        P(f"Classification result: {result}"),
        Img(src=f"/uploads/{image.filename}", alt="Uploaded image", style="max-width: 300px;")
    )

@app.get("/uploads/{filename}")
async def serve_upload(filename: str):
    return FileResponse(f"uploads/{filename}")

setup_hf_backup(app)
serve()
