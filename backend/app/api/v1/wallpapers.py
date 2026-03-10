from fastapi import APIRouter
from app.services.wallpaper_service import fetch_pexels
import random

router = APIRouter()


@router.get("/",)
async def get_wallpapers():

    # 1️⃣ Try Pexels
    images = await fetch_pexels()
    if images:
        return images

    # 2️⃣ Fallback → static
    static_images = [
        {"url": "/cyberpunk-city1.jpg"},
        {"url": "/cyberpunk-city2.jpg"},
    ]

    return [random.choice(static_images)]