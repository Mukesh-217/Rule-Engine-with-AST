class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # "operator" or "operand"
        self.left = left  # Left child for operator nodes
        self.right = right  # Right child for operator nodes
        self.value = value  # Operand value for leaf nodes (conditions)

def create_rule(rule_string):
    """
    Parses a rule string and creates the corresponding AST.
    """
    operator = "AND" if "AND" in rule_string else "OR"
    conditions = rule_string.split(operator)

    left_condition = conditions[0].strip()
    right_condition = conditions[1].strip()

    # Create an AST node with the operator
    root = Node(node_type="operator", value=operator)
    
    # Add left and right conditions as leaf nodes
    root.left = Node(node_type="operand", value=left_condition)
    root.right = Node(node_type="operand", value=right_condition)
    
    return root

def evaluate_rule(ast_node, user_data):
    """
    Evaluates the AST (rule) against the user data.
    """
    if ast_node.node_type == "operand":
        return eval_condition(ast_node.value, user_data)

    left_result = evaluate_rule(ast_node.left, user_data)
    right_result = evaluate_rule(ast_node.right, user_data)

    if ast_node.value == "AND":
        return left_result and right_result
    elif ast_node.value == "OR":
        return left_result or right_result
    else:
        raise ValueError("Invalid operator in AST")

def eval_condition(condition, user_data):
    """
    Evaluate individual conditions such as 'age > 30'.
    """
    attribute, operator, value = condition.split(" ")
    attribute_value = user_data.get(attribute)

    if operator == ">":
        return attribute_value > int(value)
    elif operator == "<":
        return attribute_value < int(value)
    elif operator == "=":
        return attribute_value == value.strip("'")
    else:
        raise ValueError("Unsupported operator")
