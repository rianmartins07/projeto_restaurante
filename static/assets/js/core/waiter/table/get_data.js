function getData() {
    let responsible_name = $('#id_responsible_name').val();
    let table_number = $("#id_tale_number").val();

    let data = new FormData()
    data.append('responsible_name', responsible_name)
    data.append('table_number', table_number)

    return data
}