import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import datetime


#EXTRACT TEMPERATURE VS TIME FOR GRAPH 1:
temp_data = pd.read_csv(r'C:\Users\david\OneDrive - Stellenbosch University\Desktop\Python\sensor_data_logrf.csv',usecols = [1,2], header=0, names = ['Time', 'Temperature'], index_col=False)
temp_data = temp_data.iloc[-1000:]
## CREATE AND STYLE TEMP VS TIME Data --> GRAPH 2:
fig = px.line(temp_data, x='Time', y="Temperature", title = 'Temperature vs Time', template = 'plotly_dark')
fig.update_layout(title_x=0.5,title_font_size = 30)
fig.update_yaxes(title_font=dict(size=18))
fig.update_xaxes(title_font=dict(size=18))

fig.show()

# EXTRACT HUMIDITY VS TIME Data:

hum_data = pd.read_csv(r'C:\Users\david\OneDrive - Stellenbosch University\Desktop\Python\sensor_data_logrf.csv',usecols = [1,5], header=0, names = ['Time', 'Humidity'], index_col=False)
hum_data = hum_data.iloc[-1900:]
# ## PLOT HUM VS TIME Data --> GRAPH2:
# fig2 = px.line(hum_data, x = 'Time', y = 'Humidity', title = 'Humidity vs Time', template = 'plotly_dark')
# fig2.update_layout(title_x = 0.5, title_font_size = 30)
# fig2.update_yaxes(title_font=dict(size=18))
# fig2.update_xaxes(title_font=dict(size=18))
# fig2.show()

## Extract Pressure vs Time Data:

# pres_data = pd.read_csv(r'C:\Users\david\OneDrive - Stellenbosch University\Desktop\Python\sensor_data_logrf.csv',usecols = [1,4], header=0, names = ['Time', 'Pressure'], index_col=False)
# pres_data = pres_data.iloc[-1000:]

## Plot Pressure vs Time Data --> GRAPH 3:

# fig3 = px.line(pres_data, x = 'Time', y = 'Pressure', title = 'Pressure vs Time', template = 'plotly_dark')
# fig3.update_layout(title_x = 0.5, title_font_size = 30)
# fig3.update_yaxes(title_font=dict(size=18))
# fig3.update_xaxes(title_font=dict(size=18))
