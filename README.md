Multi-grain LDA
=========

This progrom is modified from https://github.com/m-ochi/mglda and concentrate on the usage for chinese.

No need to install nltk toolkit and using python3 for general usage.

File
------
trainingCorpus/ -> all the training set

trainingCorpus/trainingData.txt -> is the 3500 hotel reviews and all setences are tokenized by the 中研院斷詞系統 http://ckipsvr.iis.sinica.edu.tw/

regular.py -> format the general training Data

vocabulary\_forMGLDA.py -> the library for the mglda.py

mglda.py -> the main program file

Require
--------
sudo apt-get install pyhton3
sudo apt-get install pyhton3-numpy

Usage
-------
python3 mglda.py
