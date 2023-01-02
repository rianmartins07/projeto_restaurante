
function addList() { 
    var html = `
    <tr>
        <td class="priority-1">Rian</td>
        <td class="priority-3">43999579836</td>
        <td class="priority-4">rianmartins@live.com</td>
        <td class="priority-2">Administrador</td>
        <td class="d-flex justify-content-end priority-1">
            <div class="btn-group">
            <a href="../update/index.html">
                    <img src="../../../static/assets/images/3dots.ico"
                        style="width: 20px !important ; height: 20px impr !important;"
                        alt="">
                </a>
            </div>
        </td>
    </tr>
    `
    for(var i =0;i<10;i++){
        $('#colab-content').append(html);
    }
}
addList()

