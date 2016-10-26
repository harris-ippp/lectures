SELECT 
  respondents.case_id,
  cps.years_education AS 'Parental Education', 
  SUM((activity_code/100 IN (301, 302, 303)) * duration/60.) 
    AS 'Direct Engagement'
FROM respondents
INNER JOIN cps ON 
  respondents.case_id = cps.case_id AND 
  respondents.line_no = cps.line_no
INNER JOIN activities ON
  respondents.case_id = activities.case_id
WHERE
  number_of_hh_children > 0 AND
  edited_labor_force_status < 3
GROUP BY respondents.case_id;
