#!/usr/local/bin/python
# -*- coding: utf-8 -*-

'''
Created on Sep 11, 2012

mglda用にwindowとかをつくります

'''

import re

def load_file(filename):
    corpus = []
    f = open(filename, 'r')
    doc = []
    for line in f:
#        doc = re.findall(r'\w+(?:\'\w+)?',line)
        lineArray = line.split(' ')
        if len(lineArray) > 2:
            doc.append(lineArray)
        else:
            if len(doc)>0:
                corpus.append(doc)
                doc = []
    f.close()
    return corpus

class Vocabulary:
    def __init__(self, excluds_stopwords=False):
        self.vocas = [] # id to word
        self.vocas_id = dict() # word to id
        self.docfreq = [] # id to document frequency
        self.excluds_stopwords = excluds_stopwords

    def term_to_id(self, term0):
#        term = lemmatize(term0)
        term = term0
#        if not re.match(r'[a-z]+$', term): return None
        if self.excluds_stopwords and is_stopword(term): return None
        if term not in self.vocas_id:
            voca_id = len(self.vocas)
#            print str(voca_id) + ": " + term
            self.vocas_id[term] = voca_id
            self.vocas.append(term)
            self.docfreq.append(0)
        else:
            voca_id = self.vocas_id[term]
        return voca_id

    def doc_to_ids(self, doc):
        #print ' '.join(doc)
        list = []
        words = dict()
        for term in doc:
            id = self.term_to_id(term)
            if id != None:
                list.append(id)
                if not id in words:
                    words[id] = 1
                    self.docfreq[id] += 1
        if "close" in dir(doc): doc.close()
        return list

    def doc_to_ids_each_sentence(self, doc):
        #print ' '.join(doc)
        sent_list = []
        words = dict()
        
        for sent in doc:
            list = []
            for term in sent:
                id = self.term_to_id(term)
                if id != None:
                    list.append(id)
                    if not id in words:
                        words[id] = 1
                        self.docfreq[id] += 1
            sent_list.append(list)
        if "close" in dir(doc): doc.close()
        return sent_list

    def cut_low_freq(self, corpus, threshold=1):
        new_vocas = []
        new_docfreq = []
        self.vocas_id = dict()
        conv_map = dict()
        for id, term in enumerate(self.vocas):
            freq = self.docfreq[id]
            if freq > threshold:
                new_id = len(new_vocas)
                self.vocas_id[term] = new_id
                new_vocas.append(term)
                new_docfreq.append(freq)
                conv_map[id] = new_id
        self.vocas = new_vocas
        self.docfreq = new_docfreq

        def conv(doc):
            new_doc = []
            for id in doc:
                if id in conv_map: new_doc.append(conv_map[id])
            return new_doc
        return [conv(doc) for doc in corpus]

    def __getitem__(self, v):
        return self.vocas[v]

    def size(self):
        return len(self.vocas)

    def is_stopword_id(self, id):
        return self.vocas[id] in stopwords_list
