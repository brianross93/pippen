from flask import Flask, request, redirect, render_template, url_for


app = Flask(__name__, template_folder="templates")


@app.route('/')
def page():
    """Display the web page."""
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)