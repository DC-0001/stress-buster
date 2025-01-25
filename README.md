# *Stress Buster & Therapy Personalization*

This project is a personalized stress relief and therapy assistant. Using Mira SDK, it analyzes user mood, provides therapeutic responses, and personalizes therapy sessions based on user feedback. It also fetches calming images and plays relaxing sounds to enhance user experience.

---

## *Table of Contents*
1. [About the Project](#about-the-project)
2. [Features](#features)
3. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
4. [Usage](#usage)
5. [Technologies Used](#technologies-used)
6. [Project Structure](#project-structure)
7. [License](#license)
8. [Contact](#contact)

---

## *About the Project*
This project is designed to improve mental well-being by:
- Understanding user emotions through conversational input.
- Offering tailored therapy steps based on mood analysis.
- Personalizing therapy sessions based on user feedback.
- Providing additional relaxation aids like calming images and soothing music.

---

## *Features*
- *Mood Analysis*: Analyzes user input to assess their emotional state.
- *Therapy Personalization*: Tailors therapy steps based on user feedback.
- *Relaxation Tools*:
  - Fetches URLs for calming images.
  - Plays relaxing sounds.
- *Error Handling*: Handles API or flow execution errors gracefully.

---

## *Getting Started*

### *Prerequisites*
Ensure you have the following installed on your system:
- Python 3.8 or later
- pip (Python package manager)

Install required libraries:
bash
pip install mira_sdk python-dotenv


### *Installation*
1. Clone the repository:
   bash
   git clone https://github.com/your-username/stress-buster.git
   
2. Navigate to the project directory:
   bash
   cd stress-buster
   
3. Set up environment variables:
   - Create a .env file in the root directory.
   - Add your Mira API key:
     
     MIRA_API_KEY=your-api-key-here
     

4. Ensure the required external scripts (image_fetch.py and sound_player.py) are in the project directory.

---

## *Usage*
1. Run the main script:
   bash
   python main.py
   
2. Follow the prompts to:
   - Share how your day is going.
   - Receive therapy suggestions.
   - Provide feedback for personalized therapy.
3. View calming images and listen to relaxing music as part of the experience.

---

## *Technologies Used*
- *Programming Language*: Python
- *Libraries*:
  - mira_sdk for flow execution.
  - dotenv for environment variable management.
- *External Scripts*:
  - image_fetch.py: Fetches calming images.
  - sound_player.py: Plays relaxing sounds.

---

## *Project Structure*

stress-buster/
|
├── main.py                  # Main script for the project
├── image_fetch.py           # Script to fetch calming images
├── sound_player.py          # Script to play relaxing sounds
├── .env                     # Environment variables
└── README.md                # Project documentation


---

## *License*
This project is licensed under the MIT License.

---

## *Contact*
- *Developer*: Your Name
- *Email*: your-email@example.com
- *GitHub*: [your-username](https://github.com/your-username)

---
