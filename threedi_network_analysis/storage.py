import numpy as np


def delta_v(sumax, H0, Hsumax, Hcurr, Hnew, Vsumax = None):
    """Calculate the difference in volume if the water level decreases from Hcurr to Hnew"""
    def below_sumax(H):
        return (Vsumax/Hsumax+H0)*H

    def from_sumax(H):
        return (H-Hsumax)*sumax + Vsumax

    if Vsumax is None:
        Vsumax = sumax*(Hsumax-H0)/2

    H = np.array([Hcurr, Hnew])

    V = np.piecewise(H,
        [H <= H0, (Hsumax > H) & (H > H0), H >= Hsumax],
        [lambda H: 0, lambda H: below_sumax(H), lambda x: from_sumax(H)]
    )

    return V[1] - V[2]

delta_v(sumax=100,
        H0 = 0.33,
        Hsumax = 0.56,
        Vsumax =
H0 = 0.33

H = np.array([0.25, 1.0])

)