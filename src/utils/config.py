from pathlib import Path

# Diretórios do projeto
PROJECT_ROOT = Path(__file__).parent.parent.parent
OUTPUT_DIR = PROJECT_ROOT / "output"
TEMPLATES_DIR = PROJECT_ROOT / "templates"

# Configurações da aplicação
APP_NAME = "Power BI Documentator"
APP_VERSION = "1.0.0"

# Configurações da janela
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_MIN_WIDTH = 600
WINDOW_TITLE = APP_NAME

# Configurações de log
LOG_FILE = PROJECT_ROOT / "power_bi_doc.log"
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
