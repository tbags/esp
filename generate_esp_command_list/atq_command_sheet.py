#! /usr/bin/python

import esp_command_map_pb2
import sys

_KNOWN_COMMANDS_NA = ["AT","AT+RST","AT+CIPSTATUS","AT+GMR"]
_KNOWN_COMMANDS_RA = ["AT+CWJAP","AT+CWSAP","AT+CWMODE","AT+CIPSEND","AT+CIPSTART","AT+CIPSERVER","AT+CIPSTO","AT+CIOBAUD"]

def GenCommandFile(proto, index):
 proto.generic_trm = raw_input("Enter generic ATQi(this means that you'd wirte a coloquial term): ")
 proto.at_command = raw_input("enter ARQ command (as visible in the data sheet): ")
 proto.order = index
 if(raw_input("do you intend to pass arguments for the command?(y/n)")[0] == 'y' ):
  if proto.at_command in _KNOWN_COMMANDS_RA:
   "check for type and collect data"
   print "let's collect details 1 by 1"
   NumParams=raw_input("How many arguments are you going to pass? (1 through 5)")
   Params = []
   for item in range(0,NumParams):
     Params.append(raw_input("enter parameter"))
  else:
   print "Hola we do not collect arguments for this command"

 return proto

def GenCode(input_file, language):
 pass


def main():
 input_proto = esp_command_map_pb2.AtCommand()
 index = raw_input("index you wish to start(0 ideally)")
 while (raw_input("do you wish to quit?(y/n)") == 'y'):
  print "we wish to collect command; follow the command list"
  p = GenCommandFile(input_proto.at_map.add(), index)
  index = index + 1
 i = raw_input("gen C or Python fuction? (c/p)") 
 GenCode(command_file,i) 

if __name__ == '__main__':
 main()
