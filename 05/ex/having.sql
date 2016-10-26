SELECT 
  number_of_hh_children Children, 
  AVG(daily_time_secondary_childcare_hh_children/60) 
    AS "Secondary Childcare", 
  COUNT(number_of_hh_children) N
FROM respondents 
GROUP BY number_of_hh_children 
HAVING N > 30;
