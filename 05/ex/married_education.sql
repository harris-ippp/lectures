SELECT 
  educational_attainment, 
  AVG(marital_status IN (1, 2)) Married 
FROM cps 
WHERE educational_attainment > 0 
GROUP BY educational_attainment;
