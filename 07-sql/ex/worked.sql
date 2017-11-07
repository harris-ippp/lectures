SELECT 
  years_education,
  AVG(worked_last_week = 1) Worked
FROM 
  respondents
JOIN 
  cps
ON 
  respondents.case_id = cps.case_id AND
  cps.line_no = 1
GROUP BY
  years_education
;
