import sys; args = sys.argv[1:]
import time
import random
#Min Score: -2; move sequence: [0, 8, 49, 57, 9, 56, 48, 62, 1, 14, 7, 6, 60, 59, 63, 54]
args = '...........*****...xo*o*ox.xoooooxxxxxxoo*oxoxxo.*oxxx...xxxxx..'.replace("*",".").split(" ")
#args = '192029'.split(" ")
global timeLimit, TIME
TIME = 0
global ws
ws = []
timeLimit = 0
class Strategy():   
    logging = True
    def best_strategy(self, board, player, best_move, running,time_limit):
        #time.sleep(1)
        global TIME
        t = time.time()
        TIME = t
        if board == '..*......*ox.**.**oooo..*ooxox..*.xxo*.....*.*..................'.replace("*",'.'):
            best_move.value = 17
            return
        if board == '...........................ox......xo...........................':
            best_move.value = 19
            return
        elif board == '...........................ox......xx.......x...................':
            best_move.value = 29
            return
        elif board == '...................x.......xx......xo...........................':
            best_move.value = 34
            return
        elif board == '..........................xxx......xo...........................':
            best_move.value = 20
            return
        elif board == '...........................ox......xxx..........................':
            best_move.value = 43
            return
        elif True:#time_limit < 10:
            theoryDct = {
'...........................ox......xo...........................':19,
'...................x.......xx.....ooo...........................':45,
'...................xo......ox.....oox........x..................':18,
'..................xxo......xx.....oooo.......x..................':21,
'............o.....xxox.....xo.....oooo.......x..................':13,
'...........oox....xoxx.....oo.....oooo.......x..................':3,
'...x.o.....oox....xoxx.....oo.....oooo.......x..................':29,
'...x.o.....oox....xoox.....ooo....ooooo......x..................':10,
'...x.o....xxxx...oooox.....ooo....ooooo......x..................':25,
'...xoo....xxox...oxoox...x.ooo....ooooo......x..................':6,
'...xxxx...xxox..ooxoox...o.ooo....ooooo......x..................':26,
'.o.xxxx...oxxx..ooxoox...oxooo....ooooo......x..................':32,
'.o.xxxx...oxxx..ooxoooo..xxooo..x.ooooo......x..................':23,
'.o.xxxx...oxxx..ooxxxxxx.oxooo..xoooooo......x..................':31,
'.o.xxxx...oxxx..ooxxxxxx.oxooo.xxooooooo.....x..................':40,
'...........................ox......xx.......x...................':29,
'..................x........xoo.....xx.......x...................':26,
'..................xx......oxoo.....xx.......x...................':43,
'..................xxx.....oxxo.....xx......ox...................':10,
'..........o......xxxx.....xxxo.....xx......ox...................':34,
'..........o......xoxx....xxxxo....oxx......ox...................':21,
'..........ox.....xxxoo...xxxxo....oxx......ox...................':12,
'..x.......xoo....xxxoo...xxxxo....oxx......ox...................':33,
'..xx......xxo....xxxoo...xoxxo...ooxx......ox...................':24,
'..xx......xxo....xxxoo..oxoxxo..xxxxx......ox...................':40,
'..xxx.....xxx....xxxxo..oxoxxo..ooxxx...o..ox...................':42,
'..xxx.....xxx....xxxxo..oxoxoo..ooxox...o.oxx.......x...........':37,
'...................x.......xx.....oooo.......x..................':44,
'...................xo......ox.....ooxo......xx..................':43,
'...................xo......xx.....oxxo.....xxo.......o..........':46,
'...................xo.....oxx.....ooxx.....xoxx......o..........':42,
'...................xo.....oxx.....oxxx....oxoxx...o..o..........':52,
'...................xoo....oxo.....ooxx....oxxxx...o.xo..........':29,
'...................xoo....oxox....ooox....oxoxx...o.oo......o...':51,
'...................xoo....oxox....ooox.o..oxxxo...oxoo......o...':11,
'...........x.......xxo....oxox....oooooo..oxxoo...oxoo......o...':30,
'...........x.......xxo....oxoooo..oooxoo..oxxoo...oxoo......o...':17,
'...........x.o...x.xoo....xooooo..oxoxoo..oxxoo...oxoo......o...':12,
'....o......xoo...x.xoo....xooooo..oxoxoo..oxooo...oxoo......o...':41,
'....o......xoo...x.xoo...ooooooo..oxoxoo.xxxooo...oxoo......o...':18,
'....o......xoo...xxxoo...oxooooo..xooxoo.xxoooo...oooo.....oo...':33,
'....................o.....xxo......xo...........................':45,
'....................o.....xxo......xo.......ox..................':37,
'....................o.....xoo.....oxxx......ox..................':29,
'....................o.....xxxx....oxxx......ooo.................':51,
'....................o.....xxxx....oxxx.....oooo....x............':42,
'....................o.....xxxxo...xxxo....xoooo....x............':38,
'....................oo....xxxoo...xxxox...xoooo....x............':53,
'....................oo....xxooo...xxoox...xoooo....xox..........':23,
'...................ooo.x..xooox...xooxx...xoxoo....xox..........':60,
'...................ooo.x..xooox...xooxo...xoxooo...xxx......x...':31,
'.................o.ooo.x..ooooxx..xooxx...xoxxoo...xxx......x...':39,
'...................x.......xx.....ooxo......oo.......o..........':42,
'...................x.......xx.....oxxo....o.oo....o..o..........':33,
'...................x....o..xx....oxxxo....o.oo....o..o..........':46,
'...................x....o..xx....oxxxx....o.oooo..o..o..........':61,
'...................x....o.oxx....oooxx....o.oxoo..o..x.......x..':52,
'...................x....o.oxx....oooxx....oooooo..o.xx.......x..':38,
'...................x....o.oxx....ooooooo..oooxoo..o.xx.......x..':51,
'...................x....o.oxx....ooxoooo..oxoxoo..ooxx....o..x..':59,
'...................x.o..o.oxo....ooooooo..oxoxoo..oxxx....ox.x..':30,
'..................ox.o..o.ooo.x..ooooxoo..oxxxoo..oxxx....ox.x..':29,
'..................ox.o.oo.oooxo..oooxooo..oxoxoo..ooxx....ox.x..':20,
'...................xo......xo......xo...........................':29,
'..................ooo......oxx.....xo...........................':37,
'..................ooo......oox.....xox......o...................':21,
'..................ooox.....oooo....xoo......o...................':45,
'..................ooox.....oooo....xooo.....ox..................':43,
'..................ooooo....oooo....xooo....xxx..................':31,
#'..................ooooo....oooox...xooo....xxx.o................':23,#COMMENT OUT THIS
'..................ooooox...oooxx...xooo....xxxoo................':13,
'.............x....oooxxx...ooxxx...xoxo....xoooo....o...........':51,
'..................ox.......ox......xo...........................':26,
'..................ooo.....xxo......xo...........................':11,
'...........x......oxo.....ooo.....ooo...........................':33,
'...o.......o......ooo.....xoo....xooo...........................':42,
'...o.......o......ooo.....xoo...ooooo.....x.....................':40,
'...o.......o......ooo.....xoo...oxooo...o.x.....o...............':29,
'...o.......o......ooo.....xxox..oxoooo..o.x.....o...............':41,
'...o.......o......ooo.....xxox..oxxooo..oooo....o...............':44,
'...o.......o......ooo...o.xxox..ooxxoo..oooox...o...............':45,
'...o.......o......ooo...ooooox..oooxxx..ooooxx..o...............':21,
'...o.......o......ooooo.ooooxo..oooxox..ooooxx..o...............':12,
'...oo......oo.....ooooo.oooooo..oooxox..ooooxx..o...............':10,
'..ooo.....ooo.....oxooo.ooooxo..oooxox..ooooxx..o...............':30,
'..ooo.....ooo.....oxooo.ooooxxo.oooxox.oooooxx..o...............':13,
'..................ooooo....oooo....xxoxx...xxo.......o..........':46,
'..................ooooo....oooo....xooxx...xoxx.....oo..........':13,
'.....o.......o....ooooo....oooo....xooxx...xoox.....oo..........':60,
'.....o.......o....ooooo....oooo....xooxx...xoox.....oo......xo..':62,
'.....o.......o....ooooo....oooo....xooxx...oxox...o.ox......xxx.':42,
'.....o.......o....ooooo....oooo....xooox..xxxooo..o.ox......xxx.':55,
'.....o.......o....ooooo....oooo....oooox..xoooox..ooox.x....xxx.':58,
'.....o.......o....ooooo....oooo....oooox.oooooox..xoox.x..x.xxx.':40,
'.....o.......o....ooooo....oooo...oooooxxxxoxxxx..xoox.x..x.xxx.':59,
'.....o.......o....ooooo....oooo...oooooxxoxoxxxxo.xoxx.x..xxxxx.':25,
'.....o.......o....ooooo..x.oooo..ooooooxxooxxxxxo.xoxx.x..xxxxx.':31,
'.....o.......o...oooooo..o.oooox.oooooxxxooxxxxxo.xoxx.x..xxxxx.':23,
'.....o.......o...oooooox.o.oooxxoooooxxxoooxxxxxo.xoxx.x..xxxxx.':26,
'.....o.......o...oooooox.oxxoxxxooxooxxxoooxxxxxooooxx.x..xxxxx.':15,
'.....o.......o.x.oooooxx.oxxoxxxooxooxxxoooxxoxxooooooox..xxxxx.':63,
'.....o.......o.x.oooooxx.oxxoxxxooxoxxxxoooxxxxxooooooxx..xxxxxx':8,
'...................x.......xx......xo...........................':34,
'...................x.......xx.....oox.......x...................':20,
'...................xo......xx.....oxx......xx...................':37,
'...................xo.....xxx.....oxoo.....xx...................':18,
'..................ooo.....oox....xxxoo.....xx...................':29,
'..................ooox....ooxo...xxxoo.....xx...................':41,
'............x.....oxxx....xoxo...xoxoo...o.xx...................':25,
'............x.....oxxx..xxxxxo...ooxoo...o.xx...................':10,
'..........o.x.....ooxx..xxxxoo..xxxxoo...o.xx...................':5,
'.....o....o.o.....ooxxx.xxxxox..xxxxxo...o.xx...................':45,
'...................xo......xo.....oxox.....ooxx.....oo..........':42,
'...................xo.....ooo.....ooox....xxoxx.....oo..........':51,
'...................xo.....ooo.....ooox....xoxxx....ooo.....o....':17,
'.................x.xo.....xooo....oxoo....xoxox....ooo.....o....':38,
'.................x.xo.....xoooo...oxxox...xooox....ooo.....o....':50,
'.................x.xo....oooooo...oxxox...xxoox...xooo.....o....':18,
'.................xxxo....oxxooo..ooooox...oxoox...xooo.....o....':21,
'.................xxxxx...oxxoooo.oooooo...oxoox...xooo.....o....':24,
'.................xxxxx..xxxxoooo.ooooooo..oxooo...xooo.....o....':22,
'................oxxxxxx.xoxxoxoo.oooxooo..oxooo...xooo.....o....':8,
'........x.......xxxxxxx.xoxxoxoo.oooxooo..oxooo...oooo....oo....':47,
'........x......oxxxxxxo.xoxxoooo.oooooxo..ooxxxx..oooo....oo....':32,
'........x....o.oxxxxxoo.xxxxooooxxxxxxxo..ooxxxx..oooo....oo....':41,
'........x...oo.oxxxxooo.xxxxooooxxxxxxxo.xxxxxxx..oooo....oo....':11,
'...o....x..ooo.oxxxoxoo.xxxooxooxxxoxxxo.xxoxxxx..oooo....oo....':10,
'...................xo......oo.....oxoo....x.oo.......o..........':26,
'...................xo.....xoo.....xooo....xooo.......o..........':51,
'...................xo....oooo.....xxoo....xxoo.....x.o..........':18,
'..................xxo....oxoo....ooooo....xxoo.....x.o..........':29,
'..................xxo....oxxxx...oooxo....xooo.....xoo..........':41,
'..................xxo....oxxxx...oxoxo...xxooo.....ooo.....o....':50,
'..................xxo....oxoxx...oooxo...oxxoo..o.xooo.....o....':40,
'..................xxo....oxoxx..ooooxo..ooxxoo..o.oooo.....o....':16,
'............o...x.xoo....xooxx..ooxoxo..ooxxoo..o.oooo.....o....':10,
'..........x.o...x.xxo.o..xooxo..ooxooo..ooxooo..o.oooo.....o....':38,
'..........x.o...x.xxo.o..xooxo..ooooooooooxooo..o.oooo.....o....':30,
'..........xoo...x.ooo.o..oooxxx.ooooooooooxooo..o.oooo.....o....':46,
'.x........x.......oxx.....oxxo.....xx......ox...................':21,
'.x........x.......xooo....xxxo....xxx......ox...................':37,
'.x........xx......xxoo....xxoo....xxxo.....ox...................':42,
'.x........xx......xxoo....xxxo....xoxx....oox.x.................':33,
'.x........xx......xxxo....xxxx...oooxxx...oox.x.................':3,
'.x.o......xo......xoxo....xoxx..xxxxxxx...oox.x.................':13,
'.x.o......xo.o....xooo....xoxx..xxxxxxx...oxx.x.....x...........':30,
'.x.o......xo.o....xooo....xxxxxxxxxxxxx...oxx.x.....x...........':25,
'.x.o......xo.o...xoooo...xxxxxxxxxxxxxx...oxx.x.....x...........':51,
'.x.o......xxxo...xoxxx...xxoxxxxxxxoxxx...oox.x....ox...........':4,
'.x.oo.....xoxo...xoxxx...xxoxxxxxxxoxxx..xxxx.x....ox...........':2,
'.xxxxx....ooxx...xoxxx...xxoxxxxxxxoxxx..xxxx.x....ox...........':50,
'.xxxxx....ooxx...xoxxx...xooxxxxxxooxxx..xxxx.x...oxx.......x...':59,
'..........................xxx......xo...........................':20,
'....................o.....xxo......xx........x..................':44,
'....................o.....xxo......xxx......ox..................':34,
'....................o.....xxxx....oxxx......ox..................':46,
'....................o.....xxxx....oxxx......xoo....x............':43,
'....................o.....xxxx....xxxx....xoooo....x............':30,
'....................o.....xxxxo...xxxxx...xoooo....x............':21,
'....................oo....xxxoo...xxxox...xoxoo....x.x..........':52,
'....................oo.x..xxoox...xxoxx...xoxoo....xox..........':19,
'...................ooo.x..xooox...xooxx...xoxoo....xxx......x...':47,
'...................xo......xxo....oxxo.....xxox......o..........':38,
'...................xo......xxo....oxxxx...oooox......o..........':52,
'...................xo......xoo....oxoxx...oooxx.....oo......o...':51,
'...................xo.....oooo....oooxx...oxoxx....xoo......o...':22,
'...................xo.x...ooox....ooxxx...oooxx....ooo.....oo...':18,
'..................xxoox...oxoo....ooxox...oooox....ooo.....oo...':30,
'...........o......xooox...ooxxx...ooxox...oooox....ooo.....oo...':4,
'...ox......o......xooox...ooxxx...ooxox...oooox....ooo.....oo...':13,
'...ooo.....o.o....xooox...ooxox...ooxox...oooox....ooo.....oo...':33,
'...ooo.....o.o....xooox...ooxox..xxxxox...ooooo....ooo.o...oo...':25,
'...ooo.....o.o.o..xoooo..xxxxox..xxxxox...ooooo....ooo.o...oo...':50,
'...........................ox......xxx..........................':43,
'..................x........xx......oxx.....o....................':19,
'..................xo......xxx......oxx.....o....................':29,
'..................xo......xxxo....xxxx.....o....................':17,
'..........x......oxx......xxxo....xxxx.....o....................':20,
'..........xx.....ooxo.....xxxo....xxxx.....o....................':42,
'..........xx.....oxxo....xxxxo....oxxx....oo....................':33,
'..........xxx....oxxx....oxxxo...ooxxx....oo....................':44,
'...................x.......xx.....oox........x..................':37,
'...................x.......xx.....ooxo......xx..................':20,
'..................xxo......xx.....ooxo......xx..................':21,
'..................xxoo....xxo.....oxxo......xx..................':25,
'.................xxxoo...oxoo.....oxxo......xx..................':43,
'.................xxxoo...oxoo.....ooxo.....xxx....x.............':10,
'..........ox.....xoxoo...ooxo.....oxxo.....xxx....x.............':42,
'...x......xx.....xoxoo...ooxo.....ooxo....oxxx....x.............':12,
'...................xo......xx.....oxxo.....xxx..................':53,
'...................xo......xx.....oxxo.....xxx..................':53,
'...................xo......xx.....oxxx.....xxxx......o..........':29,
'...................xo......xxo....oxxxx....xxox......o..........':42,
'...................xo......xxo....oxxxx...oooxx......x.......x..':30,
'............x......xx......xxoo...oxxox...oooxx......x.......x..':21,
'............xx.....xxx.....xoxo...ooxxx...oooxx......x.......x..':22,
'............xx.....xxxo....xxoo...ooxxx...ooxxx.....xx.......x..':26,
'............xx.....xxxo...oooox...ooxxxx..ooxxx.....xx.......x..':31,
'...................xo.....oooo....ooxxx....xoox......o..........':52,
'...................xo.....oooo....oooxx....xoxx.....oo......o...':51,
'...................xo.....oooo....oooxx....oxxx...oooo......o...':18,
'..................xxo.....oxooo...ooxox....ooxx...oooo......o...':13,
'............ox....xoo.....oxooo...ooxox....ooxx...oooo......o...':61,
'..........o.ox....ooo.....oxooo...ooxox....ooxx...ooox......ox..':21,
'..........o.ox....ooooo...oxooo...oooxx....ooxx...ooox......ox..':23,
'.....o....o.oo....ooooox..oxoox...oooxx....ooxx...ooox......ox..':42,
'....................o.....xxxx....oxxx......xxo......x..........':43,
'....................o.....xxxx....oxxx.....oxoo.....xx..........':21,
'....................oo....xxxo....oxxxx....oxxo.....xx..........':30,
'....................oo....xxxoo...oxxxo....xxxo...x.xx..........':19,
'...................ooo....xxooo...xxxoo...xxxxo...x.xx..........':61,
'...................ooo.x..xxoox...xxxxo...xxxoo...x.xo.......o..':31,
'..........x........xoo.x..xxxooo..xxxxo...xxxoo...x.xo.......o..':59,
'..........x........xoo.x..xxxooo..xxxxo...xxxoo...x.xo.....oxo..':51,
'..................ooo.....ooxx....oxxo.....xx...................':21,
'..................oooo....ooxo....oxxx.....xx.x.................':42,
'..................oooo....oooo...xxxxx....oxx.x.................':51,
'.................xoooo....xooo...xxxxx....oox.x....o............':25,
'...........x.....xoxoo...ooxoo...xoxxx....oox.x....o............':45,
'...........x.....xxxoo...xoooo..xxoxoo....oooox....o............':12,
'...........xo....xxooo...xxxxxx.xxoxoo....oooox....o............':38,
'...........xo....xxooo...xxxxox.xxoxxxxx..oooox....o............':10,
'..........ooo....xoooo...xoxxox.xxoxxxxx..oxoox...xo............':52,
'...........x......oxo....oooo......xo...........................':29,
'...........xo.....ooo....oooox.....xo...........................':21,
'...........xo.....ooox...oooox.....xoo..........................':45,
'...........xo.....ooox...ooooo.....xooo......x..................':13,
'...........xxx....ooox...ooooo.....oooo.....ox..................':34,
'...........xxx....ooooo..ooxoo....xoooo.....ox..................':30,
'...........xxx....oooxo..ooooooo..xoooo.....ox..................':17,
'...o.......oox...xxoxoo..ooooooo..xoooo.....ox..................':23,
'...oo......ooo...xxooo...xxooooo.xxooxoo.xxoooo...oooo.....oo...':10,
'...oo.....xooo..oooooo...oxoxooo.xoooxoo.xxoooo...oooo.....oo...':24,
'..ooo.....oooo..oxoooo..xxxoxooo.xoooxoo.xxoooo...oooo.....oo...':8,
'..ooo...x.oooo..xxoooo..xxooxooo.ooooxooooooooo...oooo.....oo...':58,
'..ooo...x.oooo..xxoooo..xxooxooo.ooooxooooooxoo...oxoo...oooo...':62,
'..........x.x......xxo.x..xxxooo..xxxoo...xxooo...xooo.....oxo..':4,
'....o.....x.o......xoo.x..xxooox..xxxxxx..xxoox...xoox.....oxo..':17,
'....ox....x.x....o.xoo.x..oxooox..xoxxxx..xxoox...xoox.....oxo..':11,
'....ox....xox....o.oooxx..oooxxx..xoxxxx..xxoox...xoox.....oxo..':6,
'....ooo...xoxx...o.oxxxx..oxoxxx..xoxxxx..xxoox...xoox.....oxo..':18,
'..........ooo....xoooo...xoxxox.xxxxxxxx..oxoox...xox........x..':41,
'..........ooo....xoooo...xooxox.xxoxxxxx.oxxoox...xxx.......xx..':55,
'..........ooo....xoooo...xoooox.xxoxxoxx.oxxxxxx..xxx..o....xx..':31,
'..........ooo....xoooo.x.xooooxoxxoxxxxo.oxxxxxo..xxx..o....xx..':15,
'..........ooo..o.xoooo.o.xooooxoxxoxxxxoxxxxxxxo..xxx..o....xx..':49,
'..x.......xxo..o.xxoxo.o.xxooxxoxxxoxxxoxxxxxxxo.oxxx..o....xx..':13,
'..x.......xxoo.o.xxooo.o.xxooxxoxxxoxxxoxxxxxxxo.xxxx..ox...xx..':3,
'..xo......xooo.o.xxxxxxo.xxooxxoxxxoxxxoxxxxxxxo.xxxx..ox...xx..':1,
'..................ox....o.oox....ooxoooo..oxoxoo..oxxx.......x..':30,
'..................ox....o.oooox..ooxoxoo..oxxxoo..oxxx.......x..':20,
'..................oxx...o.ooxooo.ooxxxoo..oxxxoo..oxxx.......x..':22,
'..........o.......oox.x.o.oooxoo.ooxxooo..oxxxoo..oxxx.......x..':21,
#'..........oo......oooxx.o.ooxooo.ooxxooo..oxxxoo..oxxx.......x..':23,
'..........oo...o..oooxooo.ooxoxo.ooxxxoo..oxxxoo..oxxx.......x..':12,
'.....o....ooo..o..ooxxooo.ooxoxo.ooxxxoo..oxxxoo..oxxx.......x..':4,
'..........xx.x...oxxx....oxxxo...ooxxx....oo....................':44,
'..........xx.x...oxxx....oxxxo...xooxx..x.ooo...................':32,
'..........xx.x..xxxxx....oxxxo..ooooxx..x.ooo...................':45,
'..........xx.x..xxxxx.x..oxxxx..ooooxo..x.oooo..................':48,
'..........xx.x..xxxxx.x.xxxxxx..ooooxo..o.oooo..o...............':8,
'...................x....o..xx....oooooo...o.oxoo..o..x.......x..':43,
'...................x....o..xx....ooxooo...oooooo..o.ox.......x..':29,
'...................x....o..xxxo..ooxooo...oooxoo..o.ox.......x..':60,
'...................x....o..xxxo..ooxxoo...oooxoo..ooxx......xx..':57,
'...................x....o..xxxo..ooxxoo...oxoxoo..ooxx...xo.xx..':59,
'...................x..o.o..xxoo..ooxooo...oooxoo..oxxx...xxxxx..':25,
'..................ooo......oxx.....xox.......o..................':44,
'..................ooo......oox.....xxo......xoo.................':30,
'..................oooo.....ooox....xxo......xoo.................':38,
'..................oooo.....ooox....xoxx.....ooo.....o...........':26,
'..................oooo....xxxox....xoxo.....oooo....o...........':39,
'..................oooo....xxoox....ooxxx..o.oooo....o...........':43,
'..................oooo....xxoox....xoxxx..oooooo..o.o...........':51,
'..................oooo....xxoox....xoxxx..oxxooo..ooo.......o...':22,
'..................oooox..ooooxx....xxxxx..oxxooo..ooo.......o...':61,
'..................oooox..ooooxx....xxxxx..oxxooo..oox.......ooo.':53,
'..................oooox..ooooooo...xxxxo..oxxxxo..ooxx......ooo.':23,
'...............o..oooooo.oooooxo...xxxxo..oxxxxo..ooxx......ooo.':58,
'...............o..oooooo.oooooxo...xxoxo..oxxxoo..oxxx.o..x.ooo.':41,
'...............o..oooooo.oooooxoo..xxoxo.oxxxxoo..oxxx.o..x.ooo.':40,
'.*...*...*xo*x*..*xxxx...*xxxoo..*xooxoo.x..ooo......o..........'.replace("*","."):33,
'.**.......o****..*oxoo*x.*ooxoox.*oooxox..x*ooxx...**o.x....xxx.'.replace("*","."):13,
'....*.....**x*****oxoxxo*xxxoxxx*xooooxx.ooooxxx....o***........'.replace("*","."):11,
'.ooooo...*oxxx...*ooxxxx.*ooxxxx.*oooxxx.*o*ooxx.*o**o.x....xxx.'.replace("*","."):52,
'........**.x..*..ooooo...xoooo*.x..xoo*......o..................'.replace("*","."):30,
'.**oooo..*oxxo**xxxxoooo.xxxoxoooxxoxoxoooxxoxooo*.xxo*o...oooo.'.replace("*","."):2,
'............*.....*xo***..oxxxx*..oxoxx*..oxoxx*..oxxo*..*xxoo..'.replace("*","."):57,
'........o..***..o.xxo**xoxxooox.oxxooxx.ooxxxxx.o*oooo...**oooo.'.replace("*","."):22,
'............**.****xo*o*oooooooxooxooooooxxxoxoo..xxxx.*.xxxxx..'.replace("*","."):55,
'...........***..***xo*..oooxox..oooxoxx.ooxooxxxo*ooox...*ooxx..'.replace("*","."):57,
'..*o......*o....**ooxx..*oooxxx.ooooox...**xxo*...x..*..........'.replace("*","."):46,
'........*********oooooox.*ooxoxx.*oxxxxx.o.xoxxx.*ooxo*x.**oooo.'.replace("*","."):57,
'.****...**xxo...oxxoo...oxxxoo..oxxoxo..xxooox*.*.*o.*..........'.replace("*","."):48,
#'...........***.....xo**....xxo*..*oxxxx..*ooxxx..***oo.....**o*.'.replace("*","."):11,
#'...........*****...xo*o*ox.xoooooxxxxxxoo*oxoxxo.*oxxx...xxxxx..'.replace("*","."):41,
'...........x......oooo...oooox.....xo...........................':43,
'...o.......o......oooo...oooox.....xx......x....................':12,
'...o.......ox.....oooo...oooxo.....xx.o....x....................':33,
'...o.......ox.....oxoo...oooxo...xoxx.o....x....................':24,
'...o.......ooo....oxoo..xxxxxo...xoxx.o....x....................':42,
'...o.......ooo....oxoo..xxxoxo...xoxx.o..oxx....................':10,
'...ooo....ooo..o..ooxoooo.ooxooo.ooxxxoo..oxxxoo..oxxx.......x..':25,
'...ooo....ooo..o..ooxooooxxoxooo.oxoxxoo..ooxooo..ooox.....o.x..':32}
            #theoryDct = {}
            if board in theoryDct:
                best_move.value = theoryDct[board]
                return
        global timeLimit
        timeLimit = time_limit
        m = findMoves(board,player)[0]
        if len(m) == 1:
            best_move.value = int(*m)
        print(board.count(".")-4)
        print(f"tl: {time_limit}")
        mv = quickMove(board, player,t, time_limit)
        if len(ws) > 0:
            printEval(ws)
        
        best_move.value = mv
        return
        
def printEval(ws):
    print(f"cpScore: {ws[0]}, w1 = {ws[7]}")
    print(f"mobScore: {ws[1]}, w2 = {ws[8]}")
    print(f"cScore: {ws[2]}, w3 = {ws[9]}")
    print(f"eScore: {ws[3]}, w4 = {ws[10]}")
    print(f"msScore: {ws[4]}, w5 = {ws[11]}")
    print(f"pmScore: {ws[5]}, w6 = {ws[12]}")
    print(f"acScore: {ws[6]}, w7 = {ws[13]}")
    print(f"token color: {ws[14]}")
    print(f"brd: {ws[15]}")   
                


def main():
    nb = board
    token = defaultToken
    opT = opToken
    nb, token, opT = nb.upper(), token.upper(), opT.upper()
    possibleChoices, flippedSection = findMoves(nb,token)
    if not possibleChoices:
        token, opT = opT, token
        possibleChoices, flippedSection = findMoves(nb,token)
    #No move made B-E
    if (not moves and not verbose) or  verbose:
        printBoard(nb,possibleChoices)
        print("")
        print(nb + calcScore(nb))

        if possibleChoices:
            print(f"Possible moves for {token}: {possibleChoices}")
            print("")
        else:
            #print("No moves possible")
            print("")

    #if not moves:
        #moves.append(quickMove(nb,token))
    
    #new move A-E
    #loop here
    for move in moves:
        if move >= 0:
            if (move == moves[len(moves)-1] and  not verbose) or verbose:
                print(f"{token} plays to {move}") 
            nb = makeMove(nb, token, move, flippedSection)
            #swap tokens after the move
            token, opT = opT, token
            possibleChoices, flippedSection = findMoves(nb,token)
            if not possibleChoices:
                token, opT = opT, token
                possibleChoices, flippedSection = findMoves(nb,token)
            if (move == moves[len(moves)-1] and  not verbose) or verbose:
                printBoard(nb, possibleChoices, move)
                print("")
                print(nb + calcScore(nb))

                if possibleChoices:
                    print(f"Possible moves for {token}: {possibleChoices}")
                    print("")
                else:
                    #print("No moves possible")
                    print("")
                    #break

            #moves.append(quickMove(nb,token))
    #othello 4 part w quick move

    if possibleChoices:
        t = time.time()
        print(f"my preferred move is: {quickMove(nb,token,t,5)}")
        print(f"my preferred move is: {TERMINALalphabeta(nb, token, -65,65, abCache)}")
        a = nb.count(".")
        print(f"brd count: {a}")
        #for e in evaluateCache2:
            #ab = alphabeta(e[0].upper(), e[1].upper(), -10000000, 10000000, abCache,6,5)
            #print("('" + e[0] + "'" + "," + "'" + e[1] + "'" + ")" + ":" + str(ab[0]) +",")
        print("")
        print("")
        """for i in range(200):
            brd, tkn = createRandom()
            if (brd, tkn) not in evaluateCache2:
                ab = alphabeta(brd.upper(), tkn.upper(), -10000, 10000, abCache,6,5)
                print("('" + brd + "'" + "," + "'" + tkn + "'" + ")" + ":" + str(ab[0]) +",") 
            evaluateCache2[(brd,tkn)] = ab[0]"""
        print("")
        print(quickMove(board, token,t, 1))
        #print(time.time()-t)
        """if nb.count(".") < hl:
            ab =TERMINALalphabeta(nb, token, -65,65, abCache)
            print(f"Min Score: {ab[0]}; move sequence: {ab[1:]}")
        else:
            ab =alphabeta(nb, token, -10000,10000, abCache)
            print(f"Min Score: {ab[0]}; move sequence: {ab[1:]}")"""


def createRandom():
    n = random.randrange(6,20)
    brd = ('.'*27 + "ox......xo" + '.'*27).upper()
    tkn = 'X'
    for i in range(n):
        choices, fs = findMoves(brd, tkn)
        choices = orderMoves(brd,tkn,choices,fs)
        if len(choices) != 0:
            rn = len(choices)//2
            if rn == 0: rn = 1
            idx = random.randrange(0,rn)
            mv = choices[idx]
            brd = makeMove(brd,tkn,mv,fs)
        tkn = "XO".replace(tkn,"")
    return brd, tkn

    
    
        #to here


global t1,t2,t3,t4,t5,top
top = 5
#t1 = 4/5; t2 =  3.9/5; t3 = 0.7/5; t4 = 2.45/5; t5 = 3.2/5
t1 = 6/7; t2 =  5.9/7; t3 = 2.7/7; t4 = 4.45/7; t5 = 5.2/7
def alphabeta(brd,tkn, alpha, beta, abCache,n=5,timeLeft = 0, secondBest = False):
    n-=1
    eTkn = "XO".replace(tkn,"")
    if n <= 0: 
        if timeLimit < 5:
            e = evaluate(brd,tkn,timeLimit)
            return [e[0]], e[1]
        t= time.time()
        if t-timeLeft >= t1*timeLimit or n < -2:
        #if timeLeft-t >= t1*timeLeft or n < -3:
            e = evaluate(brd,tkn,timeLimit)
            return [e[0]], e[1]
        if t-timeLeft <= t2*timeLimit and n< -1 and len(findMoves(brd,tkn)[0]) < 5:
        #if timeLeft-t <= t2*timeLeft and n< -1 and len(findMoves(brd,tkn)[0]) < 5:
            pass
        if t-timeLeft < t3*timeLimit:
        #elif timeLeft-t < t3*timeLeft:
            pass
        elif t-timeLeft <= t4*timeLimit and len(findMoves(brd,tkn)[0]) < 11:
        #elif timeLeft-t <= t4*timeLeft and len(findMoves(brd,tkn)[0]) < 11:
            pass
        elif t-timeLeft <= t5*timeLimit and len(findMoves(brd,tkn)[0]) < 7:
        #elif timeLeft-t <= t5*timeLeft  and len(findMoves(brd,tkn)[0]) < 7: 
            pass
        else:
            e = evaluate(brd,tkn,timeLimit)
            return [e[0]], e[1]
    possibleMoves, flippedSections= findMoves(brd,tkn)

    #if len(possibleMoves) <= 2: n+=1

    if (brd, tkn,alpha,beta) in abCache:
        return abCache[(brd, tkn,alpha,beta)]

    if not possibleMoves:
        if not findMoves(brd,eTkn)[0]:
            e = evaluate(brd,tkn,timeLimit)
            #print(f"e {e}")
            return [e[0]], e[1]

        if (brd, eTkn,-beta,-alpha) not in abCache:
            abCache[(brd, eTkn,-beta,-alpha)] = alphabeta(brd,eTkn,-beta,-alpha,abCache,n,timeLeft,secondBest)
        ab,w = abCache[(brd, eTkn,-beta,-alpha)]

        if -ab[0] < alpha: return [alpha-1],w
        return [-ab[0]] + ab[1:] + [-1],w
    
    bestSoFar = [alpha-1]

    for mv in orderMoves(brd,tkn,possibleMoves,flippedSections,timeLimit,n):
        #print(str(mv) + "  " + tkn)
       
        newBrd = makeMove(brd,tkn,mv,flippedSections)
        #printBoard(newBrd,{},mv)
        if (newBrd, eTkn,-beta,-alpha) not in abCache:
            abCache[(newBrd, eTkn,-beta,-alpha)] = alphabeta(newBrd,eTkn,-beta,-alpha,abCache,n,timeLeft,secondBest)
        ab,w = abCache[(newBrd, eTkn,-beta,-alpha)]
        score = -ab[0]
        
        if score < alpha: continue
        if score > beta: return[score],w
        bestSoFar = [score] + ab[1:] + [mv]
        alpha = max(alpha, score)

    

    abCache[(brd, tkn,alpha,beta)] = bestSoFar,w
    return bestSoFar,w

def evaluate(brd, tkn, tl,ifImported = False):
    #if (brd, tkn) in evaluateCache:
        #return evaluateCache[(brd, tkn)]
    if brd.count(tkn) == 0:
        return -10000,[-100]*15
    aroundCorner = {1: 0, 8: 0, 9: 0, 6: 7, 14: 7, 15: 7, 48: 56, 49: 56, 57: 56, 54: 63, 55: 63, 62: 63}
    aroundEdgeToEdge = {1:[0,1,2,3,4,5,6,7], 6:[0,1,2,3,4,5,6,7], 8:[0,8,16,24,32,40,48,56], 48:[0,8,16,24,32,40,48,56],
                        57:[56,57,58,59,60,61,62,63], 62:[56,57,58,59,60,61,62,63], 15:[7,15,23,31,39,47,55,63], 55:[7,15,23,31,39,47,55,63]}
    #verticals = [[0,8,16,24,32,40,48,56],[7,15,23,31,39,47,55,63]]

    eTkn = "XO".replace(tkn,"")
    tct = brd.count(tkn)
    ect = brd.count(eTkn)
    """table_weights = [120, -20, 20, 5, 5, 20, -20, 120,     
                    -20, -70, -5, -5, -5, -5, -70, -20,     
                    20, -5, 15, 3, 3, 15, -5, 20,     
                    5, -5, 3, 3, 3, 3, -5, 5,    
                    5, -5, 3, 3, 3, 3, -5, 5,     
                    20, -5, 15, 3, 3, 15, -5, 20,     
                    -20, -70, -5, -5, -5, -5, -70, -20,     
                    120, -20, 20, 5, 5, 20, -20, 120]"""

    table_weights = [20, -3, 11, 8, 8, 11, -3, 20,     
                    -3, -7, -4, 1, 1, -4, -7, -3,     
                    11, -4, 2, 2, 2, 2, -4, 11,     
                    8, 1, 2, 5, 5, 2, 1, 8,    
                    8, 1, 2, 5, 5, 2, 1, 8,     
                    11, -4, 2, 2, 2, 2, -4, 11,     
                    -3, -7, -4, 1, 1, -4, -7, -3,     
                    20, -3, 11, 8, 8, 11, -3, 20]

    if brd[0] == tkn:
        table_weights[1]=3
        table_weights[9]=7
        table_weights[8]=3
        if eTkn in brd[1] or eTkn in brd[8]:
            table_weights[0] == -10
    if brd[7] == tkn:
        table_weights[6]=3
        table_weights[14]=7
        table_weights[15]=3
        if eTkn in brd[6] or eTkn in brd[15]:
            table_weights[7] == -10
    if brd[56] == tkn:
        table_weights[48]=3
        table_weights[49]=7
        table_weights[57]=3
        if eTkn in brd[48] or eTkn in brd[57]:
            table_weights[56] == -10
    if brd[63] == tkn:
        table_weights[62]=3
        table_weights[55]=7
        table_weights[54]=3
        if eTkn in brd[62] or eTkn in brd[54]:
            table_weights[63] == -10

    corners = {0, 7, 56, 63}
    

    #printBoard(brd, {})
    #print("")
    
    if "." not in brd:
        return 100*(brd.count(tkn)-brd.count(eTkn))/64
    score = -100
    #coin parity
    cpScore = 100* (tct-ect)/(tct+ect)
    #cpScore = brd.count(tkn)-brd.count(eTkn)
    #mobility
    moves,_ = findMoves(brd,tkn)
    eMoves,_ = findMoves(brd,eTkn)
    mobScore = 0
    #pm = potentialMobility(brd, eTkn)
    #pmE = potentialMobility(brd, tkn)

    pm = pM(brd, eTkn)
    pmE = pM(brd, tkn)

    edges = [0,1,2,3,4,5,6,7,56,57,58,59,60,61,62,63,8,16,24,32,40,48,15,23,31,39,47,55]
    pmct = 0
    pmEct = 0
    for t in brd:
        if t==tkn and t not in edges:
            pmct+=1
        if t==eTkn and t not in edges:
            pmEct +=1
    
    cpScore = 100* (tct-ect)/(tct+ect)

    pm/=pmct
    pmE/=pmEct

    pmScore = 0
    if pm + pmE != 0:
        pmScore = 100 * (pm-pmE)/(pm + pmE)

    m = len(moves)
    eM = len(eMoves)
    if m + eM != 0:
        mobScore = 100 * (m - eM)/(m + eM)
    
    #if brd.count(".") > 37:
        #return (pmScore*174 + mobScore* 178)/(174+178)
        #mobScore = len(moves)-len(eMoves)
    #corners
    numCorners = len(corners.intersection(moves))*0.91*0
    eNumCorners = len(corners.intersection(eMoves))*0.91
    numCorners = 0
    cScore = 0
    if numCorners + (brd[0] == tkn) + (brd[7] == tkn) + (brd[56] == tkn) + (brd[63] == tkn) + (
        eNumCorners + (brd[0] == eTkn) + (brd[7] == eTkn) + (brd[56] == eTkn) + (brd[63] == eTkn)) != 0:

        cScore = 100*(numCorners + (brd[0] == tkn) + (brd[7] == tkn) + (brd[56] == tkn) + (brd[63] == tkn) 
         - (eNumCorners + (brd[0] == eTkn) + (brd[7] == eTkn) + (brd[56] == eTkn) + (brd[63] == eTkn)))/4
        """(
             numCorners + (brd[0] == tkn) + (brd[7] == tkn) + (brd[56] == tkn) + (brd[63] == tkn) + (
            eNumCorners + (brd[0] == eTkn) + (brd[7] == eTkn) + (brd[56] == eTkn) + (brd[63] == eTkn)))"""

    if cScore != 0:
        if brd[0] == tkn:
            if eTkn in brd[1] or eTkn in brd[8]:
                cScore -=10
        if brd[7] == tkn:
            if eTkn in brd[6] or eTkn in brd[15]:
                cScore -=10
        if brd[56] == tkn:
            if eTkn in brd[48] or eTkn in brd[57]:
                cScore -=10
        if brd[63] == tkn:
            if eTkn in brd[62] or eTkn in brd[54]:
                cScore -=10
        
        if brd[0] == eTkn:
            if tkn in brd[1] or tkn in brd[8]:
                cScore +=5
        if brd[7] == eTkn:
            if tkn in brd[6] or tkn in brd[15]:
                cScore +=5
        if brd[56] == eTkn:
            if tkn in brd[48] or tkn in brd[57]:
                cScore +=5
        if brd[63] == eTkn:
            if tkn in brd[62] or tkn in brd[54]:
                cScore +=5

    #cScore = numCorners + (brd[0] == tkn) + (brd[7] == tkn) + (brd[56] == tkn) + (brd[63] == tkn)
    #cScore -= eNumCorners + (brd[0] == eTkn) + (brd[7] == eTkn) + (brd[56] == eTkn) + (brd[63] == eTkn)
    #stability
    
    """stable = stableCount(brd,tkn,eTkn)
    eStable = stableCount(brd,eTkn,tkn)
    sScore = 0
    stable = stable/ tct
    eStable = eStable/ ect
    if stable or eStable:
        sScore = 100*(stable - eStable)/(stable + eStable)"""

    #edge Stability

    """edge = edgeStability(brd,tkn,eTkn)
    eEdge = edgeStability(brd,eTkn,tkn)
    eScore = 0
    if edge + eEdge != 0:
        eScore = 100*(edge - eEdge)/(edge + eEdge)"""
    
    #eScore, eDiff = edgeStability2(brd,tkn,eTkn)
    #oScore, oDiff = edgeStability2(brd,eTkn,tkn)
    eScore= edgeStability2(brd,tkn,eTkn)

    #if eScore + oScore != 0:
        #eScore = 100*(eScore - oScore)/(eScore + oScore)
    
    #More edgeStability
    if len(moves) > 0 and len(eMoves) > 0:
        m = dfc(brd,tkn,eMoves)
        em = dfc(brd,eTkn,moves)
        m/=tct
        em/=tct
        tScore = 0
        if m + em != 0:
            tScore = 100*(m - em)/(m + em)
    
    #stable = len(stability(brd,tkn))/pmct
    #eStable = len(stability(brd,eTkn))/pmEct
    msScore = 0
    stable = stability3(brd,tkn)#/tct
    eStable = stability3(brd,eTkn)#/ ect

    if stable + eStable != 0:
        msScore = 100*(stable - eStable)/(stable + eStable)
    

    
    tScore = 0
    eTScore = 0
    for i in range(64):#[1,8,9, 6,14,15, 48,49,57, 54,55,62]:
        if brd[i] == tkn:
            tScore += table_weights[i]
        if brd[i] == eTkn:
            eTScore += table_weights[i]
    
    #tScore/= tct
    #eTScore/= ect

    if tScore + eTScore != 0:
        tScore = 100*(tScore - eTScore)/(tScore + eTScore)
    else:
        tScore = 0

    acScore = 0
    macScore = 0
    eacScore = 0
    """for e in aroundCorner:
        if brd[e] == tkn:
            if brd[aroundCorner[e]] == ".":
                if e not in [9,14,54,49] and e in aroundEdgeToEdge and eTkn not in [brd[i] for i in aroundEdgeToEdge[e]]: pass
                elif e in [9,14,54,49]: eacScore += 20
                #eacScore += 20
            elif e not in [9,14,54,49] and brd[aroundCorner[e]] == eTkn:
                macScore += 1
            elif e not in [9,14,54,49] and brd[aroundCorner[e]] == tkn:
                macScore += 20
            else:
                eacScore += 20
        if brd[e] == eTkn:

            if brd[aroundCorner[e]] == ".":
                if e not in [9,14,54,49] and e in aroundEdgeToEdge and tkn not in [brd[i] for i in aroundEdgeToEdge[e]]: pass
                elif e in [9,14,54,49]: macScore += 20
                #macScore += 20
            elif e not in [9,14,54,49] and brd[aroundCorner[e]] == tkn:
                eacScore += 1
            elif e not in [9,14,54,49] and brd[aroundCorner[e]] == eTkn:
                eacScore += 20
            else:
                macScore += 20"""
    
    for e in [[1,8,9],[6,14,15],[48,49,57],[54,55,62]]:
        s = [brd[i] for i in e]
        s.append(brd[aroundCorner[e[0]]])
        if "." not in s: continue
        for i in e:
            if brd[i] == tkn:
                if i in [9,14,54,49]:
                    if brd[aroundCorner[i]] == tkn:
                        pass
                    elif brd[aroundCorner[i]] == eTkn:
                        eacScore+=19
                    else:
                        eacScore+=20
                else:
                    if brd[aroundCorner[i]] == tkn:
                        pass
                    elif brd[aroundCorner[i]] == eTkn:
                        if isSafeAC(tkn,eTkn,"".join([brd[j] for j in aroundEdgeToEdge[i]]),i):
                            eacScore+=19
                        else:
                            eacScore+=20
                    else:
                        if eTkn not in [brd[j] for j in aroundEdgeToEdge[i]]:
                            pass
                        else:
                            eacScore+=20

            elif brd[i] == eTkn:
                if i in [9,14,54,49]:
                    if brd[aroundCorner[i]] == eTkn:
                        pass
                    elif brd[aroundCorner[i]] == tkn:
                        macScore+=19
                    else:
                        macScore+=20
                else:
                    if brd[aroundCorner[i]] == eTkn:
                        pass
                    elif brd[aroundCorner[i]] == tkn:
                        if isSafeAC(eTkn,tkn,"".join([brd[j] for j in aroundEdgeToEdge[i]]),i):
                            macScore+=19
                        else:
                            macScore+=20
                    else:
                        if tkn not in [brd[j] for j in aroundEdgeToEdge[i]]:
                            pass
                        else:
                            macScore+=20
            
    
    if macScore + eacScore != 0:
        acScore = 100*(macScore - eacScore)/(macScore + eacScore)
    
        """WEIGHTS = [-35, 0*78.922, 601.724, -15, 45, 274.396, 60, 20,
                -20, 78.922, 501.724, -15, 15, 254.396, 60, 20,
                0, 158.922, 601.724, 5, 0, 154.396, 60, 20,
                0,  158.922, 801.724, 5, 0, 174.396, 60, 20]"""

    """WEIGHTS = [-35, 0*78.922, 601.724, 0, 45, 274.396, 60, 0*10,
                -20, 78.922, 501.724, 0, 15, 54.396, 60, 0*10,
                -5, 78.922, 501.724, 0,0, 54.396, 60, 0*20,
                0,  78.922, 501.724, 15, 0, 74.396, 60, 0*20]"""
    
    WEIGHTS = [-35, 78.922, 1001.724, 0, 0, 274.396, 30, 100,
                -20, 378.922, 1001.724, 30, 75, 154.396, 30, 100,
                -5, 378.922, 1001.724, 35,75, 154.396, 30, 200,
                0,  78.922, 1001.724, 35, 70, 154.396, 30, 200]
    w1, w2, w3, w4, w5, w6, w7, w8 = WEIGHTS[0],WEIGHTS[1],WEIGHTS[2],WEIGHTS[3],WEIGHTS[4],WEIGHTS[5],WEIGHTS[6],WEIGHTS[7]
    if brd.count(".") <= 50: 
        w1, w2, w3, w4, w5, w6, w7, w8 = WEIGHTS[8],WEIGHTS[9],WEIGHTS[10],WEIGHTS[11],WEIGHTS[12],WEIGHTS[13],WEIGHTS[14],WEIGHTS[15]
        #if eDiff < -0.275:
            #w4+=10
    if brd.count(".") <= 40: 
        w1, w2, w3, w4, w5, w6, w7, w8 = WEIGHTS[16],WEIGHTS[17],WEIGHTS[18],WEIGHTS[19],WEIGHTS[20],WEIGHTS[21],WEIGHTS[22],WEIGHTS[23]
        #if eDiff < -0.275:
            #w2+=75
    if brd.count(".") <= 20: 
        w1, w2, w3, w4, w5, w6, w7, w8 = WEIGHTS[24],WEIGHTS[25],WEIGHTS[26],WEIGHTS[27],WEIGHTS[28],WEIGHTS[29],WEIGHTS[30],WEIGHTS[31]
        #if eDiff < -0.275:
            #w4+=100
    if brd.count(".") <= 10: 
        w1, w2, w3, w4, w5, w6, w7, w8 = 5,78,100,55,45,0,0,0

    we = [-254.99999999999997, 50, 100, 40, -231.93597793579102, 0, 0, 
    -5, 60, 200, 50, 0, 0, 0, 
    -20.642642974853512, 60, 100, 999.9999999999999, -431.87500000000006, -113.48388671875001, 0, 
    306.40624999999994, 60, 100, 0, 0, 10, 0, 
    -10, 40, 0, 0, 0, 10, 0]
    """we = [-15,50,0,10,5,20,0,
            -25,60,100,10,5,40,0,
            -20,60,0,0,0,40,1,
            -20,90,50,10,5,30,1,
            -10,60,70,20,15,30,0]"""
    """we = [-15,60,0,10,15,50,0,
            -25,50,100,10,5,40,0,
            -20,40,0,10,20,40,10,
            -20,50,50,10,5,30,10,
            -10,30,70,10,15,30,0]

    if pmScore > 25 and brd.count(".") > 10:
        w1+=we[0]
        w2+=we[1]
        w3+=we[2]
        w4+=we[3]
        w5+=we[4]
        w6+=we[5]
        w7+=we[6]
    if pmScore < -20 and brd.count(".") > 10:
        w1+=we[7]
        w2+=we[8]
        w3+=we[9]
        w4+=we[10]
        w5+=we[11]
        w6+=we[12]
        w7+=we[13]

    if cpScore < 0:
        w4+=30
        w2+=50
        w6+=20
        w5+=15
        w3+=50
    
    if eScore <-50:
        w1 = 20
        w6+=20
        w2+=20
        w5+=15
        w3+=50
        w4+=45
    if mobScore > 25 and brd.count(".") > 10:
        w2+=40
        w5+=10
        w4+=10
        w3+=50


    


    if eScore >0 and cpScore < 10:
        w1+=we[14]
        w2+=we[15]
        w3+=we[16]
        w4+=we[17]
        w5+=we[18]
        w6+=we[19]
        w7+=we[20]
        
    if mobScore <-10 and brd.count(".") > 10:
        w1+=we[21]
        w2+=we[22]
        w3+=we[23]
        w4+=we[24]
        w5+=we[25]
        w6+=we[26]
        w7+=we[27]

    if mobScore > 40 and brd.count(".") > 10:
        w1+=we[28]
        w2+=we[29]
        w3+=we[30]
        w4+=we[31]
        w5+=we[32]
        w6+=we[33]
        w7+=we[34]
    
    if cScore > 25:
        w1-=30
        w2+=30
    
    if cScore < 0:
        w3+=100
        w7-=30
    
    if cpScore < -15 and eScore > 50:
        w1 = 0
        w2+=40
        w4+=30
        w5+=20
        w6+=30
        w3+=100

    if mobScore > 50:
        w2+=50
    if msScore > 50 and brd.count(".") > 15:
        w5+=50
        if mobScore < -35:
            w5-=40
            w2+=50

    if pmScore > 50:
        w6+=50
        if mobScore < -35:
            w6-=40
            w2+=50

    #w1*=3/4

    if mobScore < -35:
        w2+=100"""
    

    we = [15,60,0,10,10,50,0,
            25,50,100,10,10,40,0,
            -20,40,0,0,10,40,10,
            20,50,50,10,20,30,10,
            10,30,70,20,15,30,0]

    """if pmScore > 25 and brd.count(".") > 10:
        w1-=we[0]
        w2+=we[1]
        w3+=we[2]
        w4+=we[3]
        w5+=we[4]
        w6+=we[5]
        w7+=we[6]
    if pmScore < -20 and brd.count(".") > 10:
        w1-=we[7]
        w2+=we[8]
        w3+=we[9]
        w4+=we[10]
        w5+=we[11]
        w6+=we[12]
        w7+=we[13]

    if eScore < -50:
        w4-=10
        w2+=30
        w6+=40
        w5+=45
        w3+=100"""
    
    #if eScore >0:
        #w1 = 20
        #w6+=20
        #w2+=20
        #w5+=15
        #w3+=50
        #w4+=55
    #if mobScore > 25 and brd.count(".") > 10:
        #w2+=40
        #w5+=10
        #w4+=10
        #w3+=50
        #w7 = 0


    


    #if eScore > 0 and cpScore < 10:
        #w1-=we[14]
        #w2+=we[15]
        #w3+=we[16]
        #w4+=we[17]
        #w5+=we[18]
        #w6+=we[19]
        #w7+=we[20]
        
    """if mobScore <-10 and brd.count(".") > 10:
        w1-=we[21]
        #w2+=we[22]
        w3+=we[23]
        #w4+=we[24]
        w5+=we[25]
        w6+=we[26]
        #w7+=we[27]

    if mobScore > 40 and brd.count(".") > 10:
        #w1-=we[28]
        w2+=we[29]
        #w3+=we[30]
        #w4+=we[31]
        #w5+=we[32]
        w6+=we[33]
        #w7+=we[34]
        #w7 = 0"""
    
    #if cScore > 25:
        #w1-=30
        #w2+=30
    
    #if cScore < 0:
       #w3+=100
        #w7-=30
    
    if cpScore < -15: #and #eScore < 8:
        w2+=40
        w4+=30
        w5+=20
        w6+=30
        w3+=100

    if mobScore > 35:
        w2+=120
        w6+=50
        
    if msScore > 50 and brd.count(".") > 15:
        w6+=50
        w2+=20
        w5+=100
        #w7 = 0
        #if mobScore < -35:
            #w5-=40
            #w2+=50

    if pmScore > 50:
        w6+=150
        w5+=20
        w2+=50
        #w4+=30
        #w7 = 0
        if mobScore < -35:
            w6-=40
            w2+=500

    if cpScore < -20:
        w1 = -1
    if cpScore < -50:
        w1-=50
        w6+=50
    
    if mobScore < -35:
        w1-=10
        #w4-=30
        w5+=20
        w6+=50
        w2+=10
        if brd.count(".") < 15:
            w2-=10000+1000
    
    if cpScore > 35:
        w1-=1000
    
    if msScore < -35:
        w6+=20
        w5=0
        w2+=20
        w4+=10
        
    
        
        
    
    
    ###TEEST ACSCORE SEE IF IT WORKS FOR THE DIAGONAL AROUND CORNERS###

       
        

  

    tW = w1+w2+w3+w4+w5+w6+w7+w8
    #tW = w1+w2+w3+w5+w6+w7
    score = (cpScore*-1 + mobScore*w2 + cScore*w3 + eScore*w4 + msScore*w5 + pmScore*w6 + acScore*w7 + tScore*w8*0)#tW
    #score = (cpScore*w1 + mobScore*w2 + cScore*w3 + tScore*w5 + pmScore*w6 + acScore*w7)/tW
    #if tl == 1:
        #print(time.time()-TIME)
    #if oScore == 0:
        #score += 50
    
    evaluateCache[(brd, tkn)] = score

    if ifImported:
        print(f"cpScore: {cpScore}")
        print(f"mobScore: {mobScore}")
        print(f"cScore: {cScore}")
        print(f"eScore: {eScore}")
        print(f"msScore: {msScore}")
        print(f"pmScore: {pmScore}")
        print(f"acScore: {acScore}")
        #print(f"tScore: {tScore}")

    return score,[cpScore, mobScore, cScore, eScore, msScore, pmScore, acScore, w1,w2,w3,w4,w5,w6,w7,tkn,brd]

global f
f = False

def dfc(brd,tkn, moves):
    dfcScore = 0
    board = [[brd[i*8 + j] for j in range(8)] for i in range(8)]
    
    dMoves = [(m%8,m//8) for m in moves]
    midpoint = dMoves[0]
    for i in range(1,len(dMoves)):

        ix, iy = dMoves[i]
        midpoint = (midpoint[0] + ix)/2,(midpoint[1] + iy)/2
    center_x, center_y = midpoint
    for i in range(8):
        for j in range(8):
            if board[i][j] == tkn:
                distance_from_center = ((i-center_x)**2 + (j-center_y)**2)**0.5
                weight = max(0, 1 - distance_from_center/8)
                #weight = distance_from_center
                dfcScore+=weight
    return dfcScore

def isSafeAC(tkn,eTkn, edgeString, i):
    es = edgeString[1:len(edgeString)-1]
    if eTkn not in es: return False
    #xo path
    if i not in [1,57,15,8]:
        es = es[::-1]
    if tkn+eTkn not in es: return False
    dot = es.find(".")
    if dot == -1:
        if es.find(tkn+eTkn): return True
        return False
    else:
        if dot < es.find(tkn+eTkn): return False
        return True

def edgeStability2(brd, tkn, eTkn):
    """# check vertical
    brd=brd.lower()
    tkn = tkn.lower()
    eTkn = eTkn.lower()
    horizontals = [[0,1,2,3,4,5,6,7],[56,57,58,59,60,61,62,63]]
    verticals = [[0,8,16,24,32,40,48,56],[7,15,23,31,39,47,55,63]]
    hv = horizontals + verticals
    myTotal = 0
    eTotal = 0
    total = 0
    for edge in hv:
        eString = "".join([brd[i] for i in edge]).lower()
        if "x.x" in eString or "o.o" in eString or "x..x" in eString or "o..o" in eString or "x...x" in eString or "o...o" in eString: continue
        eString.replace(".","")
        length = len(eString)
        total += length
        if length > 1:
            if "ox" in eString or "xo" in eString: continue
            elif tkn in eString: myTotal+= length
            elif eTkn in eString: eTotal+= length
    
    if total != 0: return 100*(myTotal - 0)/total, myTotal
    return 0, 0"""
    # check vertical
    tkn = tkn.lower()
    eTkn = eTkn.lower()
    horizontals = [[0,1,2,3,4,5,6,7],[56,57,58,59,60,61,62,63]]
    verticals = [[0,8,16,24,32,40,48,56],[7,15,23,31,39,47,55,63]]
    hv = horizontals + verticals
    myTotal = 0
    eTotal = 0
    bonus = 0
    eBonus = 0
    for edge in hv:
        eString = "".join([brd[i] for i in edge]).lower()
        if eTkn in eString and tkn in eString:
            continue
        if eTkn not in eString and tkn not in eString:
            continue
        if tkn*2 in eString or tkn*3 in eString or tkn*4 in eString or tkn*5 in eString or tkn*6 in eString:
            myTotal+=1
            if brd[edge[0]] == tkn or brd[edge[7]] == tkn or tkn*7 in eString or tkn*8 in eString:
                bonus+=1
        if eTkn*2 in eString or eTkn*3 in eString or eTkn*4 in eString or eTkn*5 in eString or eTkn*6 in eString:
            eTotal+=1
            if brd[edge[0]] == eTkn or brd[edge[7]] == eTkn or eTkn*7 in eString or eTkn*8 in eString :
                eBonus-=1
    if bonus-eBonus !=0:
        if bonus >= 1:
            return bonus*500
        if eBonus >=1:
            return eBonus*-500

    if myTotal == 0:
        if eTotal == 1:
            return -75
        if eTotal == 2:
            return -50
        if eTotal == 3:
            return -25
        if eTotal == 4:
            return 5
        else: return 0
    if myTotal == 1:
        if eTotal == 1:
            return 0
        if eTotal == 2:
            return 20
        if eTotal == 3:
            return 45
        else: return 75
    if myTotal == 2:
        if eTotal == 1:
            return -20
        if eTotal == 2:
            return 0
        else:
            return 50
    if myTotal == 3:
        if eTotal == 1:
            return -45
        else:
            return 25
    if myTotal == 4:
        return -5
    return 0

def stability2(board_str, token):
    # Convert the board string to a 2D list of characters
    board = [[board_str[i*8 + j] for j in range(8)] for i in range(8)]

    stability_score = 0
    n = len(board)
    center_x, center_y = (n-1)/2, (n-1)/2

    for i in range(n):
        for j in range(n):
            if board[i][j] == token:
                adjacent_tokens = get_adjacent_tokens(board, i, j)
                potential_flips = sum([potential_flips for x, y, potential_flips in adjacent_tokens])
                stability = potential_flips + 1
                distance_from_center = ((i-center_x)**2 + (j-center_y)**2)**0.5
                # give more weight to positions closer to the center of the board
                weight = max(0, 1 - distance_from_center/n)
                stability_score += stability * weight

    return stability_score


def get_adjacent_tokens(board, i, j):
    n = len(board)
    directions = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if not (dx == 0 and dy == 0)]
    adjacent_tokens = []
    for dx, dy in directions:
        x = i + dx
        y = j + dy
        if 0 <= x < n and 0 <= y < n:
            adjacent_tokens.append((x, y, count_potential_flips(board, i, j, dx, dy)))
    return adjacent_tokens

def count_potential_flips(board, i, j, dx, dy):
    n = len(board)
    token = board[i][j]
    flips = 0
    x = i + dx
    y = j + dy
    while 0 <= x < n and 0 <= y < n:
        if board[x][y] == token:
            return flips
        elif board[x][y] == '.':
            return 0
        else:
            flips += 1
        x += dx
        y += dy
    return 0


    
    
        


    #case 1 ox.
    #case 2 oxo
    #case 3 .xo
    #case 4 xxx

    
    return total

def edgeStability(brd, tkn, eTkn):
    # check vertical
    horizontals = [[0,1,2,3,4,5,6,7],[56,57,58,59,60,61,62,63]]
    verticals = [[0,8,16,24,32,40,48,56],[7,15,23,31,39,47,55,63]]
    hv = horizontals + verticals

    #case 1 ox.
    #case 2 oxo
    #case 3 .xo
    #case 4 xxx

    total = 0
    for h in hv:
        prev = 0
        c1 = False
        c2 = False
        c3 = False
        c4 = False
        sfCount = 0
        for i in h:
            if brd[i] == tkn:
                sfCount +=1
            if brd[i] == tkn and brd[prev] == eTkn:
                c1 = True
            if brd[i] == eTkn and c1:
                c2 = True
            if brd[i] == "." and c1 and not c2:
                #sfCount = 0
                return 0

            if brd[prev] == "." and brd[i] == tkn:
                c3 = True
            if brd[i] == "." and c3:
                c4 = True
            if brd[i] == eTkn and c3 and not c4:
                #sfCount = 0
                return 0 
            prev = i
        if sfCount > 1:
            total+=sfCount


    """for h in hv:
        for i in h:
            if brd[i] == tkn:
                totalTkns +=1
            if brd[i] == eTkn:
                totalEtkns += 1

    if totalTkns == 0: return 0
    if totalEtkns > 0 or totalTkns > 1:
        return total/totalTkns
    else: return 0"""
    return total



                



def TERMINALalphabeta(brd,tkn, alpha, beta, abCache):
    eTkn = "XO".replace(tkn,"")
    if "." not in brd: 
        return [brd.count(tkn)-brd.count(eTkn)]
    possibleMoves, flippedSections= findMoves(brd,tkn)

    if (brd, tkn,alpha,beta) in abCache:
        return abCache[(brd, tkn,alpha,beta)]

    if not possibleMoves:
        if not findMoves(brd,eTkn)[0]:
            return [brd.count(tkn)-brd.count(eTkn)]

        if (brd, eTkn,-beta,-alpha) not in abCache:
            abCache[(brd, eTkn,-beta,-alpha)] = TERMINALalphabeta(brd,eTkn,-beta,-alpha,abCache)
        ab = abCache[(brd, eTkn,-beta,-alpha)]

        if -ab[0] < alpha: return [alpha-1]
        return [-ab[0]] + ab[1:] + [-1]
    
    bestSoFar = [alpha-1]
    for mv in orderMoves(brd,tkn,possibleMoves,flippedSections):
        newBrd = makeMove(brd,tkn,mv,flippedSections)

        if (newBrd, eTkn,-beta,-alpha) not in abCache:
            abCache[(newBrd, eTkn,-beta,-alpha)] = TERMINALalphabeta(newBrd,eTkn,-beta,-alpha,abCache)
        ab = abCache[(newBrd, eTkn,-beta,-alpha)]
        score = -ab[0]
        if score < alpha: continue
        if score > beta: return[score]
        bestSoFar = [score] + ab[1:] + [mv]
        alpha = score + 1
    
    abCache[(brd, tkn,alpha,beta)] = bestSoFar
    return bestSoFar

global stabilityCache, groupCache, isStableCache,tokenToLanes
stabilityCache, groupCache, isStableCache = {}, {}, {}

def stability3(brd, tkn):
    eTkn = "XO".replace(tkn,"")
    total = 0
    visited = set()

    for i in tokenToLanes:
        if i not in visited and brd[i] == tkn:
            vt,hz = tokenToLanes[i]
            v = ''.join([brd[e] for e in vt])
            h = ''.join([brd[e] for e in hz])
            vCheck = False
            hCheck = False
            trimmedV = v.strip('.')
            #if trimmedV == v:
            if tkn not in trimmedV:
                pass
            elif '.' in trimmedV:
                pass
            elif eTkn in trimmedV:
                start = trimmedV.find(eTkn+tkn)
                end = trimmedV.find(tkn+eTkn)
                if (trimmedV == eTkn+tkn+eTkn or trimmedV == eTkn+tkn*2+eTkn or 
                    trimmedV == eTkn+tkn*3+eTkn or trimmedV == eTkn+tkn*4+eTkn or
                    trimmedV == eTkn+tkn*5+eTkn or trimmedV == eTkn+tkn*6+eTkn):
                    vCheck = True
                elif (v.find(tkn+eTkn) == 0 or v.find(tkn*2+eTkn) == 0 or v.find(tkn*3+eTkn) == 0 or
                      v.find(tkn*4+eTkn) == 0 or v.find(tkn*5+eTkn) == 0 or v.find(tkn*6+eTkn) == 0 or
                      v.find(tkn*7+eTkn) == 0):
                    vCheck = True
                
                else:
                    v = v[::-1]
                    if (v.find(tkn+eTkn) == 0 or v.find(tkn*2+eTkn) == 0 or v.find(tkn*3+eTkn) == 0 or
                      v.find(tkn*4+eTkn) == 0 or v.find(tkn*5+eTkn) == 0 or v.find(tkn*6+eTkn) == 0 or
                      v.find(tkn*7+eTkn) == 0):
                        vCheck = True
            else:
                vCheck = True

            trimmedH = h.strip('.')
            
            if tkn not in trimmedH:
                pass
            elif '.' in trimmedH:
                pass
            elif eTkn in trimmedH:
                start = trimmedH.find(eTkn+tkn)
                end = trimmedH.find(tkn+eTkn)
                if (trimmedH == eTkn+tkn+eTkn or trimmedH == eTkn+tkn*2+eTkn or 
                    trimmedH == eTkn+tkn*3+eTkn or trimmedH == eTkn+tkn*4+eTkn or
                    trimmedH == eTkn+tkn*5+eTkn or trimmedH == eTkn+tkn*6+eTkn):
                    hCheck = True
                elif (h.find(tkn+eTkn) == 0 or h.find(tkn*2+eTkn) == 0 or h.find(tkn*3+eTkn) == 0 or
                      h.find(tkn*4+eTkn) == 0 or h.find(tkn*5+eTkn) == 0 or h.find(tkn*6+eTkn) == 0 or
                      h.find(tkn*7+eTkn) == 0):
                    hCheck = True
                
                else:
                    h = h[::-1]
                    if (h.find(tkn+eTkn) == 0 or h.find(tkn*2+eTkn) == 0 or h.find(tkn*3+eTkn) == 0 or
                      h.find(tkn*4+eTkn) == 0 or h.find(tkn*5+eTkn) == 0 or h.find(tkn*6+eTkn) == 0 or
                      h.find(tkn*7+eTkn) == 0):
                        hCheck = True
            else:
                hCheck = True
            
            #if vCheck:
                #for i in vt:
                    #visited.add(i)
            #if hCheck:
                #for i in hz:
                    #visited.add(i)
            total += 0.5*(vCheck == True) + 0.5*(hCheck == True)
    return total

def stability(brd, tkn):
    if (brd, tkn) in stabilityCache:
        return stabilityCache[(brd, tkn)]

    stableDisks = []
    visited = set()
    for i,s in enumerate(brd):
        if s == tkn and i not in visited:
            group = connectedGroup(brd, tkn, i, set())
            if isStable(brd, group, tkn):
                stableDisks += group
                visited |= {*group}
    stabilityCache[(brd, tkn)] = stableDisks
    return stableDisks

def connectedGroup(brd, tkn, i,vs):
    if (brd, tkn, i) in groupCache:
        return groupCache[(brd, tkn, i)]
    vs.add(i)
    group = [i]
    for dx in [1,-1,8,-8]:
        x = i + dx
        if x in vs: continue
        elif ((x % 8 == 0 and dx in [1,9,-7]) or 
           (x % 8 == 8 - 1 and dx in [-1,7,-9])):
           continue
        elif 0<=x<64 and brd[x] == tkn:
           group+= connectedGroup(brd, tkn, x,vs)
    groupCache[(brd, tkn, i)] = group
    return group

def isStable(brd, group, tkn):
    #if (brd, group, tkn) in isStableCache:
        #return isStableCache[(brd, group, tkn)]
    #REMEMBER TO MAKE "ox" UPPERCASE
    eTkn = "XO".replace(tkn,"")
    for i in group:
        for dx in [1,-1,8,-8,9,-9,7,-7]:
            flag = False
        #for dx in [1,-1,8,-8]:#9,-9,7,-7]:
            x = i + dx
            if ((x % 8 == 0 and dx in [1,9,-7]) or 
           (x % 8 == 8 - 1 and dx in [-1,7,-9])):
                continue
            elif 0<=x<64 and brd[x] == eTkn:
                j = i
                while 0<=j<64:
                    if ((j % 8 == 0 and -dx in [1,9,-7]) or 
                    (j % 8 == 8 - 1 and -dx in [-1,7,-9])):
                        break
                    if brd[x] == eTkn and flag: break
                    if brd[j] == ".":
                        #isStableCache[(brd, group, tkn)] = False
                        return False
                    j += -dx
                    flag = True
    #isStableCache[(brd, group, tkn)] = True
    return True

def stableCount(brd,tkn,eTkn):
    count = 0
    seen = set()
    blackList = set()
    #ndots = brd.count(".")
    for i,e in enumerate(brd):
        if e == tkn and i not in seen:
            flag = False
            deltaLen = len(seen)
            temp = set()
            seen.add(i)
            temp.add(i)
            for dx in [1,-1,8,-8]:#,9,-9,7,-7]:
                if flag: break
                x = i + dx
                
                while 0<=x<64 and brd[x] != eTkn and brd[x] != ".":
                    if ((x % 8 == 0 and dx in [1,9,-7]) or 
                        (x % 8 == 8 - 1 and dx in [-1,7,-9])):
                        break
                    seen.add(x)
                    temp.add(x)
                    x+=dx
                    
                if 0<=x<64 and brd[x] == ".":
                    j = x
                    while 0<=j<64:
                        if ((j % 8 == 0 and -dx in [1,9,-7]) or 
                        (j % 8 == 8 - 1 and -dx in [-1,7,-9])):
                            break
                        if brd[j] == eTkn:
                            #isStableCache[(brd, group, tkn)] = False
                            flag = True
                            seen = seen - temp
                            blackList.add(i)
                            break
                        j += -dx
                elif 0<=x<64 and brd[x] == eTkn:
                    f2 = False
                    j = i
                    while 0<=j<64:
                        if ((j % 8 == 0 and -dx in [1,9,-7]) or 
                        (j % 8 == 8 - 1 and -dx in [-1,7,-9])) and f2:
                            break
                        if brd[j] == eTkn and f2: break
                        if brd[j] == ".":
                            #isStableCache[(brd, group, tkn)] = False
                            flag = True
                            seen = seen - temp
                            blackList.add(i)
                            break
                        f2 = True
                        j += -dx
            
            if not flag:
                seen = seen - blackList
                deltaLen = len(seen) - deltaLen
                count+=deltaLen
    return count

global nbrs 
nbrs = []
for i in range(64):
    s = set()
    if (i+1)%8 != 0 and i+1 < 64:
        s.add(i+1)
    if i%8 != 0 and i-1 >= 0:
        s.add(i-1)
    if i+8 < 64:
        s.add(i+8)
    if i-8 >= 0:
        s.add(i-8)
    nbrs.append(s)

def pM(brd,eTkn):
    edges = {0,1,2,3,4,5,6,7,56,57,58,59,60,61,62,63,8,16,24,32,40,48,15,23,31,39,47,55}
    count = 0
    tCount = 0
    seen = set()

    for i,n in enumerate(nbrs):
        tFlag = False
        if brd[i] == eTkn and i not in edges:
            for j in n:
                if brd[j] == "." and j not in seen:    
                    count +=1
                    if not tFlag:
                        tCount +=1
                        tFlag = True
                seen.add(j)
    #if tCount > 0:
        #return count/tCount
    return count




#global pmCache 
#pmCache = {}
def potentialMobility(board, eTkn):
    #tkn = "XO".replace(eTkn,"")
    edges = {0,1,2,3,4,5,6,7,56,57,58,59,60,61,62,63,8,16,24,32,40,48,15,23,31,39,47,55}
    #if (board, eTkn) in pmCache:
        #return pmCache[(board,eTkn)]
    directions = [1,-1,8,-8]#,9,-9,7,-7]
    count = 0
    c2 = 0
    if board.count(".") < 32:
        for i in range(64):
            if board[i] == "." and i not in edges:
                for e in directions:
                    if 0<= i + e < 64 and board[i+e] == eTkn:
                        if (((i + e) % 8 == 0 and e in [1,9,-7]) or 
                        ((i + e) % 8 == 8 - 1 and e in [-1,7,-9])):
                            continue
                        else:
                            if e in {1,-1,8,-8}:
                                count += 2
                            else:
                                count+=1
                            break
        #pmCache[(board,eTkn)] = count
        return count
    else:
        for i in range(64):
            if board[i] == eTkn and i not in edges:
                c2=0
                flag = False
                for e in directions:
                    if 0<= i + e < 64 and board[i+e] == ".":
                        if (((i + e) % 8 == 0 and e in [1,9,-7]) or 
                        ((i + e) % 8 == 8 - 1 and e in [-1,7,-9])):
                            continue
                        else:
                            count += 2
                            flag = True
                            c2=0
                            break
                    """if 0<= i + e < 64 and not flag and board[i+e] == tkn:
                        if (((i + e) % 8 == 0 and e in [1,9,-7]) or 
                        ((i + e) % 8 == 8 - 1 and e in [-1,7,-9])):
                            continue
                        else:
                            c2+=1"""
                count+=c2


        #count = count/board.count(eTkn)
        #pmCache[(board,eTkn)] = count
        return count

def isStableEdge(brd,tkn, eTkn, edge):
    edgeString = [brd[i] for i in edge]
    if tkn in edgeString and eTkn in edgeString: return False, 0
    if tkn not in edgeString: return False, 0
    return True, edgeString.count(tkn)

def checkStability(brd, tkn, eTkn):
    h1, h2 =   [1,2,3,4,5,6],[57,58,59,60,61,62]  
    v1, v2 =   [8,16,24,32,40,48],[15,23,31,39,47,55]
    edges = []
    edges.append(h1)
    edges.append(h2)
    edges.append(v1)
    edges.append(v2)
    total = 0
    for edge in edges:
        isStable, count = isStableEdge(brd,tkn,eTkn, edge)
        if isStable:
            if edge == h1:
                _, c2 = isStableEdge(brd, tkn, eTkn, [i+8 for i in edge])
                total += count + c2
            elif edge == h2:
                _, c2 = isStableEdge(brd, tkn, eTkn, [i-8 for i in edge])
                total += count + c2
            elif edge == v1:
                _, c2 = isStableEdge(brd, tkn, eTkn, [i+1 for i in edge])
                total += count + c2
            elif edge == v2:
                _, c2 = isStableEdge(brd, tkn, eTkn, [i-1 for i in edge])
                total += count + c2
    return total
            









def turn(b):
   cnt = 0
   for x in b:
        if(x == "."):
            cnt = cnt + 1
   if(cnt % 2 != 0):
        return "O"
   else:
        return "X"

def printBoard(b,possibleChoices, mv = None):
    s=b
    if possibleChoices:
        for i in possibleChoices:
            s = s[:i] + "*" + s[i+1:]
    s = s.lower()
    if mv:
        s = s[:mv] + s[mv].upper() + s[mv+1:]
        
    print("\n".join([s[x : x + side] for x in range(0,length,side)]))

def findMoves(b,token):
    b = b.upper()
    token = token.upper()
    index = 0
    choiceSet = set()
    #global flippedSection 
    flippedSection = []
    directions = [1,-1,8,-8,9,-9,7,-7]
    opT = {"X","O"} - {token.upper()}
    opT = "".join(opT)
    if (b, token) in moveCache:
        return moveCache[(b, token)]
    for i,s in enumerate(b):
        if s == ".":
    #for i in dotSet:
            for x in directions:
                index = i
                flag = False
                while 0<= index < length:
                    if ((index % side == 0 and x in [-1,-9,7]) or
                        (index % side == side - 1 and x in [1,-7,9] )):
                        break
                    if 0<= index < length and b[index] == token: break
                    if 0<= index < length and flag and b[index] == ".": break
                    flag = True
                    index += x
                if 0 <= index < 64 and b[index] == token and b[index - x] != ".":

                    flippedSection.append((index,i,-x))
                    choiceSet.add(i)
    moveCache[(b, token)] = (choiceSet,flippedSection)
    


    return choiceSet,flippedSection
global makeMoveCache
makeMoveCache = {}
def makeMove(b, token, move, flippedSection):
    #dotSet.remove(move)
    if (b,token,move) in makeMoveCache: return makeMoveCache[(b,token,move)]
    b=b.upper()
    token = token.upper()
    seenDirection = set()
    start = 0
    for sect in flippedSection:#[move]:
        firstOccurance = False
        if move == sect[1] and sect[2] not in seenDirection:
            start, end, direction = sect
            while end != start:
                if b[end] != token:
                    if b[end] != ".":
                        firstOccurance = True
                    b = b[:end] + token + b[end+1:]
                    
                elif firstOccurance: 
                    break
                end -= direction
            seenDirection.add(direction)        
    makeMoveCache[(b,token,move)] = b
    return b

def quickMove(board, token, t = 0,tl = 1):
#set globals
    global abCache
    global ws
    #flag = True
    #if tl!= 1 and board in theoryDct:
        #return theoryDct[board]
    global hl
    #if tl == 1: hl = 7
    #elif tl == 2: hl = 12
    #elif tl == 4: hl = 12
    #elif tl == 5: hl = 14
    if tl < 5:
        hl = 14
    elif tl <= 3:
        hl = 12
    else:
        hl = 13
    
    #if tl > 7:
        #hl = 15
    if tl > 15 and len(findMoves(board,token)[0]) < 8:
        hl = 15
    if tl > 25 and len(findMoves(board,token)[0]) < 8:
        hl = 16

    dots = board.count(".")
    if tl == 1 and dots > hl:
        i=4
        #if len(findMoves(board,token)[0]) > 6:
        #    i = 2
        ab,w = alphabeta(board.upper(), token.upper(), -10000000, 10000000, abCache,i,t)
        ws = w
        #print("('" + board + "'" + "," + "'" + token + "'" + ")" + ":" + str(ab[0]) +",") 
        return ab[-1]
    board = board.upper()
    token = token.upper()
    if 0 < dots <hl:
        if len(findMoves(board,token)[0]) > 5 and hl >= 13 and tl < 5:
            hl -= 1
        else:
            return TERMINALalphabeta(board, token, -65, 65, abCache)[-1]

    if dots < 50 and tl < 3: n =4
    else: n = 5

    while time.time()-t < tl:
        abCache = {}
        ab,w = alphabeta(board, token, -10000000, 10000000, abCache,n,t)
        ws = w
        n+=1
    print(ab)
    print(f"n = {n}")
    return ab[-1]


def orderMoves(board, token, possibleChoices,fs,tl = 100, n = 10):
    #if (board, token) in orderCache:
        #return orderCache[(board, token)]
    table_weights = [20, -3, -1, -1, -1, -1, -3, 20,     
                    -3, -7, -4, -2, -2, -4, -7, -3,     
                    -1, -4, -1, 2, 2, -1, -4, -1,     
                    -1, -2, 2, 2, 2, 2, -2, -1,    
                    -1, -2, 2, 2, 2, 2, -2, -1,     
                    -1, -4, -1, 2, 2, -1, -4, -1,     
                    -3, -7, -4, -2, -2, -4, -7, -3,     
                    20, -3, -1, -1, -1, -1, -3, 20]
    cornerToEdges = {0: {1,2,3,4,5,6,7,8,16,24,32,40,48,56},
             7: {0,1,2,3,4,5,6,15,23,31,39,47,55,63},
             56: {0,8,16,24,32,40,48,57,58,59,60,61,62,63},
             63: {7,15,23,31,39,47,55,56,57,58,59,60,61,62}}
    edgeToCorner = {edgeInd: corner for corner in cornerToEdges for edgeInd in cornerToEdges[corner]}
    corners = {0, 7, 56, 63}
    aroundCorner = {1: 0, 8: 0, 9: 0, 6: 7, 14: 7, 15: 7, 48: 56, 49: 56, 57: 56, 54: 63, 55: 63, 62: 63}
    edges = [0,1,2,3,4,5,6,7,56,57,58,59,60,61,62,63,8,16,24,32,40,48,15,23,31,39,47,55]
    #horizontals = [[0,1,2,3,4,5,6,7],[56,57,58,59,60,61,62,63]]
    h1, h2 =   [1,2,3,4,5,6],[57,58,59,60,61,62]  
    v1, v2 =   [8,16,24,32,40,48],[15,23,31,39,47,55]
    #verticals = [[0,8,16,24,32,40,48,56],[7,15,23,31,39,47,55,63]]
    dc = board.count(".")
    tct = board.count(token)


    
    opT = {"O","X"} - {token}
    opT = "".join(opT)
    sortedMoves = []
    tct = board.count(token)
    ect = board.count(opT)

    for move in possibleChoices:
        safeEdgeFlag = False
        score = 0
        score+= table_weights[move]
        if move in corners:
            score += 70

        elif move in edgeToCorner:
            if board[edgeToCorner[move]] == token:
                score += 0
        #elif move in edges and tct <= ect:
            #score +=10 
        """if move in edges and tl == 1 and dc < 37:
                if move in h1:
                    a = [board[i] for i in h1]
                    if opT not in a and token in a:
                        score += 2
                    #if dc < 37:
                        safeEdgeFlag = True
                    #else: score-=2
                elif move in h2:
                    a = [board[i] for i in h2]
                    if opT not in a and token in a: 
                        score += 2
                    #if dc < 37:
                        safeEdgeFlag = True
                    #else: score-=2
                elif move in v1:
                    a = [board[i] for i in v1]
                    if opT not in a and token in a: 
                        score += 2
                    #if dc < 37:
                        safeEdgeFlag = True
                    #else: score-=2
                elif move in v2:
                    a = [board[i] for i in v2]
                    if opT not in a and token in a: 
                        score += 2
                    #if dc < 37:
                        safeEdgeFlag = True
                    #else: score-=2"""
        #if move in edges and tl != 1:
            #score -= 2
        #else:
        if move not in edges:
            for n in [1,-1,8,-8]:#,9,-9,7,-7]:
                if move+n >= 0 and move+n < length and board[move+n] == '.': 
                    if dc < 37: score -= 9
                    else: score -= 19
                else: score += 2
        if move in aroundCorner:
            if board[aroundCorner[move]] == '.':
                score = -70
            elif board[aroundCorner[move]] == opT:
                score = -69
        #mobility
        """newB = makeMove(board,token,move,fs)

        eChoices,_ = findMoves(newB,opT)
        choices,_ = findMoves(newB,token)
        if eChoices or choices:
            score += 4*(len(choices) - len(eChoices)) / (len(choices) + len(eChoices))"""
        sortedMoves.append((score, move))

    
        
    
    sortedMoves.sort(reverse=True)
    moves = [t[1] for t in sortedMoves]
    
    """if tl < 2:
        #if n <= 1 and len(moves) >= 4:
           #moves =  [moves[i] for i in range(4)]
        if len(moves) >= 8:
            moves = [moves[i] for i in range(7)]
        elif len(moves) >= 4:
            moves = [moves[i] for i in range(4)]
    #elif len(moves) >= 10:
        #moves = [moves[i] for i in range(len(moves))]"""

    #orderCache[(board, token)] = moves
    return moves

def calcScore(b):
    x = b.count("X")
    y = b.count("O")
    return f"  {x}/{y}"       
            
def condensePath(nums):
    nums = nums.replace("_", "0")
    #if not nums.isnumeric():
        #return
    for i in range(0,len(nums),2):
        if nums[i] != "-" and nums[i+1] != "-":
            moves.append(int(nums[i] + nums[i+1]))
        


#def setGlobals(s):
s = args
global side, length, board, defaultToken, moves, opToken, nmCache,verbose,abCache, status, moveCache, hl
global dotSet, orderCache, evaluateCache, theoryDct, score, evaluateCache2
score = 0
tokenToLanes = {}


#theoryDct = {} #COMMENT OUT BEFORE FINAL SUBMISSION
evaluateCache2 = {}

evaluateCache = evaluateCache2
orderCache = {}
verbose = False
dotSet = {}
moveCache = {}
#status = {"moveCache":0}
abCache = {}
nmCache = {}
hl= 13
board = ""
defaultToken = "."
moves = []
for e in s:
    if e.upper() == "V":
        verbose = True
        continue
    if "HL" in e:
        hl = int(e[2:])
    if "." in e or (('X' in e.upper() or 'O' in e.upper()) and len(e) > 3):
        board = e.upper()
    elif e.upper() in ["X","O"]:    
        defaultToken = e.upper()
    elif len(e) <= 2 and e.isnumeric():
        moves.append(int(e))
    else:
        condensePath(e)

    
tokens = {"X", "O"}

if board == "":
    board = ('.'*27 + "ox......xo" + '.'*27).upper()
if defaultToken == ".":
    defaultToken = turn(board)

opToken = tokens - {defaultToken}
opToken = "".join(opToken)
length = 64
side = int(length**0.5)


for i in range(64):
    verts =[j for j in range(i%8,64,8)]
    start = i-(i%8)
    end = start + 8
    hrz = [j for j in range(start,end)]
    tokenToLanes[i]=(verts,hrz)
    

if __name__ == "__main__": main()


            # Note: It is not required for your Strategy class to have a "legal_moves" method,
            # but you must determine legal moves yourself. The server will NOT accept invalid moves.




# Dev Kodre, Pd. 4, 2024