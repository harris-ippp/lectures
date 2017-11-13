import statsmodels.formula.api as smf

formula = "np.log(INCTOT) ~ AGE + RACE + EDUC + SEX"
ols = smf.wls(formula = formula, data = ipums,
                        weights = ipums["PERWT"])
model = ols.fit()
model.summary()
