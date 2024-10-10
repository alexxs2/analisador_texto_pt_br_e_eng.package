import spacy
from collections import Counter

def auto_detect_model():
    try:
        return spacy.load("pt_core_news_lg")
    except OSError:
      pass
    try:
        return spacy.load("pt_core_news_md")
    except OSError:
      pass
    
    try:
        return spacy.load("pt_core_news_sm")
    except OSError:
      pass
    
    return None

def analise_texto(texto):
    nlp = auto_detect_model()
    if nlp is None:
        print("Nenhum modelo disponível no sistema, consulte o arquivo README do pacote para escolher um dos modelos do spaCy.")
        return None
    doc = nlp(texto.lower())
    filtered_tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
    word_count = Counter(filtered_tokens)
    
    total_words = len([token for token in doc if not token.is_punct])
    filtered_words = len(filtered_tokens)
    most_common_words= word_count.most_common(5)

    print(f"\nResultado da análise do texto:\n")
    print(f"Total de palavras (sem pontuação): {total_words}")
    print(f"Total de palavras filtradas (sem stopwords e pontuação): {filtered_words}")
    print(f"Palavras mais comuns: {most_common_words}")

