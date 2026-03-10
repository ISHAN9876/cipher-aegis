from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.wallpapers import router as wallpaper_router
from app.api.v1.whitepapers import router as whitepapers_router
app = FastAPI(
    title="𐌂iρhεr αεgiς Backend",
    description="Cybersecurity Tools Platform API",
    version="0.1.0"
)
app.include_router(
    whitepapers_router,
    prefix="/api/v1/whitepapers",
    tags=["Whitepapers"]
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ THIS LINE WAS MISSING
app.include_router(
    wallpaper_router,
    prefix="/api/v1/wallpapers",
    tags=["Wallpapers"],
)

@app.get("/")
def root():
    return {
        "message": "Welcome to 𐌂iρhεr αεgiς!",
        "status": "online",
        "tagline": "Ⅎφrgε Ψφur Ↄψbεr Σdgε"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "uptime": "running"}