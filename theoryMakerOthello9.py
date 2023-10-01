my_dict = {}
#REMEMBER TO CHANGE n TO 1 if YOU WANT THE WHITE MOVES TO BE SAVED
n = 0
with open('pcgabor_2024dkodre.txt', 'r') as file:
    dot_string = None
    first_number = None
    char = None
    for line in file:
        flag = True
        retFlag = False
        for word in line.split(" "):
            if ('.' in word or "*" in word) and flag:  # check if the line contains a period
                dot_string = word.replace("*",".")
                #print("'" + dot_string + "'" + ':',end="")
                flag = False
            if (word == 'x') or (word == 'o'):
                char = word

            if len(word) > 1 and word != "-1" and word[0] == "-" and word[1] in ["1",'2','3','4','5','6','7','8','9']:
                word = word[1:]
            if word.isnumeric():
                first_number = word 
                #print(first_number + ',')

                my_dict[(dot_string, char)] = first_number
                break 
             # if so, save it as the dot string



keys = list(my_dict.keys())
values = list(my_dict.values())

temp = {}

for i in range(1, len(my_dict)):
    temp[(keys[i-1][0],keys[i][1])] = values[i]

del my_dict[keys[-1]]

theoryDct = {
'...........................ox......xo...........................':19,
'..................ox.......ox......xo...........................':26,
'..................ooo.....xxo......xo...........................':45,
'..................ooo....oooo......xx........x..................':21,
'..................ooooo..ooox......xx........x..................':12,
'............xo....ooooo..ooox......xx........x..................':10,
'..........xooo....ooooo..ooox......xx........x..................':34,
'..........xooo...oooooo..oxox.....xxx........x..................':3,
'...x......xxoo...ooxooo..ooooo....xxx........x..................':23,
'...x......xxoo...ooxxoxx.oooooo...xxx........x..................':32,
'...x......xxoo...oxxxoxx.oooooo.xoxxx........x..................':40,
'...x......xxoo...oxxxoxx.oxoooo.xooxx...xo...x..................':16,
'...x......xxoo..xxxxxoxx.oxoooo.xooooo..xo...x..................':24,
'...x......xxoo..xxxxxoxxxxxoooo.xooooo..xo...o.......o..........':31,
'..ox......oxoo..xxoxxoxxxxoxxxxxxooooo..xo...o.......o..........':5,
'..ox.x....ooxx..xxoxoxxxxxoxxoxxxoooooo.xo...o.......o..........':4,
'..oxxx...ooxxx..xooxoxxxxoooxoxxxoooooo.xo...o.......o..........':1,
'.xxxxx...oooooo.xooxoooxxooooooxxoooooo.xo...o.......o..........':50,
'.xxxxx...oooooo.xooxoooxxooooooxxoooooo.xo...o...ox..o..........':58,
'.xxxxx...oooooo.xooxoooxxooooooxxoooooo.xo...o...xo..o....xo....':60,
'.xxxxx...oooooo.xooxoooxxooooooxxoooooo.xo...o..ooo..o....xxx...':56,
'.xxxxx...oooooo.xooxoooxxooooooxxoooooo.xo...o..xoo..o..x.xxx...':6,
'.xxxxxx..ooooxo.xooxxooxxooxoooxxoooooo.xxo..o..xoo..o..x.xxx...':0,
'xxxxxxx.oooooxo.xoxxxooxxooxoooxxoooooo.xxo..o..xoo..o..x.xxx...':57,
'xxxxxxx.oooooxo.xoxxxooxxooxoooxxoooooo.xxo..o..xxo..o..xxxxx...':51,
'xxxxxxx.oooooxo.xoxxxooxxooxoooxxxooooo.xxx..o..xxxx.o..xxxxx...':43,
'xxxxxxx.oooooxo.xoxxxooxxxoxoooxxxxoooo.xxxxoo..xxxx.o..xxxxx...':47,
'xxxxxxx.oooooxo.xoxxxooxxxoxoxoxxxxoooo.xxxxoooxxxxx.o..xxxxx...':39,
'xxxxxxx.ooooxxo.xoxxxxoxxxoxoxxxxxxxxoxxxxxxoooxxxxx.x.oxxxxx...':63,
'xxxxxxx.ooooxxo.xoxxxxoxxxoxoxxxxxxxxoxxxxxxoooxxxxx.o.xxxxxxo.x':62,
'xxxxxxx.ooooxxo.xoxxxxoxxxoxoxxxxxxxooxxxxxxoooxxxxxox.xxxxxxxxx':54,
'xxxxxxx.ooooxxo.xoxxxxoxxxoxoxxxxxxxxoxxxxxxoxxxxxxxoxxxxxxxxxxx':15,
'...................x.......xx......xo...........................':34,
'...................x.......xx.....xoo....x......................':21,
'...................x.o.....xxx....xoo....x......................':20,
'...........x.......xxo.....xox....xoo....x......................':37,
'...........x.......xxxx....xoo....xooo...x......................':13,
'...........x.o.....xxox....xxxx...xooo...x......................':33,
'...........xxo.....xxxx....xxxx..ooooo...x......................':4,
'....o......xoo.....xoxx..x.xoxx..xoooo...x......................':2,
'..o.o......ooo.....xoxx..x.xoxx..xxxxxx..x......................':23,
'..oxo......xxo.....xoxoo.x.xoxx..xxxxxx..x......................':31,
'..oxxx.....xxx.....xoxoo.x.xoooo.xxxxxx..x......................':6,
'..ooooo....xxo.....xoxoo.x.xooxo.xxxxxxx.x......................':47,
'..ooooo....xxo.....xoxoo.x.xooxo.xxxxxxo.x....xo................':54,
'..ooooo....xxxx....xoxoo.x.xoooo.xxxxxoo.x....oo......o.........':7,
'..oooooo...xxxxx...xooxo.x.xoxoo.xxxxxoo.x....oo......o.........':26,
'..oooooo..xxoxxx...xooxo.xooxxoo.xxxxxoo.x....oo......o.........':18,
'..oooooo..oooxxx.xxxxxxo.xxoxxoo.xxxxxoo.x....oo......o.........':16,
'..oooooo.xxxxxxxoxxooooo.xxxxxoo.xxxxxoo.x....oo......o.........':1,
'.ooooooo.xoxxxxxoxxoooox.xxxxxox.xxxxxox.x....xx......ox........':63,
'.ooooooo.xoxxxxooxxooooo.xxxxxoo.xxxxxoo.x....xo......xo......xo':24,
'.ooooooo.xoxxxxoooxooooooxooooooxxxxxxoo.x....xo......xo......xo':0,
'ooooooooxxxxxxxoxxooooooxxxoooooxxxxxxoo.x....xo......xo......xo':40,
'oooooooooxxxxxxooxoooooooxooooooooxxxxooox....xo......xo......xo':53,
'oooooooooxxxxxxooxoooooooxooooooooxxxxooox..x.oo.....xoo......xo':61,
'oooooooooxxxxxxooxoooooooxooooooooxxxxooox..x.oo.....xoo.....ooo':60,
'oooooooooxxxxxxooxoooooooxooooooooxxxxooox..x.oo.....ooo....oooo':45,
'oooooooooxxxxxxooxoooooooxooooooooxxooooox..xooo.....ooo....oooo':52,
'oooooooooxxxxxxooxoooooooxooooooooxxooooox..oooo....oooo....oooo':50,
'oooooooooxxxxxxooxoooooooxooooooooxxooooox..oooox.o.oooo....oooo':56,
'oooooooooxxxxxxooxoooooooxooooooooxxooooox..ooooo.x.ooooo..xoooo':49,
'oooooooooxxxxxxooxoooooooxoooooooxxxooooox..oooooxx.ooooox.xoooo':58,
'oooooooooxxxxxxooxoooooooxoooooooxxxooooox..oooooox.oooooooooooo':42,
'oooooooooxxxxxxooxoxoooooxoxooooooxxoooooooxooooooo.oooooooooooo':51}


for key in temp:
    if n == 0 and key[1] == 'x' or n==1 and key[1] == 'o':
        if key not in theoryDct:
            theoryDct[key[0]] = int(temp[key])


for key in theoryDct:
        print("'" + key + "'" + ':',end="")
        print(f"{theoryDct[key]}" + ',')
