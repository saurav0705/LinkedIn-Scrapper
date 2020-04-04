f1 = open('check.txt','r+')
x = f1.read()
x = x.split("\n")

count =0
for el in x:
    if len(el) != 0:
        count=count+1

print(count)