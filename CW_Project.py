#Implement a function which convert the given boolean value into its string representation.

#Note: Only valid inputs will be given. Begin the code with the following



#def boolean_to_string(b):
 #   return str(b)

def boolean_to_string(b):
    return repr(b)


#Make a program that filters a list of strings and returns a list with only your friends name in it.

#If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

#Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]


def friend(x):
    return [name for name in x if len(name) == 4]




#Given an integral number, determine if it's a square number:

#In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

#The tests will always use some integral number, so don't worry about that in dynamic typed languages.

def is_square(n):
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n


#Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

def remove_exclam_marks(s):
    return s.replace('!', '')


#We need a function that can transform a number (integer) into a string.

#What ways of achieving this do you know?
def number_to_string(num):
    return "{:d}".format(num)