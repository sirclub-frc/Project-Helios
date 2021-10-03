from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.htm')

@app.route('/about')
def about():
    return render_template('about.htm')

@app.route('/stereo-a')
def stereo_a():
    return render_template('stereo_a.htm')

@app.route('/parker-solar-probe')
def parker_solar_probe():
    return render_template('parker_solar_probe.htm')

@app.route('/osiris-rex')
def osiris_rex():
    return render_template('osiris_rex.htm')

@app.route('/pioneer-venus-orbiter')
def pioneer_venus_orbiter():
    return render_template('pioneer_venus_orbiter.htm')

if __name__ == '__main__':
    app.run(debug=True)