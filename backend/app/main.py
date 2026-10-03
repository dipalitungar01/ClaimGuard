from fastapi import FastAPI

from app.routes.user import router as user_router
from app.routes.claim import router as claim_router


app = FastAPI(
    title="ClaimGuard API",
    version="0.1.0"
)


app.include_router(user_router)
app.include_router(claim_router)


@app.get("/health")
def health_check():
    return {"status": "ClaimGuard API is running"}
