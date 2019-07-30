def decorator(*args,**kwargs):
   print("Inside decorator")
   def wrapper(fun):
      for i in args:
         print(i)
      return fun
   return wrapper

@decorator("hello")
def fun():
   print("fun executed")

if __name__=="__main__":
   fun()


