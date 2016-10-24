SELECT ID, COUNT(id), AVG(activity) FROM (
  SELECT
    roster.case_id, AVG(edited_sex) id,
    SUM((activity_code = 10401) * (duration)) 
      AS activity
  FROM roster
  INNER JOIN activities ON 
    roster.case_id = activities.case_id
  WHERE roster.line_no = 1 AND
        18 < edited_age AND edited_age < 45
  GROUP BY roster.case_id
) GROUP BY id;
