def total(tots):
    fin = 0
    for key in tots:
        fin += key
    return fin

def treinta(total):
    return(total * 0.321)

def veinte(total):
    return(total * 0.221)

def diez(total):
    return(total * 0.121)

def aPagar(total, porc):
    paga = 0
    if(porc == 10):
        paga = total - diez(total)
    elif(porc == 20):
        paga = total - veinte(total)
    else:
        paga = total - treinta(total)
    return paga

def aRendir(total, porc):
    return(total - aPagar(total, porc))