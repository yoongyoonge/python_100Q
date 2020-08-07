from konlpy.tag import Hannanum 
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 텍스트 파일 열기
text = open('./code/data/news_20200807_kor.txt', encoding='UTF-8').read()

# 한글 형태소 분석하기
engin = Hannanum()
nouns = engin.nouns(text)
nouns = [n for n in nouns if len(n) > 1]

# 단어 숫자 세기
count = Counter(nouns)
tags = count.most_common(50)

# 워드클라우드 이미지 생성하기
wordcloud = WordCloud(font_path='c:/Windows/Fonts/malgun.ttf', background_color='white', width=1200, height=800).generate_from_frequencies(dict(tags))

# 화면에 출력하기
fig = plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')

# SVG 객체로 이미지 저장하기
plt.savefig('./code/2. data_graph/output/news_20200807_kor.svg')