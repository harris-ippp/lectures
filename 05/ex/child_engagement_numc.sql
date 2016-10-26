SELECT 
  number_of_hh_children,
  ROUND(AVG(activities_sum.child_engagement)/60, 2) AS "Child Engagement",
  COUNT(activities_sum.child_engagement) "(N)"
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
  number_of_hh_children
HAVING "(N)" > 20
ORDER BY number_of_hh_children
;

