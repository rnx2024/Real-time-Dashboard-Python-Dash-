from layout import app  # Import the app layout
import callbacks  # This will register all the callbacks
import webbrowser
import threading

def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050")

if __name__ == '__main__':
    threading.Timer(1, open_browser).start()
    app.run_server(debug=True)
