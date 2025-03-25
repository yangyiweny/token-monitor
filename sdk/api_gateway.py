from fastapi import FastAPI, Request
from .monitor import TokenMonitor
import json

app = FastAPI()
monitor = TokenMonitor()

@app.middleware("http")
async def track_token_usage(request: Request, call_next):
    # Parse request body for token usage
    body = await request.body()
    try:
        data = json.loads(body)
        if 'model' in data and 'tokens' in data:
            monitor.track_usage(data['model'], data['tokens'])
    except json.JSONDecodeError:
        pass
    
    response = await call_next(request)
    return response

@app.get("/usage")
async def get_usage():
    return monitor.get_usage()

@app.post("/threshold")
async def set_threshold(threshold: int):
    monitor.set_threshold(threshold)
    return {"message": f"Threshold set to {threshold}"}

@app.get("/check_threshold")
async def check_threshold():
    exceeded = monitor.check_threshold()
    return {"threshold_exceeded": exceeded}
