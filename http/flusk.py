from flask import Flask, render_template
import platform
import subprocess

app = Flask(__name__, template_folder = 'template')

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
    app.run(debug=True, host='0.0.0.0')
