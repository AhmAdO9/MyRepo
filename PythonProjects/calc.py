def cal(*numbers):
   x =  list(numbers)
   y = len(x)
   count = 0
   while count < y:
      if count == (y-1):
         return(print(p))
      p = x[0]*x[1]
      x.pop(0)
      x.insert(0,p)
      x.pop(1)
      count +=1
   print(p)
     


cal(34,45,56,34)
