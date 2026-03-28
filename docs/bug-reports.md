# Bug Reports: The Internet (Herokuapp)

**Autor:** João Paulo Carniel Fonseca
**Data:** 28/03/2026

---

## BUG-001: File upload sem arquivo retorna Internal Server Error

**Severidade:** Média
**Prioridade:** Média
**Status:** Aberto
**Caso de teste relacionado:** CT-020

**Descrição:**
O endpoint de upload (/upload) retorna "Internal Server Error" (HTTP 500) quando o formulário é submetido sem arquivo selecionado. O comportamento esperado seria uma mensagem amigável informando que nenhum arquivo foi selecionado.

**Passos para reproduzir:**

| Passo | Ação | Resultado |
|-------|------|-----------|
| 1 | Acessar /upload | Página de upload carregada |
| 2 | Clicar em "Upload" sem selecionar arquivo | Internal Server Error exibido |

**Resultado esperado:** Mensagem de validação: "No file selected" ou similar

**Resultado real:** Internal Server Error (HTTP 500)

**Ambiente:** The Internet (Herokuapp), Chromium via Playwright

**Observação:** Um erro 500 indica falha no servidor, não validação do lado do cliente. Em produção, isso poderia expor informações sensíveis do servidor e prejudica a experiência do usuário.

---

## BUG-002: Drag and Drop não funciona com eventos nativos do Playwright

**Severidade:** Baixa
**Prioridade:** Baixa
**Status:** Aberto
**Caso de teste relacionado:** CT-015

**Descrição:**
A página de Drag and Drop (/drag_and_drop) utiliza HTML5 Drag and Drop API de forma que não responde aos eventos de mouse sintéticos do Playwright (dragTo). Foi necessário implementar um workaround via JavaScript (DataTransfer API) para simular os eventos corretamente.

**Passos para reproduzir:**

| Passo | Ação | Resultado |
|-------|------|-----------|
| 1 | Acessar /drag_and_drop | Página carregada |
| 2 | Usar page.locator('#column-a').dragTo('#column-b') | Nenhuma mudança visual |
| 3 | Usar page.evaluate() com DataTransfer events | Drag funciona corretamente |

**Resultado esperado:** Drag and drop funcionar com eventos nativos do browser/framework de teste

**Resultado real:** Necessário workaround via JavaScript para disparar eventos HTML5 DnD

**Ambiente:** The Internet (Herokuapp), Chromium via Playwright

**Observação:** Este é um problema conhecido com implementações de HTML5 Drag and Drop. A implementação do site depende exclusivamente de DataTransfer events, que não são disparados por simulações de mouse. Documentado como referência para QAs que encontrarem o mesmo cenário.
