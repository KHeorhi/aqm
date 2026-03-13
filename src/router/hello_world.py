from fastapi import APIRouter


router = APIRouter(prefix="/api")


@router.get("/message/hello")
def hello_world():
    return {"message": "Hello World"}
