from litestar import Controller, get


class AuthController(Controller):
    path = ""

    @get(path="/authorize")
    async def authorize(self):
        """Get Authorization Code from Authorization Code from Authorization
        Server.
        """
        pass