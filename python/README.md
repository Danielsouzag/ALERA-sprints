# ALERA

Motor logico da ALERA em Python: um programa de terminal que simula o sistema de alertas de chuva e a gamificacao comunitaria. Projeto da Sprint 2 (Computational Thinking with Python) do Challenge 2026 da FIAP.

## Integrantes

| Nome | RM |
|------|----|
| Daniel Souza Gomes | 575813 |
| Victor Santos Ferreira de Morais | 575508 |
| Diego Ramos Pereira Gonzalez | 574620 |
| Diego Alejandro Ribeiro Olalla | 575447 |

## Como executar

Precisa do Python 3.10 ou superior (usa `match-case`). Nao usa bibliotecas externas.

```
python alera.py
```

## Funcionalidades

O programa abre com um menu para escolher o perfil.

**Morador**
- ver o alerta do seu bairro, com a orientacao do que fazer
- registrar missoes comunitarias e ganhar pontos
- ver o ranking dos moradores

**Administrador (Defesa Civil)** - senha de teste: `defesa123` (3 tentativas)
- painel de risco de todos os bairros
- registrar uma nova leitura de chuva e do nivel da agua
- relatorio de chuva (total, media, maior e menor por bairro)
- cadastrar morador

## Como o codigo funciona

**Dados**
- `CHUVA` e uma matriz: cada linha e um bairro e cada numero e uma leitura de chuva em mm. A ultima leitura da linha e a mais recente.
- `NIVEL` e uma lista com o nivel da agua (cm) atual de cada bairro, na mesma ordem de `BAIRROS`.
- `MORADORES` e uma lista de listas no formato `[nome, bairro, pontos]`.

**Classificacao de risco**
A funcao `classificar_risco(chuva, nivel)` usa `if/elif/else`. O risco sobe se a chuva ou o nivel da agua passar do limite:

| Risco | Chuva (mm) | Nivel da agua (cm) |
|-------|-----------|--------------------|
| normal | abaixo de 25 | abaixo de 50 |
| atencao | 25 ou mais | 50 ou mais |
| alerta | 50 ou mais | 100 ou mais |
| emergencia | 80 ou mais | 150 ou mais |

A funcao `orientacao(risco, bairro)` usa `match-case` para mostrar o que o morador deve fazer. Em emergencia, a mensagem diz apenas para sair de casa e para qual abrigo ir.

**Menus e validacao**
- Os menus usam `while True` e `match-case`, e sempre voltam ao menu anterior ao final de cada opcao.
- `ler_numero(msg, minimo, maximo)` repete a pergunta ate o usuario digitar um numero valido dentro da faixa, entao uma entrada errada nao encerra o programa.
- A senha do administrador tem 3 tentativas.

**Ranking**
`exibir_ranking()` copia a lista de moradores e ordena por pontos com dois `for` (troca de posicao), sem bibliotecas.
