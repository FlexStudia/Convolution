# coding: utf-8

# PACKGES
import numpy as np
import matplotlib.pyplot as plt

# IMPORT
import conv_core


def gauss_plot():
    # data
    x_array = conv_core.linear_extrapolation(-10, 10, 0.1)
    y_1 = np.zeros(len(x_array))
    y_2 = np.zeros(len(x_array))
    y_3 = np.zeros(len(x_array))
    y_4 = np.zeros(len(x_array))
    for i, x in enumerate(x_array):
        y_1[i] = conv_core.gauss_f(2.5, 0.2, x)
        y_2[i] = conv_core.gauss_f(-2.5, 0.5, x)
        y_3[i] = conv_core.gauss_f(2.5, 1, x)
        y_4[i] = conv_core.gauss_f(2.5, 5, x)
    # plot the data
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x_array, y_1, color='royalblue', label='mean=2.5, sigma=0.2')
    ax.plot(x_array, y_3, color='c', label='mean=2.5, sigma=1')
    ax.plot(x_array, y_4, color='limegreen', label='mean=2.5, sigma=5')
    ax.plot(x_array, y_2, color='orange', label='mean=-2.5, sigma=0.5')
    # info
    ax.set_ylabel('Gauss function')
    ax.set_title('Gauss function plot')
    ax.legend(title='Parameters')
    # display the plot
    plt.show()


def triangle_plot():
    # data
    x_array = conv_core.linear_extrapolation(-10, 10, 0.1)
    y_1 = np.zeros(len(x_array))
    y_2 = np.zeros(len(x_array))
    y_3 = np.zeros(len(x_array))
    y_4 = np.zeros(len(x_array))
    for i, x in enumerate(x_array):
        y_1[i] = conv_core.triangle_f(2.5, 0.2, x)
        y_2[i] = conv_core.triangle_f(-2.5, 0.5, x)
        y_3[i] = conv_core.triangle_f(2.5, 1, x)
        y_4[i] = conv_core.triangle_f(2.5, 5, x)
    # plot the data
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x_array, y_1, color='royalblue', label='mean=2.5, sigma=0.2')
    ax.plot(x_array, y_3, color='c', label='mean=2.5, sigma=1')
    ax.plot(x_array, y_4, color='limegreen', label='mean=2.5, sigma=5')
    ax.plot(x_array, y_2, color='orange', label='mean=-2.5, sigma=0.5')
    # info
    ax.set_ylabel('Triangle function')
    ax.set_title('Triangle function plot')
    ax.legend(title='Parameters')
    # display the plot
    plt.show()


def trapeze_plot():
    # data
    x_array = conv_core.linear_extrapolation(-10, 10, 0.1)
    y_1 = np.zeros(len(x_array))
    y_2 = np.zeros(len(x_array))
    y_3 = np.zeros(len(x_array))
    y_4 = np.zeros(len(x_array))
    for i, x in enumerate(x_array):
        y_1[i] = conv_core.trapeze_f(2.5, 0.2, 0.1, x)
        y_2[i] = conv_core.trapeze_f(-2.5, 0.5, 0.1, x)
        y_3[i] = conv_core.trapeze_f(2.5, 1, 0.5, x)
        y_4[i] = conv_core.trapeze_f(2.5, 5, 4, x)
    # plot the data
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x_array, y_1, color='royalblue', label='mean=2.5, sigma=0.2, top=0.1')
    ax.plot(x_array, y_3, color='c', label='mean=2.5, sigma=1, top=0.5')
    ax.plot(x_array, y_4, color='limegreen', label='mean=2.5, sigma=5, top=4')
    ax.plot(x_array, y_2, color='orange', label='mean=-2.5, sigma=0.5, top=0.1')
    # info
    ax.set_ylabel('Trapeze function')
    ax.set_title('Trapeze function plot')
    ax.legend(title='Parameters')
    # display the plot
    plt.show()


def lorentz_plot():
    # data
    x_array = conv_core.linear_extrapolation(-10, 10, 0.1)
    y_1 = np.zeros(len(x_array))
    y_2 = np.zeros(len(x_array))
    y_3 = np.zeros(len(x_array))
    y_4 = np.zeros(len(x_array))
    for i, x in enumerate(x_array):
        y_1[i] = conv_core.lorentz_f(2.5, 0.2, x)
        y_2[i] = conv_core.lorentz_f(-2.5, 0.5, x)
        y_3[i] = conv_core.lorentz_f(2.5, 1, x)
        y_4[i] = conv_core.lorentz_f(2.5, 5, x)
    # plot the data
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x_array, y_1, color='royalblue', label='mean=2.5, gamma=0.2')
    ax.plot(x_array, y_3, color='c', label='mean=2.5, gamma=1')
    ax.plot(x_array, y_4, color='limegreen', label='mean=2.5, gamma=5')
    ax.plot(x_array, y_2, color='orange', label='mean=-2.5, gamma=0.5')
    # info
    ax.set_ylabel('Lorentz function')
    ax.set_title('Lorentz function plot')
    ax.legend(title='Parameters')
    # display the plot
    plt.show()


def voigt_plot():
    # data
    x_array = conv_core.linear_extrapolation(-10, 10, 0.1)
    y_1 = np.zeros(len(x_array))
    y_2 = np.zeros(len(x_array))
    y_3 = np.zeros(len(x_array))
    y_4 = np.zeros(len(x_array))
    for i, x in enumerate(x_array):
        y_1[i] = conv_core.voigt_f(2.5, 0.2, 0.1, x)
        y_2[i] = conv_core.voigt_f(-2.5, 0.5, 0.1, x)
        y_3[i] = conv_core.voigt_f(2.5, 1, 0.5, x)
        y_4[i] = conv_core.voigt_f(2.5, 5, 4, x)
    # plot the data
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x_array, y_1, color='royalblue', label='mean=2.5, sigma=0.2, gamma=0.1')
    ax.plot(x_array, y_3, color='c', label='mean=2.5, sigma=1, gamma=0.5')
    ax.plot(x_array, y_4, color='limegreen', label='mean=2.5, sigma=5, gamma=4')
    ax.plot(x_array, y_2, color='orange', label='mean=-2.5, sigma=0.5, gamma=0.1')
    # info
    ax.set_ylabel('Voigt profile')
    ax.set_title('Voigt profile plot')
    ax.legend(title='Parameters')
    # display the plot
    plt.show()


def voigt_sigma_gamma_plot():
    # data
    x_array = conv_core.linear_extrapolation(-15, 15, 0.1)
    y_1 = np.zeros(len(x_array))
    y_2 = np.zeros(len(x_array))
    y_3 = np.zeros(len(x_array))
    y_4 = np.zeros(len(x_array))
    for i, x in enumerate(x_array):
        y_1[i] = conv_core.voigt_f(2.5, 5, 3, x)
        y_2[i] = conv_core.voigt_f(2.5, 3, 5, x)
        y_3[i] = conv_core.voigt_f(2.5, 3, 3, x)
        y_4[i] = conv_core.voigt_f(2.5, 5, 5, x)
    # plot the data
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x_array, y_3, color='orange', label='mean=2.5, sigma=3, gamma=3')
    ax.plot(x_array, y_1, color='royalblue', label='mean=2.5, sigma=5, gamma=3')
    ax.plot(x_array, y_2, color='c', label='mean=2.5, sigma=3, gamma=5')
    ax.plot(x_array, y_4, color='tomato', label='mean=2.5, sigma=5, gamma=5')
    # info
    ax.set_ylabel('Voigt profile')
    ax.set_title('Voigt profile plot: sigma and gamma')
    ax.legend(title='Parameters')
    # display the plot
    plt.show()


def pseudovoigt_plot():
    # data
    x_array = conv_core.linear_extrapolation(-10, 10, 0.1)
    y_1 = np.zeros(len(x_array))
    y_2 = np.zeros(len(x_array))
    y_3 = np.zeros(len(x_array))
    y_4 = np.zeros(len(x_array))
    for i, x in enumerate(x_array):
        y_1[i] = conv_core.gauss_lorentz_f(2.5, 0.2, 0.1, x, 0.5)
        y_2[i] = conv_core.gauss_lorentz_f(-2.5, 0.5, 0.1, x, 0.5)
        y_3[i] = conv_core.gauss_lorentz_f(2.5, 1, 0.5, x, 0.5)
        y_4[i] = conv_core.gauss_lorentz_f(2.5, 5, 4, x, 0.5)
    # plot the data
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x_array, y_1, color='royalblue', label='mean=2.5, sigma=0.2, gamma=0.1, g=0.5')
    ax.plot(x_array, y_3, color='c', label='mean=2.5, sigma=1, gamma=0.5, g=0.5')
    ax.plot(x_array, y_4, color='limegreen', label='mean=2.5, sigma=5, gamma=4, g=0.5')
    ax.plot(x_array, y_2, color='orange', label='mean=-2.5, sigma=0.5, gamma=0.1, g=0.5')
    # info
    ax.set_ylabel('pseudo-Voigt profile')
    ax.set_title('pseudo-Voigt profile plot')
    ax.legend(title='Parameters')
    # display the plot
    plt.show()


def pseudovoigt_sigma_gamma_plot():
    # data
    x_array = conv_core.linear_extrapolation(-15, 15, 0.1)
    y_1 = np.zeros(len(x_array))
    y_2 = np.zeros(len(x_array))
    y_3 = np.zeros(len(x_array))
    y_4 = np.zeros(len(x_array))
    for i, x in enumerate(x_array):
        y_1[i] = conv_core.gauss_lorentz_f(2.5, 5, 3, x, 0.5)
        y_2[i] = conv_core.gauss_lorentz_f(2.5, 3, 5, x, 0.5)
        y_3[i] = conv_core.gauss_lorentz_f(2.5, 3, 3, x, 0.5)
        y_4[i] = conv_core.gauss_lorentz_f(2.5, 5, 5, x, 0.5)
    # plot the data
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x_array, y_3, color='orange', label='mean=2.5, sigma=3, gamma=3, g=0.5')
    ax.plot(x_array, y_1, color='royalblue', label='mean=2.5, sigma=5, gamma=3, g=0.5')
    ax.plot(x_array, y_2, color='c', label='mean=2.5, sigma=3, gamma=5, g=0.5')
    ax.plot(x_array, y_4, color='tomato', label='mean=2.5, sigma=5, gamma=5, g=0.5')
    # info
    ax.set_ylabel('pseudo-Voigt profile')
    ax.set_title('pseudo-Voigt profile plot: sigma and gamma')
    ax.legend(title='Parameters')
    # display the plot
    plt.show()


def pseudovoigt_g_plot():
    # data
    x_array = conv_core.linear_extrapolation(-15, 15, 0.1)
    y_1 = np.zeros(len(x_array))
    y_2 = np.zeros(len(x_array))
    y_3 = np.zeros(len(x_array))
    y_4 = np.zeros(len(x_array))
    for i, x in enumerate(x_array):
        y_1[i] = conv_core.gauss_lorentz_f(2.5, 5, 5, x, 0.1)
        y_2[i] = conv_core.gauss_lorentz_f(2.5, 5, 5, x, 0.5)
        y_3[i] = conv_core.gauss_lorentz_f(2.5, 5, 5, x, 0.7)
        y_4[i] = conv_core.gauss_lorentz_f(2.5, 5, 5, x, 0.9)
    # plot the data
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x_array, y_4, color='tomato', label='mean=2.5, sigma=5, gamma=5, g=0.9')
    ax.plot(x_array, y_3, color='orange', label='mean=2.5, sigma=5, gamma=5, g=0.7')
    ax.plot(x_array, y_2, color='c', label='mean=2.5, sigma=5, gamma=5, g=0.5')
    ax.plot(x_array, y_1, color='royalblue', label='mean=2.5, sigma=5, gamma=5, g=0.1')
    # info
    ax.set_ylabel('pseudo-Voigt profile')
    ax.set_title('pseudo-Voigt profile plot: Gauss ratio impact')
    ax.legend(title='Parameters')
    # display the plot
    plt.show()


def all_plot():
    # data
    x_array = conv_core.linear_extrapolation(-15, 15, 0.1)
    y_1 = np.zeros(len(x_array))
    y_2 = np.zeros(len(x_array))
    y_3 = np.zeros(len(x_array))
    y_4 = np.zeros(len(x_array))
    y_5 = np.zeros(len(x_array))
    y_6 = np.zeros(len(x_array))
    for i, x in enumerate(x_array):
        y_1[i] = conv_core.gauss_f(2.5, 3, x)
        y_2[i] = conv_core.triangle_f(2.5, 3, x)
        y_3[i] = conv_core.trapeze_f(2.5, 3, 1, x)
        y_4[i] = conv_core.lorentz_f(2.5, 3, x)
        y_5[i] = conv_core.voigt_f(2.5, 3, 3, x)
        y_6[i] = conv_core.gauss_lorentz_f(2.5, 3, 3, x, 0.5)
    # plot the data
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x_array, y_3, color='gold', label='Trapeze')
    ax.plot(x_array, y_2, color='orange', label='Triangle')
    ax.plot(x_array, y_1, color='r', label='Gauss')
    ax.plot(x_array, y_6, color='navy', label='pseudo-Voigt (g=0.5)')
    ax.plot(x_array, y_4, color='g', label='Lorentz')
    ax.plot(x_array, y_5, color='deepskyblue', label='Voigt')
    # info
    ax.set_ylabel('functions')
    ax.set_title('All convolution functions')
    ax.legend(title='Curves\n(mean=2.5, sigma, gamma=3)')
    # display the plot
    plt.show()


def goss_sigma_plot():
    # data
    x_array = conv_core.linear_extrapolation(-1.6, 5.5, 0.05)
    y_array = np.zeros(len(x_array))
    for i, x in enumerate(x_array):
        y_array[i] = conv_core.gauss_f(2, 1, x)
    # 34.1%
    x_1_r = conv_core.linear_extrapolation(2.02, 2.98, 0.05)
    y_1_r = np.zeros(len(x_1_r))
    for i, x in enumerate(x_1_r):
        y_1_r[i] = conv_core.gauss_f(2, 1, x)
    x_1_l = conv_core.linear_extrapolation(1.02, 1.98, 0.05)
    y_1_l = np.zeros(len(x_1_l))
    for i, x in enumerate(x_1_l):
        y_1_l[i] = conv_core.gauss_f(2, 1, x)
    # 13.6%
    x_2_r = conv_core.linear_extrapolation(3.02, 3.98, 0.05)
    y_2_r = np.zeros(len(x_2_r))
    for i, x in enumerate(x_2_r):
        y_2_r[i] = conv_core.gauss_f(2, 1, x)
    x_2_l = conv_core.linear_extrapolation(0.02, 0.98, 0.05)
    y_2_l = np.zeros(len(x_2_l))
    for i, x in enumerate(x_2_l):
        y_2_l[i] = conv_core.gauss_f(2, 1, x)
    # 2.1%
    x_3_r = conv_core.linear_extrapolation(4.02, 4.98, 0.05)
    y_3_r = np.zeros(len(x_3_r))
    for i, x in enumerate(x_3_r):
        y_3_r[i] = conv_core.gauss_f(2, 1, x)
    x_3_l = conv_core.linear_extrapolation(-0.98, -0.02, 0.05)
    y_3_l = np.zeros(len(x_3_l))
    for i, x in enumerate(x_3_l):
        y_3_l[i] = conv_core.gauss_f(2, 1, x)
    # 0.1%
    x_4 = conv_core.linear_extrapolation(5, 5.5, 0.05)
    y_4 = np.zeros(len(x_4))
    for i, x in enumerate(x_4):
        y_4[i] = conv_core.gauss_f(2, 1, x)
    # plot the data
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x_array, y_array, color='black')
    ax.fill_between(x_1_r, y_1_r, facecolor='#056BA6', label="34.1%")
    ax.fill_between(x_1_l, y_1_l, facecolor='#056BA6')
    ax.fill_between(x_2_r, y_2_r, facecolor='#056BA6', alpha=.7, label="13.6%")
    ax.fill_between(x_2_l, y_2_l, facecolor='#056BA6', alpha=.7)
    ax.fill_between(x_3_r, y_3_r, facecolor='#056BA6', alpha=.5, label="2.1%")
    ax.fill_between(x_3_l, y_3_l, facecolor='#056BA6', alpha=.5)
    ax.fill_between(x_4, y_4, facecolor='#056BA6', alpha=.2, label="0.1%")
    # info
    ax.set_title('Gauss function plot and its sigma')
    ax.legend(title="Under the curve area\n(mean=2, sigma=1)")
    # display the plot
    plt.show()


def normalization_calc(spectrum_array, mean, sigma, top_sigma, sigma_1, sigma_2, convolution_gauss_ratio, convolution_type, convolution_truncation):
    j_min = 0
    j_max = spectrum_array.size - 1  # convolution_type: [0: default, 1: Gauss function, 2: triangle, 3: trapeze, 4: Lorentz function, 5: Voigt, 6: Gauss & Lorentz sum]
    if convolution_type not in [3, 5, 6]:
        for j in range(spectrum_array.size):
            if spectrum_array[j] > mean - convolution_truncation * sigma and j_min == 0:
                j_min = j
            if spectrum_array[j] > mean + convolution_truncation * sigma and j_max == spectrum_array.size - 1:
                j_max = j
                break
    elif convolution_type == 3:  # "trapeze"
        for j in range(spectrum_array.size):
            if spectrum_array[j] > mean - top_sigma - convolution_truncation * sigma and j_min == 0:
                j_min = j
            if spectrum_array[j] > mean + top_sigma + convolution_truncation * sigma and j_max == spectrum_array.size - 1:
                j_max = j
                break
    elif convolution_type in [5, 6]:  # "Voigt", "Gauss+Lorentz"
        for j in range(spectrum_array.size):
            if spectrum_array[j] > mean - convolution_truncation * (sigma_1 + sigma_2) and j_min == 0:
                j_min = j
            if spectrum_array[j] > mean + convolution_truncation * (sigma_1 + sigma_2) and j_max == spectrum_array.size - 1:
                j_max = j
                break
    # convolution function application
    index = 0
    truncated_convolution_function = np.zeros(j_max - j_min)  # convolution_type: [0: default, 1: Gauss function, 2: triangle, 3: trapeze, 4: Lorentz function, 5: Voigt, 6: Gauss & Lorentz sum]
    if convolution_type == 1:  # Gauss function
        for j in range(j_min, j_max):
            truncated_convolution_function[index] = conv_core.gauss_f(mean, sigma, spectrum_array[j])
            index += 1
    elif convolution_type == 2:  # "triangle"
        for j in range(j_min, j_max):
            truncated_convolution_function[index] = conv_core.triangle_f(mean, sigma, spectrum_array[j])
            index += 1
    elif convolution_type == 3:  # "trapeze"
        for j in range(j_min, j_max):
            truncated_convolution_function[index] = conv_core.trapeze_f(mean, sigma, top_sigma, spectrum_array[j])
            index += 1
    elif convolution_type == 4:  # "Lorentz function"
        for j in range(j_min, j_max):
            truncated_convolution_function[index] = conv_core.lorentz_f(mean, sigma, spectrum_array[j])
            index += 1
    elif convolution_type == 5:  # "Voigt profile"
        for j in range(j_min, j_max):
            truncated_convolution_function[index] = conv_core.voigt_f(mean, sigma_1, sigma_2, spectrum_array[j])
            index += 1
    elif convolution_type == 6:  # "Gauss & Lorentz sum"
        for j in range(j_min, j_max):
            truncated_convolution_function[index] =conv_core. gauss_lorentz_f(mean, sigma_1, sigma_2, spectrum_array[j], convolution_gauss_ratio)
            index += 1
    # normalization
    return np.trapz(truncated_convolution_function, spectrum_array[j_min:j_max])


def truncation_normalization():
    spectrum_array = conv_core.linear_extrapolation(-100, 100, 0.01)
    t_array = conv_core.linear_extrapolation(0.1, 10, 0.1)
    mean = 0
    # Gauss
    convolution_type = 1
    sigma = 5
    top_sigma = 0
    sigma_1 = 0
    sigma_2 = 0
    convolution_gauss_ratio = 0
    n_array_Gauss = np.zeros(len(t_array))
    for i, t in enumerate(t_array):
        n_array_Gauss[i] = normalization_calc(spectrum_array, mean, sigma, top_sigma, sigma_1, sigma_2, convolution_gauss_ratio, convolution_type, t)
    # triangle
    convolution_type = 2
    sigma = 5
    top_sigma = 0
    sigma_1 = 0
    sigma_2 = 0
    convolution_gauss_ratio = 0
    n_array_triangle = np.zeros(len(t_array))
    for i, t in enumerate(t_array):
        n_array_triangle[i] = normalization_calc(spectrum_array, mean, sigma, top_sigma, sigma_1, sigma_2, convolution_gauss_ratio, convolution_type, t)
    # trapeze
    convolution_type = 3
    sigma = 5
    top_sigma = 3
    sigma_1 = 0
    sigma_2 = 0
    convolution_gauss_ratio = 0
    n_array_trapeze = np.zeros(len(t_array))
    for i, t in enumerate(t_array):
        n_array_trapeze[i] = normalization_calc(spectrum_array, mean, sigma, top_sigma, sigma_1, sigma_2, convolution_gauss_ratio, convolution_type, t)
    # Lorentz
    convolution_type = 4
    sigma = 5
    top_sigma = 3
    sigma_1 = 0
    sigma_2 = 0
    convolution_gauss_ratio = 0
    n_array_lorentz = np.zeros(len(t_array))
    for i, t in enumerate(t_array):
        n_array_lorentz[i] = normalization_calc(spectrum_array, mean, sigma, top_sigma, sigma_1, sigma_2, convolution_gauss_ratio, convolution_type, t)
    # Voigt
    convolution_type = 5
    sigma = 5
    top_sigma = 3
    sigma_1 = 5
    sigma_2 = 5
    convolution_gauss_ratio = 0
    n_array_voigt = np.zeros(len(t_array))
    for i, t in enumerate(t_array):
        n_array_voigt[i] = normalization_calc(spectrum_array, mean, sigma, top_sigma, sigma_1, sigma_2, convolution_gauss_ratio, convolution_type, t)
    # pleudo-Voigt
    convolution_type = 6
    sigma = 5
    top_sigma = 3
    sigma_1 = 5
    sigma_2 = 5
    convolution_gauss_ratio = 0.5
    n_array_pseudo_voigt = np.zeros(len(t_array))
    for i, t in enumerate(t_array):
        n_array_pseudo_voigt[i] = normalization_calc(spectrum_array, mean, sigma, top_sigma, sigma_1, sigma_2, convolution_gauss_ratio, convolution_type, t)
    # plot the data
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(t_array, n_array_trapeze, color='#D8AD40', label="trapeze")
    ax.plot(t_array, n_array_triangle, color='#FF8800', label="triangle")
    ax.plot(t_array, n_array_Gauss, color='#A01749', label="Gauss")
    ax.plot(t_array, n_array_pseudo_voigt, color='#4258F9', label="pseudo-Voigt")
    ax.plot(t_array, n_array_voigt, color='#1CA1CD', label="Voigt")
    ax.plot(t_array, n_array_lorentz, color='#33D094', label="Lorentz")
    # info
    ax.set_ylabel('normalization')
    ax.set_xlabel('truncation')
    ax.set_title('Normalization and truncation')
    ax.legend(title="")
    # display the plot
    plt.show()


def truncation_normalization_mean_sigma():  # зависимость от sigma и mean есть, но ею можно пренебречь
    spectrum_array = conv_core.linear_extrapolation(-100, 100, 0.01)
    t_array = conv_core.linear_extrapolation(0.1, 5, 0.1)
    convolution_type = 1  # Gauss
    # 0, 5
    mean = 0
    sigma = 5
    n_array_1 = np.zeros(len(t_array))
    for i, t in enumerate(t_array):
        n_array_1[i] = normalization_calc(spectrum_array, mean, sigma, 0, 0, 0, 0, convolution_type, t)
    # -10, 5
    mean = -10
    sigma = 5
    n_array_2 = np.zeros(len(t_array))
    for i, t in enumerate(t_array):
        n_array_2[i] = normalization_calc(spectrum_array, mean, sigma, 0, 0, 0, 0, convolution_type, t)
    # 0, 0.3
    mean = 0
    sigma = 0.3
    n_array_3 = np.zeros(len(t_array))
    for i, t in enumerate(t_array):
        n_array_3[i] = normalization_calc(spectrum_array, mean, sigma, 0, 0, 0, 0, convolution_type, t)
    # plot the data
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(t_array, n_array_1, color='#D8AD40', label="mean=0, sigma=5")
    ax.plot(t_array, n_array_2, color='#FF8800', label="mean=-10, sigma=5")
    ax.plot(t_array, n_array_3, color='#A01749', label="mean=0, sigma=.3")
    # info
    ax.set_ylabel('normalization')
    ax.set_xlabel('truncation')
    ax.set_title('Normalization and truncation')
    ax.legend(title="")
    # display the plot
    plt.show()


def convolution_vs_decimation():
    spectrum_array = conv_core.linear_extrapolation(-100, 100, 0.01)
    intensity_array = np.zeros(len(spectrum_array))
    for i, e in enumerate(spectrum_array):
        intensity_array[i] = conv_core.gauss_f(5, 6, e)
    # decimation: 10 times
    destination_array_10 = conv_core.linear_extrapolation(-100, 100, 1)
    decimation_array_10 = np.zeros(len(destination_array_10))
    for i, e in enumerate(destination_array_10):
        decimation_array_10[i] = conv_core.gauss_f(5, 6, e)
    # decimation: 100 times
    destination_array_100 = conv_core.linear_extrapolation(-100, 100, 10)
    decimation_array_100 = np.zeros(len(destination_array_100))
    for i, e in enumerate(destination_array_100):
        decimation_array_100[i] = conv_core.gauss_f(5, 6, e)
    # convolution: 10 times
    my_conv = conv_core.ConvolutionCore()
    my_conv.spectrum_wavelength = spectrum_array
    my_conv.spectrum_wavelength_original = spectrum_array
    my_conv.spectrum_intensity_original = intensity_array
    my_conv.spectrum_intensity = intensity_array
    my_conv.spectrum_unit_original = "cm-1"
    my_conv.spectrum_set_up = True
    my_conv.destination_setter_linear_function(my_conv.spectrum_unit_original, -100, 100, 1)
    my_conv.convolution_setter_width_constant(1, 0, 5, 0, 10, np.NAN)
    my_conv.convolution_stack()
    convolution_array_10 = my_conv.destination_intensity
    # convolution: 100 times
    my_conv = conv_core.ConvolutionCore()
    my_conv.spectrum_wavelength = spectrum_array
    my_conv.spectrum_wavelength_original = spectrum_array
    my_conv.spectrum_intensity_original = intensity_array
    my_conv.spectrum_intensity = intensity_array
    my_conv.spectrum_unit_original = "cm-1"
    my_conv.spectrum_set_up = True
    my_conv.destination_setter_linear_function(my_conv.spectrum_unit_original, -100, 100, 10)
    my_conv.convolution_setter_width_constant(1, 0, 5, 0, 10, np.NAN)
    my_conv.convolution_stack()
    convolution_array_100 = my_conv.destination_intensity
    # plot the data
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(spectrum_array, intensity_array, label="high resolution")
    ax.plot(destination_array_10, decimation_array_10, label="decimation: 1 of 100")
    ax.plot(destination_array_10, convolution_array_10, label="convolution: 1 of 100")
    ax.plot(destination_array_100, decimation_array_100, label="decimation: 1 of 1000")
    ax.plot(destination_array_100, convolution_array_100, label="convolution: 1 of 1000")
    original_area = np.trapz(intensity_array, spectrum_array)
    decimated_10_area = np.trapz(decimation_array_10, destination_array_10)
    decimated_100_area = np.trapz(decimation_array_100, destination_array_100)
    convoluted_10_area = np.trapz(convolution_array_10, destination_array_10)
    convoluted_100_area = np.trapz(convolution_array_100, destination_array_100)
    print(f"decimated_10_area to original_area: {100 * decimated_10_area / original_area} %")
    print(f"decimated_100_area to original_area: {100 * decimated_100_area / original_area} %")
    print(f"convoluted_10_area to original_area: {100 * convoluted_10_area / original_area} %")
    print(f"convoluted_100_area to original_area: {100 * convoluted_100_area / original_area} %")
    # info
    ax.set_xlabel('wavelength')
    ax.set_ylabel('intensity')
    ax.set_title('Convolution vs decimation')
    ax.legend(title="")
    # display the plot
    plt.show()


def Dirac_plot():
    # data
    x_array = conv_core.linear_extrapolation(-10, 10, 0.1)
    y = np.zeros(len(x_array))
    y[int(len(y)/2)] = 1
    # plot the data
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x_array, y)
    # info
    ax.set_ylabel('Dirac spike')
    ax.set_title('Dirac spike plot')
    # display the plot
    plt.show()


def Dirac_truncation_conservation():
    spectrum_file_path = "C:/Users/flex_virt/Dev/Convolution_dev/tests/math_examples/dirac.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    ## destination
    destination_unit = "cm-1"
    destination_start = 0
    destination_stop = 10
    destination_step = 0.1
    ## convolution
    convolution_extrapolation_type = 1  # "zeros"
    convolution_type = 4  # "Lorentz"
    convolution_gauss_ratio = 0
    convolution_width_1_const = 2.5
    convolution_width_2_const = 1.5
    T_min = 0
    T_max = 20
    T_step = 0.1
    convolution_truncation = T_min
    x_array = []
    y_array = []
    while convolution_truncation < T_max + T_step:
        print(f"{100 * convolution_truncation / (T_max + T_step):.2f}% of 100")
        my_conv = conv_core.ConvolutionCore()
        my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
        my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
        my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
        my_conv.convolution_stack()
        x_array.append(convolution_truncation)
        y_array.append(100 * my_conv.destination_surface_area / my_conv.spectrum_surface_area)
        convolution_truncation = convolution_truncation + T_step
    # plot the data
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x_array, y_array, label='percent\nof conservation')
    ax.plot([T_min, T_max], [100, 100], label='guide line 100%')
    # info
    ax.set_xlabel('truncation')
    ax.set_ylabel('%')
    ax.set_title('Conservation of area under the convoluted curve\nfor the Dirac spike in function of truncation')
    ax.legend(title="")
    # display the plot
    plt.show()


def NH_truncation_conservation():
    spectrum_file_path = "C:/Users/flex_virt/Dev/Convolution_dev/tests/NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "C:/Users/flex_virt/Dev/Convolution_dev/tests/NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0
    convolution_type = 6
    convolution_gauss_ratio = 0.6
    convolution_file_path = "C:/Users/flex_virt/Dev/Convolution_dev/tests/NH_case/ref_cm.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    T_start = 0
    T_end = 20
    T_step = 0.1
    x_array = []
    y_array = []
    convolution_truncation = T_start
    while convolution_truncation < T_end + T_step:
        print(f"{100 * convolution_truncation / (T_end + T_step):.2f}% of 100")
        my_conv = conv_core.ConvolutionCore()
        my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
        my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
        my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
        my_conv.convolution_stack()
        x_array.append(convolution_truncation)
        y_array.append(100 * my_conv.destination_surface_area / my_conv.spectrum_surface_area)
        convolution_truncation = convolution_truncation + T_step
    # plot the data
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x_array, y_array, label='percent\nof conservation')
    ax.plot([T_start, T_end], [100, 100], label='guide line 100%')
    # info
    ax.set_xlabel('truncation')
    ax.set_ylabel('%')
    ax.set_title('Conservation of area under the convoluted curve\nfor the LEISA New Horizon data in function of truncation')
    ax.legend(title="")
    # display the plot
    plt.show()


NH_truncation_conservation()
