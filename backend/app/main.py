from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.v1 import auth, inventory, production, crm, reporting

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(inventory.router, prefix=f"{settings.API_V1_STR}/inventory", tags=["inventory"])
app.include_router(production.router, prefix=f"{settings.API_V1_STR}/production", tags=["production"])
app.include_router(crm.router, prefix=f"{settings.API_V1_STR}/crm", tags=["crm"])
app.include_router(reporting.router, prefix=f"{settings.API_V1_STR}/reporting", tags=["reporting"])

@app.get("/")
def root():
    return {"message": "Welcome to IndustriTrack API"}
