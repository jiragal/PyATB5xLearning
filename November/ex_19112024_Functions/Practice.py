def greet(name, *, reverse=False, debug=False):
    if debug:
        print("You called greet function")
    if reverse:
        return f"hello {name[::-1]}"
    return f"hello {name}"


first = greet("pramod",debug=False)
print(first)