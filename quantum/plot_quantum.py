import matplotlib.pyplot as plt
import numpy as np


def plot(c):
    m = np.power(np.matrix(c.history), 2)
    k = np.matrix(c.history)

    plot_groups = [[], []]
    N = m[0].size
    for i in range(N):
        ax = plt.subplot(421 + i*2)
        ax.plot(m[:, i], label='Probability')
        ax.set_ylim(-1, 1.5)
        plot_groups[0].append(ax)
        ax.set_ylabel('{state:>0{digits}b}'.format(state=i, digits=int(np.log2(N))))

    for i in range(N):
        ax = plt.subplot(422 + i*2)
        ax.plot(k[:, i], label='Koefficient', color='orange')
        ax.set_ylim(-1, 1.5)
        plot_groups[1].append(ax)
        ax.set_ylabel('{state:>0{digits}b}'.format(state=i, digits=int(np.log2(N))))

    for i, (name, value) in enumerate(c.marks):
        for plots in plot_groups:
            for j, plot in enumerate(plots):
                plot.annotate(
                    name, xy=(i, value[j].real ** 2), xytext=(i+0.5, 1.2),
                    arrowprops=dict(facecolor='black', shrink=0.1, width=0.3, headwidth=10),
                )

                plot.axvline(
                    x=i, ymin=0, ymax=1, c="red", linewidth=0.5, zorder=0
                )

    plt.legend()
    plt.show()
