from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired

class RFCalculatorForm(FlaskForm):
    frequence = FloatField('Fréquence en MHz', validators=[DataRequired()])
    distance = FloatField('Distance en Km', validators=[DataRequired()])
    pire = FloatField('Pire en dBm', validators=[DataRequired()])
    rxgain = FloatField('Rxgain en dBi', validators=[DataRequired()])
    sensi = FloatField('Sensibilité en dBm', validators=[DataRequired()])
    distance1 = FloatField('Distance1 en mètres', validators=[DataRequired()])
    distance2 = FloatField('Distance2 en mètres', validators=[DataRequired()])
    altso = FloatField('Altitude obstacle en mètres', validators=[DataRequired()])
    ho = FloatField('Hauteur obstacle en mètres')
    altA = FloatField('Altitude bâtiment A en mètres', validators=[DataRequired()])
    hbatA = FloatField('Hauteur bâtiment A en mètres', validators=[DataRequired()])
    altB = FloatField('Altitude bâtiment B en mètres', validators=[DataRequired()])
    hbatB = FloatField('Hauteur bâtiment B en mètres', validators=[DataRequired()])
    submit = SubmitField('Calculer')
