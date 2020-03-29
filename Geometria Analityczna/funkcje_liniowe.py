import numpy as np
import plotly.graph_objs as go

def znajdz_punkt_oddalonu_o_r_od_pocz_polprostej(pt_p, a, b, r, koniec):
    pts = znajdz_wsp_punktow_oddalone_o_r(pt_p, a, b, r)
    if koniec == '+':
        if pts[0,0] > pt_p[0]:
            return pts[0,:]
        else:
            return pts[1,:]
    elif koniec == '-':
        if pts[0, 0] < pt_p[0]:
            return pts[0, :]
        else:
            return pts[1, :]
    else:
        raise ValueError('Nieprawidłowo określony koniec półprostej: "-" lub "+"')

def znajdz_wsp_punktow_oddalone_o_r(pt, a, b, r):
    if abs(pt[1] - (a*pt[0]+b)) > 1e-4:
        raise ValueError('Punkt nie leży na prostej')

    t = [np.arctan(a), np.arctan(a) + np.pi]
    pts = np.zeros([2, 2])
    pts[:, 0] = pt[0] + r * np.cos(t)
    pts[:, 1] = pt[1] + r * np.sin(t)
    return pts

def znajdz_parametry_funkcji_przechodzacej_przez_dwa_punkty(pt1, pt2):
    A = np.array([[pt1[0], 1],
                  [pt2[0], 1]])
    B = np.array([pt1[1], pt2[1]])
    return np.linalg.solve(A, B)

def wygeneruj_wykres(a, b, zakres):
    # funkcja jako wyrażenia lambda
    f = lambda x_in: a * x_in + b

    # Współrzędne do wykresu
    x = np.linspace(zakres[0], zakres[1], 2)
    y = f(x)

    return go.Scatter(x=x, y=y, mode='lines')


def znajdz_punkt_przeciecia(a1, b1, a2, b2):
    A = np.array([[-a1, 1],
                  [-a2, 1]])
    B = np.array([b1, b2])
    return np.linalg.solve(A, B)
