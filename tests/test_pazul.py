import unittest
from ex02ReversePolishNotation import ex02TranseArithmeticExpression
from ex02ReversePolishNotation import ex02TranseReversePolishNotaion
from ex02ReversePolishNotation import ex02Excution
from ex02ReversePolishNotation import ex02StringReverse

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
    self.assertEqual(result, '1234')

# 算術式の変換が正しく行われているか
class TestTranseReversePolishNotaionFunction( unittest.TestCase ):

  def test_allPlus(self):
    intNumber = 1234
    listData= ['1','2','3','4','+','+','+']
    strOperateResult = "4321"
    result = ex02StringReverse( intNumber, listData, strOperateResult )
    self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
