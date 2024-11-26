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
    print(f"Hello {name} these are your personal information")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

personal_information("Steve", phone=1234567890, city="Bangalore", country="India")
personal_information("Sandhya")
personal_information("Steve", state="Karnataka")


