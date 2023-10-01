import sys; args = sys.argv[1:]
idx = int(args[0])-40

myRegexLst = [
  #40
  r"/^[x.o]{64}$/i",
  #41
  r"/^[xo]*\.[xo]*$/i",
  #42
  r"/^(x+o*)?\.|\.(o*x+)?$/i",
  #43
  r"/^(..)*.$/s",
  #44
  r"/^(0|1[01])([01]{2})*$/",
  #45
  r"/\w*(a[eiou]|e[aiuo]|u[aieo]|o[aieu]|i[ueao])\w*/i",
  #46
  r"/^(1?0)*1*$/",
  #47
  r"/^[bc]*(a|a?[bc]+)$/",
  #48
  r"/^([bc]|(a[bc]*){2})+$/",
  #49
  r"/^(20*|1[20]*10*)+$/"
  
  
  
]

if idx < len(myRegexLst):
  print(myRegexLst[idx])

# Dev Kodre Pd:4 2024