import pytest 
from string_utils import StringUtils

utils = StringUtils()
'capitilize'
def test_capitilize():
    "Positive"
    assert utils.capitilize("hello") == "Hello"
    assert utils.capitilize("hi friend") == "Hi friend"
    assert utils.capitilize("123456") == "123456"
    "Negative"
    assert utils.capitilize("___") == "___"
    assert utils.capitilize("155156165jjj") == "155156165jjj"
    assert utils.capitilize(" ") == " "

'trim'
def test_trim():
    "Positive"
    assert utils.trim("   hello") == "hello"
    assert utils.trim("   hi friend   ") == "hi friend   "
    "Negative"
    assert utils.trim("") == ""

@pytest.mark.xfail()
def test_trim_with_numbers_input():
    assert utils.trim(123456) == "123456"

@pytest.mark.xfail()
def test_trim_with_spaces_output():
    assert utils.trim(   "hello"   ) == "   hello   "

'to_list'
@pytest.mark.parametrize('string, delimeter, result', [
    #positive
    ("дом, подъезд, этаж", ",", ["дом", "подъезд", "этаж"]),
    ("/$#%_", "/", ["/","$","%","_"]),
    #negative
    ("None", "",[]),
    ("9,8,7 6", None, ["9","8","7 6"]),
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string,delimeter)
    assert res == result

'contains'
@pytest.mark.parametrize('string, symbol, result', [
    ("школа", "ш", True),
    ('стол', 'л', True),
    ('игра', 'и', True),
    ('кошка', 'д', False),
    ('диван', 'к', False),
    ('456', 'а', False),
])
def test_contains(string, symbol, result):
    res = utils.contains(string.symbol)
    assert res == result

'delete_symbol'
@pytest.mark.parametrize('string, symbol, result', [
    ('школа', 'ш', 'кола'),
    ('стол', 'л', 'сто'),
    ('игра', 'и', 'гра'),
    ('кошка', 'а', 'кошк'),
    ('новый диван', 'а', 'новый дивн'),
    ('456', '5', '46'),
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result 

'starts_with'
@pytest.mark.parametrize('string, symbol, result', [
    ('школа','ш', True),
    ('456','4', True),
    ('Hello', 'H', True)

    ('Волга', 'в', False),
    ('кошка', 'К', False),
    ('','/', False),
    ('hello', 'l', False)
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result 


'end_with'
@pytest.mark.parametrize('string, symbol, result', [
    ("школа", "а", True),
    ('стол', 'л', True),
    ('игра', 'а', True),
    ('кошка', 'ж', False),
    ('диван', 'к', False),
    ('456', '4', False),   
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result 

'is_empty'
@pytest.mark.parametrize('string, result', [
    ('', True),
    ('стол', False)
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result 

'list_to_string'
@pytest.mark.parametrize('lst, joiner, result', [
    (['h','i'], '', 'hi')
    ([1,2,3],None, '1,2,3')
    (['dream', 'team'], '-', 'dream-team')
    ([], None, '')
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
         res = utils.list_to_string(lst)
    else:
         res = utils.list_to_string(lst, joiner)
    assert res == result 