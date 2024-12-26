import flet as ft
import os
from smartdoc_sem_ia import main as generate_doc
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def main(page: ft.Page):
    # Configuração da página
    page.title = "Power BI Documentator"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.window_width = 800
    page.window_height = 600
    page.window_resizable = True
    page.update()
    
    # Toggle para Dark Mode
    def toggle_theme(e):
        page.theme_mode = (
            ft.ThemeMode.DARK 
            if page.theme_mode == ft.ThemeMode.LIGHT 
            else ft.ThemeMode.LIGHT
        )
        theme_button.icon = (
            ft.icons.DARK_MODE 
            if page.theme_mode == ft.ThemeMode.LIGHT 
            else ft.icons.LIGHT_MODE
        )
        page.update()
    
    theme_button = ft.IconButton(
        icon=ft.icons.DARK_MODE,
        icon_size=20,
        on_click=toggle_theme,
        tooltip="Alternar tema claro/escuro"
    )
    
    # Elementos da interface
    titulo = ft.Text("Power BI Documentator", size=32, weight=ft.FontWeight.BOLD)
    subtitulo = ft.Text("Gere documentação automatizada para seus relatórios Power BI", size=16)
    
    # Seção de instruções
    instrucoes = ft.Container(
        content=ft.Row(
            [
                # Coluna da esquerda - Como usar
                ft.Container(
                    content=ft.Column([
                        ft.Text("Como Usar:", size=16, weight=ft.FontWeight.BOLD),
                        ft.Text("1. Transforme seu arquivo .pbix em .pbit:", size=14),
                        ft.Text("   • Abra seu arquivo no Power BI Desktop", size=14),
                        ft.Text("   • Vá em Arquivo > Exportar > Modelo do Power BI", size=14),
                        ft.Text("2. Selecione o arquivo .pbit gerado", size=14),
                        ft.Text("3. Selecione um modelo Word para a documentação", size=14),
                        ft.Text("4. Escolha o diretório onde será salvo o documento", size=14),
                        ft.Text("5. Clique em 'Gerar Documentação'", size=14),
                    ]),
                    padding=20,
                    expand=True
                ),
                # Linha vertical divisória
                ft.VerticalDivider(width=1, color=ft.colors.BLACK45),
                # Coluna da direita - O que será documentado
                ft.Container(
                    content=ft.Column([
                        ft.Text("O Documento Conterá:", size=16, weight=ft.FontWeight.BOLD),
                        ft.Text("• Páginas do relatório", size=14),
                        ft.Text("• Tabelas e colunas", size=14),
                        ft.Text("• Medidas DAX", size=14),
                        ft.Text("• Fontes de dados", size=14),
                        ft.Text("• Relacionamentos entre tabelas", size=14),
                    ]),
                    padding=20,
                    expand=True
                ),
            ],
            expand=True
        ),
        padding=10,
        border=ft.border.all(1, ft.colors.BLACK45),
        border_radius=10,
        margin=ft.margin.only(bottom=20)
    )
    
    # Campo para selecionar arquivo .pbit
    def pick_pbit_file(e: ft.FilePickerResultEvent):
        if e.files:
            arquivo_pbit.value = e.files[0].path
            page.update()
            
    arquivo_pbit = ft.Text()
    pick_pbit_dialog = ft.FilePicker(
        on_result=pick_pbit_file
    )
    
    # Campo para selecionar modelo Word
    def pick_word_template(e: ft.FilePickerResultEvent):
        if e.files:
            modelo_word.value = e.files[0].path
            page.update()
            
    modelo_word = ft.Text()
    pick_word_dialog = ft.FilePicker(
        on_result=pick_word_template
    )
    
    # Campo para selecionar diretório de saída
    def pick_output_dir(e: ft.FilePickerResultEvent):
        if e.path:
            diretorio_saida.value = e.path
            page.update()
            
    diretorio_saida = ft.Text()
    pick_dir_dialog = ft.FilePicker(
        on_result=pick_output_dir
    )
    
    # Barra de progresso
    progress = ft.ProgressBar(width=400, visible=False)
    status_text = ft.Text()
    
    # Função para gerar documentação
    def generate_documentation(e):
        if not all([arquivo_pbit.value, modelo_word.value, diretorio_saida.value]):
            status_text.value = "Por favor, preencha todos os campos!"
            status_text.color = ft.colors.RED
            page.update()
            return
            
        try:
            progress.visible = True
            status_text.value = "Gerando documentação..."
            status_text.color = ft.colors.BLUE
            page.update()
            
            # Executa a geração da documentação
            resultado = generate_doc(
                arquivo_pbit=arquivo_pbit.value,
                modelo_word=modelo_word.value,
                diretorio_saida=diretorio_saida.value
            )
            
            if resultado:
                status_text.value = f"Documentação gerada com sucesso em:\n{resultado}"
                status_text.color = ft.colors.GREEN
            else:
                status_text.value = "Falha ao gerar documentação. Verifique o arquivo de log para mais detalhes."
                status_text.color = ft.colors.RED
            
        except Exception as ex:
            status_text.value = f"Erro: {str(ex)}"
            status_text.color = ft.colors.RED
            logger.error(f"Erro ao gerar documentação: {ex}")
            
        finally:
            progress.visible = False
            page.update()
    
    # Layout da interface
    page.overlay.extend([pick_pbit_dialog, pick_word_dialog, pick_dir_dialog])
    
    page.add(
        ft.Column(
            controls=[
                # Cabeçalho com título e botão de tema
                ft.Row(
                    [
                        ft.Column(
                            [titulo, subtitulo],
                            expand=True
                        ),
                        theme_button
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Divider(height=30),
                
                # Seção de instruções
                instrucoes,
                
                # Seção arquivo PBIT
                ft.Text("Arquivo Power BI (.pbit)", size=16, weight=ft.FontWeight.BOLD),
                ft.Row([
                    arquivo_pbit,
                    ft.ElevatedButton(
                        "Selecionar arquivo",
                        icon=ft.icons.FILE_UPLOAD,
                        on_click=lambda _: pick_pbit_dialog.pick_files()
                    )
                ]),
                
                ft.Divider(height=20),
                
                # Seção modelo Word
                ft.Text("Modelo Word (.docx)", size=16, weight=ft.FontWeight.BOLD),
                ft.Row([
                    modelo_word,
                    ft.ElevatedButton(
                        "Selecionar modelo",
                        icon=ft.icons.FILE_UPLOAD,
                        on_click=lambda _: pick_word_dialog.pick_files()
                    )
                ]),
                
                ft.Divider(height=20),
                
                # Seção diretório de saída
                ft.Text("Diretório de saída", size=16, weight=ft.FontWeight.BOLD),
                ft.Row([
                    diretorio_saida,
                    ft.ElevatedButton(
                        "Selecionar diretório",
                        icon=ft.icons.FOLDER,
                        on_click=lambda _: pick_dir_dialog.get_directory_path()
                    )
                ]),
                
                ft.Divider(height=30),
                
                # Botão gerar e status
                ft.Row([
                    ft.ElevatedButton(
                        "Gerar Documentação",
                        icon=ft.icons.CREATE_OUTLINED,
                        on_click=generate_documentation,
                        style=ft.ButtonStyle(
                            color=ft.colors.WHITE,
                            bgcolor=ft.colors.BLUE,
                            padding=15
                        )
                    )
                ], alignment=ft.MainAxisAlignment.CENTER),
                
                progress,
                status_text
            ],
            spacing=10
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
