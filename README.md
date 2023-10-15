# Jarvis Voice-Controlled Assistant

Jarvis is a voice-controlled assistant that can perform various tasks, including web browsing, playing music, and interacting with the OpenAI GPT-3 model.

## Prerequisites

Before running the Jarvis assistant, you'll need to set up the necessary dependencies and configuration. Make sure you have:

- Python installed
- Required Python libraries: speech_recognition, pyttsx3, openai, dotenv
- An OpenAI GPT-3 API key

## Installation

1. Clone this repository:

   ```shell
   git clone https://github.com/OmkarSangaonkar/jarvis-voice-assistant.git

2. Install the required Python libraries:
   ```shell
   pip install -r requirements.txt

3. Set up your OpenAI API key by creating a .env file and adding your API key:
   ```shell
   OPENAI_API_KEY=your_api_key_here


## Usage

To use the Jarvis voice-controlled assistant, follow these steps:

1. Run the Python script:

   ```shell
   python main.py

Jarvis will listen for voice commands. You can interact with Jarvis using the following commands:

- **"Open [website name]"**: Opens the specified website in your default web browser.
- **"Chatbot, [your question]"**: Interacts with the OpenAI GPT-3 chatbot and saves the response to a text file.
- **"Play music"**: Plays a predefined music file.
- **"What's the time?"**: Jarvis will tell you the current time.

You can extend Jarvis's capabilities by adding more voice commands and functionalities.

## Voice Command Examples

Here are some examples of voice commands you can use with Jarvis:

- **"Open YouTube"**
- **"Open Wikipedia"**
- **"Chatbot, write code for a REST API in Python."**
- **"Play music"**
- **"What's the time?"**

Feel free to add your own voice commands to extend Jarvis's functionality.

