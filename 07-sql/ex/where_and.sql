SELECT years_education, state_code
FROM cps 
WHERE years_education > 0 AND 
      state_code = 17;
