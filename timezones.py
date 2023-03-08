from datetime import datetime
import pytz

bogota_timezone = pytz.timezone('America/Bogota')
bogota_time = datetime.now(bogota_timezone)
print("Bogotá:", bogota_time.strftime("%d/%m/%Y, %H:%M:%S"))

mexico_timezone = pytz.timezone('America/Mexico_City')
mexico_time = datetime.now(mexico_timezone)
print("Ciudad de México:", mexico_time.strftime("%d/%m/%Y, %H:%M:%S"))

caracas_timezone = pytz.timezone('America/Caracas')
caracas_time = datetime.now(caracas_timezone)
print("Caracas:", caracas_time.strftime("%d/%m/%Y, %H:%M:%S"))