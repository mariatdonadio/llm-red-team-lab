import sys
from garak import cli

if __name__ == "__main__":
    # Configuramos los argumentos de forma limpia dentro de Python
    sys.argv = [
        "garak",
        "--model_type", "rest",
        "--model_name", "http://localhost:8000/chat",
        "--probes", "promptinject.HijackHateHumansMini"
    ]
    cli.main()