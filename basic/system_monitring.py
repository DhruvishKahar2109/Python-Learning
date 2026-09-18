import psutil
print("CPU:",psutil.cpu_percent(),"%")
print("Memory:",psutil.virtual_memory().percent,"%")
print("Disk:",psutil.disk_usage("/").percent,"%")
print("Ram:",psutil.disk_usage("/").total,"%")

battery = psutil.sensors_battery()
print(battery.percent)