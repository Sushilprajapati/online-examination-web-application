s = 'hello'
def r():
    global s
    s = "man"
    print(s)
def p():
    print(s)
r()
p()

