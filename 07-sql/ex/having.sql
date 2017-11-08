SELECT 
  number_of_hh_children Children, 
  AVG(daily_time_alone_non_work/60) 
    AS "Alone Time", 
  COUNT(number_of_hh_children) N
FROM respondents 
GROUP BY number_of_hh_children 
HAVING N > 30;
