import sys; args = sys.argv[1:]
idx = int(args[0])-50

myRegexLst = [
  r"/(\w)+\w*\1\w*/i",
  r"/\w*(\w)\w*(\1\w*){3}/i",
  r"/^([01])([10]*\1)*$/",
  r"/\b(?=\w*cat)\w{6}\b/i",
  r"/\b(?=\w*bri)(?=\w*ing)\w{5,9}\b/i",
  r"/\b(?!\w*cat)\w{6}\b/i",
  r"/\b((\w)(?!\w*\2))+\b/i",
  r"/^(1(?!0011)|0)*$/",
  r"/\b\w*([aeiou])(?!\1)[aeiou]\w*\b/i",
  r"/^(1(?!11)(?!01)|0)*$/"


  
]

if idx < len(myRegexLst):
  print(myRegexLst[idx])

# Dev Kodre Pd:4 2024