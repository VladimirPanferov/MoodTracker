"""Main program"""

from fastapi import FastAPI


from mood_tracker import api



app = FastAPI(
    title="Mood tracker",
    description="Трекер настроения",
)
app.include_router(api.router)
