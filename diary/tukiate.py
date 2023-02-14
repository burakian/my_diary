from datetime import datetime,timedelta
def hinichi():
    kinenbi=datetime(2022,2,19)
    kyo=datetime.now()
    keika=kyo-kinenbi
    a=str(keika.days)

    return a