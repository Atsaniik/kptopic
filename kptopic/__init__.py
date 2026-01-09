import nltk
import spacy

def _setup_resources():
    """Internal helper to ensure required data is present."""
    # NLTK Resources
    for resource in ['wordnet', 'vader_lexicon', 'punkt']:
        try:
            nltk.download(resource, quiet=True)
            
        except LookupError:
            print(f"--- Initializing: Downloading NLTK '{resource}' ---")
            nltk.data.find(f'corpora/{resource}' if resource != 'vader_lexicon' else f'sentiment/{resource}')

    try:
        spacy.load("en_core_web_sm")
    except OSError:
        print("--- Initializing: Installing spaCy model ---")
        from spacy.cli import download
        download("en_core_web_sm")

# Call this at the end of your __init__.py or before the first NLP task
_setup_resources()

