import uuid
from user_agents import parse
from datetime import datetime, timedelta
from app.models import db, PageView, UserSession, Analytics, Contact
from sqlalchemy import func, distinct
import json

def get_client_ip(request):
    """Obtém o IP do cliente, considerando proxies"""
    if request.environ.get('HTTP_CF_CONNECTING_IP'):
        return request.environ.get('HTTP_CF_CONNECTING_IP')
    elif request.environ.get('HTTP_X_FORWARDED_FOR'):
        return request.environ.get('HTTP_X_FORWARDED_FOR').split(',')[0]
    else:
        return request.remote_addr

def parse_user_agent(user_agent_string):
    """Parse user agent string para extrair informações"""
    ua = parse(user_agent_string)
    
    # Determinar tipo de dispositivo
    if ua.is_mobile:
        device_type = 'mobile'
    elif ua.is_tablet:
        device_type = 'tablet'
    else:
        device_type = 'desktop'
    
    return {
        'device_type': device_type,
        'browser': str(ua.browser.family),
        'os': str(ua.os.family),
        'is_bot': ua.is_bot
    }

def generate_session_id():
    """Gera um ID único de sessão"""
    return str(uuid.uuid4())

def track_page_view(request, page_name):
    """Registra uma visualização de página"""
    ip_address = get_client_ip(request)
    user_agent_string = request.headers.get('User-Agent', '')
    referrer = request.referrer
    session_id = request.cookies.get('session_id')
    
    # Parse user agent
    ua_info = parse_user_agent(user_agent_string)
    
    # Criar ou atualizar sessão
    if not session_id:
        session_id = generate_session_id()
    
    user_session = UserSession.query.filter_by(session_id=session_id).first()
    
    if user_session:
        user_session.last_visit = datetime.utcnow()
        user_session.page_count += 1
    else:
        user_session = UserSession(
            session_id=session_id,
            ip_address=ip_address,
            user_agent=user_agent_string,
            device_type=ua_info['device_type'],
            browser=ua_info['browser'],
            os=ua_info['os']
        )
        db.session.add(user_session)
    
    # Registrar visualização de página
    page_view = PageView(
        page=page_name,
        ip_address=ip_address,
        user_agent=user_agent_string,
        referrer=referrer,
        device_type=ua_info['device_type'],
        browser=ua_info['browser'],
        os=ua_info['os'],
        session_id=session_id
    )
    
    db.session.add(page_view)
    db.session.commit()
    
    return session_id

def get_analytics_summary():
    """Obtém resumo de analytics"""
    today = datetime.utcnow().date()
    
    # Total de visitantes únicos
    unique_visitors = db.session.query(distinct(UserSession.ip_address)).count()
    
    # Total de visualizações de página
    total_page_views = PageView.query.count()
    
    # Total de sessões
    total_sessions = UserSession.query.count()
    
    # Páginas mais visitadas
    top_pages = db.session.query(
        PageView.page,
        func.count(PageView.id).label('count')
    ).group_by(PageView.page).order_by(func.count(PageView.id).desc()).limit(5).all()
    
    # Navegadores mais usados
    top_browsers = db.session.query(
        PageView.browser,
        func.count(PageView.id).label('count')
    ).filter(PageView.browser != None).group_by(PageView.browser).order_by(
        func.count(PageView.id).desc()
    ).limit(5).all()
    
    # Dispositivos mais usados
    top_devices = db.session.query(
        PageView.device_type,
        func.count(PageView.id).label('count')
    ).filter(PageView.device_type != None).group_by(PageView.device_type).order_by(
        func.count(PageView.id).desc()
    ).all()
    
    # Tempo médio de sessão
    avg_session_duration = db.session.query(
        func.avg(UserSession.duration_seconds)
    ).scalar() or 0
    
    # Mensagens de contato
    total_contacts = Contact.query.count()
    unread_contacts = Contact.query.filter_by(read=False).count()
    
    return {
        'unique_visitors': unique_visitors,
        'total_page_views': total_page_views,
        'total_sessions': total_sessions,
        'top_pages': [(page, count) for page, count in top_pages],
        'top_browsers': [(browser, count) for browser, count in top_browsers],
        'top_devices': [(device, count) for device, count in top_devices],
        'avg_session_duration': int(avg_session_duration),
        'total_contacts': total_contacts,
        'unread_contacts': unread_contacts
    }

def get_detailed_analytics():
    """Obtém analytics detalhado com gráficos"""
    # Últimas 30 dias
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    
    # Visualizações por dia
    daily_views = db.session.query(
        func.date(PageView.timestamp).label('date'),
        func.count(PageView.id).label('count')
    ).filter(PageView.timestamp >= thirty_days_ago).group_by(
        func.date(PageView.timestamp)
    ).order_by('date').all()
    
    # Visitantes por dia
    daily_visitors = db.session.query(
        func.date(PageView.timestamp).label('date'),
        func.count(distinct(PageView.ip_address)).label('count')
    ).filter(PageView.timestamp >= thirty_days_ago).group_by(
        func.date(PageView.timestamp)
    ).order_by('date').all()
    
    # Distribuição de dispositivos
    device_distribution = db.session.query(
        PageView.device_type,
        func.count(PageView.id).label('count')
    ).filter(PageView.device_type != None).group_by(PageView.device_type).all()
    
    # Distribuição de navegadores
    browser_distribution = db.session.query(
        PageView.browser,
        func.count(PageView.id).label('count')
    ).filter(PageView.browser != None).group_by(PageView.browser).all()
    
    # Distribuição de SO
    os_distribution = db.session.query(
        PageView.os,
        func.count(PageView.id).label('count')
    ).filter(PageView.os != None).group_by(PageView.os).all()
    
    return {
        'daily_views': [(str(date), count) for date, count in daily_views],
        'daily_visitors': [(str(date), count) for date, count in daily_visitors],
        'device_distribution': [(device, count) for device, count in device_distribution],
        'browser_distribution': [(browser, count) for browser, count in browser_distribution],
        'os_distribution': [(os, count) for os, count in os_distribution]
    }
