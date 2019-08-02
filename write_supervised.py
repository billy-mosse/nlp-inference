#!/usr/bin/env python
import argparse
import json
import csv

#Convierte frases y labels de json a txt
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('sentences')
    ap.add_argument('labels', nargs='?')
    ap.add_argument('output', nargs='?')

    args = ap.parse_args()

    sentence_data = open(args.sentences, 'r')
    sentences_txt = open(args.output, 'w')
    if args.labels:
        label_data = open(args.labels, 'r')
        for sentence, label in zip(it_sentences(sentence_data), it_labels(label_data)):
            # Tenemos la oración en sentence con su categoría en label
            #print(label, sentence)
            sentences_txt.write("__label__%s %s\n" % (label, sentence))
    else:
        for sentence in it_sentences(sentence_data):
            # Tenemos una oración en sentence
            #print(sentence)
            pass
    sentence_data.close()
    sentences_txt.close()

    

def it_sentences(sentence_data):
    for line in sentence_data:
        example = json.loads(line)
        yield example['sentence2']

def it_labels(label_data):
    label_data_reader = csv.DictReader(label_data)
    for example in label_data_reader:
        yield example['gold_label']




main()
