import sys; args = sys.argv[1:]
idx = int(args[0])-60

myRegexLst = [
  r"/^(?!.*010)[01]*$/",
  r"/^(?!.*010)(?!.*101)[01]*$/",
  r"/^([01])([10]*\1)*$/",
  r"/\b((\w)(?!\w*\2\b))+\b/i",
  r"/(\w)+((\w*\1){3}|(?=\w*\1)(\w)+\w*(?!\1)\4)\w*/i",
  r"/\b(?=(\w)*(\w*\1){2}\w*)(?!(\w)+\w*(?!\1)\3)\w+\b/i",
  r"/\b(?!\w*([aeiou])\w*\1)(\w*[aeiou]){5}\w*\b/i",
  r"/^(?=0*(10*10*)*$)[10]([10]{2})*$/",
  r"/^0$|^(1(01*0)*10*)+$/",
  r"/^(?!(1(01*0)*10*)+$)1[01]*$/"



  
]

if idx < len(myRegexLst):
  print(myRegexLst[idx])

# Dev Kodre Pd:4 2024