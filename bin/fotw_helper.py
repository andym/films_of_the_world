"""Collect command-line options in a dictionary"""

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

def parse_imdb_id_from_url(url):
   import re
   m = re.search('/(tt.*?)/', url)
   imdb_id = m.group(1)
   return imdb_id

if __name__ == '__main__':
    from sys import argv
    myargs = getopts(argv)
    if '--url' in myargs:
       imdb_id = parse_imdb_id_from_url(myargs['--url'])

# imdbpie https://github.com/richardasaurus/imdb-pie
from imdbpie import Imdb
import objdict
import json

imdb = Imdb()

film = imdb.get_title(imdb_id)
film = objdict.loads(json.dumps(film))

#print film.base
# duration is retuned in seconds
#print(film.base.title + ',' + film.directors_summary[0].name + ',' + str(film.base.year) + ',' + '0:' + str(int(film.runtime / 60)))

year_part = ' (' + str(film.base.year) + ')'
print('[' + film.base.title + ']' + '(http://www.imdb.com/title/' + imdb_id + '/)' + year_part)

