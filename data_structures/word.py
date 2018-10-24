def polidrom(word):
    length = len(word)
   
    print(half)
    flag = True # True - success, False - unsuccess
    for i in range (0, length/2-1):
	print(word[i]+" "+word[length-i-1])
        if word[i] != word[length-i-1]:
            flag = False    
    return flag


res = polidrom("poliAAilep")
print(res)
