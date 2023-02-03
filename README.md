# How to use

First install the needed dependancy with python pip if you haven't already such as ```pip install nltk```
Then run ``python 4score.py``, the results will be saved as ``results.txt`` results can be viewed after running the script; if you'd like to view the results again enter in your terminal of choice ``cat results.txt`` or open it in a text editor; alternatively you may uncomment ``# os.remove("results.txt")`` to let the script delete the file after printing.

Addtionaly you may edit the python script to use an online wordlist; that will be pointed out inside the script if you ever decide to open it.

## Able to read text with audio output

you'll need to install the depenedancy for google text to speech such as:
~~mpg123~~ ``ffmpeg`` and ``ffplay`` and you should be set!

This would be only used for text only; on by default; comment it out if using voice.

    # Open the file for reading, text only; on by default.

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

These are the lines for audio output

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
    

## To sort by asending or desending order comment or uncomment one of these lines:

   
    # Sort the results by vulgarity score in descending order, uncomment this.
    # results_with_scores = sorted(results_with_scores, key=lambda x: x[0])

    # To sort in ascending order uncomment this if you haven't.
    results_with_scores = sorted(results_with_scores, key=lambda x: x[0], reverse=True)
    
    
    
## To use either the local file for vulgarity or an online file you could uncomment/comment one of these line


    # fetch stuff with a website, feel free to uncomment
    # Define a list of vulgar words
    # url = "https://www.cs.cmu.edu/~biglou/resources/bad-words.txt"
    # response = requests.get(url)
    # vulgar_words = response.text.splitlines()

      with open("Terms-to-Block.csv", "r") as file:
      vulgar_words = file.read().splitlines()
    
## And to have the files be removed after execution uncomment these two lines at the end of the script

    # Remove the files
    # os.remove("results.txt")
    # os.remove("voice.mp3")
    # os.remove("voice.wav")
