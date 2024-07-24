"""
This program is used to identified that monkeys are in trouble or not
Author : Anmol Kumar
Date   : 15 December 2022
"""

def monkey_trouble(a_simle,b_smile):
    """
    Returns True if the monkeys are in trouble otherwise False
    Parameter a_smile : indiactes monkeys are smiing or not
    Precondition a_simle : only bool type value 
    Parameter b_smile : indicates momkeys are smiling or not 
    Precondition b_smile : only bool type value

    Doctests 
    >>> monkey_trouble(True,True)
    'True'
    >>> monkey_troule(False,True)
    'False'
    """

#def monkey_trouble(a_simle,b_smile):
    if bool(a_simle)==bool(b_smile):
    	print("True")
    else:
    	print("False")

#monkey_troule(True,False)