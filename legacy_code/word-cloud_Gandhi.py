from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
<<<<<<< HEAD:legacy_code/word-cloud_Gandhi.py

# Define stopwords to be removed from the word cloud
stopwords = set(STOPWORDS)
stopwords.add('wa')


def show_wordcloud(data, title = None):
    """Generate and display a wordcloud from the given text data."""
    
=======
stopwords = set(STOPWORDS)
stopwords.add('wa')

def show_wordcloud(data, title = None):
>>>>>>> june-10-presentation:code/word-cloud_Gandhi.py
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        max_words=200,
        max_font_size=40, 
        scale=3,
        random_state=1,
        collocations=False 
    ).generate(str(data))

    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')
<<<<<<< HEAD:legacy_code/word-cloud_Gandhi.py
    
=======
>>>>>>> june-10-presentation:code/word-cloud_Gandhi.py
    if title: 
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

<<<<<<< HEAD:legacy_code/word-cloud_Gandhi.py
    plt.imshow(wordcloud) # Display Word Cloud
    plt.show()

# Function to process text from files and clean it
def process_text(volumes):
    """Reads and cleans text data from a list of volumes."""
    text = ""
    for n in volumes:
        file = f"./data/Corpus_txt/mahatma-gandhi-collected-works-volume-{n}.txt"
        with open(file, "r") as file_pointer:
            file_text = file_pointer.read()
            # Remove common unwanted words
            for word in ['Mahatma', 'Gandhi', 'COLLECTED', 'MAHATMA', 'GANDHI', 'WORKS', 'LETTER', 'photostat']:
                file_text = file_text.replace(word, '')
            text += file_text
    return text


show_wordcloud(process_text(range(1, 15)), title="Gandhi in South Africa")
show_wordcloud(process_text(range(15, 62)), title="Gandhi as a Congress Worker")
show_wordcloud(process_text(range(62, 99)), title="Gandhi as a National Leader")
=======
    plt.imshow(wordcloud)
    plt.show()

sent = ""
for n in range(1,15):
    file = "../Data/Corpus_txt/mahatma-gandhi-collected-works-volume-" + str(n) + ".txt"
    file_pointer = open(file,"r")
    file_text = file_pointer.read()
    file_text = file_text.replace('Mahatma','')
    file_text = file_text.replace('Gandhi','')
    file_text = file_text.replace('COLLECTED','')
    file_text = file_text.replace('MAHATMA','')
    file_text = file_text.replace('GANDHI','')
    file_text = file_text.replace('WORKS','')
    file_text = file_text.replace('LETTER','')
    file_text = file_text.replace('photostat','')
    sent += file_text
	
show_wordcloud(sent)

sent = ""
for n in range(15,62):
    file = "../Data/Corpus_txt/mahatma-gandhi-collected-works-volume-" + str(n) + ".txt"
    file_pointer = open(file,"r")
    file_text = file_pointer.read()
    file_text = file_text.replace('Mahatma','')
    file_text = file_text.replace('Gandhi','')
    file_text = file_text.replace('COLLECTED','')
    file_text = file_text.replace('MAHATMA','')
    file_text = file_text.replace('GANDHI','')
    file_text = file_text.replace('WORKS','')
    file_text = file_text.replace('LETTER','')
    file_text = file_text.replace('photostat','')
    sent += file_text
    
show_wordcloud(sent)

sent = ""
for n in range(62,99):
    file = "../Data/Corpus_txt/mahatma-gandhi-collected-works-volume-" + str(n) + ".txt"
    file_pointer = open(file,"r")
    file_text = file_pointer.read()
    file_text = file_text.replace('Mahatma','')
    file_text = file_text.replace('Gandhi','')
    file_text = file_text.replace('COLLECTED','')
    file_text = file_text.replace('MAHATMA','')
    file_text = file_text.replace('GANDHI','')
    file_text = file_text.replace('WORKS','')
    file_text = file_text.replace('LETTER','')
    file_text = file_text.replace('photostat','')
    sent += file_text
    
show_wordcloud(sent)
>>>>>>> june-10-presentation:code/word-cloud_Gandhi.py
