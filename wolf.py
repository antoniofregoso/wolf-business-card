# coding: utf-8
from flask import Flask, render_template, request, flash, redirect, url_for
from models.odoo import server
from config import   Config 
from models.forms import LeadForm
from models.vcard import vcard

app = Flask(__name__)
app.config.from_object(Config)
vcard().get_qr(app.config['OPTIONS']['vcard'])

@app.route('/')
@app.route('/index')
def index():
    qs = request.args
    form = LeadForm()
    form.utm_campaign.data = request.args.get('utm_campaign')
    form.utm_source.data =  request.args.get('utm_source')
    form.utm_medium.data=  request.args.get('utm_medium')
    form.utm_content.data = request.args.get('utm_content')
    form.utm_term.data = request.args.get('utm_term')
    theme = bool(app.config['OPTIONS']['wolf_theme'])
    if form.validate_on_submit():
        return redirect(url_for('gracias'))
    return render_template('index.html', theme=theme, title='Antonio Fregoso', q=qs, form=form, ga=app.config['OPTIONS']['google'])


@app.route('/gracias', methods=['GET', 'POST'])
def gracias():
    if request.method == 'POST':
        id_lead = server().set_lead(request.form)
        return render_template('lead.html', title='Sign In')
    else:
        return 'Puto'



if __name__ == '__main__':
    app.run(debug=False)
    
    