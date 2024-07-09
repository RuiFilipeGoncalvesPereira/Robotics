import os
import shutil
target = 'c:\\Users\\Rui Pereira\\Desktop\\Desktop\\Modulos\\Oracle'

dest = 'c:\\Users\\Rui Pereira\\Desktop\\Desktop\\Modulos\\Postgres5'

destination = shutil.copytree(target, dest,ignore = shutil.ignore_patterns('*.sql','*.txt', 'a'))
