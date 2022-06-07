# EUSKARARAKO LEMATIZATZAILEA / BASQUE LEMMATIZER

IXA pipes 1.1.1 tresna erabiliz euskarazko lematizatzailea nola erabili Pythonetik.

Using IXA pipes 1.1.1 tool, how to use the lemmatizer for Basque from Python.

## ERABILERA / usage: 
```
lematize.py input.txt
```
Karpetak IXA pipes-eko paketetik, lematizatzailea erabiltzeko behar diren atalak bakarrik ditu.
This folder includes only parts of IXA pipes needed to lemmatize.

IXA pipes-i buruzko INFO+ about IXA pipes: IXApipesREADME eta/and http://ixa2.si.ehu.es/ixa-pipes


#### ERRORE HAU DUT / I get this ERROR:
```
bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?
```
#### KONPONBIDEA / Solution:
```
[sudo] pip3 install lxml
```

**Gorka Urbizu**k HAP/LAP masterreko lan baterako erabilia eta hurrengo urteko ikasleei laguntzeko asmoz zabaldua. :star: 

PD :exclamation: : eztet IXApipes-en lizentzie irakurri, hau zeozertako erabili ezkeo irakurri zazu  :innocent:
