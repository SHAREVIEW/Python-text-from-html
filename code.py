from bs4 import BeautifulSoup


soup = BeautifulSoup(open("/Users/antonmudrak/Desktop/Yan/dnevnik/1941.html"),"html.parser")

for tag in soup.select('div.menu-panel'):
  tag.decompose()
for tag in soup.select('head'):
  tag.decompose()
for tag in soup.select('li'):
  tag.decompose()
for tag in soup.select('p.month-name'):
  tag.decompose()
for tag in soup.select('table.days-of-month'):
  tag.decompose()
for tag in soup.select('div.comment'):
  tag.decompose()
for tag in soup.select('p.source'):
  tag.decompose()
for tag in soup.select('div.notes'):
  tag.decompose()
for tag in soup.select('span'):
  tag.decompose()
for tag in soup.select('script'):
  tag.decompose()

with open('dnevnik.txt', 'a') as f:
    print(soup.get_text(), file=f)
f.close()
