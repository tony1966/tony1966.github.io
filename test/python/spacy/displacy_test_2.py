import spacy
nlp=spacy.load('en_core_web_sm')
doc=nlp('I live in Taiwan.')
print(f'text\tlemma_\ttag_\tpos_\tdep_\thead')  
for token in doc:
    fstr=(f'{token.text}\t{token.lemma_}\t{token.tag_}\t{token.pos_}\t'
          f'{token.dep_}\t{token.head}')
    print(fstr)