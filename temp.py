from mira_sdk import MiraClient, Flow

# Initialize the client
client = MiraClient(config={"API_KEY": "sb-43a845fa3019b91e65e8bae7a3c01d78"})

version = "1.0.1"
input_data = {
    "feeling": " i got fired today"
}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@dc-0001/mood-tracking/{version}"
else:
    flow_name = "@dc-0001/mood-tracking"

result = client.flow.execute(flow_name, input_data)
print(result)