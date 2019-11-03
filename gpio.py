def gpio_8266 (onBordname) :
    if onBordname == 'D0' : return 16
    elif onBordname == 'D1' : return 5
    elif onBordname == 'D2' : return 4
    elif onBordname == 'D3' : return 0
    elif onBordname == 'D4' : return 2
    elif onBordname == 'D5' : return 14
    elif onBordname == 'D6' : return 12
    elif onBordname == 'D7' : return 13
    elif onBordname == 'D8' : return 15
    elif onBordname == 'D9' : return 3
    elif onBordname == 'D10' : return 1
    elif onBordname == 'S3' : return 10
    elif onBordname == 'S2' : return 9

def gpio_32 (onBordname) :
    print("needs to be reimplemented for esp32")
    if onBordname == 'D0' : return 16
    elif onBordname == 'D1' : return 5
    elif onBordname == 'D2' : return 4
    elif onBordname == 'D3' : return 0
    elif onBordname == 'D4' : return 2
    elif onBordname == 'D5' : return 14
    elif onBordname == 'D6' : return 12
    elif onBordname == 'D7' : return 13
    elif onBordname == 'D8' : return 15
    elif onBordname == 'D9' : return 3
    elif onBordname == 'D10' : return 1
    elif onBordname == 'S3' : return 10
    elif onBordname == 'S2' : return 9
