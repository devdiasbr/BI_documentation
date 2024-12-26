from pathlib import Path

# Configurações da aplicação
APP_NAME = "Power BI Documentator"
APP_VERSION = "1.0.0"

# Configurações de janela
WINDOW_WIDTH = 850
WINDOW_HEIGHT = 600
WINDOW_MIN_WIDTH = 600

# Diretórios do projeto
PROJECT_ROOT = Path(__file__).parent.parent.parent
TEMPLATES_DIR = PROJECT_ROOT / "templates"
OUTPUT_DIR = PROJECT_ROOT / "output"

# Configurações de log
LOG_FILE = PROJECT_ROOT / "power_bi_doc.log"
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
