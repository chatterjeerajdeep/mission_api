from flask import Flask, jsonify, request, make_response
from pymongo import MongoClient

db_con = MongoClient()

# The following command displays the names of the databases present
# print(db_con.database_names())

db = db_con['Test_DB']

# The following command displays the names of the collections present in the database
# print(db.list_collection_names())

collection = db['my_table']

app = Flask(__name__)

@app.route("/user")
def index():
	return jsonify("Hello!! Congratulations on your first step building REST APIs with flask")

@app.route("/user/get_all", methods=["GET"])
def get_all_user_data():
	# fetch the entire data from the collection
	data = collection.find()
	output = [{"Name":data_item["Name"], "Purpose":data_item["Purpose"]} for data_item in data]
	return make_response(jsonify(output),200)

@app.route("/user/create", methods=["POST"])
def create_user():
	# get the json data from request
	data = request.get_json()
	collection.insert_one(data)
	return make_response("User Created Successfully", 200)

@app.route("/user/remove/<string:Name>", methods=["DELETE"])
def remove_user(Name):
	collection.find_one_and_delete({"Name":Name})
	return make_response("Deleted Successfully", 200)

@app.route("/user/update")




if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=4000)