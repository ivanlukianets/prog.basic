import pickle
result_d ={}
data = []
with open("data.csv", "rt") as datafile:
    next(datafile)
    for row in datafile:
        user_inf = [int(i) if (i.isdigit()) else i for i in row[:-1].split(",")]
        if user_inf[3] not in result_d:
            result_d[user_inf[3]] = {}
        for item in result_d:
            if item == user_inf[3]:
                result_d[user_inf[3]][user_inf[5]] =[]
        data.append(row)

for row in data:
    user_inf = [int(i) if (i.isdigit()) else i for i in row[:-1].split(",")]
    result_d[user_inf[3]][user_inf[5]].append(user_inf[0])
    result_d[user_inf[3]][user_inf[5]].append(user_inf[1])
    result_d[user_inf[3]][user_inf[5]].append(user_inf[2])
    result_d[user_inf[3]][user_inf[5]].append(user_inf[4])

with open('serialized_data.pkl', 'wb') as file:
    pickle.dump(result_d, file)