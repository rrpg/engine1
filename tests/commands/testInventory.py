# -*- coding: utf-8 -*-
import unittest

import tests.common
from core.localisation import _
import json


class enterTests(tests.common.common):
	def test_empty_text(self):
		self.rpgText.setAction([_('INVENTORY_COMMAND')])
		output = self.rpgText._runAction()
		self.assertEquals(output, _('INVENTORY_EMPTY'))

	def test_empty_json(self):
		self.rpgJSON.setAction([_('INVENTORY_COMMAND')])
		output = self.rpgJSON._runAction()
		self.assertEquals(output, [])

	def test_not_empty_text(self):
		self.rpgText.setAction([_('TAKE_COMMAND'), 2, 'Heavy breastplate'])
		output = self.rpgText._runAction()
		self.rpgText.setAction([_('INVENTORY_COMMAND')])
		output = self.rpgText._runAction()
		self.assertEquals(output, '  2 Heavy breastplate')

	def test_not_empty_json(self):
		self.rpgJSON.setAction([_('TAKE_COMMAND'), 2, 'Heavy breastplate'])
		output = self.rpgJSON._runAction()
		self.rpgJSON.setAction([_('INVENTORY_COMMAND')])
		output = self.rpgJSON._runAction()
		self.assertEquals(output, [{"name": "Heavy breastplate", "quantity": 2}])
