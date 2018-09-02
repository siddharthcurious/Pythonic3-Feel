def make_bold(fun):
    def wrapped():
        return "<b>"+str(fun)+"</b>"
    return wrapped

def make_italic(fun):
    def wrapped():
        return "<i>"+str(fun)+"</i>"
    return wrapped

@make_italic
@make_bold
def hello():
    return "hello world"

print(hello())

