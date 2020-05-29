function sprawdz(){
    var imieInput = capitalize(document.getElementById("imie").value);
    var nazwiskoInput = capitalize(document.getElementById("nazwisko").value);
    document.getElementById("inicjaly").value = imieInput.charAt(0)+nazwiskoInput.charAt(0);
    document.getElementById("imie1").value=imieInput;
    document.getElementById("nazwisko1").value=nazwiskoInput;
    var plec;
    if ((imieInput.charAt(imieInput.length-1).toUpperCase())=='A'){
        plec="Kobieta";
    }else{
        plec="Mężczyzna";
    }
    document.getElementById("plec").value=plec;
}

function capitalize(dane){
    dane = dane.toLowerCase();
    return dane.charAt(0).toUpperCase()+dane.slice(1);
}