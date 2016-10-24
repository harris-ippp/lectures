SELECT 
  cps.census_state,
  ROUND(SUM(CASE WHEN cps.educational_attainment >= 43
    THEN final_weight ELSE 0 END
    )/SUM(final_weight), 2) AS "Bachelor's",
  ROUND(SUM(daily_time_alone_non_work * final_weight)/SUM(final_weight)/60, 2) AS "Alone Time",
  ROUND(SUM(total_usual_hours_worked * final_weight)/SUM(final_weight)/60, 1) AS "Hours Worked",
  ROUND(SUM(daily_time_secondary_childcare_own_children * final_weight)/SUM(final_weight)/60, 2) AS "Secondary CC (Own)",
  ROUND(SUM(daily_time_with_family * final_weight)/SUM(final_weight)/60, 2) "Family Time",
  ROUND(SUM(activities_sum.child_engagement * final_weight)/SUM(final_weight)/60, 2) AS "Child Engagement"

FROM
  respondents
INNER JOIN
  cps ON (respondents.case_id = cps.case_id AND respondents.line_no = cps.line_no),
  (SELECT 
    activities.case_id, SUM(CASE WHEN activity_code4 IN (301, 302, 303) THEN duration ELSE 0 END) AS child_engagement 
   FROM activities GROUP BY case_id) 
  AS activities_sum ON (respondents.case_id = activities_sum.case_id)

WHERE
  presence_of_hh_children = 1 AND
  edited_labor_force_status < 3

GROUP BY
  cps.census_state
;

