from matplotlib import pyplot as plt
import wikipedia
from wordcloud import WordCloud,STOPWORDS

def get_wiki(query):

    print('searching')
    title = wikipedia.search(query)[0]
    page = wikipedia.page(title)

    return page.content

query = input('Enter your query for wikipedia\n')

text = get_wiki(query)

wordcloud = WordCloud(stopwords=set(STOPWORDS),width = 1000, height = 500,background_color="white").generate(text)

plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")

plt.show()
