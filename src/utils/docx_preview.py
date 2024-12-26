from docx import Document
import mammoth
import os

def convert_docx_to_html(docx_path: str) -> str:
    """
    Converte um documento DOCX para HTML para preview
    
    Args:
        docx_path (str): Caminho para o arquivo DOCX
        
    Returns:
        str: HTML do documento
    """
    if not os.path.exists(docx_path):
        return ""
        
    try:
        with open(docx_path, "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
            html = result.value
            
            # Adiciona estilos básicos
            styled_html = f"""
            <div style="font-family: Arial, sans-serif; padding: 20px; color: #333;">
                {html}
            </div>
            """
            return styled_html
    except:
        return ""
