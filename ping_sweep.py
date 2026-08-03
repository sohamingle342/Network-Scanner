import ipaddress
import nmap

# Create the Nmap scanner
scanner = nmap.PortScanner()


def ping_sweep(network):

    try:
        # Convert text into a network object
        network = ipaddress.ip_network(network, strict=False)

        print("=" * 40)
        print("        PING SWEEP")
        print("=" * 40)

        live_hosts = 0

        # Loop through every host in the network
        for host in network.hosts():

            try:
                # Host Discovery (-sn)
                scanner.scan(str(host), arguments="-sn")

                # Check if the host is alive
                if str(host) in scanner.all_hosts():

                    if scanner[str(host)].state() == "up":
                        print(f"✅ {host} is UP")
                        live_hosts += 1

            except Exception:
                # Skip any host that causes an error
                continue

        print("\n" + "=" * 40)
        print(f"Total Live Hosts : {live_hosts}")
        print("=" * 40)

    except ValueError:
        print("❌ Invalid Network Address!")


# -------- Test --------
ping_sweep("10.10.104.0/29")