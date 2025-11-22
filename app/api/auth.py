from app.services.auth.auth_service import AuthService
from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()

@router.get("/auth/token")
async def get_token():
    try:
        auth_service = AuthService() 
        token_response = await auth_service.get_access_token()  
        return {"status":"success", "data": token_response} 
    
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except Exception as e:
         raise HTTPException(status_code=500, detail=str(e))