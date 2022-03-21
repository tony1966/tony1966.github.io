import spacy
from spacy import displacy
from pathlib import Path
nlp=spacy.load('en_core_web_sm')
doc=nlp('I live in Taiwan.')
svg=displacy.render(doc)
output_path=Path('images/sent1.svg')
output_path.open('w', encoding='utf-8').write(svg)