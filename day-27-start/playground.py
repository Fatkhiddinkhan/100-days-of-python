def add(*args):
    return f"* args function\n{sum(args)}"

print(add(1,2,3,44,5,5))

def calculation(n, **kwargs):
    print(f"\n**kwargs function")
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)

print(calculation(5, add=5, multiply=5))

