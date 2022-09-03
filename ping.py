import optparse as op

def ping():
    command = op.OptionParser()
    command.add_option("-t", dest = "target_ip", help = "Target to be pinged")
    options = command.parse_args()[0]
    if not options.target_ip:
        print("Enter Target")
        return options.target_ip

print(ping())