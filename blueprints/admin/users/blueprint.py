from typing import List
from flask import Blueprint, flash, redirect, render_template, url_for
from middlewares.ctx import Ctx
from models.user import  User
from .create_form import CreateUserForm

users_map: Blueprint = Blueprint(
    'users', 
    __name__,
    url_prefix='/users',
)

@users_map.route('/', methods=["GET"])
def index():

    ctx = Ctx()
    users: List[User] = ctx.db.query(User).all()

    return render_template(
        "admin/users/index.html",
        users=users
    )

@users_map.route('/create', methods=["GET"])
def create_view():


    form = CreateUserForm()


    return render_template(
        "admin/users/create.html",
        form=form
    )

@users_map.route('/create', methods=["POST"])
def create_mutate():
    ctx = Ctx()

    form = CreateUserForm(ctx.request.form)
    if form.validate():

        new_user = User(form)
        ctx.db.add(new_user)
        ctx.db.commit()

        flash(f"'{form.name.data}' created!", "success")
    else:
        for error in form.errors:
            flash(f"{error}", "error")
    return redirect(url_for("admin.users.index"))