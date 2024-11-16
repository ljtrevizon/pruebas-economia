select EDO,sum(VOTOS_VALIDOS) as "VOTOS_TOTALES", sum(EG) as "EG", 
sum(NM) as "NM",sum(LM) as "LM",sum(JOBR) as "JOBR",
sum(JABE) as "JABE",sum(BERA) as "BERA",sum(CF) as "CF",sum(DC) as "DC",sum(EM) as "EM",sum(AE) as "AE" from resultados    
group by EDO