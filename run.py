import threading
import subprocess
import os

current_directory = os.getcwd()

main_script_path = os.path.join(current_directory, "src", "main.py")
webserver_script_path = os.path.join(current_directory, "http", "webserver.py")
def run_main():
    subprocess.run(["python", main_script_path])

def run_webserver():
    subprocess.run(["python", webserver_script_path])

if __name__ == "__main__":
    # Создаем два потока для выполнения main.py и webserver.py
    main_thread = threading.Thread(target=run_main)
    webserver_thread = threading.Thread(target=run_webserver)

    # Запускаем оба потока
    main_thread.start()
    webserver_thread.start()