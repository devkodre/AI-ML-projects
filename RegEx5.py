import sys; args = sys.argv[1:]
idx = int(args[0])-70

myRegexLst = [
  r"/^(?=.*a)(?=.*e)(?=.*i)(?=.*o)(?=.*u)[a-z]*$/m",
  r"/^(?=([^aeiou\W]*[aeiou][^aeiou\W]*){5}$)[a-z]*$/m",
  r"/^(?=[a-z]*$).*(?!.{,3}[aeiou]).w.+$/m",
  r"/^a*$|^(?=[a-z]*$)(?=(.)(.)(.))^[^\W]*\3\2\1$/m",
  r"/^(?=[^bt\W]*(bt|tb)[^bt\W]*$)[a-z]*$/m",
  r"/^([a-z])+\1[a-z]*$/m",
  r"/^(.)+(\w*\1){5}\w*$/m",
  r"/^[a-z]*((\w)\2){3}[a-z]*$/m",
  r"/^[a-z]*([^aeiou\W][a-z]*){13}$/m",
  r"/^(?!\W)(?!.*(.)(.*\1){2})[a-z]*$/m"



  
]

if idx < len(myRegexLst):
  print(myRegexLst[idx])

# Dev Kodre Pd:4 2024