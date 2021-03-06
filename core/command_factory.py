# -*- coding: utf-8 -*-

"""
Module containing the available commands of the game, the factory class to
create the commands...
Today, the available commands are:
- look,
- talk,
- move,
- enter,
- exit,
- take,
- drop,
- inventory,
- stats,
- help,
- quit,
- attack
- save
"""
import core.command
from core.commands import look, talk, move, enter, exit, take, drop, inventory,\
	help, open, stats, attack, save
from core.localisation import _
import sys

"""
Code corresponding to the quit command
"""
quit = -1

class factory:
	"""
	Class to instanciate a command from a string.
	"""

	"""
	Available commands stored in a dict with as key, the commands and as value,
	the command class to execute.
	"""
	mapping = {
		_('LOOK_COMMAND'): {'allowed_while_fighting': True, 'command': 'look'},
		_('TALK_COMMAND'): {'allowed_while_fighting': False, 'command': 'talk'},
		_('MOVE_COMMAND'): {'allowed_while_fighting': True, 'command': 'move'},
		_('ENTER_COMMAND'): {'allowed_while_fighting': True, 'command': 'enter'},
		_('EXIT_COMMAND'): {'allowed_while_fighting': True, 'command': 'exit'},
		_('TAKE_COMMAND'): {'allowed_while_fighting': False, 'command': 'take'},
		_('DROP_COMMAND'): {'allowed_while_fighting': False, 'command': 'drop'},
		_('INVENTORY_COMMAND'): {'allowed_while_fighting': True, 'command': 'inventory'},
		_('INVENTORY_SHORT_COMMAND'): {'allowed_while_fighting': True, 'command': 'inventory'},
		_('STATS_COMMAND'): {'allowed_while_fighting': True, 'command': 'stats'},
		_('HELP_COMMAND'): {'allowed_while_fighting': True, 'command': 'help'},
		_('OPEN_COMMAND'): {'allowed_while_fighting': False, 'command': 'open'},
		_('SAVE_COMMAND'): {'allowed_while_fighting': False, 'command': 'save'},
		_('ATTACK_COMMAND'): {'allowed_while_fighting': True, 'command': 'attack'}
	}

	@staticmethod
	def create(p, commandFull, savedGameId=None):
		"""
		command.factory.create(p, commandFull, savedGameId=None) -> command.command

		Create the desired command.

		@param p player.player Current player.
		@param commandFull list command to run, the first element of the list
			is the command, the other elements are the command's arguments.

		@return the created command
		"""

		cmd = commandFull[0]
		del commandFull[0]

		if cmd in (_('QUIT_COMMAND'), _('QUIT_SHORT_COMMAND')):
			return quit
		elif cmd in factory.mapping.keys():
			cmd = factory.mapping[cmd]
			module = sys.modules['core.commands.' + cmd['command']]

			if p.isFighting() and not cmd['allowed_while_fighting']:
				raise core.command.exception(_('ERROR_DENIED_COMMAND_WHILE_FIGHTING'))

			cmd = getattr(module, cmd['command'])()
		else:
			raise core.command.exception(_('ERROR_UNKNOWN_COMMAND'))

		cmd.setArgs(commandFull)
		cmd.setPlayer(p)
		cmd.setSavedGameId(savedGameId)
		return cmd
