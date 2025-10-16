from datetime import UTC, datetime

import requests
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

CAT_FACT_URL = "https://catfact.ninja/fact"


@app.get("/me", response_class=JSONResponse)
def get_profile():
    """
    Returns user profile info and a dynamic cat fact.

    A fresh cat fact is fetched from the API on every request.
    """
    cat_fact = "Could not fetch cat fact at the moment. Please try again later."
    try:
        # Always fetch a new fact for each request (no caching)
        response = requests.get(
            CAT_FACT_URL,
            timeout=5,
            headers={"Cache-Control": "no-cache"},
        )
        print(response.ok)
        cat_fact = response.json().get("fact", cat_fact)
    except requests.RequestException:
        pass
        # Graceful fallback in case of API failure

    payload = {
        "status": "success",
        "user": {
            "email": "ichekuwilson538@gmail.com",
            "name": "Wilson Icheku",
            "stack": "Python/FastAPI",
        },
        "timestamp": datetime.now(tz=UTC).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z",
        "fact": cat_fact,
    }

    return JSONResponse(content=payload, media_type="application/json")
