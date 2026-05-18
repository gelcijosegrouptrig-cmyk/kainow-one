# KAINOW ONE IA 🚀

## Descrição
**KAINOW ONE IA** é um sistema inteligente de desenvolvimento de código que utiliza inteligência artificial para gerar, analisar e melhorar código-fonte. Integrado com Cloudflare Workers e D1 Database.

## 🎯 Funcionalidades

- ✅ **Chat IA** - Conversa interativa sobre desenvolvimento
- ✅ **Geração de Código** - Criar código baseado em descrições
- ✅ **Análise de Código** - Avaliar qualidade e sugestões
- ✅ **Banco de Dados D1** - Armazenar dados de treinamento
- ✅ **API RESTful** - Endpoints para integração
- ✅ **Deploy Automático** - CI/CD com GitHub Actions

## 🏗️ Arquitetura

```
KAINOW ONE IA
├── Backend (Cloudflare Workers)
│   ├── API REST (Hono.js)
│   ├── Chat Handler
│   ├── Code Generator
│   └── Code Analyzer
├── Database (Cloudflare D1 - SQLite)
│   ├── Users
│   ├── Conversations
│   ├── Messages
│   ├── Generated Code
│   ├── Analyzed Code
│   ├── Training Data
│   └── Feedback
└── DevOps
    ├── GitHub Actions
    ├── Automated Testing
    └── Continuous Deployment
```

## 🚀 Quick Start

### Pré-requisitos
- Node.js 18+
- Cloudflare Account
- Wrangler CLI

### Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/gelcijosegrouptrig-cmyk/kainow-one.git
   cd kainow-one
   ```

2. **Configure variáveis de ambiente**
   ```bash
   cp .env.example .env.local
   ```

3. **Instale dependências**
   ```bash
   npm install
   ```

4. **Configure Cloudflare D1**
   ```bash
   wrangler d1 create kainow_one_db
   ```

5. **Execute migrations**
   ```bash
   npm run db:migrate
   ```

6. **Inicie desenvolvimento**
   ```bash
   npm run dev
   ```

## 📊 Banco de Dados

### Tabelas Criadas

1. **users** - Usuários do sistema
2. **conversations** - Conversas com IA
3. **messages** - Mensagens da conversa
4. **code_generated** - Códigos gerados
5. **code_analyzed** - Análises de código
6. **training_data** - Dados do GitHub para treinamento
7. **feedback** - Avaliações dos usuários

## 🚀 Status

**🔄 Em desenvolvimento**

Próximas funcionalidades:
- [ ] Frontend React
- [ ] CLI Tool
- [ ] AI Integration
- [ ] GitHub Scraper
- [ ] Autenticação completa
