# Stubs for urllib.request

# NOTE: These are incomplete!

from typing import Any

class BaseHandler(): ...
class HTTPRedirectHandler(BaseHandler): ...
class OpenerDirector(): ...

# TODO args should be types that extend BaseHandler (types, not instances)
def build_opener(*args: Any) -> OpenerDirector: ...
def install_opener(opener: OpenerDirector) -> None: ...

def proxy_bypass(host): ...
