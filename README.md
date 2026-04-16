![CI](https://github.com/jpcarniel/playwright-e2e-testing/actions/workflows/playwright.yml/badge.svg)

# Playwright E2E Testing

Projeto de automação de testes end-to-end para o [The Internet](https://the-internet.herokuapp.com) usando Playwright com Python e pytest.

## O que é testado

| Funcionalidade | Testes |
|----------------|--------|
| Login | Credenciais válidas/inválidas, logout |
| Checkboxes | Estados iniciais, toggle |
| Dropdown | Seleção, troca de opções |
| Drag and Drop | Arrastar entre colunas |
| Dynamic Loading | Elementos ocultos e renderizados |
| File Upload | Upload válido, submissão vazia |
| Hovers | Tooltip em avatares, links de perfil |
| Key Presses | Detecção de teclas |
| JavaScript Alerts | Alert, confirm, prompt |

## Stack

- [Playwright for Python](https://playwright.dev/python/) — framework de automação
- [pytest](https://docs.pytest.org/) — test runner
- [pytest-playwright](https://github.com/microsoft/playwright-pytest) — integração Playwright + pytest
- Python 3.12+
- Chromium (headless)
- GitHub Actions (CI)

## Como executar

```bash
# Criar e ativar virtual environment
python -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Instalar browser
python -m playwright install chromium

# Rodar todos os testes
python -m pytest -v

# Rodar teste específico
python -m pytest tests/test_login.py -v
python -m pytest tests/test_checkboxes.py -v
python -m pytest tests/test_dropdown.py -v
python -m pytest tests/test_drag_and_drop.py -v
python -m pytest tests/test_dynamic_loading.py -v
python -m pytest tests/test_file_upload.py -v
python -m pytest tests/test_hovers.py -v
python -m pytest tests/test_key_presses.py -v
python -m pytest tests/test_javascript_alerts.py -v

# Rodar com browser visível
python -m pytest -v --headed

# Rodar com traces em falhas
python -m pytest -v --tracing=retain-on-failure
```

## Estrutura do projeto

```
playwright-e2e-testing/
├── .github/workflows/     # CI com GitHub Actions
├── docs/                  # Plano de testes, casos de teste, bug reports
├── fixtures/              # Arquivos de teste (upload)
├── pages/                 # Page Objects
│   ├── checkboxes_page.py
│   ├── drag_and_drop_page.py
│   ├── dropdown_page.py
│   ├── dynamic_loading_page.py
│   ├── file_upload_page.py
│   ├── hovers_page.py
│   ├── javascript_alerts_page.py
│   ├── key_presses_page.py
│   └── login_page.py
├── tests/                 # Arquivos de teste
│   ├── test_checkboxes.py
│   ├── test_drag_and_drop.py
│   ├── test_dropdown.py
│   ├── test_dynamic_loading.py
│   ├── test_file_upload.py
│   ├── test_hovers.py
│   ├── test_javascript_alerts.py
│   ├── test_key_presses.py
│   └── test_login.py
├── conftest.py            # Fixtures pytest (page objects, browser setup)
├── pytest.ini             # Configuração do pytest
└── requirements.txt       # Dependências Python
```

## Arquitetura

- **Page Object Model:** Cada página testada tem seu próprio Page Object com seletores e ações encapsulados
- **Fixtures pytest:** Page Objects injetados como fixtures, browser gerenciado por pytest-playwright
- **Auto-waiting:** Playwright aguarda elementos automaticamente, sem sleeps explícitos
- **snake_case:** Convenção Python em todo o código

## Documentação

- [Plano de Testes](docs/test-plan.md) — escopo, estratégia, riscos
- [Casos de Teste](docs/test-cases.md) — 33 casos detalhados
- [Bug Reports](docs/bug-reports.md) — bugs encontrados durante os testes
- [Material de Estudo (GitHub Pages)](https://jpcarniel.github.io/playwright-e2e-testing/) — guia completo de QA com Playwright
