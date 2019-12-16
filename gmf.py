import numpy as np
from numpy.testing import assert_allclose
def gaussmf(x, mean, sigma):
    return np.exp(-((x - mean)**2.) / (2 * sigma**2.))
def gbellmf(x, a, b, c):
    return 1. / (1. + np.abs((x - c) / a) ** (2 * b))
def psigmf(x, b1, c1, b2, c2):
    return sigmf(x, b1, c1) * sigmf(x, b2, c2)
def sigmf(x, b, c):
    return 1. / (1. + np.exp(- c * (x - b)))
def test_gaussmf():
    x = np.arange(-4, 5.1, 0.1)
    expected = np.exp(- (x - 1.33)**2 / (2 * 0.45**2))
    test = gaussmf(x, 1.33, 0.45)
    assert_allclose(test, expected)
def test_gbellmf():
    x = np.arange(-4, 5.1, 0.1)
    a, b, c = (2.4, 0.9, 1.33)
    expected = 1 / (1 + np.abs(np.r_[x - c] / a) ** [2 * b])
    test = gbellmf(x, a, b, c)
    assert_allclose(test, expected)
def test_psigmf():
    x = np.arange(-4, 4.1, 0.1)
    b1, c1, b2, c2 = -1.75, -np.pi / 2., 0.972, 0.43
    expected = ((1 / (1. + np.exp(- c1 * (x - b1)))) *
                (1 / (1. + np.exp(- c2 * (x - b2)))))
    test = psigmf(x, b1, c1, b2, c2)
    assert_allclose(test, expected)
def test_sigmf():
    x = np.arange(-4, 4.1, 0.1)
    b1, c1 = 1.75, -np.pi / 2.
    expected = 1 / (1. + np.exp(- c1 * (x - b1)))
    test = sigmf(x, b1, c1)
    assert_allclose(test, expected)
if __name__ == '__main__':
        np.testing.run_module_suite()
