import time
import logging

from colorama import Fore, init

from utils import banner
from menu import show_menu
from scanner import scan_host
from report import save_txt_report, save_csv_report, save_json_report
from database import create_database, save_scan, show_history
from summary import show_summary
from report import save_txt_report, save_csv_report, save_json_report
from logger_config import setup_logger
from config_loader import load_config
from vulnerability import check_vulnerabilities
from logger import write_log

init(autoreset=True)
create_database()
logger = setup_logger()
config = load_config()


# Display Banner
banner()


# Show Menu
choice = show_menu()


ports = None


# Custom Port Scan
if choice == "5":
    ports = input("\nEnter Port(s) (Example: 22,80,443): ").strip()


# Exit
if choice == "6":

    show_history()

    exit()



if choice == "7":
    print("Goodbye!")
    exit()


# Get Target IPs
ips = input(
    "\nEnter IP Addresses (comma separated): "
).strip().split(",")


# Remove spaces
ips = [ip.strip() for ip in ips]


for ip in ips:

    try:

        print("\n" + "=" * 50)
        print(f"Scanning {ip}")
        print("=" * 50)


        print("\nScanning...\n")
        logger.info(f"Scan started for {ip}")
        write_log(f"Started scan for {ip}")


        # Start Timer
        start = time.time()


        # Scan Host
        results = scan_host(ip, choice, ports)


        if results is None:
            print("Invalid Choice!")
            continue


        # End Timer
        end = time.time()

        scan_time = end - start


        # Extract Results
        status = results["status"]
        os_name = results["os"]
        port_data = results["ports"]
        vulnerabilities = check_vulnerabilities(port_data)


        # Display Results
        print(f"Target IP        : {ip}")
        print(Fore.GREEN + f"Host Status      : {status.upper()}")
        print(Fore.CYAN + f"Operating System : {os_name}")
        print(f"Scan Duration    : {scan_time:.2f} seconds")


        print("\n" + "-" * 40)
        print(Fore.YELLOW + "Open Ports")
        print("-" * 40)


        for port in port_data:

            print(
                Fore.GREEN +
                f"{port['port']:<6} "
                f"{port['service']:<15} "
                f"{port['product']} "
                f"{port['version']}"
            )
# ==============================
# SECURITY FINDINGS
# ==============================    

        print("\n" + "-" * 40)
        print("Security Findings")
        print("-" * 40)


        if vulnerabilities:

            for issue in vulnerabilities:

                print(
                    f"⚠ Port {issue['port']} : {issue['issue']}"
                )

        else:

            print("No obvious issues detected")




        


        print("\n" + "=" * 40)
        print("Scan Completed Successfully")
        print("=" * 40)

        write_log(f"Completed scan for {ip}")
        logger.info(
            f"Scan completed for {ip}. Ports found: {len(port_data)}"
        )
        show_summary(
            ip,
            status,
            os_name,
            port_data,
            scan_time
        )
        print("=" * 40)



        # Save Reports

        save_txt_report(
            ip,
            status,
            os_name,
            port_data,
            scan_time,
            vulnerabilities
        )

        print("✅ TXT report saved")

        write_log("TXT report generated")


        save_csv_report(port_data)

        print("✅ CSV report saved")

        write_log("CSV report generated")


        save_json_report(
            ip,
            status,
            os_name,
            port_data,
            scan_time
        )

        print("✅ JSON report saved")

        write_log("JSON report generated")

        # Save scan history
        save_scan(
            ip,
            status,
            os_name,
            len(port_data),
            scan_time
        )

        write_log("Scan saved into SQLite database")

        print("✅ Scan history saved to database")



    except Exception as e:

        print("\nScan Failed For:", ip)
        print("Error:", e)