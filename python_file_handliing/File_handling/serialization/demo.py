import pickle
a  = open("sample.txt","wb")

dict1 = {"one":1,"two":2}

serialization = pickle.dump(dict1,a)

a .close()



