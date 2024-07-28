from flask import Flask,jsonify,request
from flask import request

app = Flask(__name__)

todos = [
  { 
      "label": "Mi primera chamba", 
      "done": False 
  }
 
] 

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text


@app.route('/todos',methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
   for pos in range(len(todos)):
      if pos == position:
         todos.pop(position) 
   return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3001, debug=True)