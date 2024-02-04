from flask import Blueprint, render_template
from flask import session
from middlewares.ctx import Ctx
from db import Session
from .create_form import CreateOrganization



organizations_map: Blueprint = Blueprint(
    'organizations', 
    __name__,
    url_prefix='/organizations',
)

@organizations_map.route('/', methods=["GET"])
def index():
    return render_template(
        "admin/organizations/index.html"
    )

@organizations_map.route('/create', methods=["GET"])
def create_view():


    form = CreateOrganization()


    return render_template(
        "admin/organizations/create.html",
        form=form
    )

@organizations_map.route('/create', methods=["POST"])
def create_mutate():
    

    form = CreateOrganization()


    return render_template(
        "admin/organizations/create.html",
        form=form
    )