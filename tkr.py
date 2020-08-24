import sys
import json
import random

import colorama
from colorama import init, Fore, Style
init(convert=True)


class item:
	def __init__(self, idfCmd, idf, strCmd, string):
		self.strCmd = strCmd
		self.idfCmd = idfCmd
		self.string = string
		self.idf = self.strCmd.idf(idf)

	def cmd(self, cmd):
		self.strCmd = cmd
		self.idf = self.strCmd.idf(self.idf)
		return self

	def tkr(self, tkr):
		self.tkr = tkr
		return self

	def __repr__(self):
		return (self.idfCmd.fore + self.idfCmd.style + self.idf + ': ' +
			self.strCmd.fore + self.strCmd.style + self.string)








class base_cmd:
	def __init__(self, name, fore, style):
		self.name = name
		self.fore = fore
		self.style = style

	def tkr(self, tkr):
		self.tkr = tkr
		return self

	def idf(self, idf):
		if idf == None: idf = ''
		n = 2
		if len(idf) != n:
			while True:
				#https://stackoverflow.com/questions/4481724/convert-a-list-of-characters-into-a-string
				#https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python
				idf = ''.join([chr(random.randrange(97, 97 + 26)) for i in range(n)])
				#if not self.tkr.list.get(idf, None): break
				break
		return idf

	def run(self, itm):
		print('running...')
		if itm2 := self.tkr.items.get(itm.idf, None):
			itm = itm2
			#https://www.programiz.com/python-programming/dictionary
			del self.tkr.items[itm.idf]
		itm.cmd(self)
		self.tkr.items[itm.idf] = itm
		self.print()

	def print(self):
		print(self)

	def __repr__(self):
		ret = self.fore + self.style + self.name + 's:\n'
		for itm in self.tkr.items.values():
			if itm.strCmd == self:
				ret += itm.__repr__() + '\n'
		return ret

"""
class todo_cmd(base_cmd):
  ...
class do_cmd(base_cmd):
  ...
"""

class tkr:
	def __init__(self, cmds, filename):
		self.cmds = {}
		for cmd in cmds:
			self.cmds[cmd.name] = cmd.tkr(self)
		self.filename = filename
		_file = open(self.filename, 'a+')
		_file.close()
		with open(self.filename, 'r') as file:
			json1 = file.read()
			if json1 == '': json1 = '{}'
			obj = json.loads(json1)
			self.loadItems(obj)

	def run(self, argv):
		if len(argv) == 1:
			print('TODO: interactive shell')
		else:
			self._run(argv)

	def _run(self, argv):
		print('tkr running...')
		for i in range(len(argv)):
			pluralCmd = self.cmds.get(argv[i][:-1], None) and argv[i][-1] == 's'
			if pluralCmd:
				self.cmds[argv[i][:-1]].print()
			if self.cmds.get(argv[i], None):
				#if pluralCmd: argv[i] = argv[i][:-1]
				idfCmd = self.cmds[argv[i]]
				i += 1
				if i >= len(argv) or self.cmds.get(argv[i], None):
					idf = self.cmds['todo'].list[0]
				else:
					idf = argv[i]
				itm = self.items.get(idf, None)
				if itm == None:
					string = idf
					itm = item(idfCmd, None, idfCmd, string).tkr(self)
				idfCmd.run(itm)
		
		self.stop()

	def stop(self):
		with open(self.filename, 'w') as file:
			obj2 = self.dumpItems()
			json2 = json.dumps(obj2)
			file.write(json2)

	def loadItems(self, obj):
		print(obj)
		self.items = {}
		for _item in obj:
			print(_item)
			idfCmd, idf, strCmd, string = _item
			self.items[idf] = item(self.cmds[idfCmd], idf, self.cmds[strCmd], string)
	
	def dumpItems(self):
		obj2 = []
		for idf in self.items.keys():
			item = self.items[idf]
			_item = (item.idfCmd.name, idf, item.strCmd.name, item.string)
			obj2.append(_item)
		return obj2

		#parse args
		#read from JSON
		#self.idfs = //get idfs from JSON
		#get idf
		#idf = self.cmds[...].idf(idf)
		#self.cmds[...].run(idf)
		#write to JSON
		#...


if __name__ == '__main__':
	#https://pypi.org/project/colorama/
	tkr([
		base_cmd('idea', Fore.CYAN, Style.NORMAL),
		#todo_cmd('todo', Fore.WHITE, Style.NORMAL),
		#do_cmd('do', Fore.WHITE, Style.BRIGHT),
		base_cmd('done', Fore.GREEN, Style.DIM),
		base_cmd('skip', Fore.RED, Style.DIM),
	], 'tkr.json').run(sys.argv)
