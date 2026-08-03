import nmap

scanner = nmap.PortScanner()


def scan_host(ip, choice, ports=None):

    if choice == "1":
        arguments = "-F"

    elif choice == "2":
        arguments = "-F -sV"

    elif choice == "3":
        arguments = "-F -O"

    elif choice == "4":
        arguments = "-F -sV -O"

    elif choice == "5":
        arguments = f" -p {ports} -sV"

    else:
        return None

    scanner.scan(ip, arguments=arguments)

    status = scanner[ip].state()

    try:
        os_name = scanner[ip]["osmatch"][0]["name"]
    except (KeyError, IndexError):
        os_name = "Could not detect"

    port_data = []

    for protocol in scanner[ip].all_protocols():

        for port in scanner[ip][protocol].keys():

            service = scanner[ip][protocol][port].get("name", "")
            product = scanner[ip][protocol][port].get("product", "")
            version = scanner[ip][protocol][port].get("version", "")

            port_data.append({
                "port": port,
                "service": service,
                "product": product,
                "version": version
            })

    return {
        "status": status,
        "os": os_name,
        "ports": port_data
    }