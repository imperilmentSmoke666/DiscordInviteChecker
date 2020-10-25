import requests
import random

count = int(input("How many urls would you like to try :"))

created_url = []

for i in range(count):
    base_url = 'https://discord.gg/'
    char_set = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    url_extension = ''.join((random.choice(char_set) for x in range(7))).strip()
    created_url.append(base_url + url_extension)

for url in created_url:
    r = requests.get(url)
    if 'content="website"' in r.text:
        print("Fail", r.url)
    else:
        print("works", r.url)
        with open("works.txt", 'a') as fp:
            fp.writelines(r.url)
