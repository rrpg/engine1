# -*- coding: utf-8 -*-
import unittest

import tests.common
from core.localisation import _
import json


class moveTests(tests.common.common):
	# test item in area
	# test item in container
	# test item in inventory
	# test player position
	# test player inventory
	# test player stats

	def test_save_no_change_text(self):
		self.rpgText.setAction([_('SAVE_COMMAND')])
		self.rpgText._runAction()

		self.initialiseTextClient()

		self.rpgText.setAction([_('INVENTORY_COMMAND')])
		output = self.rpgText._runAction()
		self.assertEquals(output, _('INVENTORY_EMPTY'))

	def test_save_no_change_json(self):
		self.rpgJSON.setAction([_('SAVE_COMMAND')])
		self.rpgJSON._runAction()

		self.initialiseJSONClient()

		self.rpgJSON.setAction([_('INVENTORY_COMMAND')])
		output = self.rpgJSON._runAction()
		self.assertEquals(output, [])

	def test_no_save_take_text(self):
		# do a change
		# restart engine
		# check the change, must not have been saved
		self.rpgText.setAction([_('TAKE_COMMAND'), 'Heavy breastplate'])
		self.rpgText._runAction()

		self.initialiseTextClient()

		self.rpgText.setAction([_('INVENTORY_COMMAND')])
		output = self.rpgText._runAction()
		self.assertEquals(output, _('INVENTORY_EMPTY'))
		self.rpgText.setAction([_('LOOK_COMMAND'), _('LOOK_OBJECTS_PARAM')])
		output = self.rpgText._runAction()
		self.assertEquals(output, _('AVAILABLE_ITEMS') +'\n'+\
			'  6 Heavy breastplate')

	def test_no_save_take_json(self):
		# do a change
		# restart engine
		# check the change, must not have been saved
		self.rpgJSON.setAction([_('TAKE_COMMAND'), 'Heavy breastplate'])
		self.rpgJSON._runAction()

		self.initialiseJSONClient()

		self.rpgJSON.setAction([_('INVENTORY_COMMAND')])
		output = self.rpgJSON._runAction()
		self.assertEquals(output, [])
		self.rpgJSON.setAction([_('LOOK_COMMAND'), _('LOOK_OBJECTS_PARAM')])
		output = self.rpgJSON._runAction()
		self.assertEquals(output, {"items": [{"name": "Heavy breastplate", "quantity": 6}]})

	def test_save_take_text(self):
		# do a change
		# save
		# restart engine
		# check the change, must have been saved
		self.rpgText.setAction([_('TAKE_COMMAND'), 'Heavy breastplate'])
		self.rpgText._runAction()
		self.rpgText.setAction([_('SAVE_COMMAND')])
		self.rpgText._runAction()

		self.initialiseTextClient()

		self.rpgText.setAction([_('INVENTORY_COMMAND')])
		output = self.rpgText._runAction()
		self.assertEquals(output, '  1 Heavy breastplate')
		self.rpgText.setAction([_('LOOK_COMMAND'), _('LOOK_OBJECTS_PARAM')])
		output = self.rpgText._runAction()
		self.assertEquals(output, _('AVAILABLE_ITEMS') +'\n'+\
			'  5 Heavy breastplate')

	def test_save_take_json(self):
		# do a change
		# restart engine
		# check the change, must not have been saved
		self.rpgJSON.setAction([_('TAKE_COMMAND'), 'Heavy breastplate'])
		self.rpgJSON._runAction()
		self.rpgJSON.setAction([_('SAVE_COMMAND')])
		self.rpgJSON._runAction()

		self.initialiseJSONClient()

		self.rpgJSON.setAction([_('INVENTORY_COMMAND')])
		output = self.rpgJSON._runAction()
		self.assertEquals(output, [{"name": "Heavy breastplate", "quantity": 1}])
		self.rpgJSON.setAction([_('LOOK_COMMAND'), _('LOOK_OBJECTS_PARAM')])
		output = self.rpgJSON._runAction()
		self.assertEquals(output, {"items": [{"name": "Heavy breastplate", "quantity": 5}]})

	def test_no_save_take_container_text(self):
		# do a change
		# restart engine
		# check the change, must not have been saved
		self.rpgText.setAction([_('TAKE_COMMAND'), 'Heavy breastplate', 'chest'])
		self.rpgText._runAction()

		self.initialiseTextClient()

		self.rpgText.setAction([_('INVENTORY_COMMAND')])
		output = self.rpgText._runAction()
		self.assertEquals(output, _('INVENTORY_EMPTY'))
		self.rpgText.setAction([_('OPEN_COMMAND'), 'chest'])
		output = self.rpgText._runAction()
		expected = [
			_('ITEMS_IN_CONTAINER_%s') % 'chest',
			'  4 Heavy breastplate'
		]
		self.assertEquals(output, '\n'.join(expected))

	def test_no_save_take_container_json(self):
		# do a change
		# restart engine
		# check the change, must not have been saved
		self.rpgJSON.setAction([_('TAKE_COMMAND'), 'Heavy breastplate', 'chest'])
		self.rpgJSON._runAction()

		self.initialiseJSONClient()

		self.rpgJSON.setAction([_('INVENTORY_COMMAND')])
		output = self.rpgJSON._runAction()
		self.assertEquals(output, [])
		self.rpgJSON.setAction([_('OPEN_COMMAND'), 'chest'])
		output = self.rpgJSON._runAction()
		self.assertEquals(output, {'items': [{'name': 'Heavy breastplate', 'quantity': 4}], 'container_type': 'chest'})

	def test_save_take_container_text(self):
		# do a change
		# save
		# restart engine
		# check the change, must have been saved
		self.rpgText.setAction([_('TAKE_COMMAND'), 'Heavy breastplate', 'chest'])
		self.rpgText._runAction()
		self.rpgText.setAction([_('SAVE_COMMAND')])
		self.rpgText._runAction()

		self.initialiseTextClient()

		self.rpgText.setAction([_('INVENTORY_COMMAND')])
		output = self.rpgText._runAction()
		self.assertEquals(output, '  1 Heavy breastplate')
		self.rpgText.setAction([_('OPEN_COMMAND'), 'chest'])
		output = self.rpgText._runAction()
		expected = [
			_('ITEMS_IN_CONTAINER_%s') % 'chest',
			'  3 Heavy breastplate'
		]
		self.assertEquals(output, '\n'.join(expected))

	def test_save_take_container_json(self):
		# do a change
		# restart engine
		# check the change, must not have been saved
		self.rpgJSON.setAction([_('TAKE_COMMAND'), 'Heavy breastplate', 'chest'])
		self.rpgJSON._runAction()
		self.rpgJSON.setAction([_('SAVE_COMMAND')])
		self.rpgJSON._runAction()

		self.initialiseJSONClient()

		self.rpgJSON.setAction([_('INVENTORY_COMMAND')])
		output = self.rpgJSON._runAction()
		self.assertEquals(output, [{"name": "Heavy breastplate", "quantity": 1}])
		self.rpgJSON.setAction([_('OPEN_COMMAND'), 'chest'])
		output = self.rpgJSON._runAction()
		self.assertEquals(output, {'items': [{'name': 'Heavy breastplate', 'quantity': 3}], 'container_type': 'chest'})

	def test_no_save_move_json(self):
		self.rpgJSON.setAction([_('MOVE_COMMAND'), _('DIRECTION_KEY_SOUTH')])
		outputMove = self.rpgJSON._runAction()

		self.initialiseJSONClient()

		self.rpgJSON.setAction([_('LOOK_COMMAND'), _('LOOK_REGION_PARAM')])
		outputLook = self.rpgJSON._runAction()
		self.assertNotEquals((outputMove['x'], outputMove['y']), (outputLook['region']['x'], outputLook['region']['y']))

	def test_save_move_json(self):
		self.rpgJSON.setAction([_('MOVE_COMMAND'), _('DIRECTION_KEY_SOUTH')])
		outputMove = self.rpgJSON._runAction()
		self.rpgJSON.setAction([_('SAVE_COMMAND')])
		self.rpgJSON._runAction()

		self.initialiseJSONClient()

		self.rpgJSON.setAction([_('LOOK_COMMAND'), _('LOOK_REGION_PARAM')])
		outputLook = self.rpgJSON._runAction()
		self.assertEquals((outputMove['x'], outputMove['y']), (outputLook['region']['x'], outputLook['region']['y']))

	def test_no_save_point_json(self):
		self.rpgJSON.setAction([_('MOVE_COMMAND'), _('DIRECTION_KEY_SOUTH')])
		outputMove = self.rpgJSON._runAction()
		self.rpgJSON.setAction([_('MOVE_COMMAND'), _('DIRECTION_KEY_SOUTH')])
		outputMove = self.rpgJSON._runAction()
		self.rpgJSON.setAction([_('TAKE_COMMAND'), 'Heavy breastplate'])
		self.rpgJSON._runAction()
		self.rpgJSON.setAction([_('SAVE_COMMAND')])
		outputSave = self.rpgJSON._runAction()
		self.assertEquals(outputSave, {'error': {'message': _('ERROR_SAVE_NO_SAVE_POINT'), 'code': 1}})

		self.initialiseJSONClient()

		self.rpgJSON.setAction([_('INVENTORY_COMMAND')])
		output = self.rpgJSON._runAction()
		self.assertEquals(output, [])
		self.rpgJSON.setAction([_('LOOK_COMMAND'), _('LOOK_OBJECTS_PARAM')])
		output = self.rpgJSON._runAction()
		self.assertEquals(output, {"items": [{"name": "Heavy breastplate", "quantity": 6}]})
		self.rpgJSON.setAction([_('LOOK_COMMAND'), _('LOOK_REGION_PARAM')])
		outputLook = self.rpgJSON._runAction()
		self.assertNotEquals((outputMove['x'], outputMove['y']), (outputLook['region']['x'], outputLook['region']['y']))