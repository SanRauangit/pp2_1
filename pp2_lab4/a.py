import json
import os
def parse_interface_data():
    filename = 'sample-data.json'
    
    if not os.path.exists(filename):
        print("Error: sample-data.json file not found!")
        return
    
    with open(filename, 'r') as file:
        data = file.read()
    
    if len(data.strip()) == 0:
        print("Error: File is empty!")
        return
    data = json.loads(data)
    interfaces = data.get('imdata', [])
    
    print("Interface Status")
    print("=" * 80)
    print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
    print("-" * 80)

    for interface in interfaces:
        attr = interface.get('l1PhysIf', {}).get('attributes', {})
        
        dn = attr.get('dn', '')
        descr = attr.get('descr', '')
        speed = attr.get('speed', '')
        mtu = attr.get('mtu', '')
        
        print(f"{dn:<50} {descr:<20} {speed:<8} {mtu:<6}")

if __name__ == "__main__":
    parse_interface_data()