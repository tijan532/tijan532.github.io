from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/')
def index():

    
    return render_template('zac_str.html')


@app.route('/tehnologije')
def tehnologije():

    return render_template('tehnologije.html')

@app.route('/zgodovina')	
def zgodovina():

    return render_template('zgodovina.html')

@app.route('/modeli')
def modeli():

    return render_template('modeli.html')


@app.route('/N07')
def N07():
    return render_template('N07.html')

@app.route('/AMD_XTX')
def AMD_XTX():
    return render_template('AMD_XTX.html')

@app.route('/AMD_GRE')
def AMD_GRE():
    return render_template('AMD_GRE.html')

@app.route('/N09')
def N09():
    return render_template('N09.html')

@app.route('/N06')
def N06():
    return render_template('N06.html')
@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')





@app.route('/getHistory')
def getHistory():
    # Pridobitev ID-jev razdelkov
    sections_url = "https://en.wikipedia.org/w/api.php?action=parse&format=json&page=Graphics_card&prop=sections"
    sections_response = requests.get(sections_url).json()
    
    # Poiščemo ID razdelka "History"
    section_id = None
    for section in sections_response["parse"]["sections"]:
        if section["line"].lower() == "history":
            section_id = section["index"]
            break
    
    if section_id is None:
        return jsonify({"error": "Section 'History' not found"})
    
    # Pridobitev vsebine razdelka "History"
    content_url = f"https://en.wikipedia.org/w/api.php?action=parse&format=json&page=Graphics_card&prop=text&section={section_id}"
    content_response = requests.get(content_url).json()
    '''
Seveda! Tukaj je primer Python kode, ki uporablja knjižnico BeautifulSoup za odstranjevanje vseh povezav (<a href="...">) iz HTML-ja. Knjižnico lahko namestiš s pip:

bash
Kopiraj
Uredi
pip install beautifulsoup4
Tukaj je Python koda:

python
Kopiraj
Uredi
from bs4 import BeautifulSoup

# Primer HTML besedila
html = "<html><body><a href='https://example.com'>Povezava</a><p>To je besedilo.</p></body></html>"

# Ustvarimo BeautifulSoup objekt
soup = BeautifulSoup(html, 'html.parser')

# Najdemo vse <a> elemente in jih odstranimo
for link in soup.find_all('a'):
    link.decompose()

# Izpišemo modificirani HTML brez povezav
modified_html = str(soup)
print(modified_html)'''
    
    # Vsebina razdelka (HTML)
    history_content = content_response["parse"]["text"]["*"]
    return jsonify({"history_content": history_content})

app.run(host='0.0.0.0', port=8080,debug=True)
