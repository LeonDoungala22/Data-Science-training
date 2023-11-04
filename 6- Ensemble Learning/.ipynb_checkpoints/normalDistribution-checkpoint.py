import matplotlib.pyplot as plt


# Plotting the histogram.


def plotNormalDistribution(mode) :
    
    plt.figure(figsize=(10,8))
    plt.hist(mode, bins=50, density=True, alpha=0.9, color='green')

    plt.show()