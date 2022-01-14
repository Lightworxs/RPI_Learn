import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


app = dash.Dash(__name__)
app.css.append_css({'external_url': 'reset.css'})
## IMPORT DATA


##START CREATING LAYOUT

app.layout = html.Div(style = {'backgroundColor':'#808080'}, children=[
    html.H1(style={'textAlign':'center'},children=["Environment Monitoring Dashboard"]),
    html.Div(style={'padding': 20},children=[
    dcc.Slider(
        id='data_range',
        min=0,
        max=1500,
        step=10,
        value=1000,
    )
    ]
    ),
    
    dcc.Graph(id = 'temp'),
    dcc.Graph(id = 'humidity'),
    dcc.Graph(id = 'pressure')

])

@app.callback(
    Output('temp', 'figure'),
    Input('data_range','value')
)
def temp_graph(data_range):
    temp_data = pd.read_csv(r'C:\Users\david\OneDrive - Stellenbosch University\Desktop\Python\sensor_data_logrf.csv',usecols = [1,2], header=0, names = ['Time', 'Temperature'], index_col=False)
    temp_data = temp_data.iloc[-data_range:]
    fig = px.line(temp_data, x='Time', y="Temperature", title = 'Temperature vs Time', template = 'plotly_dark')
    fig.update_layout(title_x=0.5,title_font_size = 30)
    fig.update_yaxes(title_font=dict(size=18))
    fig.update_xaxes(title_font=dict(size=18))
    return fig

@app.callback(
    Output('humidity','figure'),
    Input('data_range','value')
)
def hum_graph(data_range):
    hum_data = pd.read_csv(r'C:\Users\david\OneDrive - Stellenbosch University\Desktop\Python\sensor_data_logrf.csv',usecols = [1,5], header=0, names = ['Time', 'Humidity'], index_col=False)
    hum_data = hum_data.iloc[-data_range:]
    fig2 = px.line(hum_data, x = 'Time', y = 'Humidity', title = 'Humidity vs Time', template = 'plotly_dark')
    fig2.update_layout(title_x = 0.5, title_font_size = 30)
    fig2.update_yaxes(title_font=dict(size=18))
    fig2.update_xaxes(title_font=dict(size=18))
    return fig2

@app.callback(
    Output('pressure','figure'),
    Input('data_range','value')
)
def pres_graph(data_range):
    pres_data = pd.read_csv(r'C:\Users\david\OneDrive - Stellenbosch University\Desktop\Python\sensor_data_logrf.csv',usecols = [1,4], header=0, names = ['Time', 'Pressure'], index_col=False)
    pres_data = pres_data.iloc[-data_range:]
    fig3 = px.line(pres_data, x = 'Time', y = 'Pressure', title = 'Pressure vs Time', template = 'plotly_dark')
    fig3.update_layout(title_x = 0.5, title_font_size = 30)
    fig3.update_yaxes(title_font=dict(size=18))
    fig3.update_xaxes(title_font=dict(size=18))
    return fig3

if __name__ == "__main__":
    app.run_server(debug=False)