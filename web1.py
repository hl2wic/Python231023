# web1.py 
#웹크롤링
from bs4 import BeautifulSoup

#페이지 로딩
page = open("c:\\work2\\test01.html", "rt", encoding="utf-8").read() 
#검색이 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")
#전체 보기 (prettify() 원래 문서를 보여줘)
#print(soup.prettify())
#<P> 태그 전체를 검색
#print(soup.find_all("p"))
# 첫번째 <p> 만 검색
#print(soup.find("p"))
# <p class="outer-text"> 형태만 검색
#print(soup.find_all("p", class_="outer-text"))
#attrs 를 사용
#print(soup.find_all("p", attrs={"class":"outer-text"}))
# 특정 태그만 지정할 경우 id 속성
#print(soup.find_all(id="first"))
# 태그 내부의 컨텐츠를 가져오기 :  .text
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n","")
    print(title)
    


