from flask import Flask

app = Flask(__name__)

data = {166126147227: {"lockers": [1,2]},
        23119016145 : {"lockers": [1,3]},
        5016117342 : {"lockers": [2,3]}
       }

@app.route("/<int:id>/<int:locker>", methods=['GET'])
def authorise_check(id, locker):
    if (id not in data):
        return "",404
    elif(locker not in data[id]["lockers"]):
        return "", 403
    else:
        return "", 200

@app.errorhandler(404)
def page_not_found(e):
    return "", 404

if __name__ == "__main__":
    app.run(debug=True)