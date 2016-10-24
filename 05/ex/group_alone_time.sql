SELECT 
  number_of_hh_children,
  AVG(daily_time_alone)
FROM
  respondents
GROUP BY
  number_of_hh_children
;
