import requests # 크롤링 요청할 때 사용.(API 사용시 필요)
from bs4 import BeautifulSoup # 긁어 온 데이터를 잘 뽑아내기 위한 라이브러리

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#old_content > table > tbody > tr') # 웹에서 필요한 정보 우클릭 > 검사 > 해당영역 우클릭 > copy > copy selector

for tr in trs:
    a_tag = tr.select_one('td.title > div > a')
    if a_tag is not None:
        rank = tr.select_one('td:nth-child(1) > img')['alt']
        title = a_tag.text
        star = tr.select_one('td.point').text
        print(rank, title, star)
