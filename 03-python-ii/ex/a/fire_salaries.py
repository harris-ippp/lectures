total = 0
for l in open("salaries.csv"):

  if "FIRE" not in l: continue

  sl = l.strip().split(",")
  total += float(sl[4][1:])

print("Total fire salaries:")
print("  ${:.2f}".format(total))
