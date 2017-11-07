SELECT 
  cps.years_education ed,
  roster.edited_sex sex,
  ROUND(AVG(housework), 2) housework,
  COUNT(housework) "(N)"
FROM (
  SELECT
    case_id,
    SUM((activity_code/10000 = 2) * duration/60.) housework
  FROM
    activities
  GROUP BY case_id
) sum_activities
JOIN cps ON 
  cps.case_id = sum_activities.case_id AND
  cps.line_no = 1
JOIN roster ON
  sum_activities.case_id = roster.case_id AND
  roster.line_no = 1
WHERE 
  edited_age > 20
GROUP BY
  ed, sex
;
