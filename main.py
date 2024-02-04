import os
from flask import Flask

from blueprints.admin.blueprint import admin_map
from blueprints.home.blueprint import home_map

HR = {
    '-':  '-' * os.get_terminal_size().columns,
    '=': '=' * os.get_terminal_size().columns
}

app = Flask(
    __name__,
)

app.config["SECRET_KEY"] = "flnaofeiaioef"


app.register_blueprint(home_map)
app.register_blueprint(admin_map)


print(HR['=']) # Route print
print("ROUTES")
for route in app.url_map._rules:    
    print(HR['-'])
    print(f">> {f'({route.endpoint})':15} {route.methods:}   {route.rule:30} ")
print(HR['='])


if __name__ == '__main__':
    app.run(debug=True)