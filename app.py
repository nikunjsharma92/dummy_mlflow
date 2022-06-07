# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, abort
import json
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
responses = json.load(open("./data/responses.json"))
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/api/2.0/preview/mlflow/model-versions/search', methods=['GET'])
# ‘/’ URL is bound with hello_world() function.
def search():
    name = request.args["filter"]
    print("NAME: ", name, flush=True)
    args = name.split("=")
    model_name = args[1].strip("'")
    if model_name in responses:
        return responses[model_name]
    else:
        abort(404, "Resource not found")


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
