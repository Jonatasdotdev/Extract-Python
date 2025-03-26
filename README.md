# Extrator de Dados do Rol de Procedimentos ANS

## Descrição
Script Python para extração de dados da tabela de Procedimentos e Eventos em Saúde a partir de PDF do Anexo I da ANS.

## Funcionalidades
- Extração de tabelas de múltiplas páginas de PDF
- Conversão para formato CSV
- Substituição de abreviações por descrições completas
- Compactação do arquivo em ZIP

## Requisitos
- Python 3.7+
- Bibliotecas:
  - pandas
  - tabula-py
  - chardet
  - zipfile

## Instalação
```bash
pip install pandas tabula-py chardet
```



## Abreviações Substituídas
- OD: Seg. Odontológica
- AMB: Seg. Ambulatorial
- HCO: Seg. Hospitalar Com Obstetrícia
- HSO: Seg. Hospitalar Sem Obstetrícia
- REF: Plano Referência
- PAC: Procedimento de Alta Complexidade
- DUT: Diretriz de Utilização

## Tratamento de Erros
- Detecção automática de encoding
- Múltiplas estratégias de extração
- Tratamento de exceções em cada etapa
