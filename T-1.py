import json
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

with open('C:/xampp/htdocs/2020-interns/data.json') as f:
  data = json.load(f)
for i in data["rates"].keys():
    inr = data["rates"][i]['INR'] 
    eur=1
    ax.plot(eur,inr ,color='blue', marker='s')
    ax.set_title('INR Against EUR')
    ax.set(xlabel='EUR', ylabel='INR')