SELECT sex, COUNT(sex), AVG(time) FROM (
  SELECT
    roster.case_id, AVG(edited_sex) sex,
    SUM((activity_code = 10401) * (duration)) 
      AS time
  FROM roster
  INNER JOIN activities ON 
    roster.case_id = activities.case_id
  WHERE roster.line_no = 1 AND
        18 < edited_age AND edited_age < 45
  GROUP BY roster.case_id
) GROUP BY sex;
