import json

RULES_PATH = "data/rules.json"

def load_rules():
    with open(RULES_PATH) as f:
        return json.load(f)


def retrieve_rule(doc_type):
    rules = load_rules()
    
    for r in rules:
        if r["doc_type"] == doc_type:
            return r["rule"]
    
    return "No rule found"


def generate_explanation(rule, features, rule_result):
    if rule_result["status"] == "Rejected":
        return f"Rejected because: {rule}. Detected issue: {rule_result['reason']}"
    
    return f"Accepted. Rule satisfied: {rule}"