# Acevedo Engenharia - Site em Flask

Site profissional para Acevedo Engenharia - Projetos Complementares de Combate a Incêndio, desenvolvido em Python com Flask.

## Características

- **Frontend Responsivo:** Design adaptável para desktop, tablet e mobile
- **Banco de Dados SQLite:** Armazenamento de mensagens de contato
- **Analytics Detalhado:** Rastreamento completo de visitantes e comportamento
- **Painel Administrativo:** Dashboard para gerenciar mensagens e visualizar estatísticas
- **Formulário de Contato:** Integrado com validação e armazenamento
- **SEO Otimizado:** Meta tags e estrutura semântica

## Requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)

## Instalação

### 1. Clonar o repositório

```bash
git clone <seu-repositorio>
cd acevedo_flask
```

### 2. Criar ambiente virtual

```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

O arquivo `.env` já está configurado para desenvolvimento. Para produção, altere:

```bash
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=sua-chave-secreta-aqui
```

### 5. Executar a aplicação

```bash
python run.py
```

A aplicação estará disponível em `http://localhost:5000`

## Estrutura do Projeto

```
acevedo_flask/
├── app/
│   ├── __init__.py          # Inicialização da aplicação
│   ├── models.py            # Modelos de banco de dados
│   ├── routes.py            # Rotas e endpoints
│   ├── utils.py             # Funções utilitárias
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css    # Estilos CSS
│   │   ├── js/
│   │   │   └── main.js      # JavaScript
│   │   └── images/          # Imagens
│   └── templates/
│       ├── base.html        # Template base
│       ├── index.html       # Página inicial
│       ├── 404.html         # Página 404
│       └── admin/           # Templates administrativos
├── config.py                # Configurações
├── run.py                   # Script para executar
├── requirements.txt         # Dependências
├── .env                     # Variáveis de ambiente
└── README.md               # Este arquivo
```

## Funcionalidades

### Página Principal

- Hero section com chamada para ação
- Seção de serviços (6 serviços principais)
- Seção sobre a empresa
- Formulário de contato
- Footer com informações

### Banco de Dados

**Tabelas:**
- `contacts` - Mensagens de contato
- `page_views` - Visualizações de página
- `user_sessions` - Sessões de usuários
- `analytics` - Estatísticas gerais

### API Endpoints

#### Públicos
- `GET /` - Página inicial
- `POST /api/contato` - Enviar mensagem de contato
- `GET /api/analytics/summary` - Resumo de analytics
- `GET /api/analytics/detailed` - Analytics detalhado

#### Administrativos (em `/admin`)
- `GET /admin/dashboard` - Dashboard principal
- `GET /admin/mensagens` - Lista de mensagens
- `GET /admin/mensagens/<id>` - Visualizar mensagem
- `GET /admin/analytics` - Página de analytics
- `GET /admin/visitantes` - Lista de visitantes
- `POST /admin/api/mensagens/<id>/marcar-lida` - Marcar como lida
- `DELETE /admin/api/mensagens/<id>/deletar` - Deletar mensagem

## Deployment

### Heroku

1. Instale o Heroku CLI
2. Crie um arquivo `Procfile`:
   ```
   web: gunicorn run:app
   ```
3. Instale gunicorn:
   ```
   pip install gunicorn
   ```
4. Deploy:
   ```
   heroku create seu-app-name
   heroku config:set FLASK_ENV=production
   git push heroku main
   ```

### PythonAnywhere

1. Crie uma conta em pythonanywhere.com
2. Upload dos arquivos via Git ou interface web
3. Configure um novo web app com Python 3.x
4. Configure o WSGI para apontar para `app:app`

### Servidor Linux (Ubuntu/Debian)

1. Instale dependências:
   ```bash
   sudo apt-get install python3-pip python3-venv nginx supervisor
   ```

2. Configure Nginx como reverse proxy
3. Use Supervisor para gerenciar o processo Flask
4. Configure SSL com Let's Encrypt

## Desenvolvimento

### Criar nova página

1. Crie um template em `app/templates/`
2. Adicione a rota em `app/routes.py`
3. Estile com CSS em `app/static/css/style.css`

### Adicionar novo modelo

1. Defina o modelo em `app/models.py`
2. Execute `python` e:
   ```python
   from app import create_app
   from app.models import db
   app = create_app()
   with app.app_context():
       db.create_all()
   ```

## Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'flask'"

Certifique-se de que o ambiente virtual está ativado e as dependências foram instaladas:
```bash
pip install -r requirements.txt
```

### Erro: "Database is locked"

Reinicie a aplicação:
```bash
# Ctrl+C para parar
python run.py
```

### Porta 5000 já está em uso

Use uma porta diferente:
```bash
FLASK_PORT=8000 python run.py
```

## Segurança

- Altere `SECRET_KEY` em produção
- Use HTTPS em produção
- Valide todos os inputs do usuário
- Mantenha as dependências atualizadas

## Contribuindo

1. Crie uma branch para sua feature
2. Commit suas mudanças
3. Push para a branch
4. Abra um Pull Request

## Licença

Todos os direitos reservados © 2024 Acevedo Engenharia

## Suporte

Para dúvidas ou problemas, entre em contato:
- **Telefone:** (48) 99948-8177
- **E-mail:** acevedoengenharia@gmail.com

---

**Desenvolvido com ❤️ usando Python e Flask**
