def show_summary(ip, status, os_name, port_data, scan_time):

    print("\n")
    print("=" * 45)
    print("        NETWORK SCAN SUMMARY")
    print("=" * 45)


    print(f"\nTarget IP        : {ip}")

    if status.upper() == "UP":
        print("Status           : 🟢 ONLINE")
    else:
        print("Status           : 🔴 OFFLINE")


    print(f"Operating System : {os_name}")

    print(f"Open Ports       : {len(port_data)}")

    print(f"Scan Duration    : {scan_time:.2f} seconds")


    # Risk calculation

    if len(port_data) == 0:
        risk = "LOW"

    elif len(port_data) <= 3:
        risk = "MEDIUM"

    else:
        risk = "HIGH"


    print(f"Risk Level       : {risk}")


    print("\n" + "=" * 45)