# -*- coding: utf8 -*-

import sys, getpass
from PlayerModel import PlayerModel
from PlayerException import PlayerException
from GenderModel import GenderModel
from SpeciesModel import SpeciesModel

class Player:
    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._model = None

    def isConnected(self):
        return self._model is not None

    #~ Connect the player by asking him to enter his login and his password
    def loadPlayerFromStdIn(self):
        if self._login == None or self._password == None:
            self._readLoginAndPassword(False, False)

    #~ Method to connect the player
    def connect(self):
        self._model = PlayerModel.loadByLoginAndPassword(self._login, self._password)

        if self._model == None:
            self._login = None
            self._password = None
            raise PlayerException("Invalid login or password")

        return True

    #~ Read the login and the password from stdin
    def _readLoginAndPassword(self, checkLogin, confirmPassword):
        while self._login == None or self._login == '':
            self._login = raw_input("Login: ")

            if checkLogin and PlayerModel.loadByLogin(self._login) != None:
                print 'This login is already used'
                self._login = None

        confirmPassword = ''
        while (self._password == None or self._password == ''):
            self._password = getpass.getpass("Password: ")

            if confirmPassword:
                confirmPassword = getpass.getpass("Confirm password: ")
            else:
                confirmPassword = self._password

            if self._password != confirmPassword:
                print 'The passwords do not match'
                self._password = None

    def createNewPlayerFromStdIn(self):
        self._readLoginAndPassword(True, True)

        genders = GenderModel.getGenders()
        nbGenders = len(genders)

        for k, v in enumerate(genders):
            print v['name'] + " (" + str(k) + ")"

        gender = -1
        while gender < 0 or gender >= nbGenders:
            gender = raw_input("Character gender: ")
            try:
                gender = int(gender)
            except:
                gender = -1

        genderId = genders[gender]['id']


        species = SpeciesModel.getSpecies(genders[gender]['name'])
        nbSpecies = len(species)

        for k, v in enumerate(species):
            print v['name'] + " (" + str(k) + ")"
            print v['description']

        sp = -1
        while sp < 0 or sp >= nbSpecies:
            sp = raw_input("Character species: ")
            try:
                sp = int(sp)
            except:
                sp = -1

        speciesId = species[sp]['id']

        self._model = PlayerModel()
        self._model.setLogin(self._login)
        self._model.setPassword(self._password)
        self._model.setSpecies(speciesId)
        self._model.setGender(genderId)
        self._model.save()

    def getModel(self):
        return self._model
