from functions import create_encrypt

def test_create_encrypt():
    cesar3 = create_encrypt(3)
    assert cesar3("ZigZag") == "BLJBDJ"

    cesar2 = create_encrypt(2)
    assert cesar2("Hola Mundo") == "JQNCBÑWOFQ"

    cesar4 = create_encrypt(4)
    assert cesar4("Zig Zag") == "CMKDCEK"

    cesar2 = create_encrypt(2)
    assert cesar2("ZigZag") == "AKIACI"

    inverse_cesar2 = create_encrypt(-2)
    assert inverse_cesar2("AKIACI") == "ZIGZAG"