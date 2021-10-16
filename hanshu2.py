# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))
# 这里需要注意，用四个空格

# ok,that *args is actually pointless(无意义),we can just do this
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))

# this just takes one argument(参数)
def print_one(arg1):
    print("arg1: %r" % arg1)

# this one takes no arguments
def print_none():
    print("I got 'nothin'.")

print_two("Zed1", "Shaw")
print_two_again("Zed2", "Shaw")
print_one("First!")
print_none()

