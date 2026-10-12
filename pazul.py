#        1         2         3         4         5         6         7         8         9        10         1         2
#23456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
# ある数値が、10進数と8進数および2進数で上から半分までと下から順に半分までが同じ数値となる
# 10以上の最小値を求める
# 2026.10.05 S.TAKAHARA
#################################################################################
from ex02ReversePolishNotation import ex02ReversePolishNotation
from ex03FlipTheCardOver import ex03FlipTheCardOver
from ex04CuttingTheRodIntoPieces import ex04CuttingTheRodIntoPieces

def checkKaizyunn( strCheckString:str ) :                                       #
  boolFlag=True                                                                 #
  for j in range( 0, int(len(strCheckString) / 2) ):                            #
#    print(f"strCheckString[{j}]= {strCheckString[j]}  strCheckString[{len(strCheckString)-j-1}] {strNum[(len(strNum)-j-1)]}")
    if strCheckString[j] != strCheckString[(len(strCheckString)-j-1)] :         #
      boolFlag = False                                                          #
      break
#    print(f"strCheckString[{j}]= {strCheckString[j]}  strCheckString[{len(strCheckString)-j-1}] {strCheckString[(len(strCheckString)-j-1)]}  boolFlag {boolFlag}")
  return(boolFlag)

def kaizyun_01() :
  for i in range(10,30001):
    strNum=str(i)
    strOct = f"{i:o}" 
    strBin = f"{i:b}"
    #print(f" 10進数 {strNum} len{len(strNum)} 8進数 {strOct} len({len(strOct)})  2進数 {strBin} len({len(strBin)})")
    if  checkKaizyunn( strNum) == False :
      continue
    #print(f" OK 10進数 {strNum} len{len(strNum)}  8進数 {strOct}")
    if checkKaizyunn( strOct)  == False :
      continue
    print(f" OK 8進数 {strOct} len({len(strOct)})  2進数 {strBin}")
    if checkKaizyunn( strBin)   == False :
      continue
    #print(f" OK 2進数 {strBin} len({len(strBin)})")
    print(f"strNum = {strNum} strOct = {strOct} strBin = {strBin}")
  print(f"i={i}")


#########################################
# main                                  #
#########################################
#kaizyun_01()
#reversePolishNotation_02()
#transeReversePolishNotaion( "1234")

#ex02ReversePolishNotation()
#ex03FlipTheCardOver()
ex04CuttingTheRodIntoPieces()
#exit(0)
##### End of File #####
