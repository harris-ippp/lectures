SELECT 
  state_code,
  AVG(educational_attainment > 42) AS Bachelors
FROM cps
WHERE
  educational_attainment > 0 /* i.e., defined */
GROUP BY state_code
ORDER BY Bachelors DESC
LIMIT 10;
