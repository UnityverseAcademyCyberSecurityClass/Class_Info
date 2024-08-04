import subprocess

def list_available_networks():
    #setleme yapıldı
    result   = subprocess.check_output(['netsh','wlan','show','networks', 'mode=Bssid'], shell=True) 
    networks = result.decode('utf-8').split('\r\n')
    for network in networks: #networks listesinden dönecek olan liste sayısı kadar çalışır.
        if("SSID") in network:
            ssid = network.split(':')[1].strip()
            print(f"SSID : {ssid}")

#main akışta class'ı çağırdık
list_available_networks()