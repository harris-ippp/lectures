import requests, json

# we'll cover this in a few weeks.
j = requests.get("...").json

# writing to a file
with open("narcotics.json", "w") as out: 
  out.write(json.dumps(j, indent=2))

# reading a file
with open("narcotics.json") as data: 
  narcotics = json.load(data)
