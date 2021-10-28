let ventas = 0;
let cajaId = $('#caja_id').val();
let data_ = {
    cliente: '',
    caja: cajaId,
    ventas: [],
};

function evaluar_cliente(){
    data_.cliente = $('#name_search').val();
}
function evaluar_venta(numero_venta, cantidad, nombre, descuento, importe){
    let exists = false;
    let timer = 0;
    for(numero of data_.ventas){
        if(numero_venta == numero.numero){
            exists = true;
            break;
        }
        timer++;
    }
    if(exists){
        data_.ventas[timer] = {numero:numero_venta, cantidad_:cantidad, productos:nombre, descuento_:descuento, importe_:importe}
    }
    else{
        data_.ventas.push({numero:numero_venta, cantidad_:cantidad, productos:nombre, descuento_:descuento, importe_:importe});
    }
    console.log(data_);
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
                        <p class="usuarios_tablecontent usuarios_espaciado" id="nombre_producto${ventas}">${response.nombre}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado id="precio_producto${ventas}">${response.precio}</p>
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
                    let numero = $(this).attr('id')
                    numero = numero.slice(8)
                    cantidad = $(this).val()
                    descuento = $(`#descuento${numero}`).val()
                    importe = parseFloat((cantidad * response.precio) - ( ( (response.precio * cantidad) / 100 ) * descuento ));
                    $(`#importe${numero}`).html('')
                    $(`#importe${numero}`).append(Math.round((importe + Number.EPSILON) * 100) / 100);
                    total = 0;
                    $('.importes').each(function(){
                        total = total + parseFloat($(this).text());
                    });
                    $('#total').text(Math.round((total + Number.EPSILON) * 100) / 100);
                    nombre = $(`#nombre_producto${numero}`).text();
                    evaluar_venta(numero, cantidad, nombre, descuento, importe);
                    total = 0;
                    importe = 0;
                });
                $(`#descuento${ventas}`).change(function(){
                    evaluar_cliente();
                    let numero = $(this).attr('id')
                    numero = numero.slice(9)
                    cantidad = $(`#cantidad${numero}`).val()
                    descuento = $(this).val()
                    importe = parseFloat((cantidad * response.precio) - ( ( (response.precio * cantidad) / 100 ) * descuento ));
                    $(`#importe${numero}`).html('');
                    $(`#importe${numero}`).append(Math.round((importe + Number.EPSILON) * 100) / 100);
                    total = 0;
                    $('.importes').each(function(){
                        total = total + parseFloat($(this).text());
                    });
                    $('#total').text(Math.round((total + Number.EPSILON) * 100) / 100);
                    nombre = $(`#nombre_producto${numero}`).text();
                    evaluar_venta(numero, cantidad, nombre, descuento, importe);
                    total = 0;
                    importe = 0;
                });
            }
        });
    });

    $('#proceder_venta').click(function(){
        evaluar_cliente();
        $.ajax({
            url: '/cajas/usar/venta/',
            data:{json: JSON.stringify(data_)},
            type: 'GET',
            success: function(response){
                
            },
            error: function(error){
                console.log(error);
            }
        })
    });
});