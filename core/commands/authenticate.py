# -*- coding: utf-8 -*-

import core.command
from core.localisation import _

class authenticate(core.command.command):
	def run(self):
		"""
		c.run()

		If the command is run as a stand alone command, the player informations
		must be provided. If it is not run as a stand alone command, the
		informations will be read from stdin
		"""

		if len(self._args) != 2:
			raise core.command.exception(_('ERROR_AUTHENTICATE_ARGUMENTS_NUMBER'))

		(login, password) = self._args
		self._player.connect(login, password)

		return [True]

	def render(self, data):
		if len(data) > 0:
			return _('PLAYER_AUTHENTICATION_CONFIRMATION')