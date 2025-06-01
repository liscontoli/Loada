from fastapi import FastAPI
from routers import auth, password_recovery, user, load
from routers import negotiation
from routers import history

app = FastAPI()

# Register routers
app.include_router(auth.router)
app.include_router(password_recovery.router)
app.include_router(user.router)
app.include_router(load.router)
app.include_router(negotiation.router)
app.include_router(history.router)

@app.get("/")
def root():
    return {"message": "Loada backend is running"}
