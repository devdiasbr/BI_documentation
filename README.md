# Power BI Documentation Generator

Uma ferramenta com interface gráfica para gerar documentação técnica automatizada de relatórios Power BI.

Este projeto é uma versão aprimorada do [Power BI Documentation](https://github.com/data-ju/Power_BI_Documentation) originalmente criado por [Julia Cantarelli](https://github.com/data-ju). 

## ✨ Novos Recursos

- Interface gráfica amigável usando Flet
- Seleção de arquivos via interface
- Tema claro/escuro
- Instruções passo a passo integradas
- Feedback visual do progresso
- Melhor tratamento de erros e logging

## 🚀 Como Usar

1. **Pré-requisitos:**
   - Python 3.x instalado
   - Power BI Desktop

2. **Instalação:**
   ```bash
   # Clone o repositório
   git clone https://github.com/devdiasbr/BI_documentation.git
   cd BI_documentation

   # Instale as dependências
   pip install -r requirements.txt
   ```

3. **Preparação do Arquivo Power BI:**
   - Abra seu arquivo .pbix no Power BI Desktop
   - Vá em Arquivo > Exportar > Modelo do Power BI
   - Salve o arquivo .pbit

4. **Execução:**
   ```bash
   python app.py
   ```

5. **Na Interface:**
   - Selecione o arquivo .pbit gerado
   - Escolha um modelo Word para a documentação
   - Selecione o diretório de saída
   - Clique em "Gerar Documentação"

## 📄 Documentação Gerada

O documento final incluirá:
- Páginas do relatório
- Tabelas e colunas
- Medidas DAX
- Fontes de dados
- Relacionamentos entre tabelas

## 🛠️ Tecnologias Utilizadas

- Python
- Flet (Interface Gráfica)
- python-docx (Geração de documentos)
- pandas (Manipulação de dados)

## 📝 Modelo Word

- Um modelo Word padrão é fornecido no repositório
- Você pode usar seu próprio modelo, mantendo os marcadores necessários

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Enviar pull requests

## ⭐ Créditos

Este projeto é baseado no trabalho original de [Julia Cantarelli (data-ju)](https://github.com/data-ju/Power_BI_Documentation), que desenvolveu a versão inicial do script de documentação. Nossa versão adiciona uma interface gráfica e melhorias na usabilidade, mantendo a essência do projeto original.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
Desenvolvido com ❤️ por [Bruno Dias](https://github.com/devdiasbr) | Baseado no trabalho de [Julia Cantarelli](https://github.com/data-ju)
