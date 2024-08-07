select EDO,MUN,PAR,CENTRO, count(MESA) as "MESA/S", sum(EG) as "VOTOS A EDMUNDO", 
sum(NM) as "VOTOS A MADURO",sum(LM) as "VOTOS A LUIS MARTINEZ",sum(AE) as "VOTOS A ECARRI" from resultados    
group by CENTRO
order by sum(AE) desc