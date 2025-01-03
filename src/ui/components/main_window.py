import flet as ft
from pathlib import Path
from src.core.document_generator import DocumentGenerator
from src.core.pbix_converter import convert_pbix_to_pbit
from src.utils.config import (
    APP_NAME,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_MIN_WIDTH
)

class MainWindow:
    def __init__(self, page: ft.Page):
        self.page = page
        self.setup_page()
        self.init_controls()
        self.build_ui()

    def setup_page(self):
        """Configura as propriedades básicas da página"""
        self.page.title = APP_NAME
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.padding = ft.padding.all(20)
        self.page.window.width = WINDOW_WIDTH
        self.page.window.height = WINDOW_HEIGHT
        self.page.window.min_width = WINDOW_MIN_WIDTH
        self.page.window.resizable = True
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.update()

    def init_controls(self):
        """Inicializa os controles da interface"""
        self.arquivo_pbit = ft.Text()
        self.modelo_word = ft.Text()
        self.pick_pbit_dialog = ft.FilePicker(
            on_result=self.pick_pbit_file
        )
        self.pick_pbit_dialog.allowed_extensions = ["pbit", "pbix"]
        self.pick_word_dialog = ft.FilePicker(on_result=self.pick_word_template)
        
        self.page.overlay.extend([
            self.pick_pbit_dialog,
            self.pick_word_dialog
        ])

    def toggle_theme(self, e):
        """Alterna entre os temas claro e escuro"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK 
            if self.page.theme_mode == ft.ThemeMode.LIGHT 
            else ft.ThemeMode.LIGHT
        )
        self.theme_button.icon = (
            ft.icons.DARK_MODE 
            if self.page.theme_mode == ft.ThemeMode.LIGHT 
            else ft.icons.LIGHT_MODE
        )
        self.page.update()

    def build_ui(self):
        """Constrói a interface do usuário"""
        # Header
        self.theme_button = ft.IconButton(
            icon=ft.icons.DARK_MODE,
            icon_size=20,
            on_click=self.toggle_theme,
            tooltip="Alternar tema claro/escuro"
        )

        header = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text(APP_NAME, 
                           size=32, 
                           weight=ft.FontWeight.BOLD,
                           expand=True),
                    self.theme_button
                ]),
                ft.Text(
                    "Gere documentação automatizada para seus relatórios Power BI",
                    size=16
                ),
                ft.Text(
                    "Você pode usar arquivos .pbix ou .pbit - arquivos .pbix serão convertidos automaticamente",
                    size=14,
                    color=ft.colors.SECONDARY
                )
            ]),
            margin=ft.margin.only(bottom=20)
        )

        # Instruções
        instructions = ft.ResponsiveRow([
            ft.Container(
                content=ft.Column([
                    ft.Text("Como Usar:", size=16, weight=ft.FontWeight.BOLD),
                    ft.Text("1. Selecione um arquivo .pbix ou .pbit"),
                    ft.Text("2. Selecione um modelo Word (opcional)"),
                    ft.Text("3. Clique em 'Gerar Documentação'"),
                ]),
                padding=10,
                col={"sm": 12, "md": 6},
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text("O Documento Conterá:", 
                           size=16, 
                           weight=ft.FontWeight.BOLD),
                    ft.Text("• Páginas do relatório"),
                    ft.Text("• Tabelas e colunas"),
                    ft.Text("• Medidas DAX"),
                    ft.Text("• Fontes de dados"),
                    ft.Text("• Relacionamentos"),
                ]),
                padding=10,
                col={"sm": 12, "md": 6},
            ),
        ])

        # Form controls
        form_controls = ft.ResponsiveRow([
            ft.Container(
                content=ft.Column([
                    ft.FilledButton(
                        "Selecionar arquivo PBIT/PBIX",
                        icon=ft.icons.FILE_UPLOAD,
                        on_click=lambda _: self.pick_pbit_dialog.pick_files(),
                    ),
                    self.arquivo_pbit,
                ]),
                padding=10,
                col={"sm": 12, "md": 6},
            ),
            ft.Container(
                content=ft.Column([
                    ft.FilledButton(
                        "Selecionar modelo Word",
                        icon=ft.icons.DESCRIPTION,
                        on_click=lambda _: self.pick_word_dialog.pick_files(),
                    ),
                    self.modelo_word,
                ]),
                padding=10,
                col={"sm": 12, "md": 6},
            ),
        ])

        # Generate button
        generate_button = ft.Container(
            content=ft.ElevatedButton(
                "Gerar Documentação",
                icon=ft.icons.CREATE_ROUNDED,
                on_click=self.generate_documentation,
                style=ft.ButtonStyle(
                    padding=20,
                ),
            ),
            alignment=ft.alignment.center,
        )

        # Main content
        main_content = ft.Container(
            content=ft.Column([
                header,
                ft.Container(
                    content=instructions,
                    border=ft.border.all(1, ft.colors.BLACK45),
                    border_radius=10,
                    padding=10,
                    margin=ft.margin.only(bottom=20),
                ),
                form_controls,
                generate_button,
            ]),
            expand=True,
        )

        self.page.add(main_content)

    def pick_pbit_file(self, e: ft.FilePickerResultEvent):
        """Manipula a seleção do arquivo PBIT"""
        try:
            if e.files:
                file_path = e.files[0].path
                if file_path.lower().endswith('.pbix'):
                    # Mostra barra de progresso
                    progress = ft.ProgressBar(width=400)
                    self.page.add(progress)
                    self.page.update()
                    
                    # Converte o arquivo
                    pbit_path = convert_pbix_to_pbit(file_path)
                    file_path = pbit_path
                    
                    # Remove a barra de progresso
                    self.page.remove(progress)
                    self.page.update()
                    
                    # Mostra mensagem de sucesso
                    self.page.show_snack_bar(
                        ft.SnackBar(
                            content=ft.Text("Arquivo convertido com sucesso!"),
                            action="OK"
                        )
                    )
                
                self.arquivo_pbit.value = file_path
                self.arquivo_pbit.update()
        except Exception as ex:
            self.page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text(f"Erro ao selecionar arquivo: {str(ex)}"),
                    action="OK"
                )
            )

    def pick_word_template(self, e: ft.FilePickerResultEvent):
        """Manipula a seleção do modelo Word"""
        if e.files and len(e.files) > 0:
            self.modelo_word.value = e.files[0].path
            self.page.update()

    def generate_documentation(self, e):
        """Gera a documentação usando os parâmetros selecionados"""
        if not self.arquivo_pbit.value:
            self.page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("Por favor, selecione o arquivo PBIT/PBIX"),
                    action="OK"
                )
            )
            return

        try:
            # Mostra barra de progresso
            progress = ft.ProgressBar(width=400)
            self.page.add(progress)
            self.page.update()

            # Gera a documentação
            generator = DocumentGenerator()
            output_file = generator.generate(
                self.arquivo_pbit.value,
                self.modelo_word.value if self.modelo_word.value else None
            )

            # Remove a barra de progresso
            self.page.remove(progress)
            self.page.update()

            # Mostra mensagem de sucesso
            self.page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("Documentação gerada com sucesso! Verifique a pasta 'output'"),
                    action="OK"
                )
            )
        except Exception as ex:
            self.page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text(f"Erro ao gerar documentação: {str(ex)}"),
                    action="OK"
                )
            )
