# from config import ACCOUNT_ID
# from main import run_query

# def create_alert_condition(policy_id, name, condition_type, threshold, duration):
#     mutation = f"""
#     mutation {{
#       alertsNrqlConditionStaticCreate(
#         accountId: {ACCOUNT_ID}
#         policyId: {policy_id}
#         condition: {{
#           name: "{name}"
#           nrql: {{
#             query: "{condition_type}"
#           }}
#           terms: {{
#             threshold: {threshold}
#             duration: "{duration}"
#           }}
#         }}
#       ) {{
#         id
#         name
#       }}
#     }}
#     """
#     return run_query(mutation)

# def read_conditions(file_path):
#     import json
#     with open(file_path, 'r') as file:
#         return json.load(file)


