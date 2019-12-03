# controller.py
import Dao as d


def readingBreedById(searchById):
    print("Read Breed record:")
    d.readByIdBreed(searchById)


def readingPupperById(searchById):
    print("Read Pupper record:")
    d.readByIdPupper(searchById)


def readAllBreeds():
    print("ALL BREEDS: ")
    d.readBreed()


def readAllPuppers():
    print("ALL PUPPERS: ")
    d.readPupper()


def findItem(name):
    print("Find Pupper By name:")
    d.findPuppersByName(name)


def insertPupperItem(ppObj):
    print("Insert Pupper Record: ")
    d.addPupper(ppObj)


def insertBreedItem(breedObj):
    print("Insert Breed Record: ")
    d.addBreed(breedObj)


def adoptPupperrec(delid):
    print("Delete Pupper Record: ")
    d.delPupper(delid)


def findPupperMult(sex, weight):
    print("Find Pupper by sex and weight: ")
    d.selPupperMult(sex, weight)