import os
import sys
import json
import random

import colorama
from colorama import init, Fore, Style
#https://stackoverflow.com/questions/1325581/how-do-i-check-if-im-running-on-windows-in-python
if os.name == 'nt': init(convert=True)
else: init()


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
		return (Style.RESET_ALL + self.idf + self.idfCmd.fore + self.idfCmd.style + ': ' +
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
				if not self.tkr.fromIdf(idf): break
		return idf

	def run(self, itm):
		itm2 = self.tkr.fromIdf(itm.idf)
		if itm2:
			itm = itm2.item
			del self.tkr.items[itm2.index]
			itm2ItemStrCmd = itm2.item.strCmd
			itm2ItemStrCmd.print()
		itm.cmd(self)
		#https://intellipaat.com/community/8780/append-integer-to-beginning-of-list-in-python
		self.tkr.items.insert(0, itm)
		print(itm)
		print()

	def print(self):
		print(self)

	def __repr__(self):
		ret = '' #self.fore + self.style + self.name + 's:\n'
		for itm in self.tkr.items:
			if itm.strCmd == self:
				ret += itm.__repr__() + '\n'
		return ret #[:-1] #remove \n

class todo_cmd(base_cmd):
	def __init__(self, *args):
		super().__init__(*args)

	#https://www.tutorialspoint.com/How-to-override-class-methods-in-Python
	def run(self, itm):
		itm2 = self.tkr.fromIdf(itm.idf)
		if itm2:
			itm = itm2.item
			del self.tkr.items[itm2.index]
			itm2ItemStrCmd = itm2.item.strCmd
			itm2ItemStrCmd.print()
		itm.cmd(self)

		self.tkr.items.append(itm)
		print(itm)
		print()

class do_cmd(base_cmd):
	def __init__(self, *args):
		super().__init__(*args)

	def run(self, itm):
		itm2 = self.tkr.fromIdf(itm.idf)
		if itm2:
			itm = itm2.item
			del self.tkr.items[itm2.index]
			itm2ItemStrCmd = itm2.item.strCmd
			itm2ItemStrCmd.print()
		itm.cmd(self.tkr.cmds['todo'])

		self.tkr.items.insert(0, itm)
		print(itm)
		print()

	def print(self):
		print(self.tkr.cmds['todo'])

class list_cmd(base_cmd):
	def __init__(self, *args):
		super().__init__(*args)

	def run(self, itm):
		if itm.strCmd != self.tkr.cmds['todo']:
			print(Fore.RED + Style.BRIGHT + 'Error: list shouldn\'t take any arguments.')
			return
		
		for cmd in self.tkr.cmds.keys():
			if cmd != 'do': self.tkr.cmds[cmd].print()

	def print(self):
		return


class tkr:
	def __init__(self, cmds, filename):
		self.cmds = {}
		for cmd in cmds:
			self.cmds[cmd.name] = cmd.tkr(self)
		self.mainCmd = self.cmds['todo']
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
			try:
				while True:
					print(Style.RESET_ALL + 'tkr' + self.mainCmd.fore + self.mainCmd.style + '> ', end='')
					args = input()
					argv = self.parseArgs(args)
					self._run(argv)
			except KeyboardInterrupt:
				return
		else:
			self._run(argv)

	def parseArgs(self, args):
		argv = []
		acc = ''
		i = 0
		while i < len(args):
			if args[i] == '"':
				if acc: argv.append(acc)
				acc = ''
				i += 1
				while args[i] != '"':
					acc += args[i]
					i += 1
				if acc: argv.append(acc)
				acc = ''
			elif args[i] == ' ':
				argv.append(acc)
				acc = ''
			else: acc += args[i]
			i += 1
		if acc: argv.append(acc)
		return argv

	def _run(self, argv):
		#https://stackoverflow.com/questions/14785495/how-to-change-index-of-a-for-loop
		i = 0
		while i < len(argv):
			pluralCmd = self.cmds.get(argv[i][:-1], None) and argv[i][-1] == 's'
			if argv[i] == 'main':
				i += 1
				if i < len(argv) and self.cmds.get(argv[i], None):
					self.mainCmd = self.cmds[argv[i]]
					self.mainCmd.print()
				else:
					print(self.mainCmd.fore + self.mainCmd.style + 'Main list: ' + self.mainCmd.name)
					i -= 1
			elif pluralCmd:
				self.cmds[argv[i][:-1]].print()
			elif self.cmds.get(argv[i], None):
				idfCmd = self.cmds[argv[i]]
				i += 1
				if i >= len(argv) or self.cmds.get(argv[i], None):
					idf = None
					for itm in self.items:
						if itm.strCmd == self.mainCmd:
							idf = itm.idf
							break
					if idf == None:
						print(Fore.RED + Style.BRIGHT + 'Error: Main list is empty.')
						return
				else:
					idf = argv[i]
				itm = self.fromIdf(idf)
				if itm == None:
					string = idf
					itm = item(idfCmd, None, idfCmd, string).tkr(self)
				else: itm = itm.item
				idfCmd.run(itm)
			else:
				print(Fore.RED + Style.BRIGHT + 'Error: Unknown command: ' + argv[i])
				return
			i += 1
		self.stop()

	def stop(self):
		with open(self.filename, 'w') as file:
			obj2 = self.dumpItems()
			json2 = json.dumps(obj2)
			file.write(json2)

	def loadItems(self, obj):
		self.items = []
		for _item in obj:
			idfCmd, idf, strCmd, string = _item
			self.items.append(item(self.cmds[idfCmd], idf, self.cmds[strCmd], string))
	
	def dumpItems(self):
		obj2 = []
		for item in self.items:
			_item = (item.idfCmd.name, item.idf, item.strCmd.name, item.string)
			obj2.append(_item)
		return obj2
	
	def fromIdf(self, idf):
		ret = lambda: None
		for index, item in enumerate(self.items):
			if item.idf == idf:
				ret.item = item
				ret.index = index
				return ret
		return None


if __name__ == '__main__':
	#https://pypi.org/project/colorama/
	tkr([
		todo_cmd('todo', Fore.GREEN, Style.BRIGHT),
		base_cmd('idea', Fore.BLUE, Style.NORMAL),
		base_cmd('skip', Fore.YELLOW, Style.NORMAL),
		base_cmd('done', Fore.WHITE, Style.NORMAL),

		do_cmd  ('do',   Fore.MAGENTA, Style.NORMAL),
		list_cmd('list', '', ''),
	], 'tkr.json').run(sys.argv)
