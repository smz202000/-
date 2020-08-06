import urllib.request as re
response=re.urlopen('http://placekitten.com/g/800/600')
cat_img=response.read()
with open('cat_800_600.jpg','wb') as f:
    f.write(cat_img)