$(function(){
    $('#buscar_nombre').click(function(){
        search = $('#buscar_nombre_input').val()
        $.ajax({
            url : '/clientes/buscar/nombre/',
            data : {'busqueda' : search},
            type : 'GET',
            datatype : 'json',
            success : function(response){
                if(response.length >= 1){
                    $('#tabla_clientes').find('tr').remove()
                    for(cliente of response){
                        $('#tabla_clientes').append(`
                <tr>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.nombre}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.apellido}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.correo_electronico}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.telefono}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.rfc}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.razon_social}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.domicilio}</p>
                    </td>
                    <td >
                        <a href="/clientes/borrar/${cliente.pk}" class="deleteuser"><i class="bi bi-x user_butonicon"></i></a>
                    </td>
                    <td >
                        <a href="/clientes/editar/${cliente.pk}" class="deleteuser"><i class="bi bi-pencil-fill user_butonicon"></i></i></a>
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
            url : '/clientes/buscar/apellido/',
            data : {'busqueda' : search},
            type : 'get',
            datatype : 'json',
            success : function(response){
                if(response.length >= 1){
                    $('#tabla_clientes').find('tr').remove()
                    for(cliente of response){
                        $('#tabla_clientes').append(`
                <tr>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.nombre}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.apellido}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.correo_electronico}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.telefono}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.rfc}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.razon_social}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.domicilio}</p>
                    </td>
                    <td >
                        <a href="/clientes/borrar/${cliente.pk}" class="deleteuser"><i class="bi bi-x user_butonicon"></i></a>
                    </td>
                    <td >
                        <a href="/clientes/editar/${cliente.pk}" class="deleteuser"><i class="bi bi-pencil-fill user_butonicon"></i></i></a>
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
            url : '/clientes/buscar/email/',
            data : {'busqueda' : search},
            type : 'get',
            datatype : 'json',
            success : function(response){
                if(response.length >= 1){
                    $('#tabla_clientes').find('tr').remove()
                    for(cliente of response){
                        $('#tabla_clientes').append(`
                <tr>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.nombre}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.apellido}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.correo_electronico}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.telefono}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.rfc}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.razon_social}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.domicilio}</p>
                    </td>
                    <td >
                        <a href="/clientes/borrar/${cliente.pk}" class="deleteuser"><i class="bi bi-x user_butonicon"></i></a>
                    </td>
                    <td >
                        <a href="/clientes/editar/${cliente.pk}" class="deleteuser"><i class="bi bi-pencil-fill user_butonicon"></i></i></a>
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
            url : '/clientes/buscar/telefono/',
            data : {'busqueda' : search},
            type : 'get',
            datatype : 'json',
            success : function(response){
                if(response.length >= 1){
                    $('#tabla_clientes').find('tr').remove()
                    for(cliente of response){
                        $('#tabla_clientes').append(`
                <tr>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.nombre}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.apellido}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.correo_electronico}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.telefono}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.rfc}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.razon_social}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.domicilio}</p>
                    </td>
                    <td >
                        <a href="/clientes/borrar/${cliente.pk}" class="deleteuser"><i class="bi bi-x user_butonicon"></i></a>
                    </td>
                    <td >
                        <a href="/clientes/editar/${cliente.pk}" class="deleteuser"><i class="bi bi-pencil-fill user_butonicon"></i></i></a>
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
    $('#buscar_rfc').click(function(){
        search = $('#buscar_rfc_input').val()
        $.ajax({
            url : '/clientes/buscar/rfc/',
            data : {'busqueda' : search},
            type : 'get',
            datatype : 'json',
            success : function(response){
                if(response.length >= 1){
                    $('#tabla_clientes').find('tr').remove()
                    for(cliente of response){
                        $('#tabla_clientes').append(`
                <tr>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.nombre}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.apellido}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.correo_electronico}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.telefono}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.rfc}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.razon_social}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.domicilio}</p>
                    </td>
                    <td >
                        <a href="/clientes/borrar/${cliente.pk}" class="deleteuser"><i class="bi bi-x user_butonicon"></i></a>
                    </td>
                    <td >
                        <a href="/clientes/editar/${cliente.pk}" class="deleteuser"><i class="bi bi-pencil-fill user_butonicon"></i></i></a>
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
    $('#buscar_razon').click(function(){
        search = $('#buscar_razon_input').val()
        $.ajax({
            url : '/clientes/buscar/razon/',
            data : {'busqueda' : search},
            type : 'get',
            datatype : 'json',
            success : function(response){
                if(response.length >= 1){
                    $('#tabla_clientes').find('tr').remove()
                    for(cliente of response){
                        $('#tabla_clientes').append(`
                <tr>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.nombre}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.apellido}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.correo_electronico}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.telefono}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.rfc}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.razon_social}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.domicilio}</p>
                    </td>
                    <td >
                        <a href="/clientes/borrar/${cliente.pk}" class="deleteuser"><i class="bi bi-x user_butonicon"></i></a>
                    </td>
                    <td >
                        <a href="/clientes/editar/${cliente.pk}" class="deleteuser"><i class="bi bi-pencil-fill user_butonicon"></i></i></a>
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
    $('#buscar_domicilio').click(function(){
        search = $('#buscar_domicilio_input').val()
        $.ajax({
            url : '/clientes/buscar/domicilio/',
            data : {'busqueda' : search},
            type : 'get',
            datatype : 'json',
            success : function(response){
                if(response.length >= 1){
                    $('#tabla_clientes').find('tr').remove()
                    for(cliente of response){
                        $('#tabla_clientes').append(`
                <tr>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.nombre}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.apellido}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.correo_electronico}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.telefono}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.rfc}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.razon_social}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente.domicilio}</p>
                    </td>
                    <td >
                        <a href="/clientes/borrar/${cliente.pk}" class="deleteuser"><i class="bi bi-x user_butonicon"></i></a>
                    </td>
                    <td >
                        <a href="/clientes/editar/${cliente.pk}" class="deleteuser"><i class="bi bi-pencil-fill user_butonicon"></i></i></a>
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