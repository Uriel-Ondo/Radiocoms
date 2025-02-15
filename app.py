import os
from flask import Flask, render_template, request
from forms import RFCalculatorForm
from radiocoms.utils import fsl, margelibre, rayonfresnel, longueurpylone
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Pour développement ; pour production, utiliser une variable d’environnement
csrf = CSRFProtect(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = RFCalculatorForm()
    if form.validate_on_submit():
        # Récupérer les données
        frequence = form.frequence.data
        distance = form.distance.data
        pire = form.pire.data
        rxgain = form.rxgain.data
        sensi = form.sensi.data
        distance1 = form.distance1.data
        distance2 = form.distance2.data
        altso = form.altso.data
        ho = form.ho.data
        altA = form.altA.data
        hbatA = form.hbatA.data
        altB = form.altB.data
        hbatB = form.hbatB.data

        # Calculs
        fsl_value = fsl(frequence, distance)
        marge_libre = margelibre(pire, fsl_value, rxgain, sensi)
        fresnel_radius = rayonfresnel(distance1, distance2, frequence)
        pylonA_height = longueurpylone(altso, ho, fresnel_radius, altA, hbatA)
        pylonB_height = longueurpylone(altso, ho, fresnel_radius, altB, hbatB)

        # Déterminer la qualité de la liaison
        quality = ""
        if marge_libre < 15:
            quality = "Marge libre inférieure à 15 dB : Liaison non optimale."
        elif 15 <= marge_libre <= 30:
            quality = "Marge libre entre 15 et 30 dB : Liaison bonne."
        else:
            quality = "Marge libre supérieure à 30 dB : Liaison excellente."

        return render_template('index.html', form=form, fsl_value=fsl_value, marge_libre=marge_libre,
                               fresnel_radius=fresnel_radius, pylonA_height=pylonA_height,
                               pylonB_height=pylonB_height, quality=quality)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
