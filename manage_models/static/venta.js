let ventas = 0;
let data = {
    cliente: '',
    ventas: []
};

function evaluar_cliente(){
    data[0] = $('#name_search').val();
}

$(function(){
    $('#name_search').autocomplete({
        minLength: 0,
        source : '/clientes/data/nombres/',
        select : function(event, ui){
            evaluar_cliente();
        },
    });
    $('#product_search').autocomplete({
        minLength: 0,
        source : '/productos/data/nombres/',
        select : function(event, ui){
            evaluar_cliente();
        }
    });
    $('.ui-autocomplete').css({
        'list-style-type': 'none',
        'border': 'black solid thin',
    });
    $('.ui-helper-hidden-accessible').remove();

    $('#agregar_producto').click(function(){
        evaluar_cliente();
        ventas = ventas + 1;
        cliente = $('#name_search').val()
        producto = $('#product_search').val()
        producto_respuesta = $.ajax({
            url : '/producto/get/nombre/',
            data : {'producto' : producto},
            type : 'get',
            datatype : 'json',
            success : function(response){
                $('#tabla_productos').prepend(`
                <tr>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado" id="nombre_producto">${response.nombre}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado id="precio_producto"">${response.precio}</p>
                    </td>
                    <td>
                        <input type="number" id="cantidad${ventas}">
                    </td>
                    <td>
                        <input type="number" id="descuento${ventas}">
                    </td>
                    <td>
                    <p class="usuarios_tablecontent usuarios_espaciado importes" id="importe${ventas}"></p>
                    </td>
                </tr>
                `);

                $(`#cantidad${ventas}`).change(function(){
                    evaluar_cliente();
                    cantidad = $(this).val()
                    descuento = $(`#descuento${ventas}`).val()
                    importe = parseFloat((cantidad * response.precio) - ( ( (response.precio * cantidad) / 100 ) * descuento ));
                    $(`#importe${ventas}`).html('')
                    $(`#importe${ventas}`).append(Math.round((importe + Number.EPSILON) * 100) / 100);
                    total = 0;
                    $('.importes').each(function(){
                        total = total + parseFloat($(this).text());
                    });
                    $('#total').text(Math.round((total + Number.EPSILON) * 100) / 100);
                    total = 0;
                    importe = 0;
                });
                $(`#descuento${ventas}`).change(function(){
                    evaluar_cliente();
                    cantidad = $(`#cantidad${ventas}`).val()
                    descuento = $(this).val()
                    importe = parseFloat((cantidad * response.precio) - ( ( (response.precio * cantidad) / 100 ) * descuento ));
                    $(`#importe${ventas}`).html('')
                    $(`#importe${ventas}`).append(Math.round((importe + Number.EPSILON) * 100) / 100);
                    total = 0;
                    $('.importes').each(function(){
                        total = total + parseFloat($(this).text());
                    });
                    $('#total').text(Math.round((total + Number.EPSILON) * 100) / 100);
                    total = 0;
                    importe = 0;
                });
            }
        });
    });
});

// CORREGIR ERROR. CUANDO SE INTENTA EDITAR LOS DATOS DE UNA VENTA PASADA, SE ALTERA LA MÁS RECIENTE.