class Deleting_string:
    @staticmethod
    def delete(text: str, minus: str) -> str:
        new = []
        n = 0
        Flag = False

        for i in text:
            if Flag == True:
                new.append(i)    
            else:
                for x in minus[n]:
                    if i != x:
                        new.append(i)
                        n -= 1
                        break
                    else:
                        break
                if n < len(minus)-1:
                    n += 1
                else:
                    Flag = True
                
                continue
            continue

        return (''.join(new))

    #-------TESTs---------

    # print(delete('Rafael', 'Raf'))
    # print(delete('Rafafel', 'Raf'))
    # print(delete('Rafael', 'af'))
    # print(delete('Aboba', 'ob'))
    # assert delete('Rafael', 'Raf') == 'ael'
    # assert delete('Rafafel', 'Raf') == 'afel'
    # assert delete('Rafael', 'af') == 'Rael'

    #------------------------