# you can pass *args and args return a tuple
# **args it means keyword arguments i.e is first_name = "sameer" it return dictionary when you print through for loop so it gives you first_name , last_name not value so get values you need to args[x]
# To get both keyword and value so you need to use .items()
def add2(*args):

    print(args)


add2("Helle", "hi")

# args.items return tuple you can acess bu result[0] or create two var


def add(**args):
    for result, value in args.items():
        print(result, value)


add(name="sameer", age="18")
