SELECT 
  number_of_hh_children,
  AVG(daily_time_alone_non_work/60)
FROM
  respondents
GROUP BY
  number_of_hh_children
;
