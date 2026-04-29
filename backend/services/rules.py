def rule_check(features: dict, doc_type: str):
    
    # Default response
    result = {
        "status": "Accepted",
        "reason": "No rule violations"
    }

    # 🔹 Income document rules
    if doc_type == "income":
        if features.get("income", 0) > 250000:
            return {
                "status": "Rejected",
                "reason": "Income exceeds ₹2.5 lakh threshold"
            }

        if features.get("income", 0) == 0:
            return {
                "status": "Rejected",
                "reason": "Income not detected"
            }

    # 🔹 Marksheet rules
    if doc_type == "marksheet":
        if features.get("text_length", 0) < 100:
            return {
                "status": "Rejected",
                "reason": "Incomplete or unclear marksheet"
            }

    return result