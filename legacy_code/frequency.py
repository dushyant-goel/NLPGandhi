from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
stopwords = set(STOPWORDS)
stopwords.add('wa')
stopwords.add('will')
stopwords.add('may')
stopwords.add('us')
import operator

def show_wordcloud(data, title = None):
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        max_words=200,
        max_font_size=40, 
        scale=3,
        random_state=1,
        collocations=False 
    ).generate(str(data))

    sorted_d = sorted(wordcloud.words_.items(), key=operator.itemgetter(1), reverse=True)              
    plt.bar(*zip(*sorted_d[:10]))
    plt.show()

#    fig = plt.figure(1, figsize=(12, 12))
#    plt.axis('off')
#    if title: 
#        fig.suptitle(title, fontsize=20)
#        fig.subplots_adjust(top=2.3)
#
#    plt.imshow(wordcloud)
#    plt.show()

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
