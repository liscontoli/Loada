from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, user, load, negotiation, history, password_recovery

app = FastAPI(title="Loada Backend")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(load.router)
app.include_router(negotiation.router)
app.include_router(history.router)
app.include_router(password_recovery.router)