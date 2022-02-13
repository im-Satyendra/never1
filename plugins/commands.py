import requests

dmn = "https://v.gd/create.php?format=simple&url={}"
l1 = requests.get(dmn.format("https://ourclg.tech")).text
l2 = requests.get(dmn.format("https://ouhrclg.tech")).text
l3 = requests.get(dmn.format("https://ourhjclg.tech")).text
l4 = requests.get(dmn.format("https://ourdclg.tech")).text
l5 = requests.get(dmn.format("https://ourtyclg.tech")).text
print(l1+"\n"+l2+"\n"+l3+"\n"+l4+"\n"+l5+"\n")