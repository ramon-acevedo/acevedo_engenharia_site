from flask import Blueprint, render_template, request

# Blueprints
main_bp = Blueprint('main', __name__)

# ==================== ROTAS PRINCIPAIS ====================

@main_bp.route('/')
def index():
    """Página inicial"""
    return render_template('index.html')

@main_bp.route('/servicos')
def servicos():
    """Página de serviços"""
    return render_template('index.html')

@main_bp.route('/sobre')
def sobre():
    """Página sobre"""
    return render_template('index.html')

@main_bp.route('/contato')
def contato():
    """Página de contato"""
    return render_template('index.html')

# ==================== ERROR HANDLERS ====================

@main_bp.errorhandler(404)
def page_not_found(error):
    """Página não encontrada"""
    return render_template('404.html'), 404

@main_bp.errorhandler(500)
def internal_error(error):
    """Erro interno do servidor"""
    return render_template('500.html'), 500
