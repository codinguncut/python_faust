import logging
import spacy


def init(model='en'):
    logging.warning('spacy - loading')
    nlp = spacy.load(model)
    logging.warning('spacy - done')
    return nlp


def entities(nlp, doc):
    spacy_doc = nlp(doc)
    return {ent.text.strip()
            for ent in spacy_doc.ents}
