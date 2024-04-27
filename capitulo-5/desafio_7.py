

def bissexto(ano: int):

    if ano % 100 != 0 and ano % 4 == 0:
        print(f"{ano} é bissexto.")
    else:
        print(f"{ano} não é bissexto.")


bissexto(2024)
bissexto(1998)
bissexto(2000)
bissexto(2007)
bissexto(1830)
bissexto(1996)
