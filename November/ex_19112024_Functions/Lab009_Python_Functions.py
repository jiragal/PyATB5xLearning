# Paasing list of names with * argument
def _names(*names):
    for name in names:
        print(f"Hello {name}")

_names('sanjiva')   #Passing one argument
_names('John','Tom','Harry')    #Passing 3 arguments
_names()   #Passing zero arguments

# *args is used to pass variable numbers of positinal argument
# **kwargs is used to pass variable numbers of keyword arguments

def personal_information(name, **kwargs):
    