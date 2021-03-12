from flask import Flask, render_template
app = Flask(__name__, template_folder='template')
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/download')
def download():
    return send_file('resume5.pdf', as_attachment=True)



app.run(debug=True)
