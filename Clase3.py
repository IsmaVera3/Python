import pprint

myCat = {'tamano': 'gordo', 'edad': 10}

myCat['edad'] = 20
 
pprint.pprint(myCat)

print(myCat.values())
print(myCat.keys())

for i in myCat.items():
    print(i)

#res = requests.get('https://  .com')

#for chunk in res.iter_content(100000):
    print('hola')


import requests

image = requests.get("https://brockhoferart.com/meta-pcs-case")


playFile = open('imagenes.html', 'wb')

for chunk in image.iter_content(100000):
    playFile.write(chunk)





playFile.close()