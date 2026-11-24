# ALERA · Sprints de Front-End Design

**ALERA: Acompanhamento Local de Emergências e Riscos Ambientais.** O alerta de chuva com o nome da sua rua, no seu WhatsApp, para os moradores das áreas de risco de Juiz de Fora (MG).

Este repositório guarda as entregas de **Front-End Design** do Challenge FIAP 2026, sprint por sprint. O projeto completo do ALERA (com back-end) fica em outro repositório.

Grupo **MonkeyNerds**:

| Integrante | RM |
| --- | --- |
| Daniel Souza Gomes | 575813 |
| Victor Santos Ferreira de Morais | 575508 |
| Diego Ramos Pereira Gonzalez | 574620 |
| Diego Alejandro Ribeiro Olalla | 575447 |

## Protótipo publicado

**https://danielsouzag.github.io/ALERA-sprints/**

## Como executar

É só HTML e CSS, sem framework e sem instalação.

**Jeito mais simples:** baixe o repositório (botão verde **Code → Download ZIP**), descompacte e abra o arquivo `index.html` no navegador.

**Com servidor local** (recomendado para testar como no site publicado), na pasta do projeto:

```powershell
python -m http.server 5500
```

e abra `http://localhost:5500`. No VS Code, a extensão **Live Server** faz o mesmo: clique com o botão direito em `index.html` > **Open with Live Server**.

## Estrutura

```
index.html            Site de apresentação (Sprint 1)
app/                  Telas do app e do painel (Sprint 2: uma página por tela)
css/tokens.css        Design system: cores, fontes, tamanhos, espaços, cantos, sombras
css/site.css          Estilo do site
css/app.css           Estilo do app e componentes com seus estados
img/                  Fotos do site
docs/sprint1/         Design System v0.1 (PDF) e integrantes
docs/sprint2/         Fluxos, componentes por página, fluxograma e roteiro do vídeo
```

## Sprint 1 · Design System v0.1

Moodboard, referências, fluxos, tokens e componentes base: [`docs/sprint1/ALERA_FrontEnd_DesignSystem_Sprint1.pdf`](docs/sprint1/ALERA_FrontEnd_DesignSystem_Sprint1.pdf).
O código exatamente como foi entregue na Sprint 1 está marcado com a tag `sprint1` (aba **Tags** do GitHub).

## Sprint 2 · Protótipo navegável dos 3 fluxos

Os 3 fluxos que a Sprint 1 definiu, agora navegáveis no navegador:

| Fluxo | Começa em | Telas |
| --- | --- | --- |
| 1 · Morador recebe um alerta (principal) | Site → **Testar o app** | Cadastro → Cadastro feito → Alerta → Rota segura → Abrigo salvo |
| 2 · Gamificação | App → aba **Missões** | Missões → Limpe o bueiro → Missão enviada → Ranking |
| 3 · Defesa Civil | Rodapé → **Painel da Defesa Civil** | Painel → Confirmar alerta → Alerta disparado |

- Fluxos, componentes por página e fluxograma: [`docs/sprint2/FLUXOS.md`](docs/sprint2/FLUXOS.md)
- Componentes com os 6 estados (default, hover, focus, active, disabled, error): [`app/componentes.html`](app/componentes.html)
- Roteiro do vídeo: [`docs/sprint2/ROTEIRO-VIDEO.md`](docs/sprint2/ROTEIRO-VIDEO.md)

Os formulários usam a validação do próprio HTML: o erro aparece embaixo do campo depois que a pessoa mexe nele, e o envio fica bloqueado até corrigir. Nenhum dado é enviado ou guardado: é um protótipo.
