import re
import requests
import os
from bs4 import BeautifulSoup
import nltk
import subprocess
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gtts import gTTS
nltk.download('stopwords')
nltk.download('punkt')

# Prompt the user for a subject to search
print("Enter a subject to search for or enter nothing for /random/") 
subject = input()

# Set the search parameters
url = "https://find.4chan.org/?q=" + subject

# Make a request to the website with the search parameters
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the blockquote elements (these contain the search results)
results = soup.find_all("blockquote")

# Create an empty list to store the results with vulgarity scores
results_with_scores = []

# fetch stuff with a website, feel free to uncomment
# Define a list of vulgar words
# url = "https://www.cs.cmu.edu/~biglou/resources/bad-words.txt"
# response = requests.get(url)
# vulgar_words = response.text.splitlines()

with open("Terms-to-Block.csv", "r") as file:
     vulgar_words = file.read().splitlines()


# Loop through each result and calculate its vulgarity score
for result in results:
    text = result.text
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    vulgarity_score = 0
    for word in filtered_words:
        if word.lower() in vulgar_words:
            vulgarity_score += 1
    results_with_scores.append((vulgarity_score, result))

# Sort the results by vulgarity score in descending order, uncomment this.
# results_with_scores = sorted(results_with_scores, key=lambda x: x[0])

# To sort in ascending order uncomment this if you haven't.
results_with_scores = sorted(results_with_scores, key=lambda x: x[0], reverse=True)

# Open a file for writing
with open("results.txt", "w") as file:
    # Write the text of each search result to the file, excluding filenames and thread numbers
    for result in results_with_scores:
        # Find all elements with the class "fileText" (these contain the filenames) and remove them from the result
        for fileText in result[1].find_all(class_="fileText"):
            # Use a regular expression to check if the filename contains a certain file extension
            if re.search(r'\.jpg|\.png|\.gif', fileText.text):
                # If the file extension is found, remove the element from the result
                fileText.extract()
        for fileText in result[1].find_all(class_="sideArrows"):
            # Use a regular expression to check if the filename contains a certain file extension
            if re.search(sideArrows.text):
                # If the file extension is found, remove the element from the result
                fileText.extract()
                text = result[1].text
        # Write the result text and vulgarity score to the file
        file.write(result[1].text + " (Vulgarity Score: " + str(result[0]) + ")\n")

# # Open the file for reading, text only; on by default.


with open("results.txt", "r") as file:
    content = file.readlines()
    output = ""
    for line in content:
        result = line.strip()
        result_with_spaces = result.replace(" ", " ")
        result_with_spaces = re.sub(r'(\b>\b)', r' \1', result_with_spaces)
        result_with_spaces = re.sub(r'(?<=[^\s])(https?://\S+)', r' \1', result_with_spaces)
        result_with_spaces = re.sub(r'(\d+)(?=>)', r'\1 ', result_with_spaces)
        result_with_spaces = re.sub(r'(?<=[^>\d])(>)', r' \1', result_with_spaces)
        result_with_spaces = re.sub(r'^(>>\d+)', r'\1 ', result_with_spaces)
        result_with_spaces = re.sub(r'(?<=[a-z])([A-Z])', r' \1', result_with_spaces)
        output += result_with_spaces + "\n"
    if output.strip():
        print(output)

#     Voice and text output; probably want to keep this disabled unless if you're in a private place; google text to speech, much slower output.
#     OFF BY DEFAULT

# with open("results.txt", "r") as file:
#     content = file.readlines()
#     output = ""
#     for line in content:
#         result = line.strip()
#         result_with_spaces = result.replace(" ", " ")
#         result_with_spaces = re.sub(r'(\b>\b)', r' \1', result_with_spaces)
#         result_with_spaces = re.sub(r'(?<=[^\s])(https?://\S+)', r' \1', result_with_spaces)
#         result_with_spaces = re.sub(r'(\d+)(?=>)', r'\1 ', result_with_spaces)
#         result_with_spaces = re.sub(r'(?<=[^>\d])(>)', r' \1', result_with_spaces)
#         result_with_spaces = re.sub(r'^(>>\d+)', r'\1 ', result_with_spaces)
#         result_with_spaces = re.sub(r'(?<=[a-z])([A-Z])', r' \1', result_with_spaces)
#         output += result_with_spaces + "\n"
#     if output.strip():
#         print(output)
#         tts = gTTS(text=output, lang='en')
#         tts.save("voice.mp3")
#         subprocess.call(["ffplay", "-hide_banner", "-loglevel", "panic", "-i", "voice.mp3", "-af", "volume=0.5"])

#     espeak libaray, much faster than google but doesn't save; again it's disabled/commented out by default.
#     OFF BY DEFAULT

# with open("results.txt", "r") as file:
#     content = file.readlines()
#     output = ""
#     for line in content:
#         result = line.strip()
#         result_with_spaces = result.replace(" ", " ")
#         result_with_spaces = re.sub(r'(\b>\b)', r' \1', result_with_spaces)
#         result_with_spaces = re.sub(r'(?<=[^\s])(https?://\S+)', r' \1', result_with_spaces)
#         result_with_spaces = re.sub(r'(\d+)(?=>)', r'\1 ', result_with_spaces)
#         result_with_spaces = re.sub(r'(?<=[^>\d])(>)', r' \1', result_with_spaces)
#         result_with_spaces = re.sub(r'^(>>\d+)', r'\1 ', result_with_spaces)
#         result_with_spaces = re.sub(r'(?<=[a-z])([A-Z])', r' \1', result_with_spaces)
#         output += result_with_spaces + "\n"
#     if output.strip():
#         print(output)
#         subprocess.call(["espeak", "-v", "en-us", "-w", "voice.wav", output], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
#         subprocess.call(["ffmpeg", "-y", "-i", "voice.wav", "voice.mp3"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
#         subprocess.call(["ffplay", "voice.mp3"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Remove the files
# os.remove("results.txt")
# os.remove("voice.mp3")
# os.remove("voice.wav")
