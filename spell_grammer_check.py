# Spell Checker
# Have a lot of documents and huge text and if you want to check the spelling then this Python script will help you solve your problem.
# It uses the Pyspellchecker module to check spells and give correction suggestions.
# Spell Checker in Python 
# pip install pyspellchecker
from spellchecker import SpellChecker as spell
Words = spell.unknown(['Python'  , 'is' , 'a' , 'good' , 'lantyguage'])
for w in Words:
    print(spell.correction(w)) #language
    print(spell.candidates(w)) #{ language }

    
# Grammar Checker
# Inspired by Grammarly then why not try to create your own grammar checker in Python. 
# The below script will help you check your grammar it uses the Gingerit module which is an API-based module.
# Grammer Checker in Python
# pip install gingerit
from gingerit.gingerit import GingerIt
text = "Welcm Progammer to Python"
Grammer = GingerIt()
Correction = Grammer.parse(text)
print(Correction["result"]) # Welcome, Programmer to Python
print(Correction['corrections'])
