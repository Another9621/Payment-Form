
'''
x="local"
def ok():
    global x
    x="non local"    
    print("inner x" ,x)
ok()
print("outer x",x)
def nope():
    print("inside other:",x)
nope()
'''
x={}
def ok():
    global x
    x={'name':'megha'}
    print("inner:",x)
ok()
print("outer x:",x)
def nope():
    print("inside other:",x)
nope()
