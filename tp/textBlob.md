# **TextBlob: Simplified Text Processing**

O TextBlob é uma libraria de Python que tem como principal objetivo o processamento de textos. Este fornce uma API simples que permite aos utilizadores realizar tarefas comuns de PLN (Processamento de Linguagem Natural), tais como etiquetar textos, extrair nomes de frases, análise de sentimentos, classificação, tradução, entre outros.

O TextBlob dá uso às libarias [NLTK (Natural Language Toolkit)](https://www.nltk.org/) e pattern.

**Funcionalidades:**
- extração de nomes de frases
- etiquetar textos
- análise de sentimentos
- classificação (_Naive Bayes_ e _Decision Tree_)
- tokenização (dividir o texto em palavras e frases)
- frequência de palavras e frases
- _parsing_
- _n-grams_
- inflexão de palavras (colocar as palavras no plural ou no singular) e [lematização](https://dicionario.priberam.org/lematiza%C3%A7%C3%A3o)
- corretor ortográfico
- adicionar novos modelos e linguagens através de extensões
- integração do [WordNet](https://wordnet.princeton.edu/)

**Instalação:**
    
```bash 
$ pip install -U textblob
$ python -m textblob.download_corpora
``` 

**Quick Start:**

**Nota:** Os objetos TextBlob podem ser tratados como se fossem string de Python que aprenderam como fazer Processamento de Linguagem Natural. >.< 

**Criação de um TextBlob**
```py
from textblob import TextBlob

wiki = TextBlob("Sokka: My first girlfriend turned into the moon. // Zuko: That's rough, buddy.")
```

**Next Step:** experimentar a biblioteca num Jupyter Notebook para perceber o seu funcionamento e escolher algumas das _features_ mais interessantes para aplicar no caso de estudo.

[Referência Bibliográfica](https://textblob.readthedocs.io/en/dev/)