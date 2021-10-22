$(function(){
    $('#buscar_clave').click(function(){
        search = $('#buscar_clave_input').val()
        $.ajax({
            url : '/cajas/administrar/buscar/clave/',
            data : {'busqueda' : search},
            type : 'GET',
            datatype : 'json',
            success : function(response){
                if(response.length >= 1){
                    $('#tabla_cajas').find('tr').remove()
                    for(caja of response){
                        $('#tabla_cajas').append(`
                <tr>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${caja.clave}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${caja.nombre}</p>
                    </td>
                    <td>
                        <a href="/cajas/administrar/borrar/${caja.pk}" class="deleteuser"><i class="bi bi-x user_butonicon"></i></a>
                    </td>
                    <td >
                        <a href="/cajas/administrar/editar/${caja.pk}" class="deleteuser"><i class="bi bi-pencil-fill user_butonicon"></i></a>
                    </td>
                </tr>
                        `)
                    }
                }
            },
            error : function(error){
                console.log(error)
            }
        });
    });
    $('#buscar_nombre_caja').click(function(){
        search = $('#buscar_nombre_caja_input').val()
        $.ajax({
            url : '/cajas/administrar/buscar/nombre/',
            data : {'busqueda' : search},
            type : 'GET',
            datatype : 'json',
            success : function(response){
                if(response.length >= 1){
                    $('#tabla_cajas').find('tr').remove()
                    for(caja of response){
                        $('#tabla_cajas').append(`
                <tr>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${caja.clave}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${caja.nombre}</p>
                    </td>
                    <td>
                        <a href="/cajas/administrar/borrar/${caja.pk}" class="deleteuser"><i class="bi bi-x user_butonicon"></i></a>
                    </td>
                    <td >
                        <a href="/cajas/administrar/editar/${caja.pk}" class="deleteuser"><i class="bi bi-pencil-fill user_butonicon"></i></a>
                    </td>
                </tr>
                        `)
                    }
                }
            },
            error : function(error){
                console.log(error)
            }
        });
    });
});