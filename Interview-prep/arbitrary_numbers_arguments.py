def function1(*args):
    for a in args:
        print(a)

function1(1,2,3,4)

def function2(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

function2(a="a", b="2", k="6")

def function3(kwargs):
    for k, v in kwargs.items():
        print(k, v)

d = {
    "a":1,
    "b":2,
    "c":3,
    "d": 4
}
function3(d)