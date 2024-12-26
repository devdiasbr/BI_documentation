# Power BI Documentator

Uma ferramenta com interface gráfica moderna para gerar documentação automatizada de relatórios Power BI.

<div align="center">

![GitHub](https://img.shields.io/github/license/devdiasbr/BI_documentation)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Flet](https://img.shields.io/badge/flet-latest-green)

</div>

## 📋 Descrição

O Power BI Documentator é uma aplicação desktop que automatiza a criação de documentação técnica para relatórios Power BI. Com uma interface intuitiva e responsiva, o programa extrai informações detalhadas do seu relatório e gera um documento Word organizado e profissional.

## 🚀 Início Rápido

### Usando o Executável (Recomendado)

1. Baixe o arquivo `main.exe` da pasta [dist](dist/)
2. Execute o arquivo clicando duas vezes
3. Selecione seu arquivo .pbit e gere a documentação

### Instalação Manual (Para Desenvolvedores)

```bash
# Clone o repositório
git clone https://github.com/devdiasbr/BI_documentation.git
cd BI_documentation

# Instale as dependências
pip install -r requirements.txt

# Execute o programa
python main.py
```

## ✨ Funcionalidades

- Interface gráfica moderna e responsiva
- Tema claro/escuro automático
- Extração automática de:
  - Páginas do relatório
  - Tabelas e colunas
  - Medidas DAX
  - Fontes de dados
  - Relacionamentos
- Conversão automática de PBIX para PBIT
- Feedback visual em tempo real
- Tratamento de erros robusto
- Logging detalhado
- Geração automática de nomes de arquivo
- Organização automática dos arquivos de saída

## 🏗️ Estrutura do Projeto

```
BI_documentation/
├── dist/                # Executável do programa
├── output/              # Documentos gerados
├── Report/              # Arquivos do Power BI
├── src/                 # Código fonte
│   ├── core/           # Lógica principal
│   │   ├── document_generator.py
│   │   └── smartdoc_sem_ia.py
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

## 📝 Como Usar

1. **Preparação do Arquivo Power BI**
   - Você pode usar tanto arquivos .pbix quanto .pbit
   - Se usar um .pbix, o programa converterá automaticamente para .pbit
   - Ou você pode exportar manualmente:
     - Abra seu relatório no Power BI Desktop
     - Vá em Arquivo > Exportar > Modelo do Power BI
     - Salve o arquivo .pbit

2. **Gerando a Documentação**
   - Abra o programa (executável ou via Python)
   - Clique em "Selecionar Arquivo" e escolha seu .pbit
   - Escolha um modelo Word (opcional)
   - Clique em "Gerar Documentação"
   - O documento será salvo automaticamente na pasta `output/`

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**: Linguagem base
- **Flet**: Framework moderno para UI
- **python-docx**: Manipulação de documentos Word
- **pathlib**: Gerenciamento de arquivos
- **logging**: Sistema de logs

## 🔧 Configurações Avançadas

### Personalização
- **Templates**: Adicione seus modelos Word em `templates/`
- **Configurações**: Ajuste parâmetros em `src/utils/config.py`
- **Temas**: Suporte automático a tema claro/escuro

### Executável
- O arquivo `main.exe` é independente e portátil
- Não requer Python instalado
- Pode ser movido para qualquer local
- Atualizações requerem nova compilação via PyInstaller

## 🤝 Contribuindo

1. Fork o projeto
2. Crie sua Feature Branch (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a Branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

**Bruno Dias**
- GitHub: [@devdiasbr](https://github.com/devdiasbr)
- LinkedIn: [Bruno Dias](https://www.linkedin.com/in/bruno-dias-b195611a7/)

## 🙏 Agradecimentos

Agradecimento especial à [Data-Ju](https://www.youtube.com/@Data-Ju) por compartilhar conhecimento e inspirar este projeto. Este projeto é baseado no tutorial dela disponível em:
- Tutorial YouTube: [Como criar documentação automática para Power BI](https://www.youtube.com/watch?v=QnvdPVVeGpA)
- Projeto Original: [Power_BI_Documentation](https://github.com/data-ju/Power_BI_Documentation)

---

**Nota**: Para sugestões, bugs ou contribuições, por favor abra uma [issue](https://github.com/devdiasbr/BI_documentation/issues) no GitHub.
