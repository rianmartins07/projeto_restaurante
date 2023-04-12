function getData(){
    let data = new FormData()

    let nome = $('#id_nome').val();
    let valor = $('#id_valor').val();
    let descricao = $('#id_descricao').val();
    let status = $('#id_status:checked').val()
    let foto = $('#id_foto')[0].files[0];
    if (foto){
        data.append('foto', foto)
    }
    let id_pk = $('#id_pk').val()
    if (id_pk){
        data.append('id', id_pk)
    }
    status = 1

    data.append('nome', nome)
    data.append('valor', valor)
    data.append('descricao', descricao)
    data.append('status', status)
   

    return data
}
