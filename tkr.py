import sys
import json
import random

import colorama
from colorama import init, Fore, Style
init(convert=True)


class item:
	def __init__(self, idfCmd, string):
		self.strCmd = None
		self.idf = None
		self.idfCmd = idfCmd
		self.string = string

	def cmd(self, cmd):
		print('SETTING CMD')
		self.strCmd = cmd
		self.idf = self.tkr.cmds[self.strCmd].idf(self.idf)
		return self

	def tkr(self, tkr):
		print('SETTING TKR')
		self.tkr = tkr
		return self

	def __repr__(self):
		return (self.tkr.cmds[self.idfCmd].fore + self.tkr.cmds[self.idfCmd].style + self.idf + ': ' +
			self.tkr.cmds[self.strCmd].fore + self.tkr.cmds[self.strCmd].style + self.string)








class base_cmd:
	def __init__(self, name, fore, style):
		self.list = []
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
				if True or not self.tkr.list.get(idf, None): break
		return idf

	def run(self, itm):
		print('running...')
		print(itm)

"""
class todo_cmd(base_cmd):
  ...
class do_cmd(base_cmd):
  ...
"""

class tkr:
	def __init__(self, cmds):
		self.cmds = {}
		for cmd in cmds:
			self.cmds[cmd.name] = cmd.tkr(self)
		with open('tkr.json', 'w+') as file:
			json1 = file.read()
			if json1 == '': json1 = '{}'
			obj = json.loads(json1)
			self.storeObject(obj)

	def run(self, argv):
		if len(argv) == 1:
			print('TODO: interactive shell')
		else:
			self._run(argv)

	def _run(self, argv):
		print('tkr running...')
		print('self.cmds', self.cmds)
		for i in range(len(argv)):
			if self.cmds.get(argv[i], None):
				cmd = argv[i]
				i += 1
				if i >= len(argv) or self.cmds.get(argv[i], None):
					idf = self.cmds['todo'].list[0]
				else:
					idf = argv[i]
				#itm = self.getItemByIdf(idf)
				#if itm == None:
				itm = item(cmd, idf).tkr(self).cmd(cmd)
				self.cmds[cmd].run(itm)

		# run

		self.stop()

	def stop(self):
		with open('tkr.json', 'w') as file:
			obj2 = self.genObject()
			json2 = json.dumps(obj2)
			file.write(json2)

	def genObject(self):
		obj2 = {}
		for name in self.cmds.keys():
			obj2[name] = self.cmds[name].list
		return obj2

	def storeObject(self, obj):
		obj = {}
		for name in self.cmds.keys():
			self.cmds[name].list = obj.get(name, [])
		#parse args
		#read from JSON
		#self.idfs = //get idfs from JSON
		#get idf
		#idf = self.cmds[...].idf(idf)
		#self.cmds[...].run(idf)
		#write to JSON
		#...
	
	def getItemByIdf(self, idf):
		for name in self.cmds.keys():
			if item := self.cmds[name].list.get(idf, None):
				return item
		return None

if __name__ == '__main__':
	#https://pypi.org/project/colorama/
	tkr([
		base_cmd('idea', Fore.CYAN, Style.NORMAL),
		#todo_cmd('todo', Fore.WHITE, Style.NORMAL),
		#do_cmd('do', Fore.WHITE, Style.BRIGHT),
		base_cmd('done', Fore.GREEN, Style.DIM),
		base_cmd('skip', Fore.RED, Style.DIM),
	]).run(sys.argv)
