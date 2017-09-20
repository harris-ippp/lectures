SELECT 
  service,
  AVG(respondents.spouse_or_partner_present = 1) spouse,
  AVG(respondents.spouse_or_partner_present = 2) partner,
  AVG(cps.marital_status IN (4, 5)) "Divorced/Separated",
  AVG(cps.years_education) "Years Education", 
  COUNT(cps.years_education) "(N)"
FROM (
  SELECT
    case_id,
    SUM(activity_code/10000 = 14) > 0 AS service
  FROM 
    activities
  GROUP BY
    case_id
) religion
JOIN cps ON 
  religion.case_id = cps.case_id AND
  cps.line_no = 1
JOIN respondents ON
  religion.case_id = respondents.case_id AND
  respondents.line_no = 1
WHERE
  respondents.number_of_hh_children > 0 AND 
  years_education > 0 AND
  respondents.dow_of_diary_day IN (1, 6, 7)
GROUP BY
  service
;
