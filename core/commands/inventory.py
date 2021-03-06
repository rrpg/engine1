# -*- coding: utf-8 -*-

from models import item
import core.command
from core.localisation import _


class inventory(core.command.command):
	def run(self):
		"""
		c.run()

		Display the player's inventory.
		"""

		items = list()
		i = self._player.getInventory()
		for itemId in i:
			it = item.model.loadById(itemId)
			items.append({'name': it['name'], 'quantity': i[itemId]['quantity']})
		return items

	def render(self, data):
		output = list()

		if len(data) == 0:
			return _('INVENTORY_EMPTY')

		for i in data:
			output.append(str(i['quantity']).rjust(3) + ' ' + i['name'])

		return '\n'.join(output)
