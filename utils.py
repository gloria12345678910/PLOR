nachkommaStellen = 4
zwischenergebnisRunden = False

def runden(x, zwischenergebnis = False):
    if (zwischenergebnisRunden and zwischenergebnis) or not zwischenergebnis:
        return round(x*pow(10,nachkommaStellen))/pow(10,nachkommaStellen)
    else:
        return x

if __name__ == '__main__':
    print(runden(4.4354352435))