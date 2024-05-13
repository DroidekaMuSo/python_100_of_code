def add(*args):
  
  sum = 0 
  for n in args:
    sum += n

  return sum

# add(1,2,3,4,5,6,8,9,)


def calculate(n, **kwargs):
  print(kwargs)
  for key, value in kwargs.items():
    print(key)
    print(value)

  n += kwargs["add"]
  n *= kwargs["multiply"]

calculate(2, add=3, multiply=5)
