import threading
import subprocess

def run_main():
    subprocess.run(["python", "main.py"])

def run_webserver():
    subprocess.run(["python", "webserver.py"])

if __name__ == "__main__":
    # Создаем два потока для выполнения main.py и webserver.py
    main_thread = threading.Thread(target=run_main)
    webserver_thread = threading.Thread(target=run_webserver)

    # Запускаем оба потока
    main_thread.start()
    webserver_thread.start()

    # Ожидаем завершение обоих потоков
    main_thread.join()
    webserver_thread.join()
