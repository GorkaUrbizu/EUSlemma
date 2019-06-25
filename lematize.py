import sys
from bs4 import BeautifulSoup as Soup
import os

#ERABILERA / usage: lematize.py input.txt

###LEMATIZATU / lematize
# Extract lemmas from
def parseLog(file):
    handler = open(file).read()
    soup = Soup(handler, "lxml")
    words = []
    lemma = []
    POS = []
    for word in soup.findAll('wf'):
        words.append(word.get_text())
    for term in soup.findAll('term'):
        lemma.append(term['lemma'])
        POS.append(term['morphofeat'])
    return(words,lemma,POS)

if len(sys.argv) not in [2,3]:
    print("ERABILERA / usage: lematize.py input")
else:
    ixaPin = sys.argv[1]
    ixaPout = "output.naf"

    #IXApipes-i deitu / call to IXApipes
    #Sarreran input.txt fitxategia hartu eta lemak naf formatuan output.txt fitxategian irteera. 
    #take lemmas from input.txt and write them in naf format in output.txt
    os.system("cat "+ixaPin+" | java -jar ixa-pipe-tok-1.8.5-exec.jar tok -l eu | java -jar ixa-pipe-pos-1.5.1-exec.jar tag -m morph-models-1.5.0/eu/eu-pos-perceptron-epec.bin -lm morph-models-1.5.0/eu/eu-lemma-perceptron-epec.bin > "+ixaPout)
    #NAFetik hitzak, lemak eta POSak eskuratu / extract words, lemmas and POS from NAF file
    words, lemma, POS = parseLog(ixaPout)
    #Behin lemmak eskuratuta, inprimatu, fitxategian idatzi edo jarraitu prozesatzen 
    #Once we got the lemmas, write, print or do whatewer you want
    print(lemma)
