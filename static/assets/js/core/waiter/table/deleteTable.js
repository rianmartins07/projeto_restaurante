function deleteTable () {
    let id = $('#select-table :selected').attr('id');
    console.log(id)
    var settings = {
        "url": `${location.protocol}//${location.host}/api/waiter/table/${id}/`,
        "method": "DELETE",
        "timeout": 0,
        "headers" : {
            "X-CSRFToken": getCookie('csrftoken'),
            "Content-Type": "application/json",
        }

    };  

    Swal.fire({
        title: 'Voce quer realmente exluir?',
        showDenyButton: true,
        confirmButtonText: 'Sim!',
        confirmButtonColor: '#b31616',
        cancelButtonColor: '#b31616',
        denyButtonText: `Não`,
      }).then((result) => {
        if (result.isConfirmed) {
            $.ajax(settings).done(function (){
                $(`#select-table #${id}`).remove();
                $(`[table_id=${id}]`).remove();
                Swal.fire({
                    position: 'center',
                    icon: 'success',
                    title: `Excluido com sucesso`,
                    showConfirmButton: true,
                    confirmButtonColor: '#b31616',
                    timer: 3000
                });
               
            }).fail(function (response) {
                Swal.fire({
                    position: 'center',
                    icon: 'error',
                    title: `Erro!`,
                    text: JSON.parse(response.responseText).error,
                    showConfirmButton: true,
                    confirmButtonColor: '#b31616',
                    timer: 3000
                });
              })
            
            
        } else if (result.isDenied) {

        }
      })
}
  
