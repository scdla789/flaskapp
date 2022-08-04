from flask import Flask, render_template



app = Flask(__name__,
            static_url_path='',
            static_folder='project/static',
            template_folder='project/templates')

@app.route("/")
def serveStatic():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)










