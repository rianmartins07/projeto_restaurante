
function getData() {
  nome = $('#id_first_name').val();
  sobrenome = $('#id_last_name').val();
  cpf = $('#id_cpf').val();
  email = $('#id_email').val();
  data_nascimento = $('#id_data_nascimento').val();
  celular = $('#id_numero_celular').val();
  sexo = $('#id_sexo :selected').text();
  groups = $('#id_groups :selected').val()
  senha_antiga = $('#id_senha_antiga').val();
  nova_senha = $('#id_nova_senha').val();
  nova_senha_confirmação = $('#id_nova_senha').val();
  
  if (nova_senha != nova_senha_confirmação){
    Swal.fire({
      position: 'center',
      icon: 'error',
      title: `As senhas não são iguais!`,
      showConfirmButton: true,
      confirmButtonColor: '#b31616',
      timer: 3000
  });
 return 0
  }

  data = new FormData()
  data.append('first_name', nome)
  data.append('last_name', sobrenome)
  data.append('cpf', cpf)
  data.append('email', email)
  data.append('sexo', sexo)
  data.append('data_nascimento', data_nascimento)
  data.append('numero_celular', celular)
  data.append('groups', groups)
  data.append('old_password', senha_antiga)
  data.append('new_password', nova_senha)
  data.append('confirm_password', nova_senha_confirmação)
  return data;
}