# possibilities 
**Difficulties using sys.argv? possibility helps you! By Strawberry Software**

# What is possibilities?
possibilities is a simple python framework to easily use sys.argv!

# How can I install possibilities?


```py
from possibilities.main  import  add_possability, check, _Empty__  

def print_help():    
print("Help")

def print_help_test():
print("Help Test")

def print_help_test_project():
print("Help Test Project")
    
add_possability([[1,"help"],[2,_Empty__],print_help])
add_possability([[1,"help"],[2,"test"],[3,_Empty__],print_help_test])
add_possability([[1,"help"],[2,"test"],[3, "project"],print_help_test_project])
    
check(errorfunc=False)
```
