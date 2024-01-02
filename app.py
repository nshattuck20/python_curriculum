from flask import Flask, render_template, url_for
from about import about_blueprint 

app = Flask(__name__)
app.register_blueprint(about_blueprint, url_prefix='/about')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)

    with app.test_request_context(): 
        home_url = url_for('index')
        about_url = url_for('show_about', page='about')

        print("Generated URLs:")
        print("Home URL:", home_url)
        print("About URL", about_url)

 