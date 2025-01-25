from mira_sdk import MiraClient
from mira_sdk.exceptions import FlowError
import os
from dotenv import load_dotenv
from image_fetch import fetch_calming_images  # Import the function from the external file
from sound_player import play_random_sound

API_KEY = "sb-c95bfa51f34759b65fd6a11f2a8be1e7" #os.getenv("MIRA_API_KEY")
# Initialize Mira Client
client = MiraClient(config={"API_KEY": API_KEY})

flow_name = "dc-0001/your-flow-name"                 # Flow identifier
input_data = {                                             # Execution inputs
    "user_input": "my girlfriend says she doesnt love me",
    "user_feedback": "It was very challenging."
}

try:
    result = client.flow.execute(flow_name, input_data)    # Execute workflow
    print("Execution result:", result)                     # Display result
    print("Completed Test Run!!")
    calming_image_url = fetch_calming_images()
    if calming_image_url:
        print(f"Calming Image URL: {calming_image_url}")
    print("Playing relaxing music...")
    play_random_sound()
except FlowError as e:
    print("Execution error:", str(e))                      # Handle execution error
