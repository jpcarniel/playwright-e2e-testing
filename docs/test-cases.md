# Casos de Teste: The Internet (Herokuapp)

**Autor:** João Paulo Carniel Fonseca
**Data:** 28/03/2026
**Total:** 33 casos de teste

---

## Login

### CT-001: Login com credenciais válidas

**Prioridade:** Alta
**Tipo:** Funcional

**Pré-condições:** Página de login carregada

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Preencher username com "tomsmith" | Campo preenchido |
| 2 | Preencher password com "SuperSecretPassword!" | Campo preenchido |
| 3 | Clicar em "Login" | Redireciona para /secure |
| 4 | Verificar mensagem | "You logged into a secure area!" exibida |

---

### CT-002: Login com username inválido

**Prioridade:** Alta
**Tipo:** Negativo

**Pré-condições:** Página de login carregada

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Preencher username com "invaliduser" | Campo preenchido |
| 2 | Preencher password com "SuperSecretPassword!" | Campo preenchido |
| 3 | Clicar em "Login" | Permanece na página de login |
| 4 | Verificar mensagem | "Your username is invalid!" exibida |

---

### CT-003: Login com password inválido

**Prioridade:** Alta
**Tipo:** Negativo

**Pré-condições:** Página de login carregada

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Preencher username com "tomsmith" | Campo preenchido |
| 2 | Preencher password com "wrongpassword" | Campo preenchido |
| 3 | Clicar em "Login" | Permanece na página de login |
| 4 | Verificar mensagem | "Your password is invalid!" exibida |

---

### CT-004: Login com campos vazios

**Prioridade:** Média
**Tipo:** Negativo

**Pré-condições:** Página de login carregada

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Clicar em "Login" sem preencher campos | Permanece na página de login |
| 2 | Verificar mensagem | "Your username is invalid!" exibida |

---

### CT-005: Logout após login bem-sucedido

**Prioridade:** Alta
**Tipo:** Funcional

**Pré-condições:** Usuário logado em /secure

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Clicar em "Logout" | Redireciona para /login |
| 2 | Verificar mensagem | "You logged out of the secure area!" exibida |

---

## Checkboxes

### CT-006: Estados iniciais dos checkboxes

**Prioridade:** Média
**Tipo:** Funcional

**Pré-condições:** Página de checkboxes carregada

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Verificar primeiro checkbox | Desmarcado |
| 2 | Verificar segundo checkbox | Marcado |

---

### CT-007: Marcar o primeiro checkbox

**Prioridade:** Média
**Tipo:** Funcional

**Pré-condições:** Página de checkboxes carregada

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Clicar no primeiro checkbox | Checkbox marcado |

---

### CT-008: Desmarcar o segundo checkbox

**Prioridade:** Média
**Tipo:** Funcional

**Pré-condições:** Página de checkboxes carregada

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Clicar no segundo checkbox | Checkbox desmarcado |

---

### CT-009: Alternar ambos os checkboxes

**Prioridade:** Baixa
**Tipo:** Funcional

**Pré-condições:** Página de checkboxes carregada

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Clicar no primeiro checkbox | Primeiro marcado |
| 2 | Clicar no segundo checkbox | Segundo desmarcado |

---

## Dropdown

### CT-010: Estado padrão do dropdown

**Prioridade:** Média
**Tipo:** Funcional

**Pré-condições:** Página do dropdown carregada

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Verificar valor selecionado | Nenhuma opção selecionada (valor vazio) |

---

### CT-011: Selecionar Option 1

**Prioridade:** Média
**Tipo:** Funcional

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Selecionar "Option 1" no dropdown | Valor "1" selecionado |

---

### CT-012: Selecionar Option 2

**Prioridade:** Média
**Tipo:** Funcional

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Selecionar "Option 2" no dropdown | Valor "2" selecionado |

---

### CT-013: Trocar seleção de Option 1 para Option 2

**Prioridade:** Baixa
**Tipo:** Funcional

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Selecionar "Option 1" | Valor "1" selecionado |
| 2 | Selecionar "Option 2" | Valor "2" selecionado |

---

## Drag and Drop

### CT-014: Estado inicial das colunas

**Prioridade:** Média
**Tipo:** Funcional

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Verificar header da coluna A | Texto "A" |
| 2 | Verificar header da coluna B | Texto "B" |

---

### CT-015: Arrastar A para B

**Prioridade:** Alta
**Tipo:** Funcional

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Arrastar coluna A para coluna B | Headers trocam (A→B, B→A) |

---

### CT-016: Arrastar de volta para posição original

**Prioridade:** Baixa
**Tipo:** Funcional

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Arrastar A para B | Headers trocam |
| 2 | Arrastar B de volta para A | Headers voltam ao original |

---

## Dynamic Loading

### CT-017: Elemento oculto exibido após carregamento (Exemplo 1)

**Prioridade:** Alta
**Tipo:** Funcional

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Clicar em "Start" | Loading indicator aparece |
| 2 | Aguardar carregamento | Texto "Hello World!" visível |

---

### CT-018: Elemento renderizado após carregamento (Exemplo 2)

**Prioridade:** Alta
**Tipo:** Funcional

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Clicar em "Start" | Loading indicator aparece |
| 2 | Aguardar carregamento | Texto "Hello World!" visível |

---

## File Upload

### CT-019: Upload de arquivo com sucesso

**Prioridade:** Alta
**Tipo:** Funcional

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Selecionar arquivo test-upload.txt | Arquivo selecionado |
| 2 | Clicar em "Upload" | Nome do arquivo exibido na tela |

---

### CT-020: Submissão sem arquivo selecionado

**Prioridade:** Média
**Tipo:** Negativo

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Clicar em "Upload" sem selecionar arquivo | Mensagem de erro exibida |

---

## Hovers

### CT-021: Hover no primeiro avatar

**Prioridade:** Média
**Tipo:** Funcional

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Hover sobre o primeiro avatar | Nome "user1" visível |

---

### CT-022: Hover no segundo avatar

**Prioridade:** Média
**Tipo:** Funcional

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Hover sobre o segundo avatar | Nome "user2" visível |

---

### CT-023: Hover no terceiro avatar

**Prioridade:** Média
**Tipo:** Funcional

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Hover sobre o terceiro avatar | Nome "user3" visível |

---

### CT-024: Links de perfil corretos

**Prioridade:** Média
**Tipo:** Funcional

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Hover sobre cada avatar | Links apontam para /users/1, /users/2, /users/3 |

---

## Key Presses

### CT-025: Pressionar tecla de letra

**Prioridade:** Média
**Tipo:** Funcional

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Pressionar tecla "A" | Resultado exibe "You entered: A" |

---

### CT-026: Pressionar tecla Space

**Prioridade:** Baixa
**Tipo:** Funcional

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Pressionar tecla Space | Resultado exibe "You entered: SPACE" |

---

### CT-027: Pressionar tecla Tab

**Prioridade:** Baixa
**Tipo:** Funcional

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Pressionar tecla Tab | Resultado exibe "You entered: TAB" |

---

### CT-028: Pressionar tecla Escape

**Prioridade:** Baixa
**Tipo:** Funcional

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Pressionar tecla Escape | Resultado exibe "You entered: ESCAPE" |

---

## JavaScript Alerts

### CT-029: Aceitar JS Alert

**Prioridade:** Alta
**Tipo:** Funcional

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Clicar em "Click for JS Alert" | Alert exibido |
| 2 | Aceitar alert | Resultado: "You successfully clicked an alert" |

---

### CT-030: Aceitar JS Confirm

**Prioridade:** Alta
**Tipo:** Funcional

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Clicar em "Click for JS Confirm" | Confirm exibido |
| 2 | Clicar "OK" | Resultado: "You clicked: Ok" |

---

### CT-031: Cancelar JS Confirm

**Prioridade:** Alta
**Tipo:** Funcional

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Clicar em "Click for JS Confirm" | Confirm exibido |
| 2 | Clicar "Cancel" | Resultado: "You clicked: Cancel" |

---

### CT-032: Inserir texto em JS Prompt e aceitar

**Prioridade:** Alta
**Tipo:** Funcional

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Clicar em "Click for JS Prompt" | Prompt exibido |
| 2 | Digitar "Hello from Playwright" e aceitar | Resultado: "You entered: Hello from Playwright" |

---

### CT-033: Cancelar JS Prompt sem texto

**Prioridade:** Média
**Tipo:** Funcional

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Clicar em "Click for JS Prompt" | Prompt exibido |
| 2 | Clicar "Cancel" | Resultado: "You entered: null" |
