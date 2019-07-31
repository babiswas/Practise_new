from functools import wraps

def decorator(fun):
  print("Inside the decorator")
  @wraps(fun)
  def wrapper(*args):
     print(fun.__name__)
     print(fun.__doc__)
     print("Inside the wrapper")
     for i in args:
         print(i)
     return fun(*args)
  return wrapper

@decorator
def test(*args):
  ''' this is awesome'''
  print("fun is the function")
  sum=0
  print(test.__name__)
  print(test.__doc__)
  for i in args:
     sum=sum+i
  return sum

if __name__=="__main__":
  print(test(3,4,5,6))
