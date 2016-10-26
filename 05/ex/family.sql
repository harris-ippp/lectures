SELECT 
  cps.state_code,
  ROUND(AVG(cps.educational_attainment >= 43), 2) AS "Bachelor's",
  ROUND(AVG(daily_time_alone)/60, 2) AS "Alone Time",
  ROUND(AVG(total_usual_hours_worked), 1) AS "Hours Worked",
  ROUND(AVG(daily_time_secondary_childcare_hh_or_own_children)/60, 2) AS "Secondary CC (Own)",
  ROUND(AVG(daily_time_with_family)/60, 2) "Family Time",
  ROUND(AVG(activities_sum.child_engagement)/60, 2) AS "Child Engagement",
  ROUND(AVG(spouse_or_partner_present IN (1, 2)), 2) "Two Parents",
  COUNT(cps.educational_attainment) "(N)" 
FROM
  respondents
INNER JOIN cps ON 
  respondents.case_id = cps.case_id AND respondents.line_no = cps.line_no
INNER JOIN (
  SELECT 
    activities.case_id, 
    SUM((activity_code/100 IN (301, 302, 303)) * duration) AS child_engagement 
  FROM 
    activities GROUP BY case_id) 
AS activities_sum ON 
  respondents.case_id = activities_sum.case_id
WHERE
  number_of_hh_children > 0 AND
  edited_labor_force_status < 3
GROUP BY
  cps.state_code
HAVING "(N)" > 20
ORDER BY "Child Engagement"
;
