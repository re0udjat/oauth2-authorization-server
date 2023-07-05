from pathlib import Path
from litestar import Litestar
from litestar.template.config import TemplateConfig
from litestar.contrib.jinja import JinjaTemplateEngine
from controllers.base import BaseController

# Setup OAuth2 Client
client = {
    "client_id": "oauth2-client-one",
    "client_secret": "oauth2-client-secret-one",
    "return_urls": ["http://localhost:9000/callback"]
}


# Setup OAuth2 Authorization Server
authorization_server = {
    "authorization_endpoint": "http://localhost:9001/authorize",
    "token_endpoint": "http://localhost:9001/token"
}


app = Litestar(
    route_handlers=[BaseController],
    template_config=TemplateConfig(
        directory=Path("templates"),
        engine=JinjaTemplateEngine
    )
)