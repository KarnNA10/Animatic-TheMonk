a = 44 #Ultimo plano
link = "https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Storyboard/"
b = []


for i in range(35,a+1,3):
    if i<10:
        c="00"
    else: 
        c="0" # si son más de 100 me suicido
    num1 = c+str(i)
    num2 = c+str(i+1)
    num3 = c+str(i+2)
    d = "|"+num1+"!["+num1+"]("+link+num1+".png)|"+num2+"!["+num2+"]("+link+num2+".png)|"+num3+"!["+num3+"]("+link+num3+".png)|"
    b.append(d)

for i in b:
    print(i)


"""
debe quedar algo así:

|001![001](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/001.png)|002![002](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/002.png)|003![003](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/003.png)|
|004![004](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/004.png)|005![005](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/005.png)|006![006](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/006.png)|
|007![007](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/007.png)|008![008](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/008.png)|009![009](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/009.png)|
|010![010](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/010.png)|011![011](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/011.png)|012![012](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/012.png)|
|013![013](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/013.png)|014![014](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/014.png)|015![015](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/015.png)|
|016![016](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/016.png)|017![017](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/017.png)|018![018](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/018.png)|
|019![019](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/019.png)|020![020](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/020.png)|021![021](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/021.png)|
|022![022](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/022.png)|023![023](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/023.png)|024![024](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/024.png)|
|025![025](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/025.png)|026![026](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/026.png)|027![027](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/027.png)|
|028![028](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/028.png)|029![029](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/029.png)|030![030](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/030.png)|
|031![031](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/031.png)|032![032](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/032.png)|033![033](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Preview/033.png)|

|035![035](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Storyboard/035.png)|036![036](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Storyboard/036.png)|037![037](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Storyboard/037.png)|
|038![038](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Storyboard/038.png)|039![039](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Storyboard/039.png)|040![040](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Storyboard/040.png)|
|041![041](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Storyboard/041.png)|042![042](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Storyboard/042.png)|043![043](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Storyboard/043.png)|
|044![044](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Storyboard/044.png)|045![045](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Storyboard/045.png)|046![046](https://github.com/KarnNA10/Animatic-TheMonk/blob/main/Planos/Storyboard/046.png)|

Soy el capitán Clark y estos son mis backrooms
"""

