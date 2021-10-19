$(function(){
    $('#buscar_nombre').click(function(){
        search = $('#buscar_nombre_input').val()
        $.ajax({
            url : '/usuarios/buscar/nombre/',
            data : {'busqueda' : search},
            type : 'get',
            datatype : 'json',
            success : function(response){
                if(response.length >= 1){
                    $('#tabla_usuarios').find('tr').remove()
                    for(usuario of response){
                        if(usuario.tipo_usuario == 'A'){
                            tipo = 'ADMINISTRADOR'
                        }
                        if(usuario.tipo_usuario == 'V'){
                            tipo = 'VENDEDOR'
                        }
                        $('#tabla_usuarios').append(`
                        <tr>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${usuario.first_name}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${usuario.last_name}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${usuario.email}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${usuario.telefono}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${tipo}</p>
                    </td>
                    <td >
                        <a href="/usuarios/borrar/${usuario.pk}" class="deleteuser"><i class="bi bi-x user_butonicon"></i></a>
                    </td>
                    <td >
                        <a href="/usuarios/editar/${usuario.pk}" class="deleteuser"><i class="bi bi-pencil-fill user_butonicon"></i></i></a>
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
    $('#buscar_apellidos').click(function(){
        search = $('#buscar_apellidos_input').val()
        $.ajax({
            url : '/usuarios/buscar/apellidos/',
            data : {'busqueda' : search},
            type : 'get',
            datatype : 'json',
            success : function(response){
                if(response.length >= 1){
                    $('#tabla_usuarios').find('tr').remove()
                    for(usuario of response){
                        if(usuario.tipo_usuario == 'A'){
                            tipo = 'ADMINISTRADOR'
                        }
                        if(usuario.tipo_usuario == 'V'){
                            tipo = 'VENDEDOR'
                        }
                        $('#tabla_usuarios').append(`
                        <tr>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${usuario.first_name}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${usuario.last_name}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${usuario.email}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${usuario.telefono}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${tipo}</p>
                    </td>
                    <td >
                        <a href="/usuarios/borrar/${usuario.pk}" class="deleteuser"><i class="bi bi-x user_butonicon"></i></a>
                    </td>
                    <td >
                        <a href="/usuarios/editar/${usuario.pk}" class="deleteuser"><i class="bi bi-pencil-fill user_butonicon"></i></i></a>
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
    $('#buscar_email').click(function(){
        search = $('#buscar_email_input').val()
        $.ajax({
            url : '/usuarios/buscar/email/',
            data : {'busqueda' : search},
            type : 'get',
            datatype : 'json',
            success : function(response){
                if(response.length >= 1){
                    $('#tabla_usuarios').find('tr').remove()
                    for(usuario of response){
                        if(usuario.tipo_usuario == 'A'){
                            tipo = 'ADMINISTRADOR'
                        }
                        if(usuario.tipo_usuario == 'V'){
                            tipo = 'VENDEDOR'
                        }
                        $('#tabla_usuarios').append(`
                        <tr>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${usuario.first_name}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${usuario.last_name}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${usuario.email}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${usuario.telefono}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${tipo}</p>
                    </td>
                    <td >
                        <a href="/usuarios/borrar/${usuario.pk}" class="deleteuser"><i class="bi bi-x user_butonicon"></i></a>
                    </td>
                    <td >
                        <a href="/usuarios/editar/${usuario.pk}" class="deleteuser"><i class="bi bi-pencil-fill user_butonicon"></i></i></a>
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
    $('#buscar_telefono').click(function(){
        search = $('#buscar_telefono_input').val()
        $.ajax({
            url : '/usuarios/buscar/telefono/',
            data : {'busqueda' : search},
            type : 'get',
            datatype : 'json',
            success : function(response){
                if(response.length >= 1){
                    $('#tabla_usuarios').find('tr').remove()
                    for(usuario of response){
                        if(usuario.tipo_usuario == 'A'){
                            tipo = 'ADMINISTRADOR'
                        }
                        if(usuario.tipo_usuario == 'V'){
                            tipo = 'VENDEDOR'
                        }
                        $('#tabla_usuarios').append(`
                        <tr>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${usuario.first_name}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${usuario.last_name}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${usuario.email}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${usuario.telefono}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${tipo}</p>
                    </td>
                    <td >
                        <a href="/usuarios/borrar/${usuario.pk}" class="deleteuser"><i class="bi bi-x user_butonicon"></i></a>
                    </td>
                    <td >
                        <a href="/usuarios/editar/${usuario.pk}" class="deleteuser"><i class="bi bi-pencil-fill user_butonicon"></i></i></a>
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
    $('#buscar_tipo').click(function(){
        search = $('#buscar_tipo_input').val()
        $.ajax({
            url : '/usuarios/buscar/tipo/',
            data : {'busqueda' : search},
            type : 'get',
            datatype : 'json',
            success : function(response){
                if(response.length >= 1){
                    $('#tabla_usuarios').find('tr').remove()
                    for(usuario of response){
                        if(usuario.tipo_usuario == 'A'){
                            tipo = 'ADMINISTRADOR'
                        }
                        if(usuario.tipo_usuario == 'V'){
                            tipo = 'VENDEDOR'
                        }
                        $('#tabla_usuarios').append(`
                        <tr>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${usuario.first_name}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${usuario.last_name}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${usuario.email}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${usuario.telefono}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${tipo}</p>
                    </td>
                    <td >
                        <a href="/usuarios/borrar/${usuario.pk}" class="deleteuser"><i class="bi bi-x user_butonicon"></i></a>
                    </td>
                    <td >
                        <a href="/usuarios/editar/${usuario.pk}" class="deleteuser"><i class="bi bi-pencil-fill user_butonicon"></i></i></a>
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