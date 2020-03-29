# Ćwiczenie 4:
# Znajdowanie współrzędnych punktów leżących na prostej odległych o r od innego punktu leżącego na prostej


import plotly.graph_objs as go
import numpy as np

# parametry funkcji
a = 0.5
b = -1
# funkcja jako wyrażenia lambda
f = lambda x_in: a*x_in+b

# Współrzędne do wykresu
x = np.linspace(-2, 4, 2)
y = f(x)

# Współrzędne punktu
pt = [1, f(1)]

# Współrzędne punktów oddalone od r
t = [np.arctan(a), np.arctan(a)+np.pi]
r = 2
pts = np.zeros([2, 2])
pts[:, 0] = pt[0] + r*np.cos(t)
pts[:, 1] = pt[1] + r*np.sin(t)

# Rysowanie wykresu
wyk_lin = go.Scatter(x=x, y=y, name='funkcja liniowa', mode='lines')
wyk_pt = go.Scatter(x=np.array(pt[0]), y=np.array(pt[1]), name='punkt')
wyk_pt.marker = dict(
    color='rgba(0,255,0,0.5)',
    size=15,
    line=dict(
        color='rgba(0,0,0,1)',
        width=2
    )
)

wyk_pts = go.Scatter(x=pts[:, 0], y=pts[:, 1], mode='markers', name='punkty oddalone o r')

fig = go.Figure()
fig.add_trace(wyk_lin)
fig.add_trace(wyk_pt)
fig.add_trace(wyk_pts)

# Konfiguracja wyglądu
fig.update_layout(
    width=500,
    height=500,
    yaxis=dict(
        scaleanchor="x",
        scaleratio=1,
    ),
    plot_bgcolor='rgba(255,255,255,255)'
)

fig.update_xaxes(
    showgrid=True,
    gridwidth=1,
    gridcolor='lightGray',
    zeroline=True,
    zerolinewidth=1,
    zerolinecolor='lightGray',
    dtick=1,
    range=[-2, 4])

fig.update_yaxes(
    showgrid=True,
    gridwidth=1,
    gridcolor='lightGray',
    zeroline=True,
    zerolinewidth=1,
    zerolinecolor='lightGray',
    dtick=1,
    range=[-2, 1])


fig.show()