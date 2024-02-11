from flask import Blueprint, flash, redirect, render_template, url_for
from db import Organization
from middlewares.ctx import Ctx
from .create_form import CreateOrganizationForm


organizations_map: Blueprint = Blueprint(
    'organizations', 
    __name__,
    url_prefix='/organizations',
)

@organizations_map.route('/', methods=["GET"])
def index():

    ctx = Ctx()
    users = ctx.db.organizations.find_all()

    return render_template(
        "admin/organizations/index.html",
        users=users
    )

@organizations_map.route('/<int:org_id>', methods=["GET"])
def view_one(org_id: int):

    ctx = Ctx()
    organization = ctx.db.organizations.get_by_id({"id":org_id})
    if organization.err is not None: return "Uh oh"
    organization.data.name

    return render_template(
        "admin/organizations/index.html",
        organization=organization
    )

@organizations_map.route('/create', methods=["GET"])
def create_view():

    form = CreateOrganizationForm()

    return render_template(
        "admin/organizations/create.html",
        form=form
    )

@organizations_map.route('/create', methods=["POST"])
def create_mutate():
    ctx = Ctx()

    form = CreateOrganizationForm(ctx.request.form)
    if form.validate():

        flash(f"'{'Org'}' created!", "success")
    else:
        for error in form.errors:
            flash(f"{error}", "error")
    return redirect(url_for("admin.organizations.index"))