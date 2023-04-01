 
 function get_data(){
    user = $('#id_user').val();
    nome = $('#id_nome').val();
    cpf = $('#id_cpf').val();
    email = $('#id_email').val();
    dtnasc = $('#id_dtnasc').val();
    celular = $('#id_celular').val();
    sexo = $('#id_sexo :selected').text();


    data = new FormData()

    data.append('nome', user)
    data.append('user', nome)
    data.append('cpf', cpf)
    data.append('email', email)
    data.append('sexo', sexo)
    data.append('data_nascimento', dtnasc)
    data.append('numero_celular', celular)

    return data;
 }