# Extract, tokenize and get the FreqDist

from urllib import request
from pdfminer.high_level import extract_text
import nltk
from nltk.probability import FreqDist
import io

# Configuration for processing UTF-8
nltk.download('punkt')


# url of page to extract the text
urls = [
    'file:///C:\Database_texts/2fa1759f3d3fd65c4dfd9556cafbc9278d6a.pdf',
    'file:///C:\Database_texts/9a-revista-eletronica-book.pdf',
    'file:///C:\Database_texts/2015_06_0113_0138.pdf',
    'file:///C:\Database_texts/11092-Texto%20do%20artigo-36586-1-10-20091026.pdf',
    'file:///C:\Database_texts/24403-82590-1-PB.pdf',
    'file:///C:\Database_texts/32453-Texto%20do%20artigo-88084-1-10-20170424.pdf',
    'file:///C:\Database_texts/1400625866_atitude14.pdf',
    'file:///C:\Database_texts/A_desconsideracao_da_personalidade_jurid.pdf',
    'file:///C:\Database_texts/A-prote%C3%A7%C3%A3o-na-cultura-juridica.pdf',
    'file:///C:\Database_texts/atualizacao_reforma_mauroschiavi.pdf',
    'file:///C:\Database_texts/claudio_jannotti_rocha_e_mirella_karen_carvalho_bifano_muniz.pdf',
    'file:///C:\Database_texts/Dos-transplantes-juridicos.pdf',
    'file:///C:\Database_texts/Francisco-Kennedy-da-Silva-de-Oliveira.pdf',
    'file:///C:\Database_texts/jose_roberto_freire_conciliacao_judicial.pdf',
    'file:///C:\Database_texts/O_processo_do_trabalho_no_ambito_do_dire.pdf',
    'file:///C:\Database_texts/personalidade_juridica_artigo50.pdf',
    'file:///C:\Database_texts/reflexos_das_alterações_do_código_de_processo_civil.pdf',
    'file:///C:\Database_texts/revistaTRT12_29-ano2017.pdf',
    'file:///C:\Database_texts/vitor%20salino%20principios%20de%20execucao.pdf',
    'file:///C:\Database_texts/V%C3%B3lia-Bomfim-Cassar.pdf'
]

# Create a texts list
tokens_list = []

# Create the FreqDist
fdist = FreqDist()

# Loop
for url in urls:
    response = request.urlopen(url)
    raw_data = response.read()
    raw_text = extract_text(io.BytesIO(raw_data))
    tokens = tuple(nltk.word_tokenize(raw_text))
    fdist[tokens_list] += 1

# Print the FreqDist
print(fdist)
