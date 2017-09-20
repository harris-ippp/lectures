SELECT
  educational_attainment,
  AVG(spouse_or_partner_present == 1) Married, 
  COUNT(spouse_or_partner_present == 1) "(N)"
FROM cps
JOIN respondents ON
  cps.case_id = respondents.case_id AND 
  cps.line_no = 1
WHERE
  number_of_hh_children > 0
GROUP BY educational_attainment;
