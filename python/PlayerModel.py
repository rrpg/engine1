# -*- coding: utf8 -*-

from CharacterModel import CharacterModel
from Model import Model
import datetime

class PlayerModel(CharacterModel):
    def __init__(self):
        self._playerFields = {}

    @staticmethod
    def loadByLoginAndPassword(login, password):
        query = "\
            SELECT\
                id_player,\
                login\
            FROM\
                player\
            WHERE\
                login = ? AND password = ?\
        "

        model = Model.fetchOneRow(query, (login, password))

        if len(model) > 0:
            pm = PlayerModel()
            pm._setPk(model[0])
            pm.setLogin(model[1])
            return pm

        return None

    def _setPk(self, pk):
        self._playerFields["id_player"] = pk;

    def setLogin(self, login):
        self._playerFields["login"] = login;

    def setPassword(self, password):
        self._playerFields["password"] = password;


