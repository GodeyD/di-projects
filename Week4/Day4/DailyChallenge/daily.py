
matrix = ([ 
   [7,'i',3],
    ['T','s','i'],
    ['h','%','x'],
    ['i','#'],
    ['s','M'], 
    ['$','a'], 
    ['#','t','%'],
    ['^','r','!'],
        ])

array = matrix[2][1].isalpha()
idx = 0
secret_message: str = str('')

def indexx(lis):
  if len(lis) == 3:
    return idx
  elif len(lis) == 2 and idx == 0 or len(lis) == 2 and idx == 1:
    return idx
  else:
    lis += [0]
    return idx
for n in range(3):
  for lis in matrix:  
    if str(lis[indexx(lis)]).isalpha() == True:    
      secret_message += str(lis[indexx(lis)])
  idx += 1
  

print(secret_message)
