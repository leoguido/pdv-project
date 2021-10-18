$(function(){
    $('#buscar_nombre').click(function(){
        search = $('#buscar').val()
        $.ajax({
            url : '/usuarios/buscar/',
            data : {'busqueda' : search},
            type : 'get',
            datatype : 'json',
            success : function(response){
                console.log(response)
            },
            error : function(error){
                console.log(error)
            }
        });
    });
});