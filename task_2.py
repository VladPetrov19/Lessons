#2
def joiner(*args, **kwargs):
    print(args, kwargs)

joiner(6, 'world', True, [43, 88, 5], '99', 1, 2, 3, a=7, b='hello', c=9)

#2.1
def joiner(*args,**kwargs):
    print(args,kwargs)

k = 'position'
v = 'teacher'
joiner(k=v)
