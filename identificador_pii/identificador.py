from collections import Counter
import re
import pandas as pd
from pandas import DataFrame

class IdentificadorPII(DataFrame):

    def __init__(self, df:DataFrame) -> None:
        self.patterns = None

    def load_patterns(self) -> dict:
        """Carrega os padrões para buscar documentos brasileiros.
        Returns:
            dict: Dicionário com os padrões regex que serão buscados.
        """

        patterns  = {
        'cpf':  r'^\d{11}$|^\d{3}\.\d{3}\.\d{3}-\d{2}$',
        'telefone': r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$',
        'cnh': r'^[A-Z]{2}\d{9}$',
        'email':  r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
        'nis': r'\b\d{3}\.\d{5}\.\d{2}-\d{1}\b|\b\d{11}\b'
        }

        return patterns
 
    
    def add_pattern(self, pattern_name: str) -> dict:
        ...
    
    def remove_pattern(self, pattern_name: str) -> dict:
        
        ... 

    def busca_nomes(self, ): 
        ...

    def remove_stopwords(self):
        """
        Remove as stopwords do texto.
        Args:
            texto (str): Texto a ser processado.
        Returns:
            str: Texto sem stopwords.
        """
        ...

    def classify_column(self, coluna):
        """
        Função que busca os nomes e sobrenomes mais comuns no conteúdo da coluna.

        Args:
            df (pandas.DataFrame): Conjunto de dados a ser analisao.
            column_name (str): Nome da coluna a ser analisada.

        Returns:
            column_name (str): Nome da coluna.
            nome (str): nome.
            match_count (int): Quantidade de correspondencias encontradas.
            perc_match_count (float): Percentual de correspondencias encontradas.
        """
    
    def classify_df(self):
        """
        Classifica uma coluna do dataframe.

        Args:
            df (pandas.DataFrame): Conjunto de dados a ser analisao.
            column_name (str): Nome da coluna a ser analisada.

        Returns:
            column_name (str): Nome da coluna.
            pred (str): predição do tipo de dados presente na coluna.
            max_matches_col (str): Nome da coluna com mais correspondencias.
            max_matches_count (int): Quantidade de correspondencias encontradas.
            max_matches_perc (float): Percentual de correspondencias encontradas.
        """
        ...
