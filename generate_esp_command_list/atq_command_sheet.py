#! /usr/bin/python

import esp_command_map_pb2
import sys

_KNOWN_COMMANDS_NA = ["AT","AT+RST","AT+CIPSTATUS","AT+GMR"]
_KNOWN_COMMANDS_RA = []

def GenCommandFile(proto):
 proto.generic_trm = raw_input("Enter generic ATQi(this means that you'd wirte a coloquial term): ")
 proto.at_command = raw_input("enter ARQ command (as visible in the data sheet): ")

 if(raw_input("do you intend to pass arguments for the command?(y/n)")[0] == 'y' or 'Y'):
  if proto.at_command IN _KNOWN_COMMANDS_RA:
   "check for type and collect data"
   
  else:
   print "Hola we do not collect arguments for this command"
   

