import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, norm, binom

N = 7072
P = 0.45
SIZE = 1000
AVG = N * P
STD_DEV = math.pow(N * P * (1 - P), 1 / 2)


def draw_chart(bin_samples, type_name):
    # create figure
    plt.figure()

    # create x-axis range
    x_value_range = np.arange(math.floor(AVG) - 100, math.floor(AVG) + 100, 1)  # Adjust the range to cover a wider range of values

    if type_name == 'cdf':  # generate plot cdf
        plot_cdf = plt.plot(x_value_range, binom.cdf(x_value_range, N, P), color='b', linewidth=1, label='Binomial')
        plot_cdf = plt.plot(x_value_range, poisson.cdf(x_value_range, AVG), color='g', linewidth=1, label='Poisson')
        plot_cdf = plt.plot(x_value_range, norm.cdf(x_value_range, AVG, STD_DEV), color='r', linewidth=1,
                            label='Normal')

    if type_name == 'pdf':  # generate plot pdf/pmf
        plot_pdf = plt.plot(x_value_range, binom.pmf(x_value_range, N, P),
                            color='b', linewidth=1, label='Binomial')
        plot_pdf = plt.plot(x_value_range, poisson.pmf(x_value_range, AVG), color='g', linewidth=1,
                            label='Poisson')
        plot_pdf = plt.plot(x_value_range, norm.pdf(x_value_range, AVG, STD_DEV),
                            color='r', linewidth=1, label='Normal')

    # configure
    plt.xlabel('Samples')
    plt.ylabel(type_name)
    plt.title('Comparison')
    plt.legend()

    # draw graph
    plt.show()


if __name__ == '__main__':
    draw_chart(np.random.binomial(n=N, p=P, size=SIZE), type_name='cdf')
    draw_chart(np.random.binomial(n=N, p=P, size=SIZE), type_name='pdf')
