SELECT 
  state_code State, 
  AVG(marital_status IN (1, 2)) Married,
  COUNT(marital_status IN (1, 2)) "(N)"
FROM cps 
WHERE 
  marital_status > 0 AND
  age > 20 
GROUP BY State
ORDER BY Married DESC;
