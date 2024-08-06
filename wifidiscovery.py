'''
Unityverse Academy : Siber güvenlik dersleri kapsamında tamamen 
eğitim amacıyla hazırlanmış Wi-Fi ağları tarama programıdır. 
'''

import subprocess  # subprocess modülünü içe aktarır, bu modül komut satırı işlemlerini çalıştırmak için kullanılır
import re  # re modülünü içe aktarır, bu modül düzenli ifadelerle çalışmak için kullanılır

def list_available_networks():
    # 'netsh wlan show networks mode=Bssid' komutunu çalıştırır ve sonuçları yakalar
    result = subprocess.check_output(['netsh', 'wlan', 'show', 'networks', 'mode=Bssid'], shell=True)
    # Komutun çıktısını UTF-8 formatında decode eder ve satırlara böler
    networks = result.decode('utf-8').split('\r\n')
    
    network_list = []  # Bulunan ağları tutacak listeyi oluşturur
    network_info = {}  # Tek bir ağın bilgilerini tutacak geçici sözlüğü oluşturur
    
    # Komut çıktısının her bir satırını döner
    for line in networks:
        if "SSID" in line:
            # Eğer satır "SSID" içeriyorsa, SSID'yi alır ve network_info sözlüğüne ekler
            network_info['SSID'] = line.split(':')[1].strip()
        elif "BSSID" in line:
            # Eğer satır "BSSID" içeriyorsa, düzenli ifadeyle BSSID'yi yakalar ve network_info sözlüğüne ekler
            match = re.search(r'BSSID\s*:\s*(\S+)', line)
            if match:
                network_info['BSSID'] = match.group(1)
        elif "Signal" in line:
            # Eğer satır "Signal" içeriyorsa, düzenli ifadeyle sinyal gücünü yakalar ve network_info sözlüğüne ekler
            match = re.search(r'Signal\s*:\s*(\S+)', line)
            if match:
                network_info['Signal'] = match.group(1)
        elif "Radio type" in line:
            # Eğer satır "Radio type" içeriyorsa, düzenli ifadeyle radyo tipini yakalar ve network_info sözlüğüne ekler
            match = re.search(r'Radio type\s*:\s*(\S+)', line)
            if match:
                network_info['Radio type'] = match.group(1)
        elif "Authentication" in line:
            # Eğer satır "Authentication" içeriyorsa, doğrulama tipini alır ve network_info sözlüğüne ekler
            network_info['Authentication'] = line.split(':')[1].strip()
        elif "Encryption" in line:
            # Eğer satır "Encryption" içeriyorsa, şifreleme tipini alır ve network_info sözlüğüne ekler
            network_info['Encryption'] = line.split(':')[1].strip()
            # network_info sözlüğünü network_list listesine ekler ve network_info sözlüğünü sıfırlar
            network_list.append(network_info)
            network_info = {}
    
    return network_list  # Bulunan ağların listesini döner

# Ana program
networks = list_available_networks()  # Fonksiyonu çağırır ve sonuçları networks değişkenine atar

# Bulunan Wi-Fi ağlarını ekrana yazdırır
print("Available Wi-Fi Networks:")
print("---------------------------------")
for i, network in enumerate(networks):
    print(f"{i+1}. SSID: {network['SSID']}")  # Ağın SSID'sini ekrana yazdırır
    print(f"   BSSID: {network.get('BSSID', 'N/A')}")  # Ağın BSSID'sini ekrana yazdırır, yoksa 'N/A' yazdırır
    print(f"   Signal Strength: {network.get('Signal', 'N/A')} dBm")  # Ağın sinyal gücünü ekrana yazdırır, yoksa 'N/A' yazdırır
    print(f"   Authentication: {network['Authentication']}")  # Ağın doğrulama tipini ekrana yazdırır
    print(f"   Encryption: {network['Encryption']}")  # Ağın şifreleme tipini ekrana yazdırır
    print(f"   Radio type: {network.get('Radio type', 'N/A')}")  # Ağın radyo tipini ekrana yazdırır, yoksa 'N/A' yazdırır
    print("---------------------------------")  # Ayrım çizgisi ekrana yazdırır
