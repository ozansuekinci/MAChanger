import optparse
import subprocess

parse_object=optparse.OptionParser()

parse_object.add_option("-i","--interface",dest="interface",help="Way to change interface")
parse_object.add_option("-m","--mac",dest="mac_adress",help="input a new mac adress")

(user_inputs,arguments) = parse_object.parse_args()

user_interface=user_inputs.interface
user_mac_adress=user_inputs.mac_adress

print("MAChanger on fire!!")

subprocess.call(["ifconfig",user_interface,"down"])
subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_adress])
subprocess.call(["ifconfig",user_interface,"up"])
