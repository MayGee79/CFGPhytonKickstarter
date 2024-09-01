
my_name = Penelope #NameError: name 'Penelope' is not defined.
# It needs to be put in quotes to indicate that it is a string.
my_age = 29

message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)
#therefore, the correct input is the follow
my_name = 'Penelope'
my_age = 29

message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)
