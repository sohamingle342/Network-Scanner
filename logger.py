from datetime import datetime


LOG_FILE = "scanner.log"


def write_log(message):

    current_time = datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )

    with open(LOG_FILE, "a") as file:

        file.write(
            f"[{current_time}] {message}\n"
        )