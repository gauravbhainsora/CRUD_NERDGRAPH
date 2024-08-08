import json
from main import run_query
from config import ACCOUNT_ID

def list_alert_policies():
    query = f"""
    {{
      actor {{
        account(id: {ACCOUNT_ID}) {{
          alerts {{
            policiesSearch {{
              policies {{
                id
                name
                incidentPreference
              }}
            }}
          }}
        }}
      }}
    }}
    """
    return run_query(query)

def save_policies_to_json(policies, filename="policies.json"):
    with open(filename, 'w') as f:
        json.dump(policies, f, indent=4)

if __name__ == "__main__":
    policies = list_alert_policies()
    if policies:
        save_policies_to_json(policies)
        print("Policies saved to policies.json")
    else:
        print("Failed to list policies")
