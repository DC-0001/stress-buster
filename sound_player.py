import random
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame

def play_random_sound():
    sound_folder = "sounds"

    # Get list of all sound files in the folder
    sound_files = [f for f in os.listdir(sound_folder) if f.endswith((".mp3", ".wav", ".m4a"))]

    if not sound_files:
        print("Error: No sound files available.")
        return

    random_sound = random.choice(sound_files)
    sound_path = os.path.join(sound_folder, random_sound)  # Correctly join folder and filename

    try:
        if not os.path.exists(sound_path):
            print(f"Error: Sound file '{sound_path}' not found.")
            return

        pygame.mixer.init()
        pygame.mixer.music.load(sound_path)  # Use the correct path
        pygame.mixer.music.play()

        # Wait until the sound finishes playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except pygame.error as e:
        print(f"Error playing sound: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")
