import httpx
import random
from app.core.config import settings


async def fetch_pexels():
    url = "https://api.pexels.com/v1/search"

    async with httpx.AsyncClient() as client:
        response = await client.get(
            url,
            headers={"Authorization": settings.PEXELS_KEY},
            params={
                "query": "cityscape",
                "per_page": 1,
                "page": random.randint(10, 500)

            },
        )

    if response.status_code != 200:
        return []

    data = response.json()
    photos = data.get("photos", [])

    if not photos:
        return []

    return [{"url": photo["src"]["large"]} for photo in photos]