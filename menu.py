def show_menu():

    print("\nChoose Scan Type")
    print("-" * 30)
    print("1. Fast Scan")
    print("2. Service Version Scan")
    print("3. OS Detection")
    print("4. Full Scan")
    print("5. Custom Port Scan")
    print("6. View Scan History")
    print("7. Exit")

    return input("\nEnter your choice: ").strip()