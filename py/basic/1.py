list_1 = ["a", "b", "c", "d", "e"]

list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

dict_1 = {}

for key, value in zip(list_1, list_2):
    dict_1["obj_"+str(key)] = value

print(dict_1)
