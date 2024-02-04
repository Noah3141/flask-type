from flask import Blueprint, render_template

home_map: Blueprint = Blueprint(
    'home', 
    __name__,
    url_prefix='/',
)


@home_map.route('/', methods=["GET"])
def index():
    return render_template(
        "home/index.html"
    )