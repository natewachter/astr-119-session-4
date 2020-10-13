# python exceptions let you deal with
# unexpected results

try:
	print(a)   # this will throw an exception
except:
	print("a is not defined")

# there are specific types of errors to help us
try:
	print(a)   # this will throw an exception
except NameError:
	print("a is still not defined!")
except:
	print("Something else went wrong")

# this will break our program since a is not defined
print(a)