from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__)) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False)
    content = db.Column(db.String(144), unique=False)
    
    def __init__(self, title, content):
        self.title = title
        self.content = content 

class DataSchema(ma.Schema):
    class Meta: 
        fields = ('title', 'content')

data_schema = DataSchema()
datas_schema = DataSchema(many=True)

# Endpoint to create a new data
@app.route('/data', methods=["POST"])
def add_data():
    title = request.json['title']
    content = request.json['title']

    new_data = Data(title, content)
    
    db.session.add(new_data)
    db.session.commit()

    data = Data.query.get(new_data.id)

    return data_schema.jsonify(data)

# Endpoint to query all data
@app.route("/datas", methods=["GET"])
def get_datas():
    all_datas = Data.query.all()
    result = datas_schema.dump(all_datas)
    return jsonify(result)


# Endpoint for updating data
@app.route("/data/<id>", methods=["PUT"])
def data_update(id):
    data = Data.query.get(id)
    title = request.json["title"]
    content = request.json["content"]

    data.title = title
    data.content = content

    db.session.commit()
    return data_schema.jsonify(data)

#Endpoint for deleting a record
@app.route("/data/<id>", methods=["DELETE"])
def data_delete(id):
    data = Data.query.get(id)
    db.session.delete(data)
    db.session.commit()

    return data_schema.jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)

