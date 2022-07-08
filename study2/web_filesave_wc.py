import time
from urllib.request import urlopen
from bs4 import BeautifulSoup

import nltk
from nltk import tokenize
from nltk.sentiment.vader import  SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from matplotlib import font_manager,rc

#워드클라우드 모양
from PIL import Image
import numpy as np

nltk.download('vader_lexicon')
nltk.download('punkt')

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# https://www.imdb.com/
url = 'https://www.imdb.com/title/tt4154756/reviews?ref_=tt_ql_3'
print(url)
webpage = urlopen(url)
source = BeautifulSoup(webpage, 'html.parser', from_encoding='utf-8')
#---------------------------------------------------------------------------------------------

review_list = source.findAll('div', {'class': 'imdb-user-review'})
sid = SentimentIntensityAnalyzer()  
sum_review = ''   
 
print('=' * 100, end='처리확인처리확인')
print()
for review in review_list:
    content=review.find('div', {'class': 'text show-more__control'}).get_text()

    sum_review = sum_review + content    
    print(sum_review)

print('- ' * 50)
print('imdb영화 어벤져스 시리즈 ')

def my_wordcloud(text):  # 워드클라우드 만드는 부분
    print('-------------워드클라우드 그리는중-----------------------------------')
    img = Image.open('./data/camera.png')
    imgArray = np.array(img)

    # cloud = WordCloud(rc('font', family=font_name),
    #     width=2400, height=1800,
    #     ranks_only=None,
    #     relative_scaling = 0.8,
    #     stopwords = set(STOPWORDS)
    #     ).generate(text)

    cloud = WordCloud(rc('font', family=font_name),
                        background_color='white',
                        mask=imgArray,
                        max_words=1000,
                        width=900,
                        height=700,
                        random_state=43,
                        prefer_horizontal=True).generate(text)

    plt.imshow(cloud)
    plt.axis("off")
    plt.title('Movie', size=12)
    plt.savefig('./data/Movie_infi.png')  # save
    print('-------------워드클라우드 종   료 -----------------------------------')
    plt.show()  

def sFile(text):
    f = open('./data/movie.txt','w')
    f.write(text)
    time.sleep(2)
    print("txt file save done!!")
    f.close()


my_wordcloud(sum_review)
sFile(sum_review)
