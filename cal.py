#add function
def add(x,y):
    return x+y

#subtract function
def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y==0:
        raise ValueError("Can't didvide by zero")
    return x/y
