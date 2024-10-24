from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 
class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type 
        self.left = left  
        self.right = right  
        self.value = value 

def parse_rule_string(rule_string):
    return Node("operand", value="Parsed AST")

def evaluate_rule_against_data(ast, user_data):
    return True  

@app.route('/create_rule', methods=['POST'])
def create_rule():
    try:
        data = request.get_json()
        rule_string = data.get('rule_string')

        if not rule_string:
            return jsonify({'message': 'No rule string provided'}), 400
        
        ast = parse_rule_string(rule_string) 
        return jsonify({'message': 'Rule created successfully', 'ast': ast.__dict__}), 200

    except Exception as e:
        return jsonify({'message': 'Failed to create rule', 'error': str(e)}), 500

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    try:
        data = request.get_json()
        user_data = data.get('user_data')

        if not user_data:
            return jsonify({'message': 'No user data provided'}), 400

        ast = Node("operand", value="Placeholder AST") 
        result = evaluate_rule_against_data(ast, user_data)  

        return jsonify({'result': result}), 200

    except Exception as e:
        return jsonify({'message': 'Failed to evaluate rule', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
