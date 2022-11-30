import logging
import os

import sentry_sdk
from fastapi import Depends, FastAPI
from google.cloud import firestore
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.starlette import StarletteIntegration

from depends import basic_auth
from settings import settings

FORMAT = "%(levelname)-9s %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

if settings.SENTRY_DSN_SERVER:
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN_SERVER,
        environment=os.environ.get("GAE_VERSION"),
        integrations=[StarletteIntegration(), FastApiIntegration()],
        traces_sample_rate=0.2,
    )

app = FastAPI(
    title="jethro",
    dependencies=[Depends(basic_auth)],
)

# initializing firestore
db = firestore.Client(settings.GOOGLE_CLOUD_PROJECT)
collection = db.collection("")


@app.get("/")
def get():
    env_names = ["GOOGLE_CLOUD_PROJECT", "GAE_VERSION", "GAE_MEMORY_MB", "GAE_RUNTIME"]
    return {name: os.environ.get(name) for name in env_names}
