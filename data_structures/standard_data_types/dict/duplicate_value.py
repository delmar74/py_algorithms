# Exercise
# Swap keys and values. Duplicate values must create a list

dict = {"a": 1, "b": 2, "c": 3, "d": 3, "e": 3}

dict_new = {}
for i in dict:
  t = []
  if dict[i] in dict_new.keys():
    t=[]
    t.append(i)
    for k in dict_new[dict[i]]:
      t.append(k)
    dict_new[dict[i]]=t
  else:
    dict_new[dict[i]]=i

print("Initial data: " + str(dict))
print("New data: " + str(dict_new))
