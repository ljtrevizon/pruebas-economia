select EDO,MUN,PAR,CENTRO, count(MESA), sum(EG) as EG, URL from resultados  GROUP by CENTRO order by EG desc