from urllib.request import urlopen
from urllib.error import HTTPError 
from bs4 import BeautifulSoup

# 예외 상황에 대응하기.
def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e: # 페이지를 찾을 수 없거나, URL 해석에서 에러가 생긴 경우
        return None
    try:
        bs = BeautifulSoup(html, 'html.parser')
        title = bs.body.h1
    except AttributeError as e: # bs.body.h1 태그가 존재하지 않을 경우
        return None
    return title

title = get_title("http://www.pythonscraping.com/pages/page1.html")
if title:
    print(title)
else:
    print('Title을 찾을 수 없습니다.')


# findAll 함수 써서 특정 class 속에 들어간 텍스트만 끄집어오기.
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html, 'html.parser')

# HTML문서에서 녹색과 빨간색 태그를 '모두' 반환한다.
name_list = bs.findAll('span', {'class': {'green', 'red'}})
for name in name_list:
    print(name.get_text()) # 태그를 제거하고 유니코드 문자열만 반환. 항상 마지막에만 써야한다.