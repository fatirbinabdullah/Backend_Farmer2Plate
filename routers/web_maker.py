from fastapi import APIRouter


router = APIRouter(prefix="/farmer", tags=["Farmer"])


@router.get("/maker")
def root():
    return 'https://faysalmahmudsajan.github.io/'