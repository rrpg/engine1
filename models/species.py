# -*- coding: utf-8 -*-

from models.Model import Model


class model(Model):
	fields = ['id_species', 'description', 'name']

	@staticmethod
	def getSpecies():
		fields = {'id_species': 'id_species', 'description': 'description', 'name': 'name'}
		return model.loadAll(fields)
