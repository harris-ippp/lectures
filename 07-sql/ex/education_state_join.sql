SELECT 
  state_code,
  AVG(educational_attainment > 42) AS Bachelors
FROM cps
JOIN roster ON
  cps.case_id = roster.case_id AND
  cps.line_no = roster.line_no
WHERE
  educational_attainment > 0 AND /* i.e., defined */
  roster.edited_age > 25
GROUP BY state_code
ORDER BY Bachelors DESC
LIMIT 10;
