function deleteOrder(id){
    var settings = {
        "url": `${location.protocol}//${location.host}/api/orders/${id}`,
        "method": "DELETE",
        "timeout": 0,
        "headers" : {
            "X-CSRFToken": getCookie('csrftoken'),
            "Content-Type": "application/json",
        }

    };  
    console.log($('[status_id='+id+']').text())
    if($('[status_id='+id+']').val() == 'PEDIDO NA COZINHA') {
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
                Swal.fire({
                    position: 'center',
                    icon: 'success',
                    title: `Excluido com sucesso`,
                    showConfirmButton: true,
                    confirmButtonColor: '#b31616',
                    timer: 3000
                });
                $(`[id_order=${id}]`).remove();
            })
            
            
        } else if (result.isDenied) {

        }
      })
}else{
    Swal.fire({
        position: 'center',
        icon: 'Error!',
        title: `Pedido esta preparando ou pronto!`,
        showConfirmButton: true,
        confirmButtonColor: '#b31616',
        timer: 3000
    });
}

  
}