from os import path, listdir, system as sys
import yaml ,shutil

# load config file
cfg_file = 'config.yml'
with open(cfg_file, 'r') as stream:
        cfg = yaml.safe_load(stream)

# check if folders exist
for folder in cfg['folder']:
    if not path.isdir(folder):
        sys('mkdir %s' %folder)

files = listdir('unsorted')
_files = list(cfg['filetype'].keys())
for fil in files:
    n = 0
    filename = path.splitext(fil)[-1]
    for typ in _files:
        if filename.lower() in cfg['filetype'][typ]:
            n += 1
            shutil.move(path.join('unsorted', fil), path.join(typ, fil))
            break
    if n == 0:
        shutil.move(path.join('unsorted', fil), path.join('other', fil))

