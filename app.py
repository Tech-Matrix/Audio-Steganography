from flask import Flask, render_template, request, redirect
import os
import os.path
from encodeco import encode, decode

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    decodedString = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")
        
        # if "file" not in request.files and "message" not in request.form.get:
        #     return redirect(request.url)
        
        file = request.files["file"]
        message = request.form.get("message")
        # if file.filename == "" and message == "":
        #     return redirect(request.url)
        
        save_path = os.path.join("", "temp.wav")
        
        if message:
                print("Received message: ", message)
                f = open("message.txt", 'w')
                f.write(message)
                f.close()
        if file:
            file.save(save_path)
            print("Audio File received")
            f = open("message.txt", 'r')
            m = f.read()
            f.close()
            location = encode(save_path, m)
            decodedString = decode(location)
            print(decodedString)

    return render_template("index.html", message = decodedString)


if(__name__ == "__main__"):
    app.run(debug=True, threaded=True) 