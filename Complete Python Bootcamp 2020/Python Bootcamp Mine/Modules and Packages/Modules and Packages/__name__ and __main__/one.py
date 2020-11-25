# one.py

def func():
	print("func() in one.py")

print("Top Level Indentation in one.py")

if __name__ == '__main__':
	print("one.py is being run DIRECTLY!")
else:
	print("one.py has been imported")