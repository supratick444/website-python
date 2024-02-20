from fastapi import FastAPI,UploadFile,File
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/')
async def Home():
    return{"message" : "Welcome to the Home page "}

@app.get('/contacts')
def contacts():
    return {"message" : " Contact page !!"}

# i want to learn that I want to create a route where i can upload one image !

@app.post('/upload')
async def images(image : UploadFile = File(...) ):

    try:
        with open( f"uploaded_images/{image.filename}","wb") as buffer:
            buffer.write(await image.read()) 
   
        return JSONResponse(content={"message": "Image uploaded successfully"})
    except Exception as e :
         return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

import uvicorn
uvicorn.run(app)