import pickle 

with open('data.pickle', 'wb') as f: 
  pickle.dump(narcotics, f) # writing

with open('data.pickle', 'rb') as f: 
  data = pickle.load(f) # reading
