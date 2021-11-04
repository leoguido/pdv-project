$(function(){
    $('#buscar_descuento').click(function(){
        console.log({
            'productos__nombre': $('#buscar_producto_input').val(),
            'venta__cliente__razon_social': $('#buscar_cliente_input').val(),
            'venta__vendedor__usuario__username': $('#buscar_vendedor_input').val(),
            'venta__venta__caja__nombre': $('#buscar_caja_input').val(),
        })
        $.ajax({
            url : '/reportes/buscar/',
            data : {'datos':JSON.stringify({
                'productos__nombre': $('#buscar_producto_input').val(),
                'venta__cliente__razon_social': $('#buscar_cliente_input').val(),
                'venta__vendedor__usuario__username': $('#buscar_vendedor_input').val(),
                'venta__caja__nombre': $('#buscar_caja_input').val(),
                'cantidad': $('#buscar_cantidad_input').val(),
                'descuento': $('#buscar_descuento_input').val(),
                'venta__fecha_venta': [$('#buscar_fecha_input1').val(), $('#buscar_fecha_input2').val()],
                'productos__precio': [$('#buscar_valor_input1').val(), $('#buscar_valor_input2').val()],
                'importe': [$('#buscar_importe_input1').val(), $('#buscar_importe_input2').val()],
            })},
            type : 'get',
            datatype : 'json',
            success : function(response){
                if(response.length >= 1){
                    $('#tabla_venta').find('tr').remove()
                    for(venta of response){
                        $('#tabla_venta').append(`
                <tr>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${venta.productos}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${venta.fecha_venta.slice(0, venta.fecha_venta.length - 9)}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${venta.cliente}</p>
                    </td>
                    <td>
                        <p class="usuarios_tablecontent usuarios_espaciado">${venta.vendedor}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${venta.caja}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${venta.cantidad}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${venta.valor_unitario}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${venta.descuento}</p>
                    </td>
                    <td >
                        <p class="usuarios_tablecontent usuarios_espaciado">${venta.importe}</p>
                    </td>
                </tr>
                        `)
                    }
                }
            },
            error : function(error){
                console.log(error);
            }
        });
    });
    $('#descargar').click(function(){
        let url = `/Files/reporte_ventas.xls`;
        $(location).attr('href',url);
    });
});