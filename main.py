from flask import Flask, jsonify, request   
from ariadne import  graphql_sync
from flask_cors import CORS
from ariadne.explorer import ExplorerGraphiQL
from schema import schema

app = Flask(__name__)
CORS(app)  
 
explorer_html = ExplorerGraphiQL().html(None)

@app.route('/')
def index():
    return jsonify({"message": "API de GraphQL para inventario de tienda online", 
                    "graphql_endpoint": "/graphql"})

@app.route("/graphql", methods=["GET"])
def graphql_explorer():
    return explorer_html, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value={"request": request},
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)