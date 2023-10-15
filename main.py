import speech_recognition as sr
import os
# import pyttsx3
import webbrowser
import win32com.client

import time
import random
import re

import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)


# say("Hello, this is a Windows TTS test.")


def takeCommand():
    r = sr.Recognizer()  # Create a recognizer instance
    with sr.Microphone() as source:
        audio = r.listen(source)

        # r.pause_threshold = 0.8

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query
    except Exception as e:
        print(e)
        return "error while speech try again"


# for file naming
def extract_keywords(query):
    # Define a list of stopwords to filter out unimportant words
    stopwords = ["give", "me","information","suggest","the", "a", "an", "for", "about", "with", "to", "in", "on", "as", "chatbot"]

    # Tokenize the query and remove punctuation and stopwords
    words = re.findall(r'\b\w+\b', query.lower())
    keywords = [word for word in words if word not in stopwords]

    # Use the first three keywords to create the file name
    file_name = " ".join(keywords[:3])

    return file_name


# CREATE FUNCTION AND STORE OPEN AI SKELETON FOR GETTING RESPONSE IN IT

def ai(prompt):
    openai.api_key = api_key
    text = f"openai response for content : {prompt} \n ************ \n\n"

    openai.api_key = os.getenv("OPENAI_API_KEY")

    user_message = {
            "role": "user",
            "content": prompt
            }

    # Define the assistant's response as a message
    assistant_message = {
            "role": "assistant",
             "content": "Subject: Application for Fresher Web Developer Position\n\nDear Hiring Manager,\n\nI am writing to apply for the position of Fresher Web Developer at [Company Name]. As a recent graduate with a strong technical background, I am eager to kickstart my career in the field and believe that [Company Name] would be an ideal place for me to grow and further develop my skills.\n\nI have always been passionate about web development and pursued a Bachelor's degree in Computer Science with a focus on web technologies. During my studies, I gained a solid understanding of HTML, CSS, JavaScript, and PHP, and successfully completed several projects demonstrating my ability to design and develop responsive web applications.\n\nAdditionally, I have hands-on experience using frameworks such as Bootstrap and jQuery, along with a familiarity with content management systems like WordPress and Drupal. I have a keen eye for design and enjoy creating visually appealing and user-friendly interfaces.\n\nIn order to stay up-to-date with the latest industry trends and technologies, I have also taken online courses and attended workshops on topics such as web accessibility and responsive design. I am a quick learner and always strive to expand my knowledge and skills to deliver high-quality results.\n\nDuring my time as a student, I actively participated in team projects, which fostered my collaborative and communication abilities."
             }

    # Combine user and assistant messages
    messages = [user_message, assistant_message]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # Define the user's query as a message

        messages=messages,
        temperature=1,
        max_tokens=350,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Access the assistant's reply from the response
    assistant_reply = response['choices'][0]['message']['content']
    # print(assistant_reply)

    query_keywords = extract_keywords(prompt)
    file_name = f"openai/{query_keywords}.txt"

    if not os.path.exists("openai"):
        os.mkdir("openai")

    with open(f"{file_name}", "w") as f:
        f.write(assistant_reply)


# def ai(prompt):
#     openai.api_key = api_key
#
#     response = openai.Completion.create(
#         engine="text-davinci-002",  # You can use the engine you prefer
#         prompt=prompt,
#         temperature=1,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#
#     generated_text = response.choices[0].text
#     # print(generated_text)
#
#     if not os.path.exists("openai"):
#         os.mkdir("openai")
#
#     query_keywords = extract_keywords(prompt)
#
#     # Generate a random file name
#     file_name = f"{query_keywords}.txt"
#     # print(f"File Name: {file_name}")
#
#     # Create and write the text file in the "openai" folder
#     file_path = os.path.join("openai", file_name)
#     # print(f"File Path: {file_path}")
#
#     with open(file_path, "w") as f:
#         f.write(generated_text)
#



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')
    say("hello this is jarvis ai")

    while True:
        print("listening..")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.org/"],
                 ["google", "https://www.google.com"]]
        # say(query)
        for site in sites:
            if f"open {site[0]}" in query.lower():
                say(f"opening {site[0]} sir")
                webbrowser.open(f"{site[1]}")

        if "chatbot".lower() in query.lower():
            ai(prompt=query)



        if f"play music" in query.lower():
            musicpath = r'F:\All Coding Practice\2023\PythonCWH PROJ\JARVIS\OneRepublic.mp3'
            os.startfile(musicpath)

        if "the time" in query.lower():
            hour = time.strftime("%H")
            min = time.strftime("%M")
            say(f" its {hour} and  {min} minutes sir. ")
