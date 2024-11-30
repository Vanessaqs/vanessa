from flask import Flask,render_template, request


import requests

app = Flask(__name__)

def get_weather_data(city:str):
    """
    Funcion que espera el nombre de la ciudad por parametro, para luego realizar un get a openweather
    para consultar el clima de la ciudad ingresada
    """
    API_KEY = 'c5b036f5f16b6e2b5f0ad22ee4bdf43a'
    idioma = 'es'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang={idioma}&appid={API_KEY}'
    r = requests.get(url).json()
    return r

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', ciudad='', humedad='',presion='', descripcion='', icon = '',latitud='', logitud='' ,cod = '')

    ciudad= request.form.get('txtCiudad')
    if ciudad:
        data=get_weather_data(ciudad) #lo que trae el api
        cod=data.get('cod')
        if cod != 200:
            return render_template('index.html', ciudad='', humedad='',presion='', descripcion='', icon = '' , latitud='', logitud='' ,cod = cod)
        latitud=data.get('coord').get('lat')
        logitud=data.get('coord').get('lon')
        humedad=data.get('main').get('humidity')
        presion=data.get('main').get('pressure')
        descripcion=data.get('weather')[0].get('description')
        icon=data.get('weather')[0].get('icon')
        return render_template('index.html', ciudad=ciudad, humedad=humedad,presion=presion, descripcion=descripcion, icon = icon ,latitud=latitud, logitud=logitud , cod = cod)
    else:
        return render_template('index.html', ciudad='', humedad='',presion='', descripcion='', icon = '',latitud='', logitud='' ,cod = '')

@app.route('/vanessa_quispe_curriculum.html')
def vanessa_quispe_curriculum():
    return render_template('vanessa_quispe_curriculum.html')

if __name__ == "__main__":
    app.run(debug=True) 