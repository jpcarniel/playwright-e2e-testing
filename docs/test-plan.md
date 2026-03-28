# Plano de Testes: The Internet (Herokuapp)

**Autor:** João Paulo Carniel Fonseca
**Data:** 28/03/2026
**Versão:** 1.0

---

## Objetivo

Validar funcionalidades UI do site The Internet (the-internet.herokuapp.com) usando Playwright, cobrindo formulários, elementos dinâmicos, interações de mouse/teclado e diálogos JavaScript.

---

## Escopo

### Dentro do escopo

| Funcionalidade | Descrição |
|----------------|-----------|
| Login | Autenticação com credenciais válidas/inválidas, logout |
| Checkboxes | Estados iniciais, toggle de checkboxes |
| Dropdown | Seleção de opções, troca de seleção |
| Drag and Drop | Arrastar elementos entre colunas |
| Dynamic Loading | Elementos ocultos e renderizados após carregamento |
| File Upload | Upload de arquivo, submissão sem arquivo |
| Hovers | Ações de hover em avatares, links de perfil |
| Key Presses | Detecção de teclas pressionadas |
| JavaScript Alerts | Alerts, confirms e prompts do JavaScript |

### Fora do escopo

- Testes de performance
- Testes de responsividade/mobile
- Testes de acessibilidade (a11y)
- Testes de API
- Testes em múltiplos browsers (apenas Chromium)

---

## Ambiente de testes

| Item | Detalhe |
|------|---------|
| URL | https://the-internet.herokuapp.com |
| Browser | Chromium (via Playwright) |
| CI | GitHub Actions (Ubuntu latest) |
| Local | macOS, Python 3.12+ |
| Framework | pytest + pytest-playwright |

---

## Critérios de entrada

- Site disponível e acessível
- Playwright e dependências instalados
- Todas as páginas testadas acessíveis via navegação

## Critérios de saída

- Todos os casos de teste executados
- Taxa de aprovação >= 95%
- Bugs encontrados documentados
- Relatório de testes gerado

---

## Estratégia de testes

- **Padrão:** Page Object Model (POM)
- **Runner:** pytest com pytest-playwright
- **CI/CD:** GitHub Actions com execução automática a cada push/PR
- **Relatório:** pytest terminal output + trace on failure
- **Screenshots:** Apenas em falhas
- **Retry:** 1 tentativa em CI, 0 localmente

---

## Riscos

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| Site fora do ar | Baixa | Alto | Retry no CI, monitorar status |
| Seletores mudarem | Média | Médio | Page Objects centralizam seletores |
| Drag-and-drop flaky | Alta | Baixo | Workaround com JavaScript nativo |
| Dynamic loading timeout | Baixa | Médio | Auto-waiting do Playwright |
