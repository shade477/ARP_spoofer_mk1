import scapy
import optparse

def get_input():
    command = optparse.OptionParser()
    command.add_option("-t",dest="disguise_ip", help = "The ip to be used for disguise")
    command.add_option("-g", dest="Gateway_ip", help = "where to send packet")
    options = []
    options.append(command.parse_args())
    return options

print(get_input())