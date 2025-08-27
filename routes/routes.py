from fastapi import APIRouter, HTTPException, status
from models.todos import Todo
from config.database import collection_name
from schemas.schemas import list_serial
from bson import ObjectId

router  = APIRouter()

@router.get("/")
async def get_todo():
    print(">>>>> ",[obj["name"] for obj in collection_name.find()])
    todos = list_serial(collection_name.find())
    return todos

@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_todo(todo : Todo):
    ("Trynna post data")
    try:
        result = collection_name.insert_one(todo.dict())
        return {"id": str(result.inserted_id) , "message":"data inserted"}, 201
    except Exception as e:
        print("Exception raised")
        raise HTTPException(status_code = 500, detail=f"Database insert failed: {str(e)}")
