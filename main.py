# # 샘플 Python 스크립트입니다.
#
# # Ctrl+F5을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# # 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 Shift 두 번을(를) 누릅니다.
#
#
# def print_hi(name):
#     # 스크립트를 디버그하려면 하단 코드 줄의 중단점을 사용합니다.
#     print(f'Hi, {name}')  # 중단점을 전환하려면 F9을(를) 누릅니다.
#
#
# # 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조



txt = """서울 시내 대중교통 무임승차 제도가 전면 개편된다. 지하철을 무료로 이용할 수 있는 나이가 현행 65세에서 70세로 높아지는 대신, 그동안 혜택이 없던 시내버스와 마을버스가 무임승차 대상에 새로 포함된다.
 
24일 서울시의회는 본회의를 열고 이러한 내용을 담은 ‘서울시 어르신 교통비 지원 조례안’을 찬성 69명, 반대 1명으로 통과시켰다. 65세 기준으로 묶여 있던 1980년대식 교통 복지 제도가 인구 고령화 현실에 맞춰 약 40년 만에 개편되는 셈이다.
 
◆ 지하철 재원 활용해 버스 지원…추가 세금 없는 구조
 
이번 개편의 핵심은 효율적인 재배치다. 지하철을 이용하기 어려운 사각지대에 거주하는 고령층에게도 고르게 교통 복지를 제공한다는 취지다.
 
재정 부담은 지하철 연령 상향으로 해결한다. 서울시 추산에 따르면 70세 이상 시민에게 버스 요금을 지원하는 데 연간 약 525억 원이 소요된다. 반면 지하철 무임승차 연령을 70세로 올리면 약 572억 원의 운임 수입이 새로 발생한다. 지하철에서 아낀 재원으로 버스 요금을 지원하는 방식이어서 추가 재원 없이도 시행할 수 있다.
 
◆ ‘월 14회’ 한도 설정…무제한 탑승에 따른 재정 부담 방지
 
다만 과도한 재정 지출을 막기 위한 안전장치도 마련했다. 어르신들의 버스 무임승차 횟수는 ‘월 최대 14회’로 제한된다.
 
한 달에 15번 이상 버스를 탈 경우에는 정부의 대중교통 환급 서비스인 ‘K-패스’를 이용하면 된다. 서울시는 K-패스 환급금을 통해 초과 이용분에 대한 부담을 덜 수 있도록 연계할 방침이다.
 

24일 서울역버스환승센터. 연합뉴스
 
◆ 노인회도 연령 상향 동의…이르면 내년부터 전면 시행
 
지하철 무임승차 연령을 실제로 올리려면 조례 개정 등 추가 절차가 남아 있다. 그러나 전망은 밝은 편이다. 복지 축소에 반발할 것으로 예상됐던 대한노인회 서울시연합회가 오히려 “지속 가능성을 위해 연령 상향을 함께 조정하자”며 전향적인 입장을 밝혔기 때문이다.
 
서울시는 다음 달 초 어르신과 전문가, 시민들이 참여하는 공청회를 열고 구체적인 도입 시기를 논의한다. 사회적 합의가 순조롭게 이뤄진다면 이르면 내년부터 서울의 대중교통 무임승차 기준이 완전히 바뀔 것으로 보인다."""


import re
clean_text = re.sub(r"[^가-힣\s]", "", txt)
# print(clean_text)

from konlpy.tag import Okt
okt = Okt()
nouns = okt.nouns(clean_text)

stopwords = ["것", "수", "등", "더", "이", "그", "저", "및", "등"]
filtered = [w for w in nouns if w not in stopwords and len(w) > 1]

from collections import Counter
counter = Counter(filtered)
top20 = counter.most_common(20)


import torch
words = [w for w, c in top20]
counts = [c for w, c in top20]
tensor_counts = torch.Tensor(counts)

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import random


pink_colors = [
    "#87CEEB",  # 스카이 블루
    "#76D7EA",
    "#B0E0E6",  # 파우더 블루
    "#ADD8E6",  # 라이트 블루
    "#A2D2FF",
    "#CDE7FF",  # 연하늘
    "#BEE9FF"  # 파스텔 하늘
]
def pink_color_func(*args, **kwargs):
    return random.choice(pink_colors)
img= Image.open('./images/heart.png')
imgArray = np.array(img)


wc = WordCloud(
    font_path = r"C:/Windows/Fonts/malgun.ttf",
        width=1000,
        height=800,
        background_color="#F0F8FF",
        colormap = "Set3",
    max_font_size= 100,
    mask = imgArray
)

wc.generate_from_frequencies(dict(top20))
wc.recolor(color_func=pink_color_func)


# 그래프 크기를 설정합니다.
plt.figure(figsize=(12, 8))

# 워드 클라우드 이미지를 화면에 표시합니다.
# plt.figure(figsize=(10,10))

# 축 눈금을 제거합니다.
plt.axis("off")

# 제목을 설정합니다.
plt.title("Word Cloud")
plt.imshow(wc)

# 그래프를 출력합니다.
plt.show()