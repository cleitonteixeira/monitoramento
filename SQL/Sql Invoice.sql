SELECT
DISTINCT(bp.NRLANBOLPAG), f.NRINSJURFORN, f.NMRAZSOCFORN, fl.NMFILIAL, fl.CDFILIAL, bp.DTVENBOLPAG, cf.DSCLASSFINA, VRBOLPAG AS "VALOR"
FROM BOLETPAGAR bp
INNER JOIN FORNECEDOR f ON f.CDFORNECED = bp.CDFORNECED
INNER JOIN FILIAL fl ON fl.CDFILIAL = bp.CDFILIAL
INNER JOIN CONTAPAGAR cp ON cp.NRLANBOLPAG = bp.NRLANBOLPAG AND cp.DTATUAVENPAG = bp.DTVENBOLPAG
INNER JOIN CLASSFINANC cf ON cf.CDCLASSFINA = cp.CDCLASSFINA
WHERE bp.DTVENBOLPAG BETWEEN '18/10/2024' AND '18/10/2024' AND bp.CDFORNECED NOT LIKE 'J10560908%'
ORDER BY f.NMRAZSOCFORN