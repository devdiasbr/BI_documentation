import logging
from pathlib import Path
from smartdoc_sem_ia import main as generate_doc

logger = logging.getLogger(__name__)

class DocumentGenerator:
    @staticmethod
    def generate(arquivo_pbit: str, modelo_word: str, diretorio_saida: str) -> bool:
        """
        Gera a documentação do Power BI usando o arquivo PBIT e o modelo Word fornecidos.
        
        Args:
            arquivo_pbit (str): Caminho para o arquivo .pbit
            modelo_word (str): Caminho para o modelo .docx
            diretorio_saida (str): Diretório onde o documento será salvo
            
        Returns:
            bool: True se a geração foi bem sucedida, False caso contrário
        """
        try:
            generate_doc(arquivo_pbit, modelo_word, diretorio_saida)
            return True
        except Exception as ex:
            logger.exception("Erro ao gerar documentação")
            raise ex
