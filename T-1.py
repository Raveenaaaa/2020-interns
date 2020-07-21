import json
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

with open('C:/xampp/htdocs/2020-interns/data.json') as f:
  data = json.load(f)
for i in data["rates"].keys():
    inr = data["rates"][i]['INR']    
    eur=data["base"] 
    ax.plot(inr, eur, color='red', linestyle='--', linewidth=2, marker='s')
    ax.show()