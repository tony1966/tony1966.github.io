import spacy
nlp=spacy.load('en_core_web_sm')
doc=nlp('I am going to visit the White House.')
print(f'text\tlemma_\ttag_\tpos_\tdep_')  
for token in doc:   
    print(f'{token.text}\t{token.lemma_}\t{token.tag_}\t{token.pos_}\t{token.dep_}')