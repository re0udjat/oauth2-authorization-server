from pydantic import BaseModel
from pydantic import StrictStr


class Response(BaseModel):
    code: StrictStr
    message: StrictStr