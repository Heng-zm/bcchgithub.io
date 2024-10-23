from flask import Flask, request, render_template
import pyautogui

app = Flask(__name__)

# Serve the touchpad interface
@app.route('/')
def index():
    return render_template('index.html')

# Handle mouse movement (relative movement)
@app.route('/move', methods=['POST'])
def move():
    dx = int(request.form['dx'])
    dy = int(request.form['dy'])
    pyautogui.moveRel(dx, dy)  # Move the mouse relative to its current position
    return 'Moved'

# Handle mouse click
@app.route('/click', methods=['POST'])
def click():
    pyautogui.click()
    return 'Clicked'

if __name__ == '__main__':
    app.run(host='192.168.18.4', port=5000)
