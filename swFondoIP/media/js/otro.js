$(document).on('ready',function(){
        var lstSeleccion = [];
        var lstDestino = [];
        var lstUsuario = [];
        var lstPk = [];
        var lstUsers = [];
        var lstNombres = [];

        

        $("#btn_delete").click(elimina);
        function elimina(){
            var lista_codigos = [];
            $('input[name="chk[]"]:checked').each(
                function ()
                {                                  
                    lista_codigos.push($(this).val());
                });

            $.ajax({

                data : {'lista_codigos': lista_codigos, 'modelo':'7'},
                url : '/ajax/eliminar_registro/',
                type :'GET',
                dataType: 'json',

                succes: function(data){
                    alert(data);
                },
                error: function(data){
                    alert(data);
                }
            });
            
        };
        
        $("input[name='chk[]']").click(nuevo);

        function nuevo(){
            valor = $("input[name='chk[]']:checked").length;
            //alert(valor);
            button = $('#btn_delete');
            if (valor > 0){

                button.removeClass('hide');
            }
            else{
                button.addClass('hide');           
            } 


        };
        $('#btn_delete').mouseenter(enter_css);
        $('#btn_delete').mouseleave(leave_css);
        function enter_css(){
            $(this).removeClass('btn-danger');
            //$(this).addClass('btn  boton-operacion');
            //$('span#btn_span_delete').toggleClass('text-danger');
            $('btn_span_delete').addClass('text-danger');
            
        };
        function leave_css(){
            $(this).removeClass('btn-danger');
            //$(this).addClass('btn btn-default boton-operacion');
            $(this).addClass('btn-default');
            $('btn_span_delete').removeClass('text-danger')
        };

        $('.select').on('click',function(){
            var val = $(this).attr('value');
                        
            //$('#tr'+val).toggleClass('seleccionado');
            if($(this).is(':checked')){
                $('#tr'+val).attr('style','background:#FFFFCC;');
            }else{
                $('#tr'+val).attr('style','');
            }

        });    
        
        $("#btnEnviar").on('click',function(e){
            //alert('estamos aki');
            //e.preventDefault();
            lstSeleccion = [];
            $('input[name="chk[]"]:checked').each(
                function ()
                {                                  
                    lstSeleccion.push($(this).val());
                });
            $('#txtProtocolo').val(lstSeleccion);
           
        });

        $("#btnFinalizarDestino").on('click',function(e){
            //alert('aki');
            lstDestino = [];
            lstUsuario = [];
            $('input[name="destino[]"]:checked').each(
                function ()
                {
                    console.log($(this).attr("cod"));
                    lstDestino.push($(this).attr("cod"));
                    lstUsuario.push($(this).attr("nom"));
                });
            $('#txtDestino').val(lstDestino);
            $('#txtUsuario').val(lstUsuario);
            $('#seleccionarDestino').modal('hide');
            
        });
 
        $("#buscarPorNombre").on('click',function(e){
            
            var search = $('#texto_busqueda').val();
                $('#tabla tr').show();
                
                if(search.length>0)
                {
                $("#tabla tr td.nombre").not(":Contains('"+search+"')").parent().hide();
                }   
            
        });

        $("#buscarPorDNI").on('click',function(e){
            
            var search = $('#texto_busqueda').val();
                $('#tabla tr').show();
                
                if(search.length>0)
                {
                $("#tabla tr td.numeroDocumento").not(":Contains('"+search+"')").parent().hide();
                }   
            
        });
        $("#mostrarTodos").on('click',function(e){

            var search = $('#texto_busqueda').val();
                
                $('#tabla tr').show();  
        });

        $("#buscarPorProyecto").on('click',function(e){
            
            var search = $('#texto_busqueda').val();
                $('#tabla tr').show();
                
                if(search.length>0)
                { 
                $("#tabla tr td.nombre").not(":Contains('"+search+"')").parent().hide();
                }   
            
        });
        $("#buscarPorUnidadEjecutora").on('click',function(e){
            
            var search = $('#texto_busqueda').val();
                $('#tabla tr').show();
        
                if(search.length>0)
                { 
                $("#tabla tr td.cliente").not(":Contains('"+search+"')").parent().hide();
                }   
            
        });

        $("#buscarPorInstitucion").on('click',function(e){
            
            var search = $('#texto_busqueda').val();
                $('#tabla tr').show();
        
                if(search.length>0)
                { 
                $("#tabla tr td.institucion").not(":Contains('"+search+"')").parent().hide();
                }   
            
        });

        $("#buscarPorDireccion").on('click',function(e){
            
            var search = $('#texto_busqueda').val();
                $('#tabla tr').show();
        
                if(search.length>0)
                { 
                $("#tabla tr td.direccion").not(":Contains('"+search+"')").parent().hide();
                }   
            
        });

        $("#buscarPorUbicacion").on('click',function(e){
            
            var search = $('#texto_busqueda').val();
                $('#tabla tr').show();
        
                if(search.length>0)
                { 
                $("#tabla tr td.ubicacion").not(":Contains('"+search+"')").parent().hide();
                }   
            
        });

        $("#buscarPorReferencia").on('click',function(e){
            
            var search = $('#texto_busqueda').val();
                $('#tabla tr').show();
        
                if(search.length>0)
                { 
                $("#tabla tr td.referencia").not(":Contains('"+search+"')").parent().hide();
                }   
            
        });

        $("#buscarPorProtocolo").on('click',function(e){
            
            var search = $('#texto_busqueda').val();
                $('#tabla tr').show();
        
                if(search.length>0)
                { 
                $("#tabla tr td.protocolo").not(":Contains('"+search+"')").parent().hide();
                }   
            
        });

        $("#buscarPorEnviado").on('click',function(e){
            
            var search = $('#texto_busqueda').val();
                $('#tabla tr').show();
        
                if(search.length>0)
                { 
                $("#tabla tr td.enviadoPor").not(":Contains('"+search+"')").parent().hide();
                }   
            
        });

        $('#texto_Cliente').keyup(function() {
        
            var search = $('#texto_Cliente').val();
            $('#tabla tr').show();
            if(search.length>0){
                $("#tabla tr td.nombre").not(":Contains('"+search+"')").parent().hide();
                //$("#tabla tr td.micodigo").not(":Contains('"+search+"')").parent().hide();

            }

        });
              
        $(".proy").bind("click",function(){
            //alert($(this).attr("nombre"));
            $('#nombreCliente').text($(this).attr("nomClie"));
            $('#idMProy').val($(this).attr("codProy"));
            $('#nombreProyecto').text($(this).attr("nomProy"));
            $('#seleccionarConvenio').modal('hide');

        });

        $(".cliente").bind("click",function(){
            //alert($(this).attr("nombre"));
            $('#nomMCli').val($(this).attr("nomCli"));
            $('#idMCli').val($(this).attr("codCli"));
            $('#seleccionarUnidadEjecutora').modal('hide');
        });
             
        $.expr[':'].Contains = function(x, y, z){
            return jQuery(x).text().toLowerCase().indexOf(z[3].toLowerCase())>=0;
        };


        $("#localizarPorProtocolo").on("click",function(){
            //alert('hicimos click');
            //event.preventDefault();
            
            var protocolo = $('#txtprotocolo').val();
            var nombre = $('#txtnombre').val();
            var cliente = $('#txtcliente').val();
            var fecInicial=$('#txtfecinicio').val();
            var fecFinal=$('#txtfecfin').val();
            var referencia = $('#txtreferencia').val();
            
            $.ajax({
                data : {'proyecto':protocolo},
                url : '/tramitedoc/usuarioAjax/',
                type: 'get',
                success: function(data){
                    var html="";
                    for(var i=0; i<data.length; i++){
                        lstPk.push(data[i].pk);
                        lstUsers.push((data[i].fields.username).toLowerCase());
                        lstNombres.push((data[i].fields.last_name).toUpperCase() + ", " +(data[i].fields.first_name).toUpperCase());
                    }
                    
                    return lstPk;
                }    
            });

                         
            $.ajax({
                data : { 
                    "protocolo":protocolo,
                    "nombre":nombre,
                    "cliente":cliente,
                    "fecinicio":fecInicial,
                    "fecfinal":fecFinal,
                    "referencia":referencia
                },
                url : '/tramitedoc/localizarPorProtocoloAjax/',
                type: 'get',
                success: function(data){
                    
                    var html = ""
                    
                   

                    for(var i=0; i<data.length; i++){
                        var estado = "";
                        if (data[i].fields.EstBProt == '0' && data[i].fields.EstObservado == '0'){
                            estado = "Recibido";
                        }
                        if(data[i].fields.EstBProt=='1' && data[i].fields.EstObservado == '0'){
                            estado = "Enviado";
                        }
                        if(data[i].fields.EstObservado == '1'){
                            estado = "Observado";   
                        }
                        var a = 0;
                        var f = 0;
                        var recibidoPor = "";
                        for(var f=0; f<lstPk.length; f++){
                            if(lstPk[f] == data[i].fields.IdMUsuRec){

                                recibidoPor = lstUsers[f] + "-"+lstNombres[f];
                                a=a+1;
                            }
                        }
                        
                        html += '<tbody><tr><td>' + data[i].fields.IdMProt + '</td><td>' + ((data[i].fields.ProyBProt).toUpperCase()).substring(100) + 
                                '</td><td>' + ((data[i].fields.cliBProt).toUpperCase()).substring(30) +'</td><td>' + recibidoPor + 
                                '</td><td>' + estado + '</td><td>' + data[i].fields.FecEnv + 
                                '</td><td>' + data[i].fields.IdProtRef + '</td></tr></tbody>'
                    }
                    
                    $('#datosAjaxLocalizar').html(html);
                }
            });

        });

        $("#localizarPorProyecto").on("click",function(){
            //alert('hicimos click');
            //event.preventDefault();
            
            var proyecto = $('#txtBusqueda').val();
            
            $.ajax({
                data : {'proyecto':proyecto},
                url : '/tramitedoc/usuarioAjax/',
                type: 'get',
                success: function(data){
                    var html="";
                    for(var i=0; i<data.length; i++){
                        lstPk.push(data[i].pk);
                        lstUsers.push((data[i].fields.username).toLowerCase());
                        lstNombres.push((data[i].fields.last_name).toUpperCase() + ", " +(data[i].fields.first_name).toUpperCase());
                    }
                    
                    return lstPk;
                }    
            });

             
            $.ajax({
                data : {'proyecto':proyecto},
                url : '/tramitedoc/localizarPorProyectoAjax/',
                type: 'get',
                success: function(data){
                    var html = ""
                   

                    for(var i=0; i<data.length; i++){
                        var estado = "";
                        if (data[i].fields.EstBProt == '0' && data[i].fields.EstObservado == '0'){
                            estado = "Recibido";
                        }
                        if(data[i].fields.EstBProt=='1' && data[i].fields.EstObservado == '0'){
                            estado = "Enviado";
                        }
                        if(data[i].fields.EstObservado == '1'){
                            estado = "Observado";   
                        }
                        var a = 0;
                        var f = 0;
                        var recibidoPor = "";
                        for(var f=0; f<lstPk.length; f++){
                            if(lstPk[f] == data[i].fields.IdMUsuRec){

                                recibidoPor = lstUsers[f] + "-"+lstNombres[f];
                                a=a+1;
                            }
                        }
                        
                        html += '<tr><td>' + data[i].fields.IdMProt + '</td><td>' + (data[i].fields.ProyBProt).toUpperCase() + 
                                '</td><td>' + (data[i].fields.CliBProt).toUpperCase() +'</td><td>' + recibidoPor + 
                                '</td><td>' + estado + '</td><td>' + data[i].fields.FecEnv + 
                                '</td><td>' + data[i].fields.IdProtRef + '</td></tr>'
                    }
                    $('#dataProtocoloAjax').html(html);
                }
            });

        });


        $("#localizarPorUnidadEjecutora").on("click",function(){
            //alert('hicimos click');
            //event.preventDefault();
            
            var cliente = $('#txtBusqueda').val();
            
            $.ajax({
                data : {'cliente':cliente},
                url : '/tramitedoc/usuarioAjax/',
                type: 'get',
                success: function(data){
                    var html="";
                    for(var i=0; i<data.length; i++){
                        lstPk.push(data[i].pk);
                        lstUsers.push((data[i].fields.username).toLowerCase());
                        lstNombres.push((data[i].fields.last_name).toUpperCase() + ", " +(data[i].fields.first_name).toUpperCase());
                    }
                    
                    return lstPk;
                }    
            });

             
            $.ajax({
                data : {'cliente':cliente},
                url : '/tramitedoc/localizarPorUnidadEjecutoraAjax/',
                type: 'get',
                success: function(data){
                    var html = ""
                   

                    for(var i=0; i<data.length; i++){
                        var estado = "";
                        if (data[i].fields.EstBProt == '0' && data[i].fields.EstObservado == '0'){
                            estado = "Recibido";
                        }
                        if(data[i].fields.EstBProt=='1' && data[i].fields.EstObservado == '0'){
                            estado = "Enviado";
                        }
                        if(data[i].fields.EstObservado == '1'){
                            estado = "Observado";   
                        }
                        var a = 0;
                        var f = 0;
                        var recibidoPor = "";
                        for(var f=0; f<lstPk.length; f++){
                            if(lstPk[f] == data[i].fields.IdMUsuREc){

                                recibidoPor = lstUsers[f] + "-"+lstNombres[f];
                                a=a+1;
                            }
                        }
                        
                        html += '<tr><td>' + data[i].fields.IdMProt + '</td><td>' + (data[i].fields.ProyBProt).toUpperCase() + 
                                '</td><td>' + (data[i].fields.CliBProt).toUpperCase() +'</td><td>' + recibidoPor + 
                                '</td><td>' + estado + '</td><td>' + data[i].fields.FecEnv + 
                                '</td><td>' + data[i].fields.IdProtRef + '</td></tr>'
                    }
                    $('#dataProtocoloAjax').html(html);
                }
            });

        });

        
        $("#localizarPorReferencia").on("click",function(){
            //alert('hicimos click');
            //event.preventDefault();
            
            var referencia = $('#txtBusqueda').val();
            
            $.ajax({
                data : {'referencia':referencia},
                url : '/tramitedoc/usuarioAjax/',
                type: 'get',
                success: function(data){
                    var html="";
                    for(var i=0; i<data.length; i++){
                        lstPk.push(data[i].pk);
                        lstUsers.push((data[i].fields.username).toLowerCase());
                        lstNombres.push((data[i].fields.last_name).toUpperCase() + ", " +(data[i].fields.first_name).toUpperCase());
                    }
                    
                    return lstPk;
                }    
            });

             
            $.ajax({
                data : {'referencia':referencia},
                url : '/tramitedoc/localizarPorReferenciaAjax/',
                type: 'get',
                success: function(data){
                    var html = ""
                   

                    for(var i=0; i<data.length; i++){
                        var estado = "";
                        if (data[i].fields.EstBProt == '0' && data[i].fields.EstObservado == '0'){
                            estado = "Recibido";
                        }
                        if(data[i].fields.EstBProt=='1' && data[i].fields.EstObservado == '0'){
                            estado = "Enviado";
                        }
                        if(data[i].fields.EstObservado == '1'){
                            estado = "Observado";   
                        }
                        var a = 0;
                        var f = 0;
                        var recibidoPor = "";
                        for(var f=0; f<lstPk.length; f++){
                            if(lstPk[f] == data[i].fields.idMUsuREc){

                                recibidoPor = lstUsers[f] + "-"+lstNombres[f];
                                a=a+1;
                            }
                        }
                        
                        html += '<tr><td>' + data[i].fields.IdMProt + '</td><td>' + (data[i].fields.ProyBProt).toUpperCase() + 
                                '</td><td>' + (data[i].fields.CliBProt).toUpperCase() +'</td><td>' + recibidoPor + 
                                '</td><td>' + estado + '</td><td>' + data[i].fields.FecEnv + 
                                '</td><td>' + data[i].fields.IdProtRef + '</td></tr>'
                    }
                    $('#dataProtocoloAjax').html(html);
                }
            });

        });

        $("#localizarPorFecha").on("click",function(){
            //alert('hicimos click');
            //event.preventDefault();
            
            var fecha = $('#txtBusqueda').val();
            
            $.ajax({
                data : {'fecha':fecha},
                url : '/tramitedoc/usuarioAjax/',
                type: 'get',
                success: function(data){
                    var html="";
                    for(var i=0; i<data.length; i++){
                        lstPk.push(data[i].pk);
                        lstUsers.push((data[i].fields.username).toLowerCase());
                        lstNombres.push((data[i].fields.last_name).toUpperCase() + ", " +(data[i].fields.first_name).toUpperCase());
                    }
                    
                    return lstPk;
                }    
            });

             
            $.ajax({
                data : {'fecha':fecha},
                url : '/tramitedoc/localizarPorFechaAjax/',
                type: 'get',
                success: function(data){
                    var html = ""
                   

                    for(var i=0; i<data.length; i++){
                        var estado = "";
                        if (data[i].fields.EstBProt == '0' && data[i].fields.EstObservado == '0'){
                            estado = "Recibido";
                        }
                        if(data[i].fields.EstBProt=='1' && data[i].fields.EstObservado == '0'){
                            estado = "Enviado";
                        }
                        if(data[i].fields.EstObservado == '1'){
                            estado = "Observado";   
                        }
                        var a = 0;
                        var f = 0;
                        var recibidoPor = "";
                        for(var f=0; f<lstPk.length; f++){
                            if(lstPk[f] == data[i].fields.IdMUsuREc){

                                recibidoPor = lstUsers[f] + "-"+lstNombres[f];
                                a=a+1;
                            }
                        }
                        
                        html += '<tr><td>' + data[i].fields.IdMProt + '</td><td>' + (data[i].fields.ProyBProt).toUpperCase() + 
                                '</td><td>' + (data[i].fields.CliBProt).toUpperCase() +'</td><td>' + recibidoPor + 
                                '</td><td>' + estado + '</td><td>' + data[i].fields.FecEnv + 
                                '</td><td>' + data[i].fields.IdProtRef + '</td></tr>'
                    }
                    $('#dataProtocoloAjax').html(html);
                }
            });

        });

 
        
        $(".btnDetalle").bind("click",function(){
            //event.preventDefault();
            //alert('hicimos click en mi link')   
            var protocolo = $(this).attr("codigo")
            
            
            $.ajax({
                data : {'protocolo':protocolo},
                url : '/tramitedoc/busquedaDetalleProtocolo/',
                type: 'get',
                success: function(data){
                    var html = ''
                    for(var i=0; i<data.length; i++){
                        //html += '<ul><li>' + data[i].fields.idMProt + '</li></ul>'
                        //<li class="list-group-item">Documento 1</li>
                        //html += '<li class="list-group-item"><a href="#" class="dtlProtocolo" id = "detalleProt[]" urlPdf ="/media/pdf/'+data[i].fields.idDProt+'.pdf" num="'+ i +'">' + data[i].fields.nomDProt + '</a></li>'
                        html += '<a target="_blank" class="list-group-item aDoc" id = "aDoc" href="/media/'+data[i].fields.RutaPdfDProt+'" num="'+ i +'">' + data[i].fields.NomDProt + '</a>'
                    }
                    $('#lstDocs').html(html);
                    $('#txtMensaje').text($("#mensajeBandeja").attr('title'));
                    
                }
            });

        });
        
        $("aDoc").bind("click",function(){
            //Verificar 
            console.log('Hicimos click al protocolo' + $(this).attr("num"));
            
        });

        $('#texto_referencia').keyup(function() {
        
            var search = $('#texto_referencia').val();
            
            $('#tabla tr').show();
            
            
            if(search.length>0){
                $("#tabla tr td.nombre").not(":Contains('"+search+"')").parent().hide();
            }

        });

        $(".referencia").bind("click",function(){
            //alert($(this).attr("nombre"));
            $('#idRefMProt').val($(this).attr("codRef"));
            
            $('#seleccionarReferencia').modal('hide');
        });

        $(".btnObservar").bind("click",function(){
            var protocolo = $(this).attr("prot");
            var usuario = $(this).attr("usu");        
             $.ajax({
                data : {'protocolo':protocolo,'usuario':usuario},
                url : '/tramitedoc/observarProtocolo/',
                type: 'get',
                success: function(data){
                    
                    var html="";
                    html += '<h3> El protocolo: ' + protocolo + 'ha sido observado </h3>';
                    $('#mensajeError').html(html);
                    //alert('El Protocolo: '+ protocolo + ' ha sido observado.');
                    $('#frmMensaje').modal('show');
                    //location.reload();                    
                    }   
            });

        });
        $(".close").on("click",function(){
            band = $(this).attr("id");
            if(band !='false'){
                location.reload();
            }
            
        });

        $(".btnDetalleProtocolo").bind("click",function(){

            var protocolo = $(this).attr("codigo");
            
                       
            $.ajax({
                data : {'protocolo':protocolo,},
                url : '/tramitedoc/maestroProtocoloAjax/',
                type: 'get',
                success: function(data){
                    var tipoDocumento = ""
                    if(data[0].fields.docInter == '0'){
                        tipoDocumento = "Interno";
                    }else{
                        tipoDocumento  = "Externo";
                    }
                    var html="";

                    html += '<table class="table table-bordered"><tbody><tr><td><div class="form-group">'
                                +'<label class="col-lg-4 control-label" style="color:#082C4D;">Código</label>'
                                +'<label class="col-lg-7 control-label">: '+ data[0].pk +'</label>'
                            +'</div>'
                            +'<div class="form-group">'
                                +'<label class="col-lg-4 control-label" style="color:#082C4D;">Nombre</label>'
                                +'<label class="col-lg-7 control-label">: '+ data[0].fields.NomMProt +'</label>'
                            +'</div>'
                            +'<div class="form-group">'
                                +'<label class="col-lg-4 control-label" style="color:#082C4D;">Descripción</label>'
                                +'<label class="col-lg-7 control-label">: '+ data[0].fields.DescMProt +'</label>'
                            +'</div>'
                            +'<div class="form-group">'
                                +'<label class="col-lg-4 control-label" style="color:#082C4D;">Fecha de Entrega</label>'
                                +'<label class="col-lg-7 control-label">: '+ data[0].fields.FecEntMProt +'</label>'
                            +'</div>'
                            
                            +'<div class="form-group">'
                                +'<label class="col-lg-4 control-label" style="color:#082C4D;">Referencia</label>'
                                +'<label class="col-lg-7 control-label">: '+ data[0].fields.IdRefMProt +'</label>'    
                            +'</div>'
                            +'<div class="form-group">'
                                +'<label class="col-lg-4 control-label" style="color:#082C4D;">Tipo de Documento</label>'
                                +'<label class="col-lg-7 control-label">: '+ tipoDocumento +'</label>'
                            +'</div></td></tr></tbody></table>';
                   
                              
                    $('#detalleProtocolo').html(html);
                    $('#frmDetalleProtocolo').modal('show');
                    
                    }
                    
                
            });

        });
        
        $(".btnDetalleReferencia").bind("click",function(){

            var protocolo = $(this).attr("codigo");
            
                       
            $.ajax({
                data : {'protocolo':protocolo,},
                url : '/tramitedoc/maestroProtocoloAjax/',
                type: 'get',
                success: function(data){
                    var html="";

                     html += '<div class="form-group">'
                                +'<label class="col-lg-4 control-label" style="color:#082C4D;">Código</label>'
                                +'<label class="col-lg-7 control-label">: '+ data[0].pk +'</label>'
                            +'</div>'
                            +'<div class="form-group">'
                                +'<label class="col-lg-4 control-label" style="color:#082C4D;">Nombre</label>'
                                +'<label class="col-lg-7 control-label">: '+ data[0].fields.NomMProt +'</label>'
                            +'</div>'
                            +'<div class="form-group">'
                                +'<label class="col-lg-4 control-label" style="color:#082C4D;">Descripción</label>'
                                +'<label class="col-lg-7 control-label">: '+ data[0].fields.DescMProt +'</label>'
                            +'</div>'
                            +'<div class="form-group">'
                                +'<label class="col-lg-4 control-label" style="color:#082C4D;">Fecha de Entrega</label>'
                                +'<label class="col-lg-7 control-label">: '+ data[0].fields.FecEntMProt +'</label>'
                            +'</div>'
                            +'<div class="form-group">'
                                +'<label class="col-lg-4 control-label" style="color:#082C4D;">Referencia</label>'
                                +'<label class="col-lg-7 control-label">: '+ data[0].fields.IdRefMProt +'</label>'
                            +'</div>';
                   /*
                    html +=   '<blockquote><p style="color:#555">Código del Protocolo : '+ data[0].fields.idMProt +'</p>'
                             +'<p style="color:#555">Nombre del Protocolo : '+ data[0].fields.nomMProt +'</p>'   
                             +'<p style="color:#555">Descripción : '+ data[0].fields.descMProt +'</p>'   
                             +'<p style="color:#555">Fecha de Entrega : '+ data[0].fields.fecEntMProt +'</p>'
                             +'<p style="color:#555">Referencia : '+ data[0].fields.idRefMProt +'</p></blockquote>';
                            
                     */       
                            
                            
                    $('#detalleReferencia').html(html);
                    //alert('El Protocolo: '+ protocolo + ' ha sido observado.');   
                } 
            });
            
            $.ajax({
                data : {'protocolo':protocolo,},
                url : '/tramitedoc/busquedaDetalleProtocolo/',
                type: 'get',
                success: function(data){
                    var html="";
                    var htmlfor="";
                    var htmlfin ="";

                    html += '<table id="" class="table table-condensed">'
                                +'<thead>'
                                    +'<tr>'
                                        +'<th>Código</th>'
                                        +'<th>Nombre</th>'
                                        +'<th>PDF</th>'
                                    +'<tr>'
                                +'</thead>'
                                //+'<a target="_blank" href="/media/'+data[0].fields.rutaPDFMProy+'"><label class="col-lg-7 control-label">: '+ pdfProyecto +'</label></a>'    
                                +'<tbody>';

                                    for(var x=0;x<data.length;x++){
                                        //alert(data[x].fields.fecIniMCol + '- ' + data[x].fields.rutaPDFMCol);
                                        htmlfor += '<tr>'
                                            +'<td>'+data[x].pk+'</td>'
                                            +'<td>'+data[x].fields.NomDProt+'</td>'
                                            +'<td><a href="/media/'+ data[x].fields.RutaPdfDProt +'" target="_blank">'+data[x].fields.RutaPdfDProt+'</a></td>'
                                        +'</tr>';
                                    }
                                htmlfin +='</tbody>'+'</table>';
                                html = html + htmlfor + htmlfin
                        
                    $('#documentosReferencia').html(html);
                    //alert('El Protocolo: '+ protocolo + ' ha sido observado.');   
                } 
            });
            
            $('#frmDetalleReferencia').modal('show');

        });
        
        function cargarUsuarios(){
            var protocolo =''
            /*ids = [];
            usr = [];
            nom = [];*/
            $.ajax({
                data : {'protocolo':protocolo},
                url : '/tramitedoc/usuarioAjax/',
                type: 'get',
                success: function(data){
                    var html="";
                    for(var i=0; i<data.length; i++){
                        lstPk.push(data[i].pk);
                        lstUsers.push(data[i].fields.username);
                        lstNombres.push((data[i].fields.last_name).toUpperCase() + ", " +(data[0].fields.first_name).toUpperCase());
                    }
                    
                    return lstPk;
                }    
            });
        };

        $(".btnDetalleConvenio").bind("click",function(){

            var convenio = $(this).attr("codigo");
            var cliente = $(this).attr("cliente");
                        
            $.ajax({
                data : {'convenio':convenio,},
                url : '/tramitedoc/maestroConvenioAjax/',
                type: 'get',
                success: function(data){
                    //alert(data[0].fields.idMProy);
                    //$('#frmMensaje').modal('show');
                    var html="";
                    
                    /*html +=   '<blockquote><p style="color:#555">Código del Protocolo : '+ data[0].fields.idMProt +'</p>'
                             +'<p style="color:#555">Nombre del Protocolo : '+ data[0].fields.nomMProt +'</p>'   
                             +'<p style="color:#555">Descripción : '+ data[0].fields.descMProt +'</p>'   
                             +'<p style="color:#555">Fecha de Entrega : '+ data[0].fields.fecEntMProt +'</p>'
                             +'<p style="color:#555">Referencia : '+ data[0].fields.idRefMProt +'</p></blockquote>';
                    */
                    var pdfProyecto = "No se ha registrado aún";
                    var pdfConvenio = "No se ha registrado aún";
                    var pdfActaCierre = "No se ha registrado aún";
                    if(data[0].fields.rutaPDFMProy != ""){
                        pdfProyecto = data[0].fields.RutaPDFMProy;
                    }
                    if(data[0].fields.rutaPDFConvMProy != ""){
                        pdfConvenio = data[0].fields.RutaPDFConvMProy;
                    }
                    if(data[0].fields.rutaPDFACMProy != ""){
                        pdfActaCierre = data[0].fields.RutaPDFACMProy;
                    }
                    html += '<div class="form-group">'
                                +'<label class="col-lg-4 control-label" style="color:#082C4D;">Nº de Convenio</label>'
                                +'<label class="col-lg-8 control-label">: '+ data[0].pk +'</label>'
                            +'</div>'
                            +'<div class="form-group">'
                                +'<label class="col-lg-4 control-label" style="color:#082C4D;">Convocatoria</label>'
                                +'<label class="col-lg-8 control-label">: '+ data[0].fields.IdConv +'</label>'
                            +'</div>'
                            +'<div class="form-group">'
                                +'<label class="col-lg-4 control-label" style="color:#082C4D;">Unidad Ejecutora</label>'
                                +'<label class="col-lg-8 control-label">: '+ (cliente).substring(0,32) +'</label>'
                            +'</div>'
                            +'<div class="form-group">'
                                +'<label class="col-lg-4 control-label" style="color:#082C4D;">Nombre del Proyecto</label>'
                                +'<label class="col-lg-8 control-label">: '+ (data[0].fields.NomMProy).substring(0,32) +'</label>'
                            +'</div>'
                            +'<div class="form-group">'
                                +'<label class="col-lg-4 control-label" style="color:#082C4D;">CCI</label>'
                                +'<label class="col-lg-8 control-label">: '+ data[0].fields.NumCtaInterMProy +'</label>'
                            +'</div>'
                            
                            +'<div class="form-group">'
                                +'<label class="col-lg-4 control-label" style="color:#082C4D;">Perfil del Proyecto</label>'
                                +'<a target="_blank" href="/media/'+data[0].fields.RutaPDFMProy+'"><label class="col-lg-8 control-label">: '+ (pdfProyecto).substring(11,50) +'</label></a>'    
                            +'</div>'
                            +'<div class="form-group">'
                                +'<label class="col-lg-4 control-label" style="color:#082C4D;">Convenio</label>'
                                +'<a target="_blank" href="/media/'+data[0].fields.RutaPDFConvMProy+'"><label class="col-lg-8 control-label">: '+ (pdfConvenio).substring(11,50) +'</label></a>'
                            +'</div>'
                            +'<div class="form-group">'
                                +'<label class="col-lg-4 control-label" style="color:#082C4D;">Acta de Cierre</label>'
                                +'<a target="_blank" href="/media/'+data[0].fields.RutaPDFACMProy+'"><label class=col-lg-8 control-label>: '+ (pdfActaCierre).substring(11,50) +'</label></a>'
                               
                            +'</div>'
                            +'<div class="form-group">'
                                +'<label class="col-lg-12 control-label"></label>'
                                +'<label class="col-lg-12 control-label"></label>'
                                +'<label class="col-lg-12 control-label"></label>'
                            +'</div>'

                            +'<div class="form-group">'
                                +'<label class="col-lg-4 control-label" style="color:#082C4D;">Inicia el</label>'
                                +'<label class="col-lg-3 control-label">: '+ data[0].fields.FecIniRealMProy +'</label>'
                                +'<label class="col-lg-2 control-label" style="color:#082C4D;">Termina</label>'
                                +'<label class="col-lg-3 control-label">: '+ data[0].fields.FecFinRealMProy +'</label>'
                            +'</div>'
                            +'<div class="form-group">'
                                
                                +'<label class="col-lg-4 control-label" style="color:#082C4D;"">Duración (m)</label>'
                                +'<label class="col-lg-8 control-label">: '+ data[0].fields.TiempoMProy +' meses</label>'
                            +'</div>'

                            +'</div>'
                            +'<div class="form-group">'
                                +'<label class="col-lg-12 control-label"></label>'
                                +'<label class="col-lg-12 control-label"></label>'
                                +'<label class="col-lg-12 control-label"></label>'
                            +'</div>'

                            //TABLA DE FINANCIAMIENTO DEL PROYECTO
                            +'<div class="form-group col-lg-12">' 
                            +'<table class="table table-condensed">'
                                +'<thead>'
                                    +'<tr style="align:center;">'
                                        +'<th></th>'
                                        +'<th style="width:120px; text-align:center; background-color: #222; color:#fff">Financiamiento</th>'
                                        +'<th style="width:120px; text-align:center; background-color: #222; color:#fff">Adendas</th>'
                                        +'<th style="width:120px; text-align:center; background-color: #222; color:#fff">Total</th>'
                                    +'</tr>'
                                +'</thead>'
                                +'<tbody>'
                                    
                                    +'<tr>'
                                        +'<td align="center">Fondo Italo Peruano</td>'
                                        +'<td align="right"> S/. '+ data[0].fields.MontTInvRealFipMProy +'</td>'
                                        +'<td align="right"> S/. '+ data[0].fields.MontTotAdeFipMProy +'</td>'
                                        +'<td style="font-weight: bold; text-align:right;"> S/. '+ parseFloat(parseFloat(data[0].fields.MontTInvRealFipMProy) + parseFloat(data[0].fields.MontTotAdeFipMProy)) +'</td>'
                                    +'</tr>'
                                    +'<tr>'
                                        +'<td align="center">Unidad Ejecutora</td>'
                                        +'<td align="right"> S/. '+ data[0].fields.MontTInvRealCliMProy +'</td>'
                                        +'<td align="right"> S/. '+ data[0].fields.MontTotAdeCliMProy +'</td>'
                                        +'<td style="font-weight: bold; text-align:right;"> S/. '+ parseFloat(parseFloat(data[0].fields.MontTInvRealCliMProy) + parseFloat(data[0].fields.MontTotAdeCliMProy)) +'</td>'
                                    +'</tr>'
                                    +'<tr>'
                                        +'<td align="center">Asociados</td>'
                                        +'<td align="right"> S/. '+ data[0].fields.MontTInvRealOtrMProy +'</td>'
                                        +'<td align="right"> S/. '+ data[0].fields.MontTotAdeOtrMProy +'</td>'
                                        +'<td style="font-weight: bold; text-align:right;"> S/. '+ parseFloat(parseFloat(data[0].fields.MontTInvRealOtrMProy) + parseFloat(data[0].fields.MontTotAdeOtrMProy)) +'</td>'
                                    +'</tr>'
                                    +'<tr>'
                                        
                                        +'<td colspan="3" style="font-weight: bold; text-align:right;">TOTAL</td>'
                                        +'<td style="font-weight: bold; text-align:right;"> S/. '+ parseFloat(parseFloat(parseFloat(data[0].fields.MontTInvRealOtrMProy) + parseFloat(data[0].fields.MontTotAdeOtrMProy))+parseFloat(parseFloat(data[0].fields.MontTInvRealCliMProy) + parseFloat(data[0].fields.MontTotAdeCliMProy))+parseFloat(parseFloat(data[0].fields.MontTInvRealFipMProy) + parseFloat(data[0].fields.MontTotAdeFipMProy))) +'</td>'
                                    +'</tr>'
                                    +'<tr>'
                                        +'<td colspan="3"></td>'
                                        +'<td></td>'
                                    +'</tr>'
                                    +'<tr>'
                                        +'<td colspan="3"></td>'
                                        +'<td></td>'
                                    +'</tr>'
                                +'</tbody>'
                            +'</table>'
                            +'</div>'
                            //FIN DE TABLA DE FINANCIMIENTO
                            
                            //+'<p style="color:#ff0000;">Convocatoria :</p><p>2013</p><br>'
                            +'</td>';

                    $('#detalleConvenio').html(html);
                    //alert('El Protocolo: '+ protocolo + ' ha sido observado.');
                    
                    //location.reload();                    
                    }

            });
            
            //alert(empPk[0]);
            
            $.ajax({
                data : {'convenio':convenio,},
                url : '/tramitedoc/colaboradoresConvenioAjax/',
                type: 'get',
                success: function(data){
                    //alert(data[0].fields.idMPer);
                    var html="";
                    var htmlfor="";
                    var htmlfin="";
                    html += '<table id="" class="table table-condensed">'
                                +'<thead>'
                                    +'<tr>'
                                        +'<th>Responsable</th>'
                                        +'<th>Inicia</th>'
                                        +'<th>Termina</th>'
                                        +'<th>Duración (m)</th>'
                                        +'<th>Monto Total S/.</th>'
                                        +'<th>PDF</th>'
                                    +'<tr>'
                                +'</thead>'
                                //+'<a target="_blank" href="/media/'+data[0].fields.rutaPDFMProy+'"><label class="col-lg-7 control-label">: '+ pdfProyecto +'</label></a>'    
                                +'<tbody>';

                                    for(var x=0;x<data.length;x++){
                                        //alert(data[x].fields.fecIniMCol + '- ' + data[x].fields.rutaPDFMCol);
                                        htmlfor += '<tr>'
                                            +'<td><label class="nombreResponsable" id="'+ data[x].fields.IdMPer +'">'+data[x].fields.IdMPer+'</label></td>'
                                            +'<td>'+data[x].fields.FecIniMCol+'</td>'
                                            +'<td>'+data[x].fields.FecFinMCol+'</td>'
                                            +'<td>'+data[x].fields.TiempoMCol+'</td>'
                                            +'<td>'+data[x].fields.MontoMCol+'</td>'
                                            +'<td><a href="/media/'+ data[x].fields.RutaPDFMCol +'" target="_blank">'+(data[x].fields.RutaPDFMCol).substring(12,40);+'</a></td>'
                                        +'</tr>';
                                    }
                                htmlfin +='</tbody>'+'</table>';
                                html = html + htmlfor + htmlfin

                    $('#colaboradoresConvenio').html(html);
                                 
                    }

            });
            
            $.ajax({
                data : {'convenio':convenio,},
                url : '/tramitedoc/modificatoriasConvenioAjax/',
                type: 'get',
                success: function(data){
                   
                    var html="";
                    var htmlfor="";
                    var htmlfin="";
                    
                    html += '<table id="" class="table table-condensed">'
                                +'<thead>'
                                    +'<tr>'
                                        +'<th>Inicia</th>'
                                        +'<th>Finaliza</th>'
                                        +'<th>F. FIP</th>'
                                        +'<th>F. UE</th>'
                                        +'<th>F. ASOC</th>'
                                        +'<th>PDF</th>'
                                    +'<tr>'
                                +'</thead>'
                                //+'<a target="_blank" href="/media/'+data[0].fields.rutaPDFMProy+'"><label class="col-lg-7 control-label">: '+ pdfProyecto +'</label></a>'    
                                +'<tbody>';

                                    for(var x=0;x<data.length;x++){
                                        //alert(data[x].fields.fecIniMCol + '- ' + data[x].fields.rutaPDFMCol);
                                        //monto = 0.0;
                                        //monto = parseFloat(data[x].fields.montAportFIPDProy) + parseFloat(data[x].fields.montAportCliDProy) + parseFloat(data[x].fields.montAportOtrDProy);
                                        htmlfor +='<tr>'
                                            +'<td>'+data[x].fields.FecFirmaDProy+'</td>'
                                            +'<td>'+data[x].fields.FecFinDProy+'</td>'
                                            +'<td class="text-right">S/. '+data[x].fields.MontAportFIPDProy+'</td>'
                                            +'<td class="text-right">S/. '+data[x].fields.MontAportCliDProy+'</td>'
                                            +'<td class="text-right">S/. '+data[x].fields.MontAportOtrDProy+'</td>'
                                            +'<td><a href="/media/'+ data[x].fields.RutaPDFDProy +'" target="_blank">'+(data[x].fields.RutaPDFDProy).substring(11)+'</a></td>'
                                        +'</tr>';
                                    }
                                htmlfin +='</tbody>'+'</table>';
                                html = html + htmlfor + htmlfin

                    $('#modificatoriasConvenio').html(html);
                                       
                    }

            });
        
            $('#frmDetalleConvenio').modal('show');

        });
        
        //nombreResponsable
        
        
        $(".btnCrear").bind("click",function(){
            var html = '';
            html += '<input type="text" class="form-control" id="esto"  name="esto" placeholder="Ingrese apellido paterno">';
            
            $('#pruebaAki').html(html);
        });

        $("#btnAgregarModificatoria").on("click",function(){
            $('#frmAgregarModificatoria').modal('show');

        });

        $("#btnAgregarColaborador").on("click",function(){
            $('#frmAgregarColaborador').modal('show');
        
        });

        $("#btnRegistrarColaborador").on("click",function(){
            var esto = "adsfadsf";
            var archivo = $('#id_rutaPDFMCol').val();
            alert(archivo);
            $.ajax({
                data : {'esto':esto,'archivo':archivo},
                url : '/tramitedoc/registrarColaboradorAjax/',
                type: 'get',
                success: function(data){
                    alert('olas');
                    alert(data.status);
                },
                error: function(a,b,c){
                    alert(b);
                }
            });

        });

        // VERIFICAR JS
        $(".filtrarRegion").bind("click",function(){
             
            
            var protocolo = $(this).attr("codigo")
            
            
            $.ajax({
                data : {'protocolo':protocolo},
                url : '/tramitedoc/busquedaDetalleProtocolo/',
                type: 'get',
                success: function(data){
                    var html = ''
                    for(var i=0; i<data.length; i++){
                        //html += '<ul><li>' + data[i].fields.idMProt + '</li></ul>'
                        //<li class="list-group-item">Documento 1</li>
                        //html += '<li class="list-group-item"><a href="#" class="dtlProtocolo" id = "detalleProt[]" urlPdf ="/media/pdf/'+data[i].fields.idDProt+'.pdf" num="'+ i +'">' + data[i].fields.nomDProt + '</a></li>'
                        html += '<a target="_blank" class="list-group-item aDoc" id = "aDoc" href="/media/'+data[i].fields.RutaPdfDProt+'" num="'+ i +'">' + data[i].fields.NomDProt + '</a>'
                    }
                    $('#lstDocs').html(html);
                }
            });

        });
        
        $("#idRegMCli").on("change",function(){
            var idregion = $(this).attr("value");
            //alert(idregion);
            
            $.ajax({
                data : {'idregion':idregion},
                url : '/tramitedoc/listaDepartamentoAjax/',
                type: 'get',
                success: function(data){
                    html = '<option value="">Seleccione...</option>';
                    for(var i=0;i<data.length;i++){
                        //alert(data[x].fields.fecIniMCol + '- ' + data[x].fields.rutaPDFMCol);
                        html += '<option value="'+ data[i].pk +'">'+ data[i].fields.NomDTab +'</option>';
                                
                        }
                        $('#idDepMCli').html(html);

                }
            });

        });

        $("#idDepMCli").on("change",function(){
            var iddepa = $(this).attr("value");
            //alert(iddepa);
            
            $.ajax({
                data : {'iddepa':iddepa},
                url : '/tramitedoc/listaProvinciaAjax/',
                type: 'get',
                success: function(data){
                    html = '<option value="">Seleccione...</option>';
                    for(var i=0;i<data.length;i++){
                        //alert(data[x].fields.fecIniMCol + '- ' + data[x].fields.rutaPDFMCol);
                        html += '<option value="'+ data[i].pk +'">'+ data[i].fields.NomDTab +'</option>';
                                
                        }
                        $('#idProvMCli').html(html);

                }
            });

        });

        $("#idProvMCli").on("change",function(){
            var idprov = $(this).attr("value");
            //alert(iddepa);
            
            $.ajax({
                data : {'idprov':idprov},
                url : '/tramitedoc/listaDistritoAjax/',
                type: 'get',
                success: function(data){
                    html = '<option value="">Seleccione...</option>';
                    for(var i=0;i<data.length;i++){
                        //alert(data[x].fields.fecIniMCol + '- ' + data[x].fields.rutaPDFMCol);
                        html += '<option value="'+ data[i].pk +'">'+ data[i].fields.NomDTab +'</option>';
                                
                        }
                        $('#idDistMCli').html(html);

                }
            });

        });

        $(".montoReal").on("focusout",function(){
            var montoRealFip = 0.0;
            var montoRealClie = 0.0;
            var montoRealOtros = 0.0;
            
            montoRealFip = $("#montTInvRealFipMProy").val();
            montoRealClie = $("#montTInvRealCliMProy").val();
            montoRealOtros = $("#montTInvRealOtrMProy").val();
            

            var total = (parseFloat(montoRealFip) + parseFloat(montoRealClie) + parseFloat(montoRealOtros));

            //$('#idRefMProt').val($(this).attr("codRef"));
            
            $("#montTotRealMProy").val(total);
            
        });
        $(".montoAdendas").on("focusout",function(){
            var montoFip = 0.0;
            var montoClie = 0.0;
            var montoOtros = 0.0;
            
            montoFip = $("#montTotAdeFipMProy").val();
            montoClie = $("#montTotAdeCliMProy").val();
            montoOtros = $("#montTotAdeOtrMProy").val();
            

            var total = (parseFloat(montoFip) + parseFloat(montoClie) + parseFloat(montoOtros));

            //$('#idRefMProt').val($(this).attr("codRef"));
            
            $("#montTotAdeTotMProy").val(total);
            
        });

        /* ===  SOLO NUMEROS == */
        $(".noModificarValorDeTexto").keydown(function(event) {
            if(event.shiftKey)
            {
                event.preventDefault();
            }
            if(event.keyCode != 9){
                event.preventDefault();   
            }
        });
        
        $("#idMPer").on("change",function(){
            var codPer = $(this).val();
            //alert(codPer);
            
            $.ajax({
                data : {'codPer':codPer},
                url : '/tramitedoc/tipoPersonalAjax/',
                type: 'get',
                success: function(data){
                    //html = '<option value="">Seleccione...</option>';
                    if(data.status=="True"){
                        
                        $("#personalExterno").addClass("hide");
                    }
                    else{
                        
                        $("#personalExterno").removeClass("hide");
                    }
                    
                    /*for(var i=0;i<data.length;i++){
                        //alert(data[x].fields.fecIniMCol + '- ' + data[x].fields.rutaPDFMCol);
                        html += '<option value="'+ data[i].pk +'">'+ data[i].fields.nomDTab +'</option>';
                                
                        }
                        $('#idDistMCli').html(html);*/

                }
            });

        });
        
        $("#montoMenMCol").on("focusout",function(){
            //obtenemos la fecha de inicio y la de fin
            var fechaInicio = new Date($("#fecIniMCol").val());
            var fechaFin = new Date($("#fecFinMCol").val());

            var pagoMensual = parseFloat($(this).val());

            var difAnio = fechaFin.getYear() - fechaInicio.getYear();
            var difmes = fechaFin.getMonth() - fechaInicio.getMonth();
            var tiempo = (difAnio * 12) + difmes;

            var montoTotal = pagoMensual * tiempo;

            $("#tiempoMCol").val(tiempo);
            $("#montoMCol").val(montoTotal);
            console.log(tiempo);
        });
        $("#fecFinRealMProy").on("focusout",function(){
            //obtenemos la fecha de inicio y la de fin
            var fechaInicio = new Date($("#fecIniRealMProy").val());
            var fechaFin = new Date($("#fecFinRealMProy").val());

            var difAnio = fechaFin.getYear() - fechaInicio.getYear();
            var difmes = fechaFin.getMonth() - fechaInicio.getMonth();
            var tiempo = (difAnio * 12) + difmes;

            $("#tiempoMProy").val(tiempo);
            $("#fecEntRealMProy").val($("#fecFinRealMProy").val());
            
            
            
        });

        $("#chkObservar").on("click",function(){
            if($(this).is(":checked")){
                $("#protObservado").val("1");

            }else{
                $("#protObservado").val("0");
            }


            
        });
        //VERIFICAR SI ESTA FUNCION TRABAJA
        $("#agregar_usuario").on("click",function(){
            cod = '2';
            $.ajax({
                data : {'id':cod},
                url : '/ajax/editar_usuario/',
                type: 'get',
                success: function(data){
                    //html = '<option value="">Seleccione...</option>';
                    if(data.status=="True"){
                        
                        $("#personalExterno").addClass("hide");
                    }
                    else{
                        
                        $("#personalExterno").removeClass("hide");
                    }
                    
                    /*for(var i=0;i<data.length;i++){
                        //alert(data[x].fields.fecIniMCol + '- ' + data[x].fields.rutaPDFMCol);
                        html += '<option value="'+ data[i].pk +'">'+ data[i].fields.nomDTab +'</option>';
                                
                        }
                        $('#idDistMCli').html(html);*/

                }
            });
            
            
        });
        
        $("#nuevo_usuario").on("click",function(){
             $('#divMensaje').addClass("hide");
        });

        $("#nuevo_personal").on("click",function(){
             $('#divMensaje').addClass("hide");
        });


        $("#grabar_usuario").on("click",function(){
            
            p1 = $("#id_password").val();
            p2 = $("#id_password2").val();
            us = $("#id_username").val();
            tu = $("#id_tipoUsuario").val();
            cl = $("#id_idMCli").val();
            pr = $("#id_idMPer").val();
            //alert($("#id_fecIngreso").val());
            
            if(p1==='' || p2==='' || us==='' || tu==='' || cl==='' || pr===''){
                $('#mensaje_modal').removeClass("hide");
                $('#mensaje').text('Deben ingresarse todos los campos.');
            }
            else{
                if(p1!=p2){
                    $('#mensaje_modal').removeClass("hide");
                    $('#mensaje').text('Las constraseñas no coinciden.');

                }
                else{
                    var frm = $('#form_nuevo_usuario');
                    frm.serialize()
                    console.log(frm.attr("method"));
                    $.ajax({
                        type: 'post',
                        url: '/administracion/usuarios/',
                        data: frm.serialize(),
                        success: function (data) {
                            //alert(data.mensaje);
                            /*$(':input','#form_nuevo_usuario')
                                .not(':button, :submit, :reset, :hidden')
                                .val('')
                                .removeAttr('checked')
                                .removeAttr('selected');*/
                            $('#nuevo_usuario_modal').modal('hide');
                            html = '<tr class="text-info" id="tr'+ data.id +'"><td class="text-center">'+data.id+'</td><td class="nombre">'+data.last_name+'</td><td>'+data.first_name+'</td><td>'+data.username+'</td><td>'+data.tipoUsuario+'</td><td>'+ data.fecIngreso+'</td>';
                            html += '<td><a href="#" class="editar_registro" codigo="' + data.id + '" modelo="0"><span class="text-warning glyphicon glyphicon-pencil"></span></a></td><td ><a href="#" class="eliminar_registro" codigo="' + data.id + '" modelo="0"><span class="text-danger glyphicon glyphicon-trash"></span></a></td></tr>';
                            frm[0].reset();
                            $('#tabla').append(html);
                            $('#div_mensaje').removeClass("hide");
                            $('p#mensaje').text('Se ha registrado un nuevo usuario');

                        },
                        error: function(data) {
                            //alert('Ha sucedido un error' + data.mensaje);
                            $(':input','#form_nuevo_usuario')
                                .not(':button, :submit, :reset, :hidden')
                                .val('')
                                .removeAttr('checked')
                                .removeAttr('selected');
                            $('#nuevo_usuario_modal').modal('hide');
                            $('#div_mensaje').removeClass("hide");
                            $('#mensaje').text(data.mensaje + ', ' + data.status );
                        }
                    });   
                }
            }
        });
        
        
        $("#grabar_personal").on("click",function(){
            
            ap = $("#id_ApePMPer").val();
            am = $("#id_ApeMMPer").val();
            nom = $("#id_NomMPer").val();
            fn = $("#id_FechNacMPer").val();
            tp = $("#id_IdTipPerMPer").val();
            td = $("#id_IdTipDocMPer").val();
            nd = $("#id_NDocMPer").val();
            fi = $("#id_FecIngMPer").val();
            te = $("#id_Tel1MPer").val();
            em1 = $("#id_Email1MPer").val();
            ia = $("#id_IdArea").val();

            
            if(ap==='' || am==='' || nom===''){
                $('#mensaje_modal').removeClass("hide");
                $('#mensaje').text('Deben ingresarse todos los campos'); 
            }
            else{
                
                    var frm = $('#frm_nuevo_personal');
                    //alert(frm.attr('method'));
                    $.ajax({
                        type: 'post',
                        url: '/administracion/personal/',
                        data: frm.serialize(),
                        success: function (data) {

                            //alert(data.mensaje);
                            /*$(':input','#form_nuevo_personal')
                                .not(':button, :submit, :reset, :hidden, ')
                                .val('')
                                .removeAttr('checked')
                                .removeAttr('selected');*/
                            
                            html = '<tr class="text-info"><td>'+data[0].pk+'</td><td>'+data[0].fields.ApePMPer +' ' +data[0].fields.ApeMMPer +'</td><td>'+data[0].fields.NomMPer+'</td><td>'+data[0].fields.FechNacMPer+'</td><td>'+data[0].NDocMPer+'</td><td>'+ data[0].fields.Tel1MPer+'</td><td>'+ data[0].fields.Email1MPer +'</td></tr>';
                            html += '<td><a href="#" class="editar_registro" codigo="' + data[0].pk + '" modelo="4"><span class="text-warning glyphicon glyphicon-pencil"></span></a></td><td ><a href="#" class="eliminar_registro" codigo="' + data[0].pk + '" modelo="4"><span class="text-danger glyphicon glyphicon-trash"></span></a></td></tr>';
                            frm[0].reset();
                            $('#tabla').append(html);
                            $('#mensaje_modal').removeClass("hide");
                            $('#mensaje_personal').text('success'+data.mensaje);
                            $('#nuevo_personal_modal').modal('hide');
                            $('#tabla').append(html);

                        },
                        error: function(data) {
                            //$('#nuevo_personal_modal').modal('hide');
                            $('#mensaje_modal').removeClass("hide");
                            $('#mensaje_personal').text('Error: ' + data.mensaje);
                        }
                    });   
                
            }
        });
        
        $("#btn_modificar_password").on("click",function(){
            
            pass1 = $("#pass1").val();
            pass2 = $("#pass2").val();
            if(pass2==='' || pass1===''){
                $('#divMensajePassword').removeClass("show");
                $('#mensaje_modificar_password').text('Ingresar datos en ambos campos.');
            }else{
                if(pass2===pass1){

                    $.ajax({
                        data : {'pass1':pass1},
                        url : '/administracion/modificar/password/',
                        type: 'GET',
                        success: function(data){
                            /*$(':input','#form_modificar_password')
                                .not(':button, :submit, :reset, :hidden')
                                .val('');*/
                                //alert('1');
                                $('#divMensajePassword').removeClass("hide");
                                $("#mensaje_modificar_password").text(data.mensaje);
                                
                            
                        },
                        error: function(data){
                            /*$(':input','#form_modificar_password')
                                .not(':button, :submit, :reset, :hidden')
                                .val('');*/
                                //alert('2');
                                $("#divMensajePassword").removeClass("hide");
                                $("#mensaje_modificar_password").text(data.mensaje);

                        }
                    });

                }
                else{
                    $("#divMensajePassword").removeClass("hide");
                    $("#mensaje_modificar_password").text("Las contraseñas no coinciden");
                }
            }
                
        });
        
        $("#estado_menu").on("click",function(){
            cod = $(this).attr("cod")

            if (cod === '1'){
                $("#menus").removeClass("hide");
                $("#cuerpo").removeClass("col-lg-12");
                $("#cuerpo").addClass("col-lg-10");
                $("#datosPress").attr("height:550px;width:1350px; overflow:scroll;");
                $(this).attr("cod",0);
                $(this).text('Ocultar Menú');

            }else{
                $("#menus").addClass("hide");
                $("#cuerpo").removeClass("col-lg-10");
                $("#cuerpo").addClass("col-lg-12");
                $("#datosPress").attr("style","height:550px;width:auto; overflow:scroll;");
                $(this).attr("cod",1);
                $(this).text('Mostrar Menú');
            }
         });


        $("#nuevo").on("click",function(){
            var html="";
            for(var i=0; i<5; i++){
                html += "<button class='nn' cod='"+i+"''>"+i+"</button>";
            }
            $("#esto_div").html(html);
         });
         $(".nn").live("click",function(){
            alert($(this).attr("cod"));
         });


        function eliminar_registro(modelo, id){
            $.ajax({
                    type: 'get',
                    url: '/appwebfip/ajax/eliminar_registro/',
                    data: {'modelo':modelo,'codigo':id},
                    success: function(data) {
                        $('#div_mensaje').removeClass("hide");
                        $('p#mensaje').text(data.mensaje);
                        $('#tr'+id).fadeOut("slow", function(){
                                $(this).remove();
                        });
                        
                    },
                    error: function(data) {
                        $('#div_mensaje').removeClass("hide");
                        $('p#mensaje').text('Error :' + data.mensaje);
                    }
            });
         }

        $(".eliminar_registro").live("click",function(){
            $('#div_mensaje').addClass("hide");
            modelo = $(this).attr("modelo");
            id = $(this).attr("codigo");
            //alert(modelo +'-'+id)
            eliminar_registro(modelo, id);
         });
        
        $("#btnCargarPresupuesto").on("click",function(){
            $("#cargador").show();
         });
         




        




});