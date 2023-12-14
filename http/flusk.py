from flask import Flask, render_template
import platform
import subprocess
import psutil
import requests

THINGSPEAK_API_KEY = 'DD6SO7KDVHVT2IEY'

app = Flask(__name__, template_folder = 'template')

def memory_usage_task():
    """Фоновая задача для отправки информации о занятой памяти."""
    while True:
        memory_usage = psutil.virtual_memory()
        requests.post(f'https://api.thingspeak.com/update?api_key={THINGSPEAK_API_KEY}&field1={(memory_usage)}')
        time.sleep(30)

@app.route('/')
def index():
    pi_info = {
        "System": platform.system(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Processor": platform.processor(),
        "Uptime": subprocess.check_output(["uptime"]).decode("utf-8")
    }
    return render_template('index.html', pi_info=pi_info)

@app.route('/shutdown', methods=['POST'])
def shutdown():
    # Выполняем команду выключения
    subprocess.call(['sudo', 'shutdown', '-h', 'now'])
    return None

if __name__ == '__main__':
    memory_thread = threading.Thread(target=memory_usage_task)
    app.run(debug=True, host='0.0.0.0')
