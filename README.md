# analisador_texto_pt_br_e_eng

**Descrição**: 

O pacote **Analisador_Texto_pt_br_e_eng** é utilizado para:

- Identificação das palavras mais comuns.
- Remoção de stopwords.
- Outras análises de processamento de linguagem natural.
Ele utiliza a biblioteca spaCy para realizar o processamento de linguagem em ambos os idiomas.

## Instalação

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar o pacote:

```bash
pip install analisador_texto_pt_br_e_eng
```

## Modo de uso

Português
```python
from analisador_texto_pt_br_e_eng.analisador_texto_pt_br import pt_br
pt_br.analise_texto("Seu texto em português aqui.")
```

Inglês
```python
from analisador_texto_pt_br_e_eng.analyze_text_eng import eng
eng.analyze_text("Your English text here.")
```
## Requisitos
Para assegurar o correto funcionamento do pacote, é necessário realizar o download dos modelos de linguagem do spaCy para português e inglês.

## Modelos do spaCy para Português

Para analisar textos em português, você pode escolher entre três tamanhos de modelos:

**pt_core_news_sm (small)**: Modelo leve e rápido.

- Benefícios: Ideal para análises rápidas ou ambientes com restrições de memória.

- Desvantagens: Menos preciso e captura menos variações linguísticas.

**Comando para instalar**
```python
python -m spacy download pt_core_news_sm
```

**pt_core_news_md (medium)**: Modelo balanceado.

- Benefícios: Melhor precisão do que o modelo "small", com um desempenho razoável.

- Desvantagens: Ocupa mais memória e tempo de processamento.

**Comando para instalar**
```python
python -m spacy download pt_core_news_md
```

**pt_core_news_lg (large)**: Modelo grande, mais preciso.

- Benefícios: Captura mais nuances linguísticas e tem maior precisão nas análises.

- Desvantagens: Mais pesado, consome mais memória e tempo de processamento.

**Comando para instalar**
```python
python -m spacy download pt_core_news_lg
```

## Modelos do spaCy para Inglês

Da mesma forma, para textos em inglês, há diferentes modelos disponíveis:

**en_core_web_sm (small)**: Modelo leve e rápido.

- Benefícios: Ótimo para tarefas simples ou quando o desempenho é uma prioridade.

- Desvantagens: Menor precisão, captura menos informações detalhadas.

**Comando para instalar**
```python
python -m spacy download en_core_web_sm
```
**en_core_web_md (medium)**: Modelo médio, balanceado.

- Benefícios: Melhor precisão em comparação com o modelo pequeno.

- Desvantagens: Um pouco mais lento e consome mais memória.

**Comando para instalar**
```python
python -m spacy download en_core_web_md
```
**en_core_web_lg (large)**: Modelo grande e mais robusto.

- Benefícios: Alta precisão, captura mais nuances do idioma.

- Desvantagens: O modelo mais pesado, consome mais recursos de memória e processamento.

**Comando para instalar**	
```python
python -m spacy download en_core_web_lg
```
## Author
Alexsandro Da Silva Bezerra

## License
[MIT](https://choosealicense.com/licenses/mit/)