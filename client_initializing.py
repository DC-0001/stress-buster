from mira_sdk import MiraClient, CompoundFlow
from mira_sdk.exceptions import FlowError
import os
from dotenv import load_dotenv
from image_fetch import fetch_calming_images  # Import the function from the external file
from sound_player import play_random_sound

# Load API key from environment file
load_dotenv()
API_KEY = "sb-c95bfa51f34759b65fd6a11f2a8be1e7"  #os.getenv("MIRA_API_KEY")

# Initialize Mira Client
client = MiraClient(config={"API_KEY": API_KEY})

# Flow details
flow = "@dc-0001/stress-buster"
flow_name = "@dc-0001/therapy-personalisation"

# Function to get input and display response
def run_therapy():
    # Take user input
    user_input = input("How is your day going? ")

    # Prepare test inputs
    test_input = {
        "user_input": user_input,
        "user_feedback": "none"  # Default until therapy feedback is given
    }

    try:
        # Run the first flow to analyze mood
        response = client.flow.execute(flow, test_input)
        print(f"Response: {response}")

        # Take therapy feedback
        therapy_feedback = input("How was the therapy? ")

        # Prepare input for second flow
        input_data = {
            "therapy_steps": response,
            "therapy_feedback": therapy_feedback
        }

        # Run the second flow for personalization
        result = client.flow.execute(flow_name, input_data)
        print(f"Result: {result}")
        
        # Fetch calming images
        calming_image_urls = fetch_calming_images()
        if calming_image_urls:
            print(f"Calming Image URLs: {calming_image_urls}")
        
        # Play relaxing music
        print("Playing relaxing music...")
        play_random_sound()

    except FlowError as e:
        print(f"Test failed: {str(e)}")

# Run the therapy function
run_therapy()
