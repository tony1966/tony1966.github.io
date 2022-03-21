import spacy
from spacy import displacy
nlp=spacy.load('en_core_web_sm')
doc=nlp('I live in Taiwan.')
displacy.serve(doc, style='ent')