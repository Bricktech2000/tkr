import sys

import colorama
from colorama import init, Fore, Style
init(convert=True)

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
		n = 2
		if idf.length != n:
			while True:
				idf = [rndChr()] * n
				if not self.tkr.idfs.contains(idf): break
		return idf
	def run(self, idf):
		print('running...')

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
			self.cmds[cmd.name] = cmd.tkr(tkr)
	def run(self, argv):
		if len(argv) == 1:
			print('TODO: interactive shell')
		else:
			self._run(argv)
	def _run(self, argv):
		print('tkr running...')
		print('self.cmds', self.cmds)
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
	]).run(sys.argv)