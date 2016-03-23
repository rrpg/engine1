# -*- coding: utf-8 -*-
import unittest

import tests.common
from core.localisation import _
import json


class createPlayerTests(tests.common.common):
	login = None

	def test_no_argument_provided_text(self):
		self.rpg.setAction(['create-player'])
		output = self.rpg._runAction()
		self.assertEquals(output, _('ERROR_SIGNUP_NOT_ENOUGH_ARGUMENTS'))

	def test_no_argument_provided_json(self):
		self.rpg.setAction(['create-player'])
		output = self.rpg._runAction(True)
		self.assertEquals(output, {"error": {"message": _('ERROR_SIGNUP_NOT_ENOUGH_ARGUMENTS'), "code": 1}})

	def test_login_already_used_text(self):
		self.rpg.setAction(['create-player', 'TEST_PLAYER', 1, 1])
		output = self.rpg._runAction()
		self.assertEquals(output, _('ERROR_SIGNUP_LOGIN_ALREADY_USED'))

	def test_login_already_used_json(self):
		self.rpg.setAction(['create-player', 'TEST_PLAYER', 1, 1])
		output = self.rpg._runAction(True)
		self.assertEquals(output, {"error": {"message": _('ERROR_SIGNUP_LOGIN_ALREADY_USED'), "code": 1}})

	def test_invalid_gender_text(self):
		self.rpg.setAction(['create-player', 'TEST_PLAYER_SOME', 'some gender', 1])
		output = self.rpg._runAction()
		self.assertEquals(output, _('ERROR_SIGNUP_INVALID_GENDER'))

	def test_invalid_gender_json(self):
		self.rpg.setAction(['create-player', 'TEST_PLAYER_SOME', 'some gender', 1])
		output = self.rpg._runAction(True)
		self.assertEquals(output, {"error": {"message": _('ERROR_SIGNUP_INVALID_GENDER'), "code": 1}})

	def test_invalid_species_text(self):
		self.rpg.setAction(['create-player', 'TEST_PLAYER_SOME', '1', 'some species'])
		output = self.rpg._runAction()
		self.assertEquals(output, _('ERROR_SIGNUP_INVALID_SPECIES'))

	def test_invalid_species_json(self):
		self.rpg.setAction(['create-player', 'TEST_PLAYER_SOME', '1', 'some species'])
		output = self.rpg._runAction(True)
		self.assertEquals(output, {"error": {"message": _('ERROR_SIGNUP_INVALID_SPECIES'), "code": 1}})

	def test_text(self):
		self.rpg.setAction(['create-player', 'TEST_PLAYER_SOME', '1', '1'])
		output = self.rpg._runAction()
		self.assertEquals(output, _('PLAYER_CREATION_CONFIRMATION'))

	def test_json(self):
		self.rpg.setAction(['create-player', 'TEST_PLAYER_SOME', '1', '1'])
		output = self.rpg._runAction(True)
		self.assertEquals(output, 'TEST_PLAYER_SOME')
