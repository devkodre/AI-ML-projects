import sys; args = sys.argv[1:]
idx = int(args[0])-30

myRegexLst = [
  r"/^0$|^10[01]$/",
  r"/^[01]*$/",
  r"/0$/",
  r"/\w*[aeiou]\w*[aeiou]\w*/i",
  r"/^1[01]*0$|^0$/",
  r"/^[01]*110[01]*$/",
  r"/^.{2,4}$/s",
  r"/^\d{3} *-? *\d\d *-? *\d{4}$/",
  r"/^.*?d\w*/mi",
  r"/^1[01]*1$|^0[10]*0$|^[01]$|^$/",
]

if idx < len(myRegexLst):
  print(myRegexLst[idx])

# Dev Kodre Pd:4 2024