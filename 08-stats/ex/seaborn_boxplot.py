ax = sns.boxplot(data = ipums,
                 x = "EDUC5", y = "INCTOTK",
                 hue = "SEX", linewidth = 2)

ax.get_legend().set_bbox_to_anchor((1.3, 1))
ax.set_ylim(0, 300)
ax.set_ylabel("Income [Thousands]")
ax.set_xlabel("Education")

ax.figure.savefig("income_box.pdf",
                  bbox_inches='tight',
                  pad_inches=0.05)
