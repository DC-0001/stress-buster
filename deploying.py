from mira_sdk import MiraClient, CompoundFlow
from mira_sdk.exceptions import FlowError
API_KEY = "sb-c95bfa51f34759b65fd6a11f2a8be1e7" #os.getenv("MIRA_API_KEY")

# Initialize Mira Client
client = MiraClient(config={"API_KEY": API_KEY})

flow = CompoundFlow(source="/Users/dakshveerchahal/Desktop/Mira_Hackathon/gpt.yaml")           # Load flow configuration

try:
    client.flow.deploy(flow)                               # Deploy to platform
    print("Compound flow deployed successfully!")          # Success message
except FlowError as e:
    print(f"Deployment error: {str(e)}")                   # Handle deployment error
