# Virtual Environments in Python
# Virtual environments are a way to create isolated Python
# environments for different projects.
# By default, when you install packages using pip, they are
# installed globally for the entire system.
# pip install something will install the package globally, and
#is prone to version conflicts between projects.(dependency hell) 
#Virtual environments solve this problem by creating isolated 
# environments for each project.
# A virtual environment is a self-contained directory tree that
# contains a Python installation for a particular version of Python,
# plus a number of additional packages.
# To create a virtual environment, use the venv module that comes
# pip install virtualenv if you are using Python 2
# pre-installed with Python 3.3 and later.
# Create a virtual environment named '.venv'
# python -m venv .venv
# Activate the virtual environment
# On Windows
# .venv\Scripts\activate
# On Unix or MacOS
# source .venv/bin/activate
# Once activated, you can install packages using pip, and they will
# be installed only in the virtual environment. 
# pip install package_name (flask, django, requests, etc)
# You can also list the installed packages using:
# pip list
# To deactivate the virtual environment and return to the global
# Python environment, simply run:
# deactivate
# To delete the virtual environment, simply remove the directory
# rm -rf myenv
# Virtual environments are a powerful tool for managing Python
# projects and avoiding dependency conflicts.

from cowpy import cow

my_cow = cow.Moose().milk("Hello from the virtual environment!")
print(my_cow)
# Example of using an external package within a virtual environment
cow_art = cow.Cowacter().milk("This is a cow character!")
print(cow_art)

cow_art2 = cow.Bunny().milk("This is a bunny character!")
print(cow_art2)


# Create a Cow with a tongue
cheese = cow.Moose(tongue=True)
msg = cheese.milk("My witty mesage, with tongue")
print(msg)


# Create a Cow
cheese = cow.Moose()

# Get a cowsay message by milking the cow
msg = cheese.milk("My witty mesage")

# do something with the message
print(msg)

# Create a Cow with a thought bubble
cheese = cow.Moose(thoughts=True)
msg = cheese.milk("My witty mesage, with thought")
print(msg)

# Create a Cow with a tongue
cheese = cow.Moose(tongue=True)
msg = cheese.milk("My witty mesage, with tongue")
print(msg)

# Create a Cow with dead eyes
cheese = cow.Moose(eyes='dead')
msg = cheese.milk("my witty mesage, i'm dead")
print(msg)

# Get a cow by name
cow_cls = cow.get_cow('moose')
cheese = cow_cls()
msg = cheese.milk("Cow by name is moose")
print(msg)

# Create a Cow with a thought bubble, a tongue, and dead eyes
cheese = cow.Moose(thoughts=True, tongue=True, eyes='dead')
msg = cheese.milk("My witty mesage with several attributes")
print(msg)

# Create a random cow with a message
msg = cow.milk_random_cow("A random message for fun")
print(msg)
# Create a Cow with a thought bubble, a tongue, and dead eyes
cheese = cow.Daemon(thoughts=True, tongue=True, eyes='paranoid')
msg = cheese.milk("My witty mesage with several attributes")
print(msg)
cheese = cow.MechAndCow(thoughts=True, tongue=True, eyes='greedy')
msg = cheese.milk("MMechAndCow bip bop boop")
print(msg)
cheese = cow.DragonAndCow(thoughts=True, tongue=True, eyes='greedy')
msg = cheese.milk("DragonAndCow bip bop boop")
print(msg)
cheese = cow.Moofasa(thoughts=True, tongue=True, eyes='greedy')
msg = cheese.milk("DragonAndCow bip bop boop")
print(msg)
cheese = cow.Ghostbusters(thoughts=True, tongue=True, eyes='greedy')
msg = cheese.milk("Ghostbusters bip bop boop")
print(msg)
cheese = cow.BongCow(thoughts=True, tongue=True, eyes='greedy')
msg = cheese.milk("Bongcow bip bop boop")
print(msg)
cheese = cow.Supermilker(thoughts=True, tongue=True, eyes='greedy')
msg = cheese.milk("Supermilker bip bop boop")
print(msg)
# all the eye options
eye_options = cow.eye_options()
print(f"Eye options: {eye_options}")

# all the cowacter options
cow_options = cow.cow_options()
print(f"Cow options: {cow_options}")