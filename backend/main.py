from fastapi import FastAPI, Response, status
from utils import get_client


clients = [
    {
        "client_id": "oauth-client-1",
        "client_secret": "oauth-client-secret-1",
        "return_urls": ["http://localhost:9000/callback"]
    }
]


app = FastAPI()


@app.get("/")
async def index():
    return {
        "code": "200.00",
        "message": "Welcome to Authorization Server"
    }


@app.get("/authorize", status_code=status.HTTP_200_OK)
async def oauth2_authorize(client_id: str, return_url: str, response: Response):
    client = get_client(client_id, clients)
    if client is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "code": "400.01",
            "message": "Unknown client"
        }
    elif return_url not in client["return_urls"]:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "code": "400.02",
            "message": "Invalid return URL"
        }
    return {
        "code": "200.00",
        "message": "Authorize successful"
    }