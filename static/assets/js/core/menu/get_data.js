function getData(){
    let data = new FormData()

    let nome = $('#id_nome').val();
    let valor = $('#id_valor').val();
    let descricao = $('#id_descricao').val();
    let status = $('#id_status:checked').val()
    let foto = $('#id_foto')[0].files[0];

    data.append('nome', nome)
    data.append('valor', valor)
    data.append('descricao', descricao)
    data.append('status', status)
    data.append('foto', foto)

    return data
}
