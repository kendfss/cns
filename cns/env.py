from subprocess import run, Popen
from time import sleep
from typing import Dict, List, Callable
import inspect, os, platform, re, sys, warnings

from pyperclip import copy, paste
from sl4ng import show, getsource, pop, unzip, main, join, regenerator, kill, kbd
from filey import Thing, Place, File, Scanner, Library, mcd, search_iter, ffplay, convert
import sl4ng


this = __file__
here = os.path.dirname(__file__)
pwd = Place(os.getcwd())

unix = lambda path: copy(f"/mnt/{path}".replace(':','').replace('\\','/').lower())

architecture = platform.architecture()
def clear():
    Popen('clear')
    sleep(.2)
def cls():
    clear()
    show(map(repr, cd), head=False, tail=False)
def cd(path):
    global pwd
    os.chdir(path)
    pwd.path = path
def killfl():
    kill('fl64')
    kill('ilbridge')    


escaped = tuple(i for i in kbd() if re.escape(i) != i)
def functions(module):
    isfunc = lambda x: inspect.isfunction(x[1])
    return tuple(filter(isfunc, (i[1] for i in inspect.getmembers(module))))
        
c = Place('c:/')
e = Place('e:/')
f = Place('f:/')
kali = Place(r"\\wsl$\kali-linux\home\eli2and40")

user = Place('~')
documents = user/'documents'
root = c if c.exists else None
appdata = user/'appdata'

downs = downloads = user / 'Downloads'
tools = downs / 'tools'
langs = downs / 'tools/languages' # need library class
gosrc = Place(r'C:\Program Files\Go\src')
web = Library(
    langs['css'],
    langs['html'],
    langs['javascript'],
    langs.up['web'],
    r"E:\Projects\web\jayess",
)

dev = Place(r"e:/")
sp = dev / 'shellpower'

gitting = dev / 'gitting'
git = downs / "tools/git"
clones = gitting/'gitclone/clones'
ignore = clones / 'github/gitignore'
mdn = gitting / r'gitclone\clones\mdn\content\files\en-us'
brython = gitting / r'gitclone\clones\brython-dev\brython\www\doc\en'
kendfss = clones['kendfss']

def igpy(path):
    """
    Add a python .gitignore file to the given path
    """
    home = pwd.path
    mode = "a" if '.gitignore' in os.listdir(path) else "w"
    os.chdir(path)
    with open('.gitignore', mode) as fob:
        pig = File(r"E:\gitting\gitclone\clones\github\gitignore\Python.gitignore").cat()
        fob.write(f'\n{pig}')
    os.chdir(home)

def iggo(path):
    """
    Add a golang .gitignore file to the given path
    """
    home = pwd.path
    mode = "a" if '.gitignore' in os.listdir(path) else "w"
    os.chdir(path)
    with open('.gitignore', mode) as fob:
        pig = File(r"E:\gitting\gitclone\clones\github\gitignore\Go.gitignore").cat()
        fob.write(f'\n{pig}')
    os.chdir(home)


projects = dev / 'projects'
monties = projects / 'monties'

site = dev / 'Languages\Python38-64\lib'
docs = monties / 'docs'

prod = Place(r'f:/')
flps = prod / 'programs/project_files/fl'

exotics = {
    "cdot": "·",
}
exords = {key: ord(val) for key, val in exotics.items()}
tfs = [
    r'C:\Users\Kenneth\childlist.txt',
    r'C:\Users\Kenneth\file.txt',
    r'C:\Users\Kenneth\parentlist.txt',
]
