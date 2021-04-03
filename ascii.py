# Made by Atom Development - (C) Atomic
# MIT License

# Importing modules.
import os
import pyfiglet
# Menu
mainm = """
=====================
Text-To-ASCII Creator
Made by Atomic - ATOM
=====================
"""
# Functions
print(mainm)
atext = input("Text : ")
print("Result : ")
result = pyfiglet.figlet_format(atext)
print(result)
file = open("result.txt", "w") 
file.write(result)
print("Saved into result.txt")
file.close() 