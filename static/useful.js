function check_zip_code(){
    const zipCode = document.getElementById("zipCode")
    const street = document.getElementById("street")
    const neighborhood = document.getElementById("neighborhood")
    const city = document.getElementById("city")
    const state = document.getElementById("state")

    zipCode.addEventListener('input', (event) => {
        if(zipCode.value.length == 9){
            var url = "https://viacep.com.br/ws/" + zipCode.value + "/json/";

            var xhttp = new XMLHttpRequest();
            xhttp.open("GET", url, false);
            xhttp.send();
            response = xhttp.responseText;
            response = JSON.parse(response)
            if(response['erro'] == 'true'){
                alert('Insira um CEP Válido');
                zipCode.value = '';
                street.value = '';
                neighborhood.value = '';
                city.value = '';
                state.selectedIndex = 0;
            } else {
                street.value = response.logradouro
                neighborhood.value = response.bairro
                city.value = response.localidade
                var text = '';
                if(response['uf'] == 'SC'){
                    text = 'Santa Catarina'
                };
                for (var i = 0; i < state.options.length; i++) {
                    if (state.options[i].text === text) {
                        state.selectedIndex = i;
                        break;
                    };
                };
        };
        };
    }); 
};

function clear_results(){
    const chk1 = document.getElementById("switchSubscription")
    const sea = document.getElementById("searchGraduationCourse")
    const occupationArea = document.getElementById("occupationArea");

    occupationArea.addEventListener('change', (event) => {
        if (chk1.checked) {
            chk1.checked = false
        }
    });

    sea.addEventListener('keydown', (event) => {
        if (chk1.checked) {
            chk1.checked = false
        }
        var text = 'Área de atuação';
        $("#occupationArea").val(text);
    }); 
};

function check_date(){
    const date_initial = document.getElementById("date_initial");
    const date_final = document.getElementById("date_final");

   date_final.addEventListener('change', (event) => {

        if (date_initial.value > date_final.value) {
            alert('A data inicial não pode ser maior que a data final');
            date_final.value = ''
        };
    }); 
}