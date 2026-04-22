
from fastapi import FastAPI
from routes.expenses import router as expense_router
from auth.auth_routes import router as auth_router

app = FastAPI(title="FinSight AI Pro")

app.include_router(expense_router)
app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "FinSight AI Pro Running"}
