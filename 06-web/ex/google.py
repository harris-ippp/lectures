api = "https://maps.googleapis.com/maps/api/"

geoc = "geocode/json?address=Harris School"
dire = "directions/json?origin=Philadelphia&" + \
       "destination=Chicago"
dist = "distancematrix/json?origins=Chicago,IL|" + \
       "Tucson,AZ&destinations=Philly"

key  = "&key=YOUR_KEY"

j = requests.get(api + geoc).json()

