SELECT 
  cps.educational_attainment ed,
  roster.edited_sex sex,
  AVG(housework)
FROM (
  SELECT
    case_id,
    SUM((activity_code/10000 = 2) * duration) housework
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
GROUP BY
  ed, sex
;
