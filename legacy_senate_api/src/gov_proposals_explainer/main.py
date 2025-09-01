from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from gov_proposals_explainer import routers

app = FastAPI()


@app.get("/", tags=["root"])
async def read_root():
    return HTMLResponse(
        """
        <h1>Gov Proposals Explainer</h1>
        <p>API documentation: <a href="/docs">/docs</a></p>
        """
    )

app.include_router(routers.senate_router, tags=["senate"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=6969)
