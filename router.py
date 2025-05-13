def get_assignee_email(category):
    routing = {
        "Facilities": "ops@freeaxez.com",
        "IT Support": "itsupport@freeaxez.com",
        "HR": "hr@freeaxez.com",
        "Finance": "finance@freeaxez.com",
        "Sales Enablement": "sales@freeaxez.com"
    }
    return routing.get(category, "unassigned@freeaxez.com")
