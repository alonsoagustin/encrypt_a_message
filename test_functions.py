from functions import encrypt

def test_encrypt():
    assert encrypt("Hola mundo", 2) == "JQNCBÑWOFQ"
    assert encrypt("ZigZag", 2) == "AKIACI"
    assert encrypt("AKIACI", -2) == "ZIGZAG"
    assert encrypt("ZigZag", 3) == "BLJBDJ"
    assert encrypt("BLJBDJ", -3) == "ZIGZAG"