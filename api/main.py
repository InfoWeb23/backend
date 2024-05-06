from fastapi import FastAPI, Request
from database import insert_user, validate_user
from models import UserRegistration

app = FastAPI()

@app.post("/register")
async def register_user(request: Request, user_data: UserRegistration):
    try: 
        if validate_user(user_data.dict()):
            insert_user(user_data.dict())
            return {"status": "success", "message": "User has successfully inserted."}
        else:
            return {"status": "error", "message": "Invalid user data provided."}
    except Exception as e:
        return {"status": "error", "message": f"An error occurred: {e}"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)