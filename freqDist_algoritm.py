import urllib.request
import io
import nltk
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

# Baixar os arquivos PDF
pdf_urls = [
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

pdf_files = []

for url in pdf_urls:
    pdf_files.append(urllib.request.urlopen(url))

# Extrair o texto de cada arquivo PDF
def extract_text_from_pdf(file):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    for page in PDFPage.get_pages(file, caching=True, check_extractable=True):
        page_interpreter.process_page(page)
    text = fake_file_handle.getvalue()
    converter.close()
    fake_file_handle.close()
    return text

texts = []
for pdf_file in pdf_files:
    texts.append(extract_text_from_pdf(pdf_file))

# Tokenizar e calcular a distribuição de frequência
tokens = []
for text in texts:
    tokens += nltk.word_tokenize(text.lower())
freq_dist = nltk.FreqDist(tokens)

# Imprimir as 50 palavras mais frequentes
print(freq_dist.most_common(50))
