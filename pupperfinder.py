# Pupperfinder.py
import controller as c
import datetime
import Model as m
from decimal import *

from classes.controller import readAllBreeds, readAllPuppers


def actionItems():
    print("Press 1 for Show Breed By ID\n"
          "Press 2 for Show Pupper By ID\n"
          "Press 3 for Show all Puppers\n"
          "Press 4 for Show all Breeds\n"
          "Press 5 for show Pupper By Name\n"
          "Press 6 for Show Puppers by weight and sex\n"
          "Press 7 for insert Breed\n"
          "Press 8 for insert Pupper\n"
          "Press 9 for adopt Pupper\n"
          "Press 0 for exit\n")

    choice = int(input("Your Choice: "))

    if choice == 1:
        showBreedByID()
        actionItems()

    elif choice == 2:
        readingPupperId()
        actionItems()

    elif choice == 3:
        readAllPuppers()
        actionItems()

    elif choice == 4:
        readAllBreeds()
        actionItems()

    elif choice == 5:
        findPupperByName()
        actionItems()

    elif choice == 6:
        findPupperByMult()
        actionItems()

    elif choice == 7:
        addBreedRecord()
        actionItems()

    elif choice == 8:
        addPupperRecord()
        actionItems()

    elif choice == 9:
        adoptPupper()
        actionItems()

    elif choice == 0:
        print("exiting - Thank you!")

def showBreedByID():
    searchId = int(input("Enter the breed id you are looking for: "))
    c.readingBreedById(searchId)


def readingPupperId():
    searchId = int(input("Enter the pupper id you are looking for: "))
    c.readingPupperById(searchId)


def findPupperByName():
    name = input("Enter the pupper name you are looking for: ")
    c.findItem(name)


def findPupperByMult():
    sex = input("Enter the Sex of Pupper you are looking for: ")
    weight = input("Enter the Max Weight of Pupper you are looking for: ")
    c.findPupperMult(sex, weight)


def addPupperRecord():
    try:
        name = input("Enter Puppy Name: ")
        sex = input("Enter Puppy Sex: ")
        weight = Decimal(input("Enter Puppy weight: "))
        height = Decimal(input("Enter Puppy height: "))
        color = input("Enter Puppy Color: ")
        date_of_birth = input("Enter a Puppy Date of Birth: YYYYMMDD : ")
        breed_id = int(input('Enter Breed ID: '))
        ppObj = m.Pupper(name, sex, weight, height, color, date_of_birth, breed_id)
        c.insertPupperItem(ppObj)
    except:
        print("Missing Attributes Error - Try again")


def addBreedRecord():
    name = input("Enter Breed Name: ")
    temperament = input("Enter Temperament: ")
    coat = input("Enter Coat: ")
    breedObj = m.Breed(name, temperament, coat)
    c.insertBreedItem(breedObj)


def adoptPupper():
    delid = int(input("Enter Pupper ID to adopt: "))
    c.adoptPupperrec(delid)


actionItems()