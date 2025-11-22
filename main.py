from pathlib import Path

from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / "src"
INDEX_FILE = SRC_DIR / "index.html"

app = FastAPI(
    title="Carolina Chip Fab Site",
    description="FastAPI wrapper for serving the static Carolina Chip Fab site locally.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=["system"])
async def healthcheck() -> dict[str, str]:
    """
    Lightweight health endpoint for sanity checks.
    """
    return {"status": "ok"}


@app.get("/{asset_path:path}", response_class=HTMLResponse)
async def serve_static(asset_path: str = "") -> Response:
    """
    Serve files from the src directory. Directories fall back to their index.html (if present).
    """
    if asset_path in ("", "/"):
        if not INDEX_FILE.exists():
            raise HTTPException(status_code=500, detail="index.html not found in /src")
        return HTMLResponse(INDEX_FILE.read_text(encoding="utf-8"))

    target = (SRC_DIR / asset_path).resolve()

    if SRC_DIR not in target.parents and target != SRC_DIR:
        raise HTTPException(status_code=404, detail="Not found")

    if target.is_dir():
        target = target / "index.html"

    if not target.exists() or not target.is_file():
        raise HTTPException(status_code=404, detail="Not found")

    return FileResponse(target)

