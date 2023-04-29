function getCountries(){
    fetch("https://restcountries.com/v3.1/all")
    .then(response => response.json())
    .then(data => {
        var countryNames = [];
        for (var i = 0; i < data.length; i++){
            countryNames.push(data[i].name.common);
        }
        countryNames.sort();
        var select = document.querySelector('#country')
        for (var i = 0; i < countryNames.length; i++){
            var option = document.createElement("option");
            option.value = countryNames[i];
            option.text = option.value;
            select.add(option);
        }
    })
    .catch(error => console.log("Error fetching countries: " + error));
}
document.addEventListener("DOMContentLoaded", () => {
    getCountries();
    document.querySelectorAll('.course-detail-button').forEach(element =>{
        element.onclick = () =>{
            var value = element.value;
            var options = document.querySelector('#courses').children;
            for(var i = 0; i < options.length; i++){
                if(options[i].value === value){
                    console.log(options[i].value)
                    setTimeout(options[i].setAttribute('selected', true), 0);
                    console.log(options[i].selected)
                    document.querySelector('#courses').children[3].setAttribute('selected', true)
                }
            }
        }
    })
})