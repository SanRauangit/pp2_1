import json

def parse_interface_data():
    """Parse JSON data and display interface status in formatted table"""
    
    try:
        with open('sample-data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Error: sample-data.json file not found!")
        return
    except json.JSONDecodeError:
        print("Error: Invalid JSON format!")
        return
    
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