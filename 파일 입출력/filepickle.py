import pickle
# data_file=open("data.pickle",'wb')
# profile={'name':'김성중','age':'24','score':[1,3,5,7,9]}
# pickle.dump(profile, data_file)
# data_file.close()

# data_file=open('data.pickle','rb')
# profile=pickle.load(data_file)
# print(profile)
# data_file.close()

with open('data.pickle','rb') as profile:
    print(pickle.load(profile))