
from collections import Counter
def aldaketakEgin(ema):
    h1=input("Idatzi aldatu nahi duzun karakterea.")
    h2=input("Zein karakterez aldatu nahi duzu?")
    return ema.replace(h1,h2)
def main():
# Testua programan sartu
    textua = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."
    hizkiak = Counter(textua) #txetuan hizki bakoitza zenbat aldiz agertzen den ikusi
    print("Hizki kopurua = ", len(hizkiak))
    print(hizkiak)
    print('\n')
    print('Gure testuan gehien errepikatzen diren hiru karaktereak hauek dira:') 
    erabilienak=hizkiak.most_common(3)
    #hizkiak.most_common(3), funtzio horrekin gehien errepikatzen diren 3 hizkiak soilik hartuko ditugu
    print(erabilienak)
    print('\n')
    # Orain emaitza lortzen saiatuko gara, horretarako gaztelanian gehien erabiltzen diren hizkiak gure textuan gehien erabiltzen diren hizkiak replace egingo diegu
    ema= textua
    #Programak badakizki gaztelaniaz gehien errepikatzen diren hizkiak hauexek direla: e eta a, beraz, textuan gehien agertzen diren hizkiekin aldatuko ditu.
    print("Programak badaki gaztelaniaz gehien erabiltzen diren hizkiak 'e' eta 'a' direla, beraz hauek aldatuko ditu testuan gehien errepikatzen diren hizkiegaz")
    print('\n')
    #erabilienak tuplak gordetzen dituen zerrenda bat denez, lehenengo [indize] listaren indizea adierazten du eta bigarren tuplaren [index] adierazten du
    ema= ema.replace(erabilienak[1][0], 'e')
    ema= ema.replace(erabilienak[2][0], 'a')
    print(ema)
    print("\n")
    print("Horain saiatu aldatzen silaba bakerreko hizkiak, hiru karaktere dituztenak, adibidez, 's' hizkiaz amaitu daitekela badakigu...")
    ema= aldaketakEgin(ema)
    jarraitu = "b"
    while jarraitu=="b":
        print(ema)
        jarraitu=input("Aldaketa gehiago egin nahi dituzu? (b/e) ")
        if jarraitu != "b":
            print("Agur!")
            break;
        ema = aldaketakEgin(ema)
main()