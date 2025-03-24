from flask import Flask, render_template_string, Response  
import mirana  

app = Flask(__name__)  

@app.route("/")  
def dashboard():  
    return render_template_string('''  
    <!DOCTYPE html>  
    <html lang="en">  
    <head>  
        <meta charset="UTF-8">  
        <meta name="viewport" content="width=device-width, initial-scale=1.0">  
        <title>Mirana Dashboard</title>  
        <style>  
            body { background-color: #000; color: #00ff00; font-family: 'Courier New', monospace; }  
            h1 { text-align: center; font-size: 2.5em; text-shadow: 0 0 5px #00ff00; }  
            .menu { display: flex; justify-content: space-around; margin: 20px; }  
            .menu a { color: #00ff00; text-decoration: none; font-size: 1.2em; }  
            .alerts, .live-monitoring, .graphs { margin: 20px; padding: 10px; border: 1px solid #00ff00; border-radius: 5px; }  
            .alert-card { background-color: #111; padding: 10px; margin: 5px; border-radius: 5px; color: red; }  
            .logo { text-align: center; margin-top: 20px; }  
            .footer { text-align: center; margin-top: 20px; color: #00ff00; }  
            @keyframes glow {  
                0% { text-shadow: 0 0 5px #00ff00; }  
                50% { text-shadow: 0 0 20px #00ff00; }  
                100% { text-shadow: 0 0 5px #00ff00; }  
            }  
            h1, .menu a { animation: glow 2s infinite; }  
        </style>  
    </head>  
    <body>  
        <div class="logo">  
            <img src="https://example.com/logo.png" alt="Logo" width="100">  
        </div>  
        <h1>Mirana - Cyber Defense System</h1>  
        <div class="menu">  
            <a href="#alerts">Alerts</a>  
            <a href="#live-monitoring">Live Monitoring</a>  
            <a href="#graphs">Graphs</a>  
        </div>  
        <div id="alerts" class="alerts">  
            <h2>Alerts</h2>  
            <div id="alert-list"></div>  
        </div>  
        <div id="live-monitoring" class="live-monitoring">  
            <h2>Live Network Flow</h2>  
            <div id="live-flow"></div>  
        </div>  
        <div id="graphs" class="graphs">  
            <h2>Traffic Statistics</h2>  
            <canvas id="traffic-chart"></canvas>  
        </div>  
        <div class="footer">  
            <p>Made by Uzair @xunsec</p>  
        </div>  
        <script>  
            const eventSource = new EventSource("/stream");  
            const alertList = document.getElementById("alert-list");  

            eventSource.onmessage = function(event) {  
                const newAlert = document.createElement("div");  
                newAlert.className = "alert-card";  
                newAlert.textContent = event.data;  
                alertList.appendChild(newAlert);  
            };  
        </script>  
    </body>  
    </html>  
    ''')  

@app.route("/stream")  
def stream():  
    def generate():  
        while True:  
            if mirana.alerts:  
                yield f"data: {mirana.alerts.pop(0)}\n\n"  
    return Response(generate(), mimetype="text/event-stream")  

if __name__ == "__main__":  
    print("Mirana - Made by Uzair @xunsec")  
    import threading  
    threading.Thread(target=mirana.start_sniffing).start()  
    app.run(debug=True)  
