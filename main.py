from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pdf2image import convert_from_bytes
from PIL import Image
import pytesseract
import io

app = FastAPI()

@app.get("/")
async def health():
    return JSONResponse(status_code=200, content={"content": "ok"})

@app.post("/extract-text/")
async def extract_text_from_pdf(file: UploadFile = File(...)):
    if file.content_type != 'application/pdf':
        return JSONResponse(status_code=400, content={"error": "Arquivo não é um PDF"})

    file_bytes = await file.read()

    try:
        images = convert_from_bytes(file_bytes, dpi=150)

        full_text = ''

        for image in images:
            text = pytesseract.image_to_string(image, lang='por')
            full_text += f'{text.strip()}\n\n'

        return {"text": full_text.strip()}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
