from subprocess import run, Popen
from time import sleep
from typing import Dict, List, Callable
from itertools import permutations
import inspect, os, platform, re, sys, warnings, math

from pyperclip import copy, paste
from sl4ng import show, getsource, pop, unzip, main, join, regenerator, kill, kbd, splitall
from filey import Thing, Place, File, Scanner, Library, mcd, search_iter, ffplay, convert, forbiddens
import sl4ng, filey


arch = platform.architecture()
this = __file__
here = os.path.dirname(__file__)
pwd = Place(os.getcwd())
ff = lambda: ffplay(paste(), loop=0)
rm = lambda: os.remove(paste())
smp = lambda: os.rename(paste(), os.path.join("samples", paste()))

def unix(path=None): 
    path = path if isinstance(path, str) and os.path.exists(path) else paste()
    path = (f"/mnt/{path}").replace(':','').replace('\\','/').lower()
    copy(path)
    print(path)

def pp():
    [*map(pop, paste().splitlines())]
def pt():
    pop(this)
def rp():
    [*map(os.remove, paste().splitlines())]

def fname():
    copy("".join(splitall(forbiddens+'.', paste())).strip().replace(' ', '_'))

def diffs(adjacent:bool=False):
    unix = lambda path: f"/mnt/{path}".replace(':','').replace('\\','/').lower()
    lines = paste().splitlines()
    cmd = 'diff --text %s {} | aplay' % ("-y " if adjacent else "")
    for i, (one, two) in enumerate(permutations(lines, 2)):
        args = f'"{unix(one)}" "{unix(two)}"'
        print(cmd.format(args))
        copy(cmd.format(args))
        if i < math.factorial(len(lines)):
            input("press enter to continue")
def qmap(func, itr, ex=lambda *args: None):
    for i in itr:
        try:
            yield func(i)
        except:
            yield ex(i)
            
def clear() -> None:
    Popen('clear')
    sleep(.2)
def cls() -> None:
    clear()
    show(map(repr, cd), head=False, tail=False)
def cd(path:str=None) -> None:
    global pwd
    if isinstance(path, type(None)):
        path = os.getcwd()
    os.chdir(path)
    pwd.path = path
def killfl() -> None:
    kill('fl64')
    kill('ilbridge')    
def exp(power, base=2):
    return f"{pow(base, power):,}"
    

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
tools = Place('f:/tools')
langs = tools / 'languages' # need library class
gosrc = Place(r'C:\Program Files\Go\src')
web = Library(
    langs['css'],
    langs['html'],
    langs['javascript'],
    langs.up['web'],
    r"E:\Projects\web\jayess",
)
golang = langs / "golang"
python = langs / "python"

dev = Place(r"e:/")
sp = dev / 'shellpower'

gitting = dev / 'gitting'
git = tools / "git"
clones = gitting/'gitclone/clones'
ignore = clones / 'github/gitignore'
mdn = gitting / r'gitclone\clones\mdn\content\files\en-us'
brython = gitting / r'gitclone\clones\brython-dev\brython\www\doc\en'
kendfss = clones['kendfss']
# processing = clones / "processing" Library(
processing = Library(
    clones/"processing/processing-docs",
    clones/"processing/processing-doclet",
    langs/"processing",
    langs/"java",
)
processes = Place(r"F:\Visuals\processes")

def igpy(path:str=None) -> None:
    """
    Add a python .gitignore file to the given path
    """
    origin = pwd.path
    os.chdir(paste() if isinstance(path, type(None)) else path)
    mode = "a" if '.gitignore' in os.listdir() else "w"
    with open('.gitignore', mode) as fob:
        pig = File(r"E:\gitting\gitclone\clones\github\gitignore\Python.gitignore").cat()
        header = "# Python\n"*3
        header = "\n" + header if mode=="a" else header
        fob.write(f'{header}\n{pig}')
    os.chdir(origin)

def iggo(path:str=None) -> None:
    """
    Add a golang .gitignore file to the given path
    """
    origin = pwd.path
    os.chdir(paste() if isinstance(path, type(None)) else path)
    mode = "a" if '.gitignore' in os.listdir() else "w"
    with open('.gitignore', mode) as fob:
        pig = File(r"E:\gitting\gitclone\clones\github\gitignore\Go.gitignore").cat()
        header = "# Golang\n"*3
        header = "\n" + header if mode=="a" else header
        fob.write(f'{header}\n{pig}')
    os.chdir(origin)


projects = dev / 'projects'
monties = projects / 'monties'

site = dev / 'Languages/Python38-64/lib'
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
