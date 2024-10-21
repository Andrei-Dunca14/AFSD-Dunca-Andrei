sir="AC Milan a câștigat un duel extrem de disputat cu Inter Milano, rivala din oraș și a obținut prima victorie în fața nerrazzurilor după șase înfrângeri consecutive. Rossonerii s-au impus pe final de joc și și-au asigurat o victorie care le aduce trei puncte extrem de importante în Serie A, după un start slab de sezon"
mijloc=len(sir)//2
partea1=sir[:mijloc]
partea2=sir[mijloc:]
partea1.strip()
partea2=partea2[::-1]
partea2=partea2.replace(',',' ')
partea2=partea2.replace('.',' ')
print(partea1.upper()+partea2.capitalize())

