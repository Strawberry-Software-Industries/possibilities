import sys

class _Empty__:
    "_Empty__"

possabilites=[]
def check(search_in:list=sys.argv,delete_possabilites:bool=False,errorfunc:callable=None):
    global possabilites
    if errorfunc==None:
        def errorfunc(arg):
            print(arg)

    if errorfunc==False:
        def errorfunc(arg):
            pass

    def check_empty(object):
        if object[1]==_Empty__:
            try:
                search_in[object[0]]
            except:
                return True
            return False
        else:
            return False
    
    def chec(object):
        try:
            if isinstance(object[1],str) or object[1] in [_Empty__]:
                if search_in[object[0]]==object[1]:
                    return True
            return False
        except IndexError:
            if check_empty(object):
                return True
            if errorfunc==None:
                errorfunc(f"{object[0]} as Index in sys.argv is empty")
                return False
            else:
                try:
                    errorfunc(f"{object[0]} as Index in sys.argv is empty")
                    return False
                except:
                    return False
    for a in possabilites:
        worked=True
        for b in a:
            if not callable(b):
                if not chec(b):
                    worked=False
        if worked:
            a[len(a)-1]()
    if delete_possabilites:
        possabilites=[]

def add_possability(possability:list):
    """possability is supposed to be a List
    Here is an example how you could call the command:
    add_possability(possability=[[1,"help"],[2,"test"],some_function_you_defined])

    That would mean if the first arg in the sys.argv(of course after the file name) is equal to "help" and the second arg in sys.argv is equal to "test",
    it would call the function you passed in.
    
    If you pass _Empty__ in it will only call the function if the sys.argv at the Index you passed is empty, as an example:
    possability=[[1,_Empty__],some_function_you_defined]

    This would call the function, if the Text in sys.argv at the Index you passed is empty.
    """
    global possabilites
    for a in possability:
        if isinstance(a,list):
            if len(a)==2:
                if isinstance(a[0],int) and (isinstance(a[1],str) or a[1] == _Empty__):
                    pass
                else:
                    possability.pop(possability.index(a))
                    print(f"In {a} At Index 0 is not an integer or at Index 1 is not an string.") 
            else:
                print(f"{a} has not a length of 3")
        elif callable(a) and possability.index(a)+1 == len(possability):
            pass
        else:
            print(f"{a} is not a list")
    if callable(possability[len(possability)-1]):
        possabilites.append(possability)
    else:
        print("Last arg is not callable")

def print_help():
    print("Help")

def print_help_test():
    print("Help Test")

add_possability([[1,"help"],[2,_Empty__],print_help])
add_possability([[1,"help"],[2,"test"],print_help_test])

check(errorfunc=False)
