#!usr/bin/python3
import os 
target=input("please enter domain to scan: ")
os.system(f"nmap {target}")
