import requests as requests
import matplotlib.pyplot as plt
import re
import time
num=[]
plt.ion()
while (1):
    response = requests.get("https://api.bilibili.com/x/relation/stat?vmid=777536&jsonp=jsonp")
    it = re.findall(r"\"follower\":(.*?)}}",response.text)
    num.append(it[0])
    plt.clf()
    plt.plot(num)
    plt.gca().invert_yaxis()
    plt.locator_params(nbins = 10)
    plt.pause(0.1)
    plt.ioff()
    print(it[0])
    time.sleep(1)
