import threading
import subprocess

def run_main():
    subprocess.run(["python", "./src/main.py"])

def run_webserver():
    subprocess.run(["python", "./http/webserver.py"])

if __name__ == "__main__":
    # Создаем два потока для выполнения main.py и webserver.py
    main_thread = threading.Thread(target=run_main)
    webserver_thread = threading.Thread(target=run_webserver)

    # Запускаем оба потока
    main_thread.start()
    webserver_thread.start()