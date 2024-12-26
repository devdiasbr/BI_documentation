# Power BI Documentator

Uma ferramenta com interface gráfica moderna para gerar documentação automatizada de relatórios Power BI.

## Descrição

O Power BI Documentator é uma aplicação desktop que automatiza a criação de documentação técnica para relatórios Power BI. Com uma interface intuitiva e responsiva, o programa extrai informações detalhadas do seu relatório e gera um documento Word organizado e profissional.

## Funcionalidades

- Interface gráfica moderna e responsiva
- Tema claro/escuro
- Extração automática de:
  - Páginas do relatório
  - Tabelas e colunas
  - Medidas DAX
  - Fontes de dados
  - Relacionamentos
- Feedback visual em tempo real
- Tratamento de erros robusto
- Logging detalhado

## Estrutura do Projeto

```
BI_documentation/
├── output/               # Documentos gerados
├── Report/              # Arquivos do Power BI
├── src/                 # Código fonte
│   ├── core/           # Lógica principal
│   │   └── document_generator.py
│   ├── ui/             # Interface do usuário
│   │   ├── components/ # Componentes da UI
│   │   │   └── main_window.py
│   │   └── app.py
│   └── utils/          # Utilitários
│       └── config.py
├── templates/          # Modelos de documento
├── main.py            # Ponto de entrada
└── requirements.txt   # Dependências
```

## Como Usar

1. **Pré-requisitos**
   - Python 3.8 ou superior
   - Power BI Desktop

2. **Instalação**
   ```bash
   # Clone o repositório
   git clone https://github.com/seu-usuario/BI_documentation.git
   cd BI_documentation

   # Instale as dependências
   pip install -r requirements.txt
   ```

3. **Preparação do Arquivo**
   - Abra seu relatório no Power BI Desktop
   - Vá em Arquivo > Exportar > Modelo do Power BI
   - Salve o arquivo .pbit

4. **Execução**
   ```bash
   python main.py
   ```

5. **Na Interface**
   - Selecione o arquivo .pbit
   - Escolha um modelo Word
   - Selecione o diretório de saída
   - Clique em "Gerar Documentação"

## Tecnologias

- **Python 3.8+**: Linguagem principal
- **Flet**: Framework para interface gráfica
- **python-docx**: Geração de documentos Word
- **pathlib**: Manipulação de caminhos
- **logging**: Sistema de logs

## Personalização

O projeto suporta personalização através de:
- Modelos Word customizados
- Configurações em `src/utils/config.py`
- Temas claro/escuro

## Contribuindo

1. Fork o projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Créditos

Desenvolvido por [Bruno Dias](https://github.com/devdiasbr)

---

**Nota**: Para sugestões, bugs ou contribuições, por favor abra uma issue no GitHub.
