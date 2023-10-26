# web1.py 
#웹크롤링
from bs4 import BeautifulSoup

#페이지 로딩
page = open("c:\\work2\\test01.html", "rt", encoding="utf-8").read() 
#검색이 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")
#전체 보기 (prettify() 원래 문서를 보여줘)
print(soup.prettify())


