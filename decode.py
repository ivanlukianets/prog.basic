import pickle
with open('serialized_data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    print("Info from file:", loaded_data)