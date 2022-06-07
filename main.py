from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

class SortedList(Resource):
    def get(self, numbers):
        sortednumbers = sorted(numbers)
        return{"sortednumbers":sortednumbers}

api.add_resource(SortedList, '/<string:numbers>')


if __name__ == "__main__":
    app.run(debug=True)