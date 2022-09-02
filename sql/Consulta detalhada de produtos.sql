-- Comando para seleção de colunas
SELECT nome, descricao, valor
-- Comando para definir as tabelas que serão envolvidas
FROM produtos
-- A palavra reservada WHERE, defini as restrições na consulta
--   em outras palavra pode-se filtrar o que deseja apresentar
--   como resultado da consulta
WHERE
    -- É necessário a utilização das colunas disponíveis da tabela
    --   definida como fonte de dados da consulta
    -- O filtro acontece com a utilziação de expressões que geram
    --   um resultado lógico com o =, >=, <> ...
    nome = 'Cama'