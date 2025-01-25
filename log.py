import json
from datetime import datetime
from textblob import TextBlob

# Example function to log user input with timestamp
def log_user_input(user_input, mood_log_file='mood_log.json'):
    # Analyzing the sentiment
    blob = TextBlob(user_input)
    sentiment = blob.sentiment.polarity  # -1 (negative) to 1 (positive)
    
    # Create a new log entry with timestamp and sentiment
    log_entry = {
        'timestamp': str(datetime.now()),
        'user_input': user_input,
        'sentiment': sentiment
    }

    # Log the data to the file
    try:
        with open(mood_log_file, 'a') as file:
            json.dump(log_entry, file)
            file.write('\n')
    except Exception as e:
        print(f"Error logging user input: {e}")

# Example function to summarize mood changes
def summarize_mood(mood_log_file='mood_log.json'):
    try:
        with open(mood_log_file, 'r') as file:
            logs = [json.loads(line.strip()) for line in file.readlines()]
        
        mood_summary = ""
        for log in logs:
            sentiment = "positive" if log['sentiment'] > 0 else "negative" if log['sentiment'] < 0 else "neutral"
            mood_summary += f"On {log['timestamp']}, the user felt {sentiment}. User input: {log['user_input']}\n"
        
        return mood_summary
    except Exception as e:
        print(f"Error summarizing mood: {e}")
        return "No mood data available."

# Log user inputs and generate mood summary
log_user_input("I feel anxious today.")
log_user_input("I'm feeling better now.")
print(summarize_mood())
