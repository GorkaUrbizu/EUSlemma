IXA pipes 1.1.1 release
=======================

In this folder you can find the ready-to-use pre-compiled pipes and then
the source code of each component which can be compiled following the
instructions. The pre-compiled binaries **will work on any machine as long
as a JVM 1.7+ is available**.

# Binary usage:

+ POS and Lemma: cat berria.txt | java -jar ixa-pipe-tok-1.8.5-exec.jar tok -l eu | java -jar ixa-pipe-pos-1.5.1-exec.jar tag -m morph-models-1.5.0/eu/eu-pos-perceptron-epec.bin -lm morph-models-1.5.0/eu/eu-lemma-perceptron-epec.bin

+ Chunking: cat berria.txt | java -jar ixa-pipe-tok-1.8.5-exec.jar tok -l eu | java -jar ixa-pipe-pos-1.5.1-exec.jar tag -m morph-models-1.5.0/eu/eu-pos-perceptron-epec.bin -lm morph-models-1.5.0/eu/eu-lemma-perceptron-epec.bin | java -jar ixa-pipe-chunk-1.1.1-exec.jar tag -m chunk-models-1.1.0/eu-chunk-epec.bin

+ Named Entity Recognition: cat berria.txt | java -jar ixa-pipe-tok-1.8.5-exec.jar tok -l eu | java -jar ixa-pipe-pos-1.5.1-exec.jar tag -m morph-models-1.5.0/eu/eu-pos-perceptron-epec.bin -lm morph-models-1.5.0/eu/eu-lemma-perceptron-epec.bin | java -jar ixa-pipe-nerc-1.6.1-exec.jar tag -m nerc-models-1.5.4/eu/eu-clusters-egunkaria.bin

Please check the [IXA pipes] main website](http://ixa2.si.ehu.es/ixa-pipes) for detailed documentation of each tool.

# API usage

ixa pipes are in Maven central. Please go to search.maven.org and find the latest dependency.


# Contact information

````shell
Rodrigo Agerri
IXA NLP Group
University of the Basque Country (UPV/EHU)
E-20018 Donostia-San Sebastián
rodrigo.agerri@ehu.eus
````
