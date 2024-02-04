from flask import Flask

from blueprints.admin.blueprint import admin_map
from blueprints.home.blueprint import home_map
from utils.print_rules import print_rules



app = Flask(
    __name__,
)

app.config["SECRET_KEY"] = "flnaofeiaioef"


app.register_blueprint(home_map)
app.register_blueprint(admin_map)

print_rules(app.url_map._rules)


if __name__ == '__main__':
    app.run(debug=True)