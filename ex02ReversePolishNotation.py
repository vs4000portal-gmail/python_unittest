#        1         2         3         4         5         6         7         8         9        10         1         2
#23456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
# ある数値が、10進数と8進数および2進数で上から半分までと下から順に半分までが同じ数値となる
# 10以上の最小値を求める
# 2026.10.05 S.TAKAHARA
#################################################################################
#################################################################################
# 数字文字列の間に演算子を入れて演算式の文字列リストを作成するだけ              #
# 引数 演算子文字列                                                             #
#      数値文字列                                                               #
# 戻り値 演算子の文字列リスト                                                   #
# 注意 エラー処理していない。                                                   #
#      例えば、演算子[*/+- ]以外の場合エラーにするとか、数値判定とか            #
#      文字数チェックとか。今は、演算子文字列が固定で3個としている              #
#################################################################################
def ex02TranseArithmeticExpression( strOperator:str, strNumber:str )-> list :
  listOriginalMathematicalExpression = []                                       # 結果格納用リストの初期化
  intPreviousValue = 0                                                          # 前回数値の保存(桁が増えるのでその文増やして保存)
  intNumberIndex = 0                                                            # ループ処理時の数値文字列の参照位置
  for intLoop in range(0,3):                                                    # 演算子分ループする
    if strOperator[ intLoop ] == " " :                                          # スペースの場合は、左が１０桁目となる
      intPreviousValue = ( intPreviousValue * 10 ) \
       + int( strNumber[ intNumberIndex ] ) * 10                                # 数値として保存する
    else :                                                                      # スペース以外の演算子の場合
      listOriginalMathematicalExpression.append( str(intPreviousValue + int( strNumber[ intNumberIndex ] ) ) )
      listOriginalMathematicalExpression.append( strOperator[ intLoop ] )       # 結果リストに数値、演算子を追加
      intPreviousValue = 0                                                      # 前回値をクリアする
    intNumberIndex += 1                                                         # 数値をインクリメント。。文字と同じでは
  listOriginalMathematicalExpression.append( str( intPreviousValue + int( strNumber[ intNumberIndex ] ) ) ) # 最後のけたを数式に追加
  return(listOriginalMathematicalExpression)

#################################################################################
# 算術式から逆ポーランド表記のリストを取得する                                  #
# 引数 算術式文字列                                                             #
# 戻り値 逆ポーランド表記の文字列リスト                                         #
# 注意 エラー処理していない。                                                   #
#      この処理では'(',')'は処理対象外                                          #
#################################################################################
def ex02TranseReversePolishNotaion( listNumber : list)->list :
  listReversePolishNotation = []                                                # 逆ポーランド表記のリスト
  listStack = []                                                                # 演算子のスタック領域
  intListNumberLen = len(listNumber)                                            # 文字数
  intLoop = 0                                                                   # for文でも良かったけど数値取り出しなどあるので
  while intLoop < intListNumberLen :                                            # リスト分ループ
 ##   print(f"intLoop = {intLoop} intListNumberLen = {intListNumberLen} listNumber[ {intLoop} ] = {listNumber[ intLoop ]}")
    if listNumber[ intLoop ] == "*" or listNumber[ intLoop ] == "/" :           # 割り算と掛け算の演算子処理
 ##     print("listNumber[ intLoop ]")
      listReversePolishNotation.append(listNumber[ intLoop + 1])                # 数値をリストに追加
      listReversePolishNotation.append(listNumber[ intLoop ])                   # 演算子(*,/)をリストに追加
      intLoop += 1                                                              # 数値分ループ変数に１を加える
    elif listNumber[ intLoop ] == "+" or listNumber[ intLoop ] == "-" :         # 足し算と引き算の演算子処理
 ##     print("listNumber[ intLoop ]")
      listStack.append(listNumber[ intLoop ])                                   # 演算子をスタックに追加する
    else :                                                                      # その他（数値の）処理
      listReversePolishNotation.append(listNumber[ intLoop ])                   # リストに追加
    intLoop += 1                                                                # for文じゃなかった。インクリメント
  while len(listStack) > 0 :                                                    # スタックされた演算子の処理
    listReversePolishNotation.append( listStack.pop() )                         # リストに追加する
  return( listReversePolishNotation )                                           # リストを戻り地として返す

#################################################################################
# 逆ポーランド表記のリストを計算する                                            #
# 引数 逆ポーランド表記の文字列リスト                                           #
# 戻り値 逆ポーランド表記の計算結果(文字列)                                     #
# 注意 エラー処理していない。                                                   #
#################################################################################
def ex02Excution( listReversePolishNotation : list)->str :
  listNumberStack = []                                                          # 数値をスタックに保存
  intLen = len(listReversePolishNotation)                                       # 引数のリスト要素数
  if intLen <= 1 : return("0")                                                  # だって演算しないんだモーン
##  print(f"intLen = {intLen} listData = {listReversePolishNotation[0]}")
  for i in range(0, len(listReversePolishNotation)  ):                          # 引数のリスト要素数分ループ
    strCheckData = listReversePolishNotation[ i ]                               # リストから要素を取り出す
    if strCheckData == '*' :                                                    # '*'の場合の処理
      intGetRightData = int(listNumberStack.pop())                              # スタックから右辺のデータを取り出す
      intGetLeftData = int(listNumberStack.pop())                               # スタックから左辺のデータを取り出す
      strExec = str(int(intGetLeftData * intGetRightData))                      # 乗算を行う
      listNumberStack.append(strExec)                                           # スタックに値を追加する
    elif strCheckData == '+' :                                                  # '+'の場合の処理
      intGetRightData = int(listNumberStack.pop())                              # スタックから右辺のデータを取り出す
      intGetLeftData = int(listNumberStack.pop())                               # スタックから左辺のデータを取り出す
      strExec = str(int(intGetLeftData + intGetRightData))                      # 加算を行う
      listNumberStack.append(strExec)                                           # スタックに値を追加する
    elif strCheckData == '-' :                                                  # '-'の場合の処理
      intGetRightData = int(listNumberStack.pop())                              # スタックから右辺のデータを取り出す
      intGetLeftData = int(listNumberStack.pop())                               # スタックから左辺のデータを取り出す
      strExec = str(int(intGetLeftData - intGetRightData))                      # 引き算を行う
      listNumberStack.append(strExec)                                           # スタックに追加
    elif strCheckData == '/' :                                                  # '/'の場合の処理
      intGetRightData = int(listNumberStack.pop())                              # スタックから右辺のデータを取り出す
      intGetLeftData = int(listNumberStack.pop())                               # スタックから左辺のデータを取り出す
      if intGetRightData == 0 :                                                 # 右辺が'0'の場合の処理
#        print("0 Div ERROR")
        return("0")                                                             # '0'を返す
      strExec = str(int(intGetLeftData / intGetRightData))                      # 割り算を行う(整数となるので切り捨て)
      listNumberStack.append(strExec)                                           # スタックに追加
    else :                                                                      # その他（数値の）処理
      listNumberStack.append(strCheckData)                                      # スタックに追加

  return( str(listNumberStack.pop()))                                           # 値を返す

def ex02StringReverse(intNumber : str, listOriginalMathematicalExpression : list, strOperateResult : str)-> int :
  intCompNumber=0
  if len(strOperateResult) == 0 :
    print("文字数が0桁なのでerror")
    exit(0)

  if int(strOperateResult) > 0 :
    for intLoop in range(0,len(strOperateResult)) :
      intCompNumber = (intCompNumber * 10 ) + int(strOperateResult[len(strOperateResult) - intLoop - 1] )
  intOperateResult = int(strOperateResult)

  if intNumber == intCompNumber :
    print("★☆ヽ(´ー｀)ノ☆★    intNumber == intOperateResult")
    print(f" もとの数値変換後の数値が等しい intNumber({intNumber}) == intCompNumber({intCompNumber}) strNumber = {str(intNumber)}")
    return(0)
  return(1)

def ex02ReversePolishNotation() :
  # 4桁の数値の間に +,-,*,/の演算子と数値の左側をx10して足し合わせる演算子を入れて計算した結果が
  # 元の値をひっくり返した値となる数値を求める。
  # 
  strOperator="+-*/ "
  print("reversePolishNotation_02")
  for operator1 in range(0,5):
    for operator2 in range(0,5):
      for operator3 in range(0,5):
        for intNumber in range(1000,9999+1):
          listOriginalMathematicalExpression = []  # 初期化
          strNumber = str( intNumber )
          strOperate=strOperator[ operator1 ] + strOperator[ operator2 ]  + strOperator[ operator3 ] 
          listOriginalMathematicalExpression = ex02TranseArithmeticExpression( strOperate, strNumber )
          listData = ex02TranseReversePolishNotaion( listOriginalMathematicalExpression )
          strOperateResult = ex02Excution( listData )
          intCheckResult = ex02StringReverse(intNumber, listOriginalMathematicalExpression, strOperateResult)
          if intCheckResult == 0 :
            print(f"strNumber = {strNumber} listOriginalMathematicalExpression = ", end="")
            for i in range(0, len(listOriginalMathematicalExpression)  ):
              print(listOriginalMathematicalExpression[i], end="")
            print(f" strOperateResult = {strOperateResult}")
