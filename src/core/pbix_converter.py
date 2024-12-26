import os
import shutil
import tempfile
import zipfile

def convert_pbix_to_pbit(pbix_path: str) -> str:
    """
    Converte um arquivo .pbix para .pbit
    
    Args:
        pbix_path (str): Caminho para o arquivo .pbix
        
    Returns:
        str: Caminho para o arquivo .pbit gerado
    """
    # Verifica se o arquivo existe
    if not os.path.exists(pbix_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {pbix_path}")
        
    # Verifica se é um arquivo .pbix
    if not pbix_path.lower().endswith('.pbix'):
        raise ValueError("O arquivo deve ter extensão .pbix")
    
    # Cria um diretório temporário
    with tempfile.TemporaryDirectory() as temp_dir:
        # Copia o arquivo .pbix para o diretório temporário
        temp_pbix = os.path.join(temp_dir, 'temp.pbix')
        shutil.copy2(pbix_path, temp_pbix)
        
        # Renomeia para .zip para extrair o conteúdo
        temp_zip = os.path.join(temp_dir, 'temp.zip')
        os.rename(temp_pbix, temp_zip)
        
        # Extrai o conteúdo
        with zipfile.ZipFile(temp_zip, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        
        # Remove os arquivos de dados
        data_dir = os.path.join(temp_dir, 'Data')
        if os.path.exists(data_dir):
            shutil.rmtree(data_dir)
            
        # Cria o arquivo .pbit
        pbit_path = os.path.splitext(pbix_path)[0] + '.pbit'
        with zipfile.ZipFile(pbit_path, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
            for root, _, files in os.walk(temp_dir):
                for file in files:
                    if file != 'temp.zip':
                        file_path = os.path.join(root, file)
                        arc_name = os.path.relpath(file_path, temp_dir)
                        zip_ref.write(file_path, arc_name)
    
    return pbit_path
