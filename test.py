import requests
c ="((1[0-9][0-9]\.)|(2[0-4][0-9]\.)|(25[0-5]\.)|([1-9][0-9]\.)|([0-9]\.)){3}((1[0-9][0-9])|(2[0-4][0-9])|(25[0-5])|([1-9][0-9])|([0-9]))"
print("正则匹配IP：",c)
f = open("test.txt","r")
a=[]
for i in f.readlines():
    a.append(i.strip())
for x in range(len(a)):
    try:
        code = requests.get(a[x],timeout=5).status_code
        print(a[x], code)
    except:
        print (a[x],"链接超时")
f.close()
