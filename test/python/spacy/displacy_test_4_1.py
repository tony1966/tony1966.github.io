import spacy
from spacy import displacy
nlp=spacy.load('en_core_web_sm')
doc=nlp('I live in Taiwan.')
print('Token\tent_type_\texplain')
for token in doc:
    print(f'{token.text}\t{token.ent_type_}\t{spacy.explain(token.ent_type_)}')