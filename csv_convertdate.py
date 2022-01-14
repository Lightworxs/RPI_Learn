import pandas as pd
import datetime as dt

df = pd.read_csv(r'C:\Users\david\OneDrive - Stellenbosch University\Desktop\Python\sensor_data_log.csv', parse_dates= [[0,1]], infer_datetime_format=True, dayfirst = True)
print(df)
# df['Date_Time'] = pd.to_datetime(df['Date_Time'],format = '%d/%m/%Y %H/%m/%s')
# print(df)
df.to_csv(r'C:\Users\david\OneDrive - Stellenbosch University\Desktop\Python\sensor_data_logrf.csv')
# time.strftime("%Y%M%D %H%M%S")