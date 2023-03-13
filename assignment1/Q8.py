import matplotlib.pyplot as plt
year = [2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012]
no_application_per_year = [921261, 929198, 1043739, 1186454,
1194938, 1304495, 1356805, 1282000, 479651]
plt.scatter(year,no_application_per_year,color="hotpink")
plt.xlabel("year")
plt.ylabel("no of application per year ")
plt.title("Q8")
plt.grid()
plt.show()