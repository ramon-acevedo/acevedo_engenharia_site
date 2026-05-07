# Guia de Instalação Rápida - Acevedo Engenharia Flask

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes)
- Git (opcional)

## 🚀 Instalação em 5 Passos

### Passo 1: Extrair o arquivo ZIP

```bash
unzip acevedo_engenharia_flask.zip
cd acevedo_flask
```

### Passo 2: Criar ambiente virtual

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### Passo 3: Instalar dependências

```bash
pip install -r requirements.txt
```

### Passo 4: Executar a aplicação

```bash
python run.py
```

Você verá uma mensagem como:
```
============================================================
Acevedo Engenharia - Flask Application
============================================================
Environment: development
Debug Mode: True
Server: http://0.0.0.0:5000
============================================================
```

### Passo 5: Acessar o site

Abra seu navegador e acesse: **http://localhost:5000**

## 📊 Acessar o Painel Administrativo

O painel administrativo está em: **http://localhost:5000/admin/dashboard**

### Funcionalidades do Admin:
- **Dashboard:** Estatísticas gerais e resumo
- **Mensagens:** Todas as mensagens de contato recebidas
- **Analytics:** Dados detalhados de visitantes
- **Visitantes:** Lista de sessões e usuários

## 🗄️ Banco de Dados

O banco de dados SQLite é criado automaticamente na primeira execução:
- Arquivo: `acevedo.db`
- Tabelas: contacts, page_views, user_sessions, analytics

## 🔧 Configurações

Edite o arquivo `.env` para alterar:

```env
FLASK_ENV=development          # Mude para 'production' em produção
FLASK_DEBUG=True              # Mude para 'False' em produção
FLASK_HOST=0.0.0.0            # Host do servidor
FLASK_PORT=5000               # Porta do servidor
SECRET_KEY=sua-chave-secreta  # Altere em produção
```

## 📁 Estrutura de Arquivos

```
acevedo_flask/
├── app/                       # Código da aplicação
│   ├── templates/            # Arquivos HTML
│   ├── static/               # CSS, JS e imagens
│   ├── models.py             # Modelos de banco de dados
│   ├── routes.py             # Rotas da aplicação
│   └── utils.py              # Funções utilitárias
├── config.py                 # Configurações
├── run.py                    # Script para executar
├── requirements.txt          # Dependências
└── README.md                 # Documentação completa
```

## 🌐 Deployment (Hospedagem)

### Heroku

1. Instale Heroku CLI
2. Crie arquivo `Procfile`:
   ```
   web: gunicorn run:app
   ```
3. Deploy:
   ```bash
   heroku create seu-app-name
   git push heroku main
   ```

### PythonAnywhere

1. Crie conta em pythonanywhere.com
2. Upload dos arquivos
3. Configure web app com Python 3.x
4. Aponte WSGI para `app:app`

### Servidor Linux

1. Instale Python e dependências
2. Configure Nginx como reverse proxy
3. Use Supervisor para gerenciar o processo
4. Configure SSL com Let's Encrypt

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'flask'"

```bash
pip install -r requirements.txt
```

### Erro: "Address already in use"

Use uma porta diferente:
```bash
FLASK_PORT=8000 python run.py
```

### Erro: "Database is locked"

Reinicie a aplicação (Ctrl+C e execute novamente)

## 📞 Suporte

- **Telefone:** (48) 99948-8177
- **E-mail:** acevedoengenharia@gmail.com

## ✅ Checklist de Verificação

- [ ] Python 3.8+ instalado
- [ ] Arquivo ZIP extraído
- [ ] Ambiente virtual criado e ativado
- [ ] Dependências instaladas
- [ ] Aplicação rodando em http://localhost:5000
- [ ] Painel admin acessível em http://localhost:5000/admin/dashboard
- [ ] Formulário de contato funcionando
- [ ] Analytics registrando visitantes

## 🎉 Pronto!

Seu site está funcionando! Agora você pode:

1. **Personalizar:** Edite templates em `app/templates/`
2. **Estilizar:** Modifique CSS em `app/static/css/style.css`
3. **Adicionar funcionalidades:** Crie novas rotas em `app/routes.py`
4. **Hospedar:** Faça deploy em um servidor

---

**Desenvolvido com ❤️ usando Python e Flask**
