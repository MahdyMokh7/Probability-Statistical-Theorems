import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from time import sleep
from IPython import display



# reading the csv file and converting to DataFrame
df = pd.read_csv("digits.csv")

# storing the 2 last rows in a variable
last_row = df.iloc[-1:]
last_row2 = df.iloc[-2:-1]

# test
print("last_row2:  \n", last_row2)
print("last_row1:  \n", last_row)

# deleting the 2 last rows
df.drop(index=[200, 201], inplace=True)

# test
print(df['label'].value_counts())
print(df.info())



# part2
THRESHOLD = 128
df_bin = df.copy()
df_bin[df_bin < THRESHOLD] = 0
df_bin[df_bin >= THRESHOLD] = 1
df_bin['label'] = df['label']
# test a sample part of the DataFrame
print(df_bin.iloc[1:18, 127:134])



# # part3
# rand_row = random.randint(0, 199)

# rand_row = df_bin.iloc[rand_row:rand_row+1, 1:]
# values = []
# for col in rand_row.columns:
#     values.append(rand_row[col])
# rand_row_array = np.array(values)
# pic = rand_row_array.reshape(28, 28)
# plt.imshow(pic, cmap="Greys")
# plt.show()

print(df_bin)
# part4
## you need these imports

t = 1000
p = np.linspace(0,1,t)
fy = stats.beta.pdf(p, a=1, b=1)

def update(fy: np.array, n:bool) -> np.array:
    p = np.linspace(0,1,t)
    # calculate P(N = n| Y = p) which is a bernouli distribution
    # calculate integral(0 -> 1) fy * pny
    pny = stats.bernoulli.pmf(n, p)
    integral = np.sum(fy * pny) / t
    post = fy * pny / integral
    return post

plt.figure(figsize=(10,8))
for i in range(100):
    # replace 'df' with your dataframe's name, this is just a suggestion, you do not have to code exactly like this
    n =  df_bin[df_bin['label'] == 8].iloc[i, df_bin.columns.get_loc('pixel404')]
    fy = update(fy, n)

    # dynamic plot
    # do not change this part
    plt.plot(p, fy, 'r', label='1')
    plt.ylim(-1, 10)
    plt.xlim(0, 1)
    plt.text(0.1,9,f'number of seen data : {i + 1}, p = {fy.argmax() / t :.2f}', color='purple')
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    sleep(0.05)


