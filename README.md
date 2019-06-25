# EUSKARARAKO LEMATIZATZAILEA / BASQUE LEMMATIZER

IXA pipes 1.1.1 tresna erabiliz euskarazko lematizatzailea nola erabili Pythonetik.
(Karpetak IXA pipes-eko paketetik, lematizatzailea erabiltzeko behar diren atalak bakarrik ditu.)


Using IXA pipes 1.1.1 tool, how to use the lemmatizer for Basque from Python.
(This folder includes only parts of IXA pipes needed to lemmatize.)

#ERABILERA / usage: lematize.py input.txt


IXA pipes-i buruzko info+ / info+ about IXA pipes: 

IXApipesREADME eta/and http://ixa2.si.ehu.es/ixa-pipes




ERRORE HAU DUT / I get this ERROR:

bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?

KONPONBIDEA / Solution:

[sudo] pip3 install lxml

IXA pipes 1.1.1 release


Gorka Urbizuk HAP/LAP masterreko lan baterako erabilia eta hurrengo urteko ikasleei laguntzeko asmoz zabaldua. 

PD: eztet IXApipes-en lizentzie irakurri, hau zeozertako erabili ezkeo irakurri zazu xD