def decorator(*args,**kwargs):
   print("Inside the decorator")
   def wrapper(fun):
       print("Inside the wrapper")
       for i in args:
          print(i)
       return fun     
   return wrapper

@decorator("hello","Mello","Tello")
def fun(*args):
  print("Executing fun")
  for i in args:
     print(i)


if __name__=="__main__":
   fun(1,2,3)
   