from flask import Blueprint, render_template
from .organizations.blueprint import organizations_map
from .users.blueprint import users_map

admin_map: Blueprint = Blueprint(
    'admin', 
    __name__,
    url_prefix='/admin',
)

admin_map.register_blueprint(organizations_map) # type:ignore
admin_map.register_blueprint(users_map)         # type:ignore

@admin_map.route('/', methods=["GET"])
def index():
    return render_template(
        "admin/index.html"
    )