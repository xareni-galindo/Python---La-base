
"""
Created on Sun Nov  8 17:38:27 2026

@author: Xareni
"""

"""
--------------------------------------------------------------------------------
Partie 1

Étape 1 : Créez votre module data_utils.py
Créez un fichier data_utils.py sur votre ordinateur en utilisant un éditeur de texte (comme Notepad, VS Code, ou autre). C'est tout à fait possible aussi en utilisant Google collab, en mettant tout votre code dans une cellule de code et en le téléchargant avec l'extension .py.

Dans ce fichier, ajoutez les variables et fonctions suivantes :

Variables : PI, E (nombre d'Euler)
Fonctions : carre(x), cube(x), factorielle(n), valeur_absolue(x), maximum(liste), minimum(liste), moyenne(liste), ecart_type(liste), mediane(liste)
Enregistrez le fichier et assurez-vous qu'il est bien nommé data_utils.py.


------------------------------------------------------------------------------------
"""


# Import Libraries
import math
import numpy as np


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

    
    
"""
-----------------------------------------------------------------------------------
Partie 2

Etape 1 : Refaites le process qu'on a vu ensemble dans les quêtes et au début du challenge pour créer une nouvelle version du module 
data_utils_V2.py en rajoutant de nouvelles fonctions.

Création du fichier data_utils_V2.py

Ajout et développement de nouvelles fonctions :

somme_cumulee(liste): calcule la somme cumulée d'une liste et retourne une liste. 
Par exemple, pour la liste [1, 2, 3, 4], la somme cumulée serait [1, 3, 6, 10].

compter_occurrences(liste): retourne un dictionnaire contenant le nombre d'occurrences de chaque élément de la liste. 
Par exemple, pour la liste [1, 2, 2, 3], le résultat serait {1: 1, 2: 2, 3: 1}.

inverser_dict(dictionnaire): inverse les clés et les valeurs d'un dictionnaire. 
Par exemple, pour le dictionnaire {'a': 1, 'b': 2}, le résultat serait {1: 'a', 2: 'b'}.

filtrer_pairs(liste): retourne une nouvelle liste contenant uniquement les nombres pairs de la liste d'entrée. 
Par exemple, pour la liste [1, 2, 3, 4], le résultat serait [2, 4].

celsius_to_fahrenheit(celsius): convertit une température de Celsius en Fahrenheit et retourne un nombre. 
Par exemple, pour une température de 0°C, le résultat serait 32°F. Rappel : la formule est F = (C * 9/5) + 32

trouver_doublons(liste): retourne une liste des éléments qui apparaissent plus d'une fois dans la liste d'entrée. 
Par exemple, pour la liste [1, 2, 2, 3, 3], le résultat serait [2, 3].

calculer_moyenne_ponderee(valeurs, poids): calcule la moyenne pondérée d'une liste de valeurs avec une liste de poids correspondante
et retourne un nombre. Par exemple, pour les valeurs [3, 5] et les poids [1, 2], le résultat serait 4.33.

------------------------------------------------------------------------------------
"""
    
def somme_cumulee(liste): 
    """Calculates the cumulative sum of a list and returns a list."""

    some_cum = np.cumsum(liste)
    
    return  some_cum   
    

def compter_occurrences(liste): 
    """Retourns a dictionary containing the number of occurrences of each item in the list."""
    
    dic_occurences ={}
    
    for e in liste: 
        e_occur = liste.count(e)
        dic_occurences[e] = e_occur

    return dic_occurences


def inverser_dict(dictionnaire):
    """ Reverses the keys and values in a dictionary."""
    inverse_dic ={}
    
    for k, v in dictionnaire.items():

        inverse_dic[v] = k
    
    return inverse_dic


def filtrer_pairs(liste):
    """Returns a new list containing only the even numbers from the input list."""
    pairs = []
    
    for e in liste: 
        if e%2 == 0:
            pairs.append(e)
            
    return pairs


def celsius_to_fahrenheit(celsius): 
    """ Converts a temperature from Celsius to Fahrenheit and returns a number. """
    fahrenheit = (celsius*9/5) + 32
    
    return fahrenheit 


def trouver_doublons(liste): 
    """Returns a list of elements that appear more than once in the input list.If list is empty returns None"""
    
    doublons =[]
    
    #checking if the list is not empty
    n=len(liste)
    
    if n == 0: 
        return None
    else: 
        for e in liste: 
            counts =liste.count(e)
            if counts > 1:
                flag = any(x==e for x in doublons)
                if flag== False:
                    doublons.append(e)
                else: 
                    continue
    doublons.sort()        
    
    return doublons



def calculer_moyenne_ponderee(valeurs, poids):
    """Calculates the weighted average of a list of values using a corresponding list of weights and returns a number"""
    
    wighted_avg = round(np.average(valeurs, weights=poids),2)
    
    return wighted_avg











