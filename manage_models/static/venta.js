$(function(){
    $('#name_search').autocomplete({
        source : '/clientes/data/nombres/'
    });
    $('#product_search').autocomplete({
        source : '/productos/data/nombres/'
    });
    $('.ui-autocomplete').css({
        'list-style-type': 'none',
        'border': 'black solid thin',
    })
    $('.ui-helper-hidden-accessible').remove()

    let ventas = 0;

    $('#agregar_producto').click(function(){
        cliente = $('#name_search').val()
        producto = $('#product_search').val()
        producto_respuesta = $.ajax({
            url : '/producto/get/nombre/',
            data : {'producto' : producto},
            type : 'get',
            datatype : 'json',
            success : function(response){
                ventas++;
                $('#tabla_productos').prepend(`
                <tr>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${cliente}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${response.nombre}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${response.precio}</p>
                    </td>
                    <td>
                        <input type="number" id="cantidad${ventas}">
                    </td>
                    <td>
                        <input type="number" id="descuento${ventas}">
                    </td>
                    <td>
                        <button id="calcular_importe${ventas}" class="btn btn-success">Aceptar</button>
                    </td>
                    <td>
                    <p class="usuarios_tablecontent usuarios_espaciado" id="importe${ventas}"></p>
                    </td>
                </tr>
                `);

                $(`#calcular_importe${ventas}`).click(function(){
                    cantidad = $(`#cantidad${ventas}`).val()
                    descuento = $(`#descuento${ventas}`).val()
                    importe = parseFloat((cantidad * response.precio) - ( ( (response.precio * cantidad) / 100 ) * descuento ));
                    $(`#importe${ventas}`).append(importe);
                    $(`#calcular_importe${ventas}`).remove();
                    $(`#descuento${ventas}`).prop('disabled', true);
                    $(`#cantidad${ventas}`).prop('disabled', true);
                });
            },
        });
    });
});