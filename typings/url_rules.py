from typing import Any, Literal, NamedTuple, Set, TypedDict, Union
from werkzeug.routing import Map

# {
#     'rule': , 
#     'is_leaf': True, 
#     'is_branch': False, 
#     'map': Map([
#         <Rule '/static/<filename>' (GET, HEAD, OPTIONS) -> static>,<Rule '/admin/foo' (GET, HEAD, OPTIONS) -> admin_blueprint.index>]), 
#     'strict_slashes': True, 
#     'merge_slashes': True, 
#     'subdomain': '', 
#     'host': None, 
#     'defaults': None, 
#     'build_only': False, 
#     'alias': False, 
#     'websocket': False, 
#     'methods': {'GET', 'HEAD', 'OPTIONS'}, 
#     'endpoint': 'static', 
#     'redirect_to': None, 
#     'arguments': {'filename'}, 
#     'provide_automatic_options': True, 
# }

class UrlRuleDict(NamedTuple):
    rule: str
    "'/static/<path:filename>'"
    is_leaf: bool
    is_branch: bool
    map: Any
    strict_slashes: bool
    merge_slashes: bool
    subdomain: str
    host: Union[Any, None]
    defaults: Union[Any, None]
    build_only: bool
    alias: bool
    websocket: bool
    methods: Set[Literal['GET', 'HEAD', 'OPTIONS', 'POST', 'PUT']]
    endpoint: Literal['static'] | str
    redirect_to: Union[Any, None]
    arguments: Set[str]
    provide_automatic_options: bool















