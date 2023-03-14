# Extract and tokenization the text

import goose3
import nltk

# Configuration for processing UTF-8
nltk.download('punkt')

# url of page to extract the text
url: str = 'https://www.treinaweb.com.br/blog/dicas-para-ser-mais-produtivo-no-trabalho-remoto'

# Extract the content of text
g = goose3.Goose()
article = g.extract(url=url)

# Get a text extracted
text = article.cleaned_text

# Print the text
print(text)

# Tokenization
tokens = nltk.word_tokenize(text)

print(tokens)
