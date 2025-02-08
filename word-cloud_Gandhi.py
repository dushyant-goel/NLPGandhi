from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Define stopwords to be removed from the word cloud
stopwords = set(STOPWORDS)
stopwords.add('wa')


def show_wordcloud(data, title = None):
    """Generate and display a wordcloud from the given text data."""
    
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
    
    if title: 
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

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
