import logging
from pathlib import Path
from smartdoc_sem_ia import main as generate_doc
from src.utils.config import OUTPUT_DIR

logger = logging.getLogger(__name__)

class DocumentGenerator:
    @staticmethod
    def generate(arquivo_pbit: str, modelo_word: str) -> bool:
        """
        Gera a documentação do Power BI usando o arquivo PBIT e o modelo Word fornecidos.
        O arquivo será salvo automaticamente no diretório output.
        
        Args:
            arquivo_pbit (str): Caminho para o arquivo .pbit
            modelo_word (str): Caminho para o modelo .docx
            
        Returns:
            bool: True se a geração foi bem sucedida, False caso contrário
        """
        try:
            # Garante que o diretório output existe
            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            
            # Gera o nome do arquivo de saída baseado no nome do arquivo PBIT
            arquivo_pbit_path = Path(arquivo_pbit)
            nome_saida = arquivo_pbit_path.stem + "_documentado.docx"
            caminho_saida = str(OUTPUT_DIR / nome_saida)
            
            generate_doc(arquivo_pbit, modelo_word, str(OUTPUT_DIR))
            return True
        except Exception as ex:
            logger.exception("Erro ao gerar documentação")
            raise ex
