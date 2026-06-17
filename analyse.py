import pandas as pd

#reads csv file into memory
pd.options.display.max_rows = 5000
filename = 'telemetry_data.csv'
df = pd.read_csv(filename)

#gets the max vibrations for each turbine then prints the turbines that fails anomaly rules
maxVibration = df.groupby('turbine_id')['vibration_mm_s'].max()
print("The following turbines have unnaceptable vibrations and need urgent maintainence:")
for turbine_id, max_vibration in maxVibration.items():
    if max_vibration > 15.0:
        print(turbine_id)

#gets the average temperature for each turbine then prints the turbines that fails anomly rules
avgTemp = df.groupby('turbine_id')['temperature_c'].mean()
print("The following turbines have an unacceptable average temperature and need urgent maintainence:")
for turbine_id, avg_temp in avgTemp.items():
    if avg_temp > 85.0:
        print(turbine_id)