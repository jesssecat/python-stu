def login(usr):
    if usr == 'jesse':
        return True
def wrapper1(funcname):
    print('funcname:',funcname)
    def wrapper2(argv):
        if login(argv):
            print('funcname:',funcname)
            return funcname(argv)
        else:
            return error
    return wrapper2


def home(usr):
    print('this is the home page!')
    print('hello ,',usr)

home = wrapper1(home)
home('jesse')
