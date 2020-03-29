# Ćwiczenie 2:
# Rysowanie dwóch funkcji liniowych
# Lokalizacja punktu przecięcia z zastosowaniem własnoręcznie zdefiniowanych funkcji

import plotly.graph_objs as go
import numpy as np
import funkcje_liniowe


# Pierwsza funkcja liniowa
a1 = 0.5
b1 = -1

# Druga funkcja liniowa
a2 = -1.25
b2 = 1

# Punkt przecięcia
pt_p = funkcje_liniowe.znajdz_punkt_przeciecia(a1, b1, a2, b2)

zakres = [-2, 2]

# Wykres pierwszej funkcji
wyk_lin1 = funkcje_liniowe.wygeneruj_wykres(a1, b1, zakres)
wyk_lin1.name = 'funkcja 1'
wyk_lin1.marker = dict(color='rgba(255,0,0,1)')

# Wykres drugiej funkcji
wyk_lin2 = funkcje_liniowe.wygeneruj_wykres(a2, b2, zakres)
wyk_lin2.name = 'funkcja 2'
wyk_lin2.marker = dict(color='rgba(0,0,255,1)')

# Wykres punktu przecięcia
sc_ptp = go.Scatter(x=np.array(pt_p[0]), y=np.array(pt_p[1]), name='przecięcie')
sc_ptp.marker = dict(
    color='rgba(0,255,0,0.5)',
    size=15,
    line=dict(
        color='rgba(0,0,0,1)',
        width=2
    )
)

fig = go.Figure()
fig.add_trace(wyk_lin1)
fig.add_trace(wyk_lin2)
fig.add_trace(sc_ptp)

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
    dtick=0.5,
    range=[-2, 2])

fig.update_yaxes(
    showgrid=True,
    gridwidth=1,
    gridcolor='lightGray',
    zeroline=True,
    zerolinewidth=1,
    zerolinecolor='lightGray',
    dtick=0.5,
    range=[-2, 2])


fig.show()
