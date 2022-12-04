# Реализуйте алгоритм перемешивания списка.

import random
  
list = [1, 3, 5, 7, 9]
print ('Оригинал: ' + str(list))
  
for i in range(len(list)-1, 0, -1):
    j = random.randint(0, i + 1)  
    list[i], list[j] = list[j], list[i] 
      
 
print ("Перемешанный : " +  str(list))