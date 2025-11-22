## Carolina Chip Fab Site

Static marketing page for Carolina Chip Fab. The site deploys to Vercel as fully static assets under `src/`, while local development now uses a lightweight FastAPI server so we can preview everything without relying on Node/Express.

### Local development

```bash
# one-time setup (installs deps into .venv/)
uv sync

# run the dev server (installs deps if missing, activates env automatically)
uv run uvicorn main:app --reload
```

Visit <http://127.0.0.1:8000> and stop the server with `Ctrl+C`. If you prefer to activate the environment manually, use `source .venv/bin/activate`; uv will reuse it automatically.

### Deploying

- `vercel.json` serves everything directly from `src/`, so `vercel --prod` just uploads static assets.
- Any edits to HTML/CSS/JS/images live under `src/`.

Questions? Ping Blake. Better README achieved. 😉