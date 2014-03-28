import unittest
import sys
import os
sys.path.append(os.path.realpath(__file__ + "/../../../"))

import tests.common
from tests.output_capturer import capturer


class takeTests(tests.common.common):
	def test_no_item_given_text(self):
		with capturer() as output:
			self.rpgText.init(self.dbFile, 'TEST_PLAYER', 'TEST_PLAYER', ['take'])
			self.rpgText._runAction()
		self.assertTrue(output == ['What shall I take?'])

	def test_no_item_given_json(self):
		with capturer() as output:
			self.rpgJSON.init(self.dbFile, 'TEST_PLAYER', 'TEST_PLAYER', ['take'])
			self.rpgJSON._runAction()
		self.assertTrue(output == ['{"error": {"message": "What shall I take?", "code": 1}}'])

	def test_unknown_item_text(self):
		with capturer() as output:
			self.rpgText.init(self.dbFile, 'TEST_PLAYER', 'TEST_PLAYER', ['take', 'some dummy item'])
			self.rpgText._runAction()
		self.assertTrue(output == ['I don\'t see this here.'])

	def test_unknown_item_json(self):
		with capturer() as output:
			self.rpgJSON.init(self.dbFile, 'TEST_PLAYER', 'TEST_PLAYER', ['take', 'some dummy item'])
			self.rpgJSON._runAction()
		self.assertTrue(output == ['{"error": {"message": "I don\'t see this here.", "code": 1}}'])

	def test_item_not_here_text(self):
		with capturer() as output:
			self.rpgText.init(self.dbFile, 'TEST_PLAYER', 'TEST_PLAYER', ['take', 'Mist potion'])
			self.rpgText._runAction()
		self.assertTrue(output == ['I don\'t see this here.'])

	def test_item_not_here_json(self):
		with capturer() as output:
			self.rpgJSON.init(self.dbFile, 'TEST_PLAYER', 'TEST_PLAYER', ['take', 'Mist potion'])
			self.rpgJSON._runAction()
		self.assertTrue(output == ['{"error": {"message": "I don\'t see this here.", "code": 1}}'])

	def test_quantity_too_high_text(self):
		with capturer() as output:
			self.rpgText.init(self.dbFile, 'TEST_PLAYER', 'TEST_PLAYER', ['take', 10, 'Heavy breastplate'])
			self.rpgText._runAction()
		self.assertTrue(output == ['There are not enough items of this kind'])

	def test_quantity_too_high_json(self):
		with capturer() as output:
			self.rpgJSON.init(self.dbFile, 'TEST_PLAYER', 'TEST_PLAYER', ['take', 10, 'Heavy breastplate'])
			self.rpgJSON._runAction()
		self.assertTrue(output == ['{"error": {"message": "There are not enough items of this kind", "code": 1}}'])

	def test_with_quantity_text(self):
		with capturer() as output:
			self.rpgText.init(self.dbFile, 'TEST_PLAYER', 'TEST_PLAYER', ['take', 2, 'Heavy breastplate'])
			self.rpgText._runAction()
		self.assertTrue(output == ['You take 2 Heavy breastplate'])

	def test_with_quantity_json(self):
		with capturer() as output:
			self.rpgJSON.init(self.dbFile, 'TEST_PLAYER', 'TEST_PLAYER', ['take', 2, 'Heavy breastplate'])
			self.rpgJSON._runAction()
		self.assertTrue(output == ['{"name": "Heavy breastplate", "quantity": 2}'])

	def test_implied_quantity_text(self):
		with capturer() as output:
			self.rpgText.init(self.dbFile, 'TEST_PLAYER', 'TEST_PLAYER', ['take', 'Heavy breastplate'])
			self.rpgText._runAction()
		self.assertTrue(output == ['You take 1 Heavy breastplate'])

	def test_implied_quantity_json(self):
		with capturer() as output:
			self.rpgJSON.init(self.dbFile, 'TEST_PLAYER', 'TEST_PLAYER', ['take', 'Heavy breastplate'])
			self.rpgJSON._runAction()
		self.assertTrue(output == ['{"name": "Heavy breastplate", "quantity": 1}'])

unittest.main()
