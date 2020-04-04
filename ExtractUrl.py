import re
from bs4 import BeautifulSoup
import operator


def dumpToFile(lst):
    f= open('links-all.txt','a+',encoding="utf-8")
    for l in lst:
        f.write(l+"\n")
    f.close()


fl = open('linkedin-all.txt','r+',encoding="utf-8")
#print(f.read())
x = fl.read()
fl.close()
soup = BeautifulSoup(x, "html.parser")
list1=[]
for a in soup.find_all('a'):
    # print(a['href'])
    list1.append(a['href'])
   
# list_final=[]
# for l in list1:
#     if 'Contact' not in str(l[0]):
#         list_final.append([l[0].get_text(),l[1]])

# print(len(list_final))
# for l in list1:
#     print(l)
# companies = [link.get_text() for link in soup.findAll("a",class_='link')]
# print(companies)
# filterlst = []
# for comp in companies:
#     if(comp.startswith('Pune')):
#         filterlst.append(comp)

        

            
# for lst in filterlst:
#     print(lst)



list1 = set(list1)
for l in list1:
    print(l)
print(len(list1))
dumpToFile(list1)