"""Main program"""

from fastapi import FastAPI

from mood_tracker.api import router



app = FastAPI(
    title="Mood tracker",
    description="Трекер настроения",
)
app.include_router(router)
