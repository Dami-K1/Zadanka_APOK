var EUR, USD, GBP

function PobierzKursWaluty(waluta){
    let xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) {
                var kursObj = JSON.parse(this.responseText)
                document.getElementById("data").innerHTML = kursObj.rates[0].effectiveDate
                document.getElementById(waluta).innerHTML = kursObj.rates[0].mid
                return kursObj.rates[0].mid
            }
        }
        // https://api.nbp.pl/
        xhttp.open("GET", "http://api.nbp.pl/api/exchangerates/rates/A/" +waluta+ "/?format=json");
        xhttp.send();
}

function PokazKursyWalutIDate() {
    PobierzKursWaluty("EUR")
    PobierzKursWaluty("USD")
    PobierzKursWaluty("GBP")
    PokazKalkulator()
}

function PokazKalkulator(){
    var x = document.getElementById("kalkulator")
    x.style.display = "block"
}

function CzytajKursy(){
    EUR = document.getElementById("EUR").innerHTML
    USD = document.getElementById("USD").innerHTML
    GBP = document.getElementById("GBP").innerHTML
}

function PLNfun(){
    CzytajKursy()
    var PLNi = document.getElementById("PLNinput").value
    document.getElementById("EURinput").value = (PLNi/EUR).toFixed(2)
    document.getElementById("USDinput").value = (PLNi/USD).toFixed(2)
    document.getElementById("GBPinput").value = (PLNi/GBP).toFixed(2)
    document.getElementById("EURinput").readOnly = true
    document.getElementById("USDinput").readOnly = true
    document.getElementById("GBPinput").readOnly = true
}

function EURfun(){
    CzytajKursy()
    var EURi = document.getElementById("EURinput").value
    document.getElementById("PLNinput").value = (EURi*EUR).toFixed(2)
    document.getElementById("USDinput").value = ((EURi*EUR)/USD).toFixed(2)
    document.getElementById("GBPinput").value = ((EURi*EUR)/GBP).toFixed(2)
    document.getElementById("PLNinput").readOnly = true
    document.getElementById("USDinput").readOnly = true
    document.getElementById("GBPinput").readOnly = true
}

function USDfun(){
    CzytajKursy()
    var USDi = document.getElementById("USDinput").value
    document.getElementById("PLNinput").value = (USDi*USD).toFixed(2)
    document.getElementById("EURinput").value = ((USDi*USD)/EUR).toFixed(2)
    document.getElementById("GBPinput").value = ((USDi*USD)/GBP).toFixed(2)
    document.getElementById("PLNinput").readOnly = true
    document.getElementById("EURinput").readOnly = true
    document.getElementById("GBPinput").readOnly = true
}

function GBPfun(){
    CzytajKursy()
    var GBPi = document.getElementById("GBPinput").value
    document.getElementById("PLNinput").value = (GBPi*GBP).toFixed(2)
    document.getElementById("EURinput").value = ((GBPi*GBP)/EUR).toFixed(2)
    document.getElementById("USDinput").value = ((GBPi*GBP)/USD).toFixed(2)
    document.getElementById("PLNinput").readOnly = true
    document.getElementById("EURinput").readOnly = true
    document.getElementById("USDinput").readOnly = true
}

function Wyczysc()
{
    document.getElementById("PLNinput").value=""
    document.getElementById("EURinput").value=""
    document.getElementById("USDinput").value=""
    document.getElementById("GBPinput").value=""
    document.getElementById("PLNinput").readOnly = false
    document.getElementById("EURinput").readOnly = false
    document.getElementById("USDinput").readOnly = false
    document.getElementById("GBPinput").readOnly = false
}
