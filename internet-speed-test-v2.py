from speedtest import Speedtest    
from win10toast import ToastNotifier

s = Speedtest()
toast = ToastNotifier()

download = s.download()     # Getting download speed
upload = s.upload()     # Getting upload speed
download_speed = int(download/(1_048_576))     # Mbps
upload_speed = int(upload/(1_048_576))

#Creates message
toast.show_toast(
    "internet speed test",
    f"download: {download_speed} MB/S \n upload: {upload_speed} MB/s",
    duration = 20,
    #icon_path = "icon.ico",
    #threaded = True,
    )
