# How to use

First install the needed dependancy with python pip if you haven't already such as ```pip install nltk```
Then run ``python 4score.py``, the results will be saved as ``results.txt`` results can be viewed after running the script; if you'd like to view the results again enter in your terminal of choice ``cat results.txt`` or open it in a text editor; alternatively you may uncomment ``# os.remove("results.txt")`` to let the script delete the file after printing.

Addtionaly you may edit the python script to use an online wordlist; that will be pointed out inside the script if you ever decide to open it.

## Able to read text with audio output

you'll need to install the depenedancy for google text to speech such as:
~~mpg123~~ ``ffmpeg`` and ``ffplay`` and you should be set!

be sure to uncomment these following lines too; be sure to comment the lines above it IE

    with open("results.txt", "r") as file:
    # Read the contents of the file
    file_contents = file.read()
    # Print the contents of the file
    print(file_contents)

These are the lines for audio output

    with open("results.txt", "r") as file:
    # Read the contents of the file
    file_contents = file.read()
    # Print the contents of the file
    print(file_contents)
    # Generate the voice
    tts = gTTS(text=file_contents, lang='en')
    # Save the voice to a file
    tts.save("voice.mp3")
    # Play the voice
    os.system("mpg123 voice.mp3")
    

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
