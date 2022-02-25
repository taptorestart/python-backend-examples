from typing import List

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import shutil

app = FastAPI()


@app.post("/files/")
async def create_files(
    files: List[bytes] = File(..., description="Multiple files as bytes")
):
    for index, file in enumerate(files):
        filename = f'{index}'
        save_bytes(file, '.', filename)
    return {"file_sizes": [len(file) for file in files]}


def save_bytes(file_bytes: bytes, path: str, name: str):
    file = open(f'{path}/{name}', 'wb')
    try:
        file.write(file_bytes)
    finally:
        file.close()


@app.post("/uploadfiles/")
async def create_upload_files(
    files: List[UploadFile] = File(..., description="Multiple files as UploadFile")
):
    for file in files:
        save_upload_file(file, '.', file.filename)
    return {"filenames": [file.filename for file in files]}


def save_upload_file(upload_file: UploadFile, path: str, name: str):
    with open(f'{path}/{name}', 'wb') as buffer:
        shutil.copyfileobj(upload_file.file, buffer)


@app.get("/")
async def main():
    content = """
<body>
<p>Multiple files as bytes
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</p>
<p>Multiple files as UploadFile
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</p>
</body>
    """
    return HTMLResponse(content=content)
