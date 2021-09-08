from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        print("FORM DATA RECEIVED")
        
        if "file" not in request.files and "message" not in request.form.get:
            return redirect(request.url)
        
        file = request.files["file"]
        message = request.form.get("message")
        if file.filename == "" and message == "":
            return redirect(request.url)
        
        save_path = os.path.join("", "temp.wav")
        file.save(save_path)
        if file:
            print("Audio File received")
        if message:
                print("Received message: ", message)
        
            
    return render_template("index.html")

if(__name__ == "__main__"):
    app.run(debug=True, threaded=True) 