import pickle

a = open("sample.txt","rb")

read = pickle.load(a)

print(read)
a.close()