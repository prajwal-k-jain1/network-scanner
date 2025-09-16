#!/usr/bin/env python
import scapy.all as scapy
import optparse
def scan(ip):
    arp_request=scapy.ARP(pdst=ip)
    # print(arp_request.summary())
    # print(scapy.ls(scapy.ARP()))
    # arp_request.show()
    ethernet=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # print(ethernet.summary())
    # scapy.ls(scapy.Ether())
    # ethernet.show()
    broadcast_request=ethernet/arp_request
    # broadcast_request.show()
    # answered,unanswered=scapy.srp(broadcast_request,timeout=1)
    # print(answered.summary())
    answered=scapy.srp(broadcast_request, timeout=1,verbose=False)[0]
    clients_list=[]
    for element in answered:
        # print(element[1])
        client_dict={"ip":element[1].psrc,"mac":element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list
def print_results(results_list):
    print("ip\t\t\t\t\tmac\n---------------------------------")
    for i in results_list:
        print(i["ip"]+'\t\t'+i["mac"])
def get_subnet_value():
    parser=optparse.OptionParser()
    parser.add_option('--ip','--ip_adress',dest="ip_adress",help="this options is used to specify the ip adress")
    parser.add_option('--s','--subnet',dest="subnet",help="this options is used to specify the subnet")
    values=parser.parse_args()[0]
    if(values.ip_adress):return values.ip_adress
    if(values.subnet):return values.subnet

ask_ip=get_subnet_value()
results=scan(ask_ip)
print_results(results)




