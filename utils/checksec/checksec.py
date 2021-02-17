#!/usr/bin/env python3
import argparse
import subprocess
import json


def check_value_is_yes(name,value):
    if value == 'yes' or value == 'full': 
        print(name+': OK')
        return 0
    else:
        print(name+': FAIL')
        return 1

def check_value_is_no(name,value):
    if value == 'no': 
        print(name+': OK')
        return 0
    else:
        print(name+': FAIL')
        return 1


def main():
    #Setup argument
    parser = argparse.ArgumentParser()
    parser.add_argument("-b","--binary", help="Path to binary file", required=True)
    args = parser.parse_args()
    file_name = args.binary
    
    #Run checksec
    checksec_data = subprocess.run(['checksec', '--output=json', '--file='+ file_name], universal_newlines=True, stdout=subprocess.PIPE)
    checksec_json = json.loads(checksec_data.stdout)
    print('Checksec Results')
    print('----------------')
    error_sum = 0
    file_name = list(checksec_json.keys())[0]
    error_sum += check_value_is_yes('RELRO',checksec_json[file_name]['relro'])
    error_sum += check_value_is_yes('CANARY',checksec_json[file_name]['canary'])
    error_sum += check_value_is_yes('NX',checksec_json[file_name]['nx'])
    error_sum += check_value_is_yes('PIE',checksec_json[file_name]['pie'])
    error_sum += check_value_is_no('RPATH',checksec_json[file_name]['rpath'])
    error_sum += check_value_is_no('RUNPATH',checksec_json[file_name]['runpath'])
    error_sum += check_value_is_no('SYMBOLS',checksec_json[file_name]['symbols'])
    error_sum += check_value_is_yes('FORTIFY',checksec_json[file_name]['fortify_source'])

    return error_sum

if __name__ == "__main__":
    main()