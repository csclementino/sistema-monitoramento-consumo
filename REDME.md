# 🧮 Analisador de Consumo Semanal

Este projeto Python tem como objetivo auxiliar o usuário a mapear e analisar o consumo diário (como de água, energia ou qualquer outro recurso) ao longo de semanas definidas, fornecendo informações como:

- Valores máximos e mínimos de consumo
- Média geral
- Valores abaixo da média

## 📋 Funcionalidades

- Solicita do usuário o número de semanas e dias por semana para monitoramento
- Coleta os valores de consumo para cada dia
- Calcula o valor máximo e mínimo registrado
- Retorna a média geral de consumo
- Lista todos os valores abaixo da média

## 🧠 Como funciona

O programa é estruturado em funções modulares, com uma função `main()` que organiza o fluxo de execução. O usuário interage com o programa por meio do terminal.

### Exemplo de Execução

```bash
Digite quantas semanas: 2
Digite quantos dias na semana: 3
Semana 1:
Digite o consumo para o dia 1: 10
Digite o consumo para o dia 2: 12
Digite o consumo para o dia 3: 9
Semana 2:
Digite o consumo para o dia 1: 15
Digite o consumo para o dia 2: 11
Digite o consumo para o dia 3: 8

Valor Maximo: 15.0 Litros
Valor Minimo: 8.0 Litros
Média de consumo: 10.83 Litros
Valores abaixo da media: [10.0, 9.0, 8.0] Litros
