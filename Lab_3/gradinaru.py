import requests
import smtplib
from bs4 import BeautifulSoup
Parola = 'qijm jhlx rnrl wejl'
from apscheduler.schedulers.blocking import BlockingScheduler

#print(parola_google)
#mai jos adresa care primeste email-ul
to_addr_list = ['stefangradinaru23@gmail.com']
cc_addr_list = ['']
#mai jos adresa de email care trimite email-ul
sender = 'stefangradinaru23@.com'
subject = 'A scazut pretul la produsul dorit'
counter = 0

def sendemail(sender, message, subject, to_addr_list, cc_addr_list=[]):
    try:
        smtpserver = 'smt.gmail.com:587'
        header = 'From: %s\n' % sender
        header+= 'To: %s\n' % ','.join(to_addr_list)
        header+= 'cc: %s\n' % ','.join(cc_addr_list)
        header+= 'Subject; %s\n' % subject
        message = header + message
        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(sender, Parola)
        problems=server.sendmail(sender,to_addr_list, message)
        server.quit()
        return True
    except Exception as e:
        print("A aparut o eroare in trimiterea email-ului")
        return False

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}
    
def Scrape():
    url = "https://www.emag.ro/telefon-mobil-apple-iphone-16-128gb-5g-black-mye73zd-a/pd/DHY67LYBM/"
    page = requests.get(url, headers = headers, timeout=10,allow_redirects=True)
    soup = BeautifulSoup(page.text, 'html.parser')
    #print (soup.prettify())
    #print(soup.find_all('p'))
Scrape()

def data_scraping():
    req = requests.get("https://www.emag.ro/telefon-mobil-apple-iphone-16-128gb-5g-black-mye73zd-a/pd/DHY67LYBM/")
    soup = BeautifulSoup(req.text, 'html.parser')
    pret = soup.find('p', attrs={'class':'product-new-price'}).text
    print(pret)
    pret = pret[0:5]
    pret = pret.replace(".","")
    pret = int(pret)
    pret_de_referinta = 4.749
    titlu_produsului = data_nume()
    ratingul_produsului = rating_produs()
    if(pret < pret_de_referinta and counter == 0):
        print("Pretul este mai mic decat pretul de referinta")
        mesaj = f"Pretul actual; {pret} RON\n"
        mesaj+= f"A scazut pretul la {titlu_produsului}\n"
        mesaj+= f"Ratingul produsului {rating_produs}\n"
        sendemail(sender,mesaj,subject,to_addr_list,cc_addr_list=[])
    else:
        print("Pretul este mai mare sau egal cu pretul de referinta")
        print(pret)
        


def data_nume():
    req = requests.get("https://www.emag.ro/telefon-mobil-apple-iphone-16-128gb-5g-black-mye73zd-a/pd/DHY67LYBM/")
    soup = BeautifulSoup(req.text, "html.parser")
    nume_produs = soup.find('h1', attrs={'class':'page-title'}).text
    print(nume_produs)

def rating_produs():
    req = requests.get("https://www.emag.ro/telefon-mobil-apple-iphone-16-128gb-5g-black-mye73zd-a/pd/DHY67LYBM/")
    soup = BeautifulSoup(req.text, "html.parser")
    rating = soup.find('p', attrs={'class':'review-rating-data'}).text
    print("Rating =", rating)
    
scheduler = BlockingScheduler()
scheduler.add_job(data_scraping, 'interval', seconds=10)
scheduler.start()

