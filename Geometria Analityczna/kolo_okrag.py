import plotly
import numpy as np

go = plotly.graph_objs

t = np.linspace(0,2*np.pi,60)

r_kolo = 1
x0_kolo = -1
y0_kolo = 0

pts_kolo = np.zeros([len(t),2])
pts_kolo[:, 0] = x0_kolo + r_kolo*np.sin(t)
pts_kolo[:, 1] = y0_kolo + r_kolo*np.cos(t)

sc_kolo = go.Scatter(x=pts_kolo[:, 0], y=pts_kolo[:, 1], name='kolo', fill='toself')

r_okrag = 0.5
x0_okrag = 1
y0_okrag = 0

pts_okrag = np.zeros([len(t),2])
pts_okrag[:, 0] = x0_okrag + r_okrag*np.sin(t)
pts_okrag[:, 1] = y0_okrag + r_okrag*np.cos(t)

sc_okrag = go.Scatter(x=pts_okrag[:, 0], y=pts_okrag[:, 1], name='okrag', mode='lines')

fig = go.Figure()
fig.add_trace(sc_kolo)
fig.add_trace(sc_okrag)
# fig.add_trace(scatter_b)
# fig.add_trace(scatter_c)
#
fig.update_layout(
    width=500,
    height=500,
    yaxis=dict(
        scaleanchor="x",
        scaleratio=1,
    )
)

fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightGray')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightGray')

fig.update_xaxes(zeroline=True, zerolinewidth=1, zerolinecolor='lightGray')
fig.update_yaxes(zeroline=True, zerolinewidth=1, zerolinecolor='lightGray')

fig.update_layout(plot_bgcolor='rgba(255,255,255,255)')

fig.show()
