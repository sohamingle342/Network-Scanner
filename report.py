from datetime import datetime
import csv
import json


# Save TXT Report
def save_txt_report(ip, status, os_name, port_data, scan_time, vulnerabilities):

    current_time = datetime.now()

    with open("scan_report.txt", "w") as file:

        file.write("=" * 40 + "\n")
        file.write("NETWORK SCANNER REPORT\n")
        file.write("=" * 40 + "\n\n")


        file.write(
            f"Date : {current_time.strftime('%d-%m-%Y')}\n"
        )

        file.write(
            f"Time : {current_time.strftime('%I:%M:%S %p')}\n\n"
        )


        file.write(f"Target IP        : {ip}\n")
        file.write(f"Host Status      : {status.upper()}\n")
        file.write(f"Operating System : {os_name}\n")
        file.write(f"Scan Duration    : {scan_time:.2f} seconds\n\n")


        file.write("-" * 40 + "\n")
        file.write("Open Ports\n")
        file.write("-" * 40 + "\n")


        for port in port_data:

            file.write(
                f"{port['port']:<6} "
                f"{port['service']:<15} "
                f"{port['product']} "
                f"{port['version']}\n"
            )

        file.write("\n")
        file.write("-" * 40 + "\n")
        file.write("Security Findings\n")
        file.write("-" * 40 + "\n")


        if vulnerabilities:

            for issue in vulnerabilities:

                file.write(
                    f"Port {issue['port']} : "
                    f"{issue['issue']}\n"
                )

        else:

            file.write(
                "No obvious issues detected\n"
            )


        file.write("\n")
        file.write("=" * 40 + "\n")
        file.write("Scan Completed Successfully\n")
        file.write("=" * 40 + "\n")





# Save CSV Report
def save_csv_report(port_data):

    with open(
        "scan_report.csv",
        "w",
        newline=""
    ) as csv_file:


        writer = csv.writer(csv_file)


        writer.writerow(
            [
                "Port",
                "Service",
                "Product",
                "Version"
            ]
        )


        for port in port_data:

            writer.writerow(
                [
                    port["port"],
                    port["service"],
                    port["product"],
                    port["version"]
                ]
            )





# Save JSON Report
def save_json_report(ip, status, os_name, port_data, scan_time):


    report = {

        "date":
        datetime.now().strftime("%d-%m-%Y"),

        "time":
        datetime.now().strftime("%I:%M:%S %p"),

        "target_ip":
        str(ip),

        "host_status":
        str(status).upper(),

        "operating_system":
        str(os_name),

        "scan_duration":
        f"{scan_time:.2f} seconds",

        "open_ports":
        port_data
    }



    with open(
        "scan_report.json",
        "w"
    ) as json_file:


        json.dump(
            report,
            json_file,
            indent=4,
            default=str
        )