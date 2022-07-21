import numpy
import numpy as np

nachkommaStellen = 2
zwischenergebnisRunden = False

def runden(x, zwischenergebnis = False):
    if (zwischenergebnisRunden and zwischenergebnis) or not zwischenergebnis:
        return round(x*pow(10,nachkommaStellen))/pow(10,nachkommaStellen)
    else:
        return x

def createEmptyArray(length):
    x = np.asarray([])
    for i in range(length):
        x=np.append(x, np.nan)
    return x


if __name__ == '__main__':
    x = np.asarray([1,numpy.nan,4])
    print(np.isnan(x[1]))