from scapy.all import sniff, IP, TCP  
from loguru import logger  

def packet_callback(packet):  
    if IP in packet:  
        src_ip = packet[IP].src  
        dst_ip = packet[IP].dst  
        if TCP in packet:  
            src_port = packet[TCP].sport  
            dst_port = packet[TCP].dport  
            logger.info(f"Packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")  

def start_sniffing():  
    logger.info("Starting packet sniffing...")  
    sniff(prn=packet_callback, store=False)  

if __name__ == "__main__":  
    start_sniffing()  
