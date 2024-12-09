"""Main entrypoint for the app."""

import asyncio
from typing import Optional, Union
from uuid import UUID
from typing import Dict, List, Optional, Sequence, Tuple
import json
import os

from fastapi import Body, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from plot import generate_html_response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path



app = FastAPI()
app.mount("/static", StaticFiles(directory="PLOT_topic_over_time"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["null", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/plot/")
async def return_plot(ognization_name: str):
    iec_paths = [i for i in os.listdir("./PLOT_topic_over_time") if ognization_name in i and '.csv' not in i]
    iec_paths = [Path(os.path.join("static", i)) for i in iec_paths]
    # return FileResponse(Path('./PLOT_topic_over_time/3gpp.png'))
    return iec_paths

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
