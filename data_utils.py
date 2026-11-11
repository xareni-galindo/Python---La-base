"""
Created on Sun Nov  8 15:33:50 2026

@author: Xareni
"""

"""
--------------------------------------------------------------------------------

Étape 1 : Créez votre module data_utils.py
Créez un fichier data_utils.py sur votre ordinateur en utilisant un éditeur de texte (comme Notepad, VS Code, ou autre). C'est tout à fait possible aussi en utilisant Google collab, en mettant tout votre code dans une cellule de code et en le téléchargant avec l'extension .py.

Dans ce fichier, ajoutez les variables et fonctions suivantes :

Variables : PI, E (nombre d'Euler)
Fonctions : carre(x), cube(x), factorielle(n), valeur_absolue(x), maximum(liste), minimum(liste), moyenne(liste), ecart_type(liste), mediane(liste)
Enregistrez le fichier et assurez-vous qu'il est bien nommé data_utils.py.


------------------------------------------------------------------------------------
"""
# Import math Library
import math

euler = math.e
pi = math.pi

def carre(x):
    """Return the squere of a value X."""
    carre = x*x
    
    return carre

def cube(x):
    """Return the cube of a value X."""
    cube = x**3
    
    return cube

def factorielle(n):
    """Return the factorial of a value X."""
    multiplication = 1

    for i in range(1, n + 1):
        multiplication *= i
    
    return multiplication


def valeur_absolue(x): 
    """Return the absolute value of a value X."""
    
    if x>0:
        valeaur_abs = x
    elif x<0:
        valeaur_abs = -1*x
    else:
        valeaur_abs = 0
    return valeaur_abs
        
        
def maximum(liste): 
    """Return the maximum value of a list. Returns None if the list if empty"""
    max_list = max(liste)
    
    return max_list
    
    
def minimum(liste):
    """Return the minimum value of a list. Returns None if the list if empty"""
    min_list = min(liste)
    
    return min_list

def moyenne(liste):
    """Return the average value of a list. Returns None if the list if empty"""
    #checking the list is not empty
    n = len(liste)
    
    if n == 0: 
        return None
    else: 
        moyenne = sum(liste)/ len(liste)
    
        return moyenne
    
def ecart_type(liste): 
    """Return the standard deviation of a list. Returns None if the list if empty"""
    #checking the list is not empty
    n = len(liste)
    
    if n == 0:
        return None
    else:
        # Calculate the mean
        mean = sum(liste) / n
        
        # Calculate the sum of squared differences
        sq_diff = 0
        
        for num in liste:
            sq_diff = sq_diff + (num - mean)**2
                
        ecart_type = math.sqrt(sq_diff/n)
        
        return ecart_type
    
def mediane(liste): 
    """Return the median value of a list. Returns None if the list if empty 
    If the length of the list is odd, the function returns the middle value, ils the length
    of the list is even,the function returns the average between the 2 center values
    
    """
    #checking the list is not empty    
    n = len(liste)
    
    if n==0: 
        return None
    else: 
        #sorting the list
        liste = liste.sort()
        
        if n % 2 == 0:
            mediane = (liste[n//2 - 1] + liste[n//2]) / 2
            
            return mediane
        else: 
            mediane = liste[n//2]
            
            return mediane

    
    
    
    
    
























