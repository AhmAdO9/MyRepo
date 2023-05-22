def cal(*numbers):
    # for i in numbers:
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
     


cal(1,2,3,4,5,6,7,8,9)
