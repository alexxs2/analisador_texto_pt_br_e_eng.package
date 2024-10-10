import spacy
from collections import Counter

def auto_detect_model():
    try:
        return spacy.load("en_core_web_lg")
    except OSError:
      pass
    try:
        return spacy.load("en_core_web_md")
    except OSError:
      pass
    
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
      pass
    
    return None

def analyze_text(text):
    nlp = auto_detect_model()
    if nlp is None:
        print("No model available on the system, see the package README file to choose one of the spaCy models.")
        return None
    doc = nlp(text.lower())
    filtered_tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
    word_count = Counter(filtered_tokens)
    
    total_words = len([token for token in doc if not token.is_punct])
    filtered_words = len(filtered_tokens)
    most_common_words= word_count.most_common(5)

    print(f"\nText Analysis Result:\n")
    print(f"Total words (excluding punctuation): {total_words}")
    print(f"Filtered words (excluding stopwords and punctuation): {filtered_words}")
    print(f"Most common words: {most_common_words}")
