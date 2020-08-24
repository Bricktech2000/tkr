Functionnality
---
* types
    * idea
    * todo & do
    * done
    * skip




Usage
---

* tkr idea "str": push_front str on ideas
* tkr idea: pop_front todo push_front ideas
* tkr ideas: logs current ideas
<br><br>
* tkr todo "str": push_back str on todo
* tkr todo: pop_front todo push_back todo
* tkr todos: logs bugs and todos
<br><br>
* tkr do "str": push_front str on todo
* tkr do: pop_front ideas push_back todo ???
* tkr dos: ???
<br><br>
* tkr done "str": push_front str to done
* tkr done: pop_front todo push_front done
* tkr dones: logs everything in done
<br><br>
* tkr skip "str": push_front str on skip
* tkr skip: pop_front todo push_front skip
* tkr skips: logs skipped ideas, todos and bugs


> where "str" can be a raw string or a two-letter identifier from any dequque



Pseudo Code
---

```
class base_cmd:
  def __init__(self, name, color):
    self.list = [ ]
    self.name = name
    self.color = color
    ...
  def tkr(self, tkr):
    self.tkr = tkr
    return self
  def idf(self, idf):
    n = 2
    if idf.length != n:
      do:
        idf = [rndChr()] * n
      while self.tkr.idfs.contains(idf)
    return idf
  def run(self, idf):
    ...

class todo_cmd(base_cmd):
  ...
class do_cmd(base_cmd):
  ...

class tkr:
  def __init__(self, cmds):
    self.cmds = {}
    for cmd in cmds:
      self.cmds[cmd.name] = cmd.tkr(tkr)
    ...
  def run(self):
    //parse args
    //read from JSON
    self.idfs = //get idfs from JSON
    //get idf
    idf = self.cmds[...].idf(idf)
    self.cmds[...].run(idf)
    //write to JSON
    ...

if __name__ == '__main__':
  new tkr([
    new base_cmd('idea', ...),
    new todo_cmd('todo', ...),
    new do_cmd('do', ...),
    new base_cmd('done', ...),
    new base_cmd('skip', ...),
  ]).run()
```



{
  <list>: {
    <idf>: (<from>, <message>),
    <idf>: (<from>, <message>),
    ...
  },
  ...
}

