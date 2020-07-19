
import json
import matplotlib.pyplot as plt

with open('C:/xampp/htdocs/2020-interns/data.json') as f:
  data = json.load(f)

for i in data["rates"].keys():
    inr = data["rates"][i]['INR']    
    print(inr)