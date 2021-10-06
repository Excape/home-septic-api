from flask import Request


def is_authorized(request: Request) -> bool:
    headers = request.headers
    # TODO we would do some more complex stuff with authorization here
    # just check whether there is an API key set
    return "X-API-KEY" in headers
