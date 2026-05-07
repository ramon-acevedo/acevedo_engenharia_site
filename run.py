#!/usr/bin/env python3
"""
Script para executar a aplicação Flask
"""

import os
from app import create_app
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Criar aplicação
app = create_app(os.environ.get('FLASK_ENV', 'development'))

if __name__ == '__main__':
    # Configurações para desenvolvimento
    debug = os.environ.get('FLASK_DEBUG', True)
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_PORT', 5000))
    
    print(f"\n{'='*60}")
    print(f"Acevedo Engenharia - Flask Application")
    print(f"{'='*60}")
    print(f"Environment: {os.environ.get('FLASK_ENV', 'development')}")
    print(f"Debug Mode: {debug}")
    print(f"Server: http://{host}:{port}")
    print(f"{'='*60}\n")
    
    app.run(
        host=host,
        port=port,
        debug=debug
    )
