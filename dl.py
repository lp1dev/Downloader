#!/usr/bin/python

import re
import requests
from sys import argv
URL_REGEXP=re.compile('((http|https)(://.*?"))')

def     usage():
  print("""
  dl.py will download all the link contents of a given file
  
   usage: %s [file]
  """)
  return 0

def	main():
  if len(argv) < 2:
    return usage()
  with open(argv[1]) as f:
    content = f.read()
    links = re.findall(URL_REGEXP, content)
    i = 0
    for link in links:
      print("\r~ Downloading %s...[%s/%s]" %(link[0], i, len(links)))
      r = requests.get(link[0])
      if r.status_code != 200:
        print("Error, status_code", r.status_code, r.text)
      else:
        with open("%s" %i, "wb") as f:
          f.write(r.content)
      i += 1
  return 0


if __name__ == '__main__':
  main()
