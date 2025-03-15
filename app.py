from flask import Flask, render_template_string  

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
            body { background-color: #1e1e1e; color: #ffffff; font-family: Arial, sans-serif; }  
            h1 { color: #00ff00; }  
        </style>  
    </head>  
    <body>  
        <h1>Mirana - Live Network Flow</h1>  
        <div id="live-packets"></div>  
        <script>  
            // Live updates ke liye JavaScript code  
        </script>  
    </body>  
    </html>  
    ''')  

if __name__ == "__main__":  
    app.run(debug=True)  
