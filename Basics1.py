### Variable Creation 1 

# There are two main environments to program in Python.
# The first is using an "Integrated Development Environment" such as 
# IDLE that allows you to write a program as if you were writing in
# Microsoft Word or a notepad. Obviously it has more features than a
# notepad and it wont spell check your English like Microsoft Word,
# but it allows the user to write, debug, and save code in a simple
# fashion. The second environment is by Python's pseudo command line.
# Here, you will be able to immediately see the line of code's output
# after you finish it.

# In this basics section of learning Python, we will compare the two.
# First we will look at how to program using the command line.
#
# Here we have a variable a that is assigned a value of 1.
a = 1
# We are able to see its value by printing it:
print a
# If we are in Python's command line, then it will look like this:
>>> a = 1
>>> a
1

# A simple string. A string is a sequence of characters"
b = "Hello World"
print b

>>> b = "Hello World"
>>> b
'Hello World'

# A list. A list can be a sequence of characters or numbers (and more)
# separated by a comma.
# Here is a list of just numbers
c = [4,5,6]
print c

>>> c = [4,5,6]
>>> c
[4, 5, 6]

# Here is a list of just strings (sequence of characters)
d = ["Happy","Fun","Cool"]
print d

>>> d = ["Happy","Fun","Cool"]
>>> d
['Happy', 'Fun', 'Cool']

# Here is a mixed list
e = [5, 'Nice', 6, 'Bananas']
print e

>>> e = [5, 'Nice', 6, 'Bananas'] 
>>> e
[5, 'Nice', 6, 'Bananas']

# Here is a special feature data structure in the Python language.
# It's called a dictionary. Just like a dictionary, you can look up the
# definition of a term. In Python, we call the "term/word" a "key".
# Each key is unique, but may have more than one definition. 
peoplesAges = {"Tom":52,"Mary":50,"Issac":24,"Steven":20}
print peoplesAges

>>> peoplesAges = {"Tom":52,"Mary":50,"Issac":24,"Steven":20}
>>> peoplesAges
{'Steven': 20, 'Mary': 50, 'Issac': 24, 'Tom': 52}

# As mentioned before, each key is unique. This means that there should
# be no two keys the same.  For example, if we have the key "Tom"
# mentioned twice in the dictionary, then the dictionary only remembers
# the last key.
peoplesAges2 = {"Tom":52,"Mary":50,"Issac":24,"Tom":42,"Steven":20}
print peoplesAges

>>> peoplesAges = {"Tom":52,"Mary":50,"Issac":24,"Tom":52,"Steven":20}
>>> peoplesAges
{'Steven': 20, 'Mary': 50, 'Issac': 24, 'Tom': 42}

# Dictionaries can have more than "answer" for each key. Here
# we have each person with their name as the key. Their age and favorite
# fruit describes them, which is put into a mixed list of the form [number,string]
>>> peoplesAges3 = {"Tom":[52,"Apples"],"Mary":[50,"Bananas"],"Issac":[24,"Kiwi"],"Steven":[20,"Oranges"]}
>>> peoplesAges3
{'Steven': [20, 'Oranges'], 'Mary': [50, 'Bananas'], 'Issac': [24, 'Kiwi'], 'Tom': [52, 'Apples']}





