# import requests
#
# from bs4 import BeautifulSoup
#
# actno = input()
# url = input()
# href = []
# r = requests.get(url)
# soup = BeautifulSoup(r.content, 'html.parser')
# atags = soup.find_all('a')
# for i in atags:
#     hrefs = i.get('href')
#     href.append(hrefs)
# # for j in href:
# #     if j == f"#act{int(actno) - 1}":
# #         print(j)
# print(href[actno - 1])
#
# import requests
#
# from bs4 import BeautifulSoup
#
# actno = input()
# url = input()
# titles = []
# r = requests.get(url)
# soup = BeautifulSoup(r.content, 'html.parser')
# # print(soup)
# tags = soup.find_all('h2')
# # print(tags)
# for i in tags:
#     texts = i.text
#     # print(texts)
#     titles.append(texts)
# print(titles[actno])