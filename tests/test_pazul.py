import unittest
from ex02ReversePolishNotation import ex02TranseArithmeticExpression
from ex02ReversePolishNotation import ex02TranseReversePolishNotaion
from ex02ReversePolishNotation import ex02Excution
from ex02ReversePolishNotation import ex02StringReverse
#from ex04CuttingTheRodIntoPieces import ex04setMan
from ex04CuttingTheRodIntoPieces import ex04setMan,ex04cutRod,ex04CheckWorkCompleted
#from ex04CuttingTheRodIntoPieces import ex04CheckWorkCompleted

class TestTranseArithmeticExpressionFunction( unittest.TestCase ):
  def test_allPlus(self):
    strOperator="+++"
    strNumber="1234"
    result = ex02TranseArithmeticExpression( strOperator, strNumber )
    self.assertListEqual(result, ['1','+','2','+','3','+','4'])

  def test_etcOperater(self):
    result = ex02TranseArithmeticExpression( "*-/", "1342" )
    self.assertListEqual(result, ['1','*','3','-','4','/','2'])

  def test_firstSpace(self):
    result = ex02TranseArithmeticExpression( " ++", "3210" )
    self.assertListEqual(result, ['32','+','1','+','0'])

  def test_middleSpace(self):
    result = ex02TranseArithmeticExpression( "+ +", "3210" )
    self.assertListEqual(result, ['3','+','21','+','0'])

  def test_lastSpace(self):
    result = ex02TranseArithmeticExpression( "++ ", "3210" )
    self.assertListEqual(result, ['3','+','2','+','10'])

  def test_allSpace(self):
    result = ex02TranseArithmeticExpression( "   ", "3210" )
    self.assertListEqual(result, ['3210'])

# 算術式の変換が正しく行われているか
class TestTranseReversePolishNotaionFunction( unittest.TestCase ):

  def test_allPlus(self):
    listNumber=['1','+','2','+','3','+','4']
    result = ex02TranseReversePolishNotaion( listNumber )
    self.assertListEqual(result, ['1','2','3','4','+','+','+'])

  def test_etcOperater(self):
    listNumber=['1','*','3','-','4','/','2']
    result = ex02TranseReversePolishNotaion( listNumber )
    self.assertListEqual(result, ['1','3','*','4','2','/','-'])

  def test_allSpace(self):
    listNumber=['1234']
    result = ex02TranseReversePolishNotaion( listNumber )
    self.assertListEqual(result, ['1234'])

# 逆ポーランド表記の計算
class TestExcutionFunction( unittest.TestCase ):

  def test_allPlus(self):
    listData= ['1','2','3','4','+','+','+']
    result = ex02Excution( listData )
    self.assertEqual(result, '10')

  def test_etcOperater(self):
    listData=  ['2','3','*','4','2','/','-']
    result = ex02Excution( listData )
    self.assertEqual(result, '4')

  def test_2spaceOperater(self):
    listData=  ['999','8','*']
    result = ex02Excution( listData )
    self.assertEqual(result, '7992')

  def test_allSpace(self):
    listData=  ['1234']
    result = ex02Excution( listData )
    self.assertEqual(result, '0')

# 算術式の変換が正しく行われているか
class TestTranseReversePolishNotaionFunction( unittest.TestCase ):

  def test_allPlus(self):
    intNumber = 1234
    listData= ['1','2','3','4','+','+','+']
    strOperateResult = "4321"
    result = ex02StringReverse( intNumber, listData, strOperateResult )
    self.assertEqual(result, 0)

# 算術式の変換が正しく行われているか
class Testex04CuttingTheRodIntoPiecesFunction( unittest.TestCase ):
  def test_setOneManOneRod(self):
    """初期処理木1個で作業員3人の割り振り"""
    listRod = [8]
    intM = 3
    listMan= [0]
    result = ex04setMan( listRod, intM )
    self.assertListEqual(result, listMan)

  def test_setMan1(self):
    """木4個で作業員3人の割り振り"""
    listRod = [2,2,2,2]
    intM = 3
    listMan= [0,1,2]
    result = ex04setMan( listRod, intM )
    self.assertListEqual(result, listMan)

  def test_setMan2(self):
    """木4個で3個1[cm]とする作業員3人の割り振り"""
    listRod = [1,2,1,1]
    intM = 3
    listMan= [1]
    result = ex04setMan( listRod, intM )
    self.assertListEqual(result, listMan)

  def test_cutRod(self):
    """木1個で作業員1人で木を切る"""
    listRod = [8]
    listMan= [0]
    listAfterRod = [4,4]
    result = ex04cutRod( listRod, listMan)
    self.assertListEqual(result, listAfterRod)

  def test_cutRod1(self):
    """木4個で作業員3人で木を切る"""
    listRod = [1,2,1,1]
    listMan= [1]
    listAfterRod = [1,1,1,1,1]
    result = ex04cutRod( listRod, listMan)
    self.assertListEqual(result, listAfterRod)

  def test_cutRod2(self):
    """木4個を作業員3人で木を切る"""
    listRod = [3,2,3,2]
    listMan= [0,1,2]
    listAfterRod = [1,1,1,2,2,1,2]
    result = ex04cutRod( listRod, listMan)
    self.assertListEqual(result, listAfterRod)

  def test_CheckWorkCompleted_false1(self):
    """木1個が1[cm]より長いので1(偽)"""
    listRod = [8]
    intCheck = 1
    result = ex04CheckWorkCompleted( listRod )
    self.assertEqual( result, intCheck)

  def test_CheckWorkCompleted_false2(self):
    """木8個中最後が1[cm]より長いので1(偽)"""
    listRod = [1,1,1,1,1,1,1,2]
    intCheck = 1
    result = ex04CheckWorkCompleted( listRod )
    self.assertEqual( result, intCheck)

  def test_CheckWorkCompleted_OK(self):
    """木8個が全て1[cm]なので0(真)"""
    listRod = [1,1,1,1,1,1,1,1]
    intCheck = 0
    result = ex04CheckWorkCompleted( listRod )
    self.assertEqual( result, intCheck)

if __name__ == '__main__':
    unittest.main()
