import sys
from pathlib import Path

# Permite importar modulos del directorio raiz del ejercicio al correr pytest.
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
