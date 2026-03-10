from fastapi import APIRouter, HTTPException
from app.core.supabase import supabase

router = APIRouter()


@router.get("/")
def get_whitepapers():
    response = supabase.table("whitepapers").select("*").execute()

    if response.data is None:
        raise HTTPException(status_code=404, detail="No whitepapers found")

    return response.data