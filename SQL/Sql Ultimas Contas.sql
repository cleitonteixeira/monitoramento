SELECT
lt.NRLANCCONT, nf.NRNOTAFISC, lt.VRLANCCUST
,lt.CDCONTCTBL, lt.CDCENTCUST,nf.DTENTRSAID, fc.NRINSJURFORN, fc.NMRAZSOCFORN, fl.NMFILIAL
FROM NOTAFISCAL nf
INNER JOIN LANCCCUSTO lt ON lt.NRLANCCONT = nf.NRLANCTBDOC
INNER JOIN FORNECEDOR fc ON fc.CDFORNECED = nf.CDFORNECED
INNER JOIN FILIAL fl ON fl.CDFILIAL = lt.CDCENTCUST
WHERE nf.DTENTRSAID BETWEEN '01/10/2024' AND '17/10/2024' AND nf.IDENTRSAIDOP = 'E' AND lt.VRLANCCUST > '0'
ORDER BY nf.DTENTRSAID DESC, lt.NRLANCCONT DESC