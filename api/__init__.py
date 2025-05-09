from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

APP_TITLE = "ISDBI Multi-Agents"
APP_VERSION = "0.0.1"
APP_DESCRIPTION = "ISDBI Multi-Agents"


app = FastAPI(
	title=APP_TITLE,
	version=APP_VERSION,
	description=APP_DESCRIPTION
)

from api import endpoints

app.include_router(endpoints.router)

origins = [
    "*"
]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])