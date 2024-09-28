import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp


FILE_ADD = "Tarbiat.csv"

df = pd.read_csv(FILE_ADD)
METRO = df.columns[0]
BRT = df.columns[1]

fig1, ax = plt.subplots(1, 1)

plt.hist(df, color=["orange", "blue"], bins=12)

plt.legend([METRO, BRT])
plt.xticks(range(0, 13))
ax.set_xlabel("Pass")
ax.set_ylabel("frequency")
ax.set_title("Histogram")

# Show histogram
plt.show()


# part2
SIZE_DATA = 10000
dist = {}
lam = {}

# metro
fig2, (ax1, ax2) = plt.subplots(1, 2)
lam[METRO] = 3
dist[METRO] = np.random.poisson(lam=lam[METRO], size=10000)
ax1.hist(dist[METRO], rwidth=0.8, color='darkorange', bins=12)
ax1.set_title(f"Poisson with Lamda={lam[METRO]}")
plt.xticks(range(0, 13))

ax2.hist(df[METRO], rwidth=0.8, color='coral', bins=12)
ax2.set_title("Metro")
plt.xticks(range(0, 13))

plt.tight_layout()
plt.show()



# BRT comparing real and estimated graph
fig3, (ax1, ax2) = plt.subplots(1, 2)

# estimated
lam[BRT] = 1
dist[BRT] = np.random.exponential(scale=lam[BRT], size=SIZE_DATA)
ax1.hist(dist[BRT], color='darkblue', rwidth=0.8, bins=12)
ax1.set_title(f"Exponential with Lamda={lam[BRT]}")
plt.xticks(range(0, 13))

# real
ax2.hist(df[BRT], color='blue', rwidth=0.8, bins=8)
ax2.set_title("BRT")
plt.xticks(range(0, 13))
plt.tight_layout()
plt.show()



calculated_lam = {}
calculated_lam[METRO] = df[METRO].mean()
calculated_lam[BRT] = df[BRT].mean()

# METRO comparing real and calculated dist. graph
fig4, (ax3, ax4) = plt.subplots(1, 2)
dist[METRO] = np.random.poisson(lam=calculated_lam[METRO], size=10000)
ax3.hist(dist[METRO], rwidth=0.8, color='darkorange', bins=12)
ax3.set_title(f"Poisson with Lamda={calculated_lam[METRO]}")
plt.xticks(range(0, 13))

# real
ax4.hist(df[METRO], rwidth=0.8, color='coral', bins=12)
ax4.set_title("Metro")
plt.xticks(range(0, 13))

plt.tight_layout()
plt.show()


# BRT comparing real and calculated dist. graph
fig5, (ax3, ax4) = plt.subplots(1, 2)

# estimated
dist[BRT] = np.random.exponential(scale=calculated_lam[BRT], size=SIZE_DATA)
ax3.hist(dist[BRT], color='darkblue', rwidth=0.8, bins=12)
ax3.set_title(f"Exponential with Lamda={calculated_lam[BRT]}")
plt.xticks(range(0, 13))

# real
ax4.hist(df[BRT], color='blue', rwidth=0.8, bins=8)
ax4.set_title("BRT")
plt.xticks(range(0, 13))
plt.tight_layout()
plt.show()



# part3
fig6, ax5 = plt.subplots(1,1)
ax5.hist(df[METRO], bins=12, density=True, rwidth=0.8, color="darkgreen")
ax5.set_xlabel("passes")
ax5.set_ylabel("density")
plt.show()



# part4
# X
X_dist = sp.poisson(mu=calculated_lam[METRO])
x_chart = np.arange(0, 12, 1)
y_chart = sp.poisson.pmf(x_chart, mu=calculated_lam[METRO])
plt.plot(x_chart, y_chart, label=f"X ~ poisson({calculated_lam[METRO]})")
# metro
plt.hist(df[METRO], rwidth=0.8, color='coral', bins=12, density=True, label="Metro")
plt.xticks(range(0, 13))

plt.legend()
plt.show()



# part6
# Z distribution
lam_z = calculated_lam[METRO] + calculated_lam[BRT]
x_zchart = np.arange(0, 13, 1)
y_zchart = sp.poisson.pmf(x_zchart, mu=lam_z)
plt.plot(x_zchart, y_zchart, label=f"Z ~ poisson({lam_z})")
# metro + brt
sums = df.sum(axis=1)
sum_df = pd.DataFrame(sums, columns=['Sums'])
plt.hist(sum_df, rwidth=0.8, color='coral', bins=19, density=True, label="Metro+Brt")
plt.xticks(range(0, 13))

plt.legend()
plt.show()



# part7
lam_x = calculated_lam[METRO]
lam_y = calculated_lam[BRT]
lam_z = lam_x + lam_y
N = 8
x_zchart = np.arange(0, 13, 1)
y_zchart = sp.binom.pmf(x_zchart, N, lam_x / lam_z)
plt.plot(x_zchart, y_zchart, label=f"W ~ Bin({N}, {lam_x / lam_z})")

plt.legend()
plt.show()



# part8
lam_x = calculated_lam[METRO]
lam_y = calculated_lam[BRT]
lam_z = lam_x + lam_y
N = 8
x_zchart = np.arange(0, 10, 1)
y_zchart = sp.binom.pmf(x_zchart, N, lam_x / lam_z)
plt.plot(x_zchart, y_zchart, label=f"W ~ Bin({N}, {lam_x / lam_z})")

conditioned_df = df[(df[METRO] + df[BRT]) == 8]
plt.hist(conditioned_df[METRO], rwidth=0.8, bins=9,color='gray', density=True, label="Metro|Metro+Brt")
plt.xticks(range(0, 11))

plt.legend()
plt.show()
