from typing import List
from flask import Blueprint, flash, redirect, render_template, url_for
from blueprints.admin.users.edit_form import UpdateUserForm
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
    users: List[User] = ctx.db.users.get_by_id(23)
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

    try: 
        form = CreateUserForm(ctx.request.form)
        if form.validate():

            new_user = User(form)
            ctx.db.add(new_user)
            ctx.db.commit()

            flash(f"'{form.name.data}' created!", "success")
        else:
            for error in form.errors:
                flash(f"{error}", "error")
    except:
        ctx.db.rollback()
        flash("Error creating user", "error")
    return redirect(url_for("admin.users.index"))


@users_map.route('/update', methods=["GET"])
def update_view():
    form = UpdateUserForm()
    return render_template(
        "admin/users/update.html",
        form=form
    )


@users_map.route('/update', methods=["POST"])
def update_mutate():
    ctx = Ctx()

    try: 
        form = UpdateUserForm(ctx.request.form)

        user = (ctx.db.query(User)
            .filter(User.name == form.name.data)
            .first()
        )

        if user is None:
            flash(f"No user found with the name: {form.name.data or 'None'}", "warning")
            return redirect(url_for(endpoint="admin.users.update_mutate"))
        
        for field, value in form.data.items():
            if value is not None:
                setattr(user, field, value)

        ctx.db.commit()

        flash(f"'{form.name.data}' updated!", "success")
    except Exception as e:
        ctx.db.rollback()
        flash(f"Error updating user: {e}", "error")
    return redirect(url_for("admin.users.index"))