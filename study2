from matplotlib import font_manager

import matplotlib.pyplot as plt
from wordcloud import WordCloud

#워드클라우드 모양
from PIL import Image
import numpy as np

path= "C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=path).get_name()

file = open('./data/movie.txt', 'r', encoding='utf-8')
rFile=file.read()

img = Image.open('./data/camera.png')
imgArray = np.array(img)

wordcloud = WordCloud(background_color ='white',
                      mask = imgArray,
                      max_words=1000 ,
                      width = 900,
                      height = 700,
                      random_state = 43,
                      font_path=path ,
                      prefer_horizontal = True).generate(rFile)

plt.figure()
plt.imshow(wordcloud)
plt.axis('off')
plt.title('Movie', size = 16)
plt.savefig('./data/Movie.png') # save
plt.show()
