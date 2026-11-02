
import os

from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import StreamingResponse
from fastapi_clerk_auth import (
    ClerkConfig,
    ClerkHTTPBearer,
    HTTPAuthorizationCredentials,
)
from openai import OpenAI

app = FastAPI()

jwks_url = os.getenv("CLERK_JWKS_URL")

if not jwks_url:
    raise RuntimeError("CLERK_JWKS_URL is not configured")

clerk_config = ClerkConfig(jwks_url=jwks_url)
clerk_guard = ClerkHTTPBearer(clerk_config)


@app.get("/api")
def idea(
    creds: HTTPAuthorizationCredentials = Depends(clerk_guard),
):
    user_id = creds.decoded["sub"]

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="GROQ_API_KEY is not configured",
        )

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
    )

    prompt = [
        {
            "role": "user",
            "content": (
                "Generate a new business idea involving AI agents. "
                "Include a title, problem statement, solution, target "
                "customers, features, and business model. "
                "Use Markdown headings and bullet points."
            ),
        }
    ]

    stream = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=prompt,
        stream=True,
    )

    def event_stream():
        for chunk in stream:
            content = chunk.choices[0].delta.content

            if content:
                for line in content.split("\n"):
                    yield f"data: {line}\n\n"

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )
