import numpy as np

def ols_with_se(X, y):
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    sigma2 = (resid @ resid) / (len(y) - len(beta))
    XtX_inv = np.linalg.inv(X.T @ X)
    se = np.sqrt(np.diag(sigma2 * XtX_inv))
    return beta, se, sigma2

def ssvs_gibbs(y, X, tau, c, n_iter=30000, burn_in=5000, random_state=0):
    rng = np.random.default_rng(random_state)
    n, p = X.shape
    tau = np.asarray(tau)
    c = np.full(p, c)

    gamma = np.zeros(p, dtype=int)
    beta = np.zeros(p)

    XtX = X.T @ X
    Xty = X.T @ y
    beta_ols, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta_ols
    sigma2 = (resid @ resid) / (n - p)

    samples = []

    for it in range(n_iter):
        var0 = tau**2
        var1 = (c * tau)**2
        prior_var = var0 * (1 - gamma) + var1 * gamma

        prec = XtX / sigma2 + np.diag(1/prior_var)
        cov = np.linalg.inv(prec)
        mean = cov @ (Xty / sigma2)
        beta = rng.multivariate_normal(mean, cov)

        resid = y - X @ beta
        shape = 0.5 * n
        scale = 0.5 * (resid @ resid)
        sigma2 = 1.0 / rng.gamma(shape, 1.0 / scale)

        # vectorized gamma update
        log_a = -0.5*np.log(var1) - 0.5*(beta**2)/var1
        log_b = -0.5*np.log(var0) - 0.5*(beta**2)/var0
        m = np.maximum(log_a, log_b)
        prob = np.exp(log_a - m) / (np.exp(log_a - m) + np.exp(log_b - m))
        gamma = rng.binomial(1, prob)

        if it >= burn_in:
            samples.append(gamma.copy())

    return np.array(samples)
