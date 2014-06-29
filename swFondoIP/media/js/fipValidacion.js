   $().ready(function () {
            //FORMULARIO UNIDAD EJECUTORA
            $("#frmUnidadEjecutora").validate({
                debug: false,
                rules: {
                    idMCli:{required:true},
                    nomMCli:{required:true},
                    idTipMCli:{required:true},
                    idTipInstMCli:{required:true},
                    dirMCli:{required:true},
                    idPaisMCli:{required:true},
                    idRegMCli:{required:true},
                    idDepMCli:{required:true},
                    idProvMCli:{required:true},
                    idDistMCli:{required:true},
                    refMCli:{required:true},
                    tel1MCli:{required:true, minlength:5, maxlength:15},
                    tel2MCli:{minlength:5, maxlength:15},
                    tel3MCli:{minlength:5, maxlength:15},
                    estMCli:{required:true} 
                },
                messages: {
                  
                    //FORMULARIO CLIENTE
                    idMCli: "Ing. codigo de cliente",
                    nomMCli: "Campo obligatorio",
                    idTipMCli: "Seleccione",
                    idTipInstMCli: "Seleccione",
                    dirMCli: "Campo obligatorio",
                    idPaisMCli: "Seleccione",
                    idRegMCli: "Seleccione",
                    idDepMCli: "Seleccione",
                    idProvMCli: "Seleccione",
                    idDistMCli: "Seleccione",
                    refMCli: "Campo obligatorio",
                    tel1MCli:"Campo obligatorio",
                    estMCli: "Seleccione"
                }
            });

            //FORMULARIO PERSONAL
            $("#frmPersonal").validate({
                debug: false,
                rules: {
                    idMPer : {required :true },
                    apePMPer : {required:true},
                    apeMMPer : {required:true},
                    nomMPer : {required:true},
                    fechNacMPer : {required:true},
                    idTipPerMPer : {required:true},
                    idTipDocMPer : {required:true},
                    nDocMPer : {required:true},
                    //estMPer = {required:true},
                    fecIngMPer : {required:true}
                },
                messages: {
                    idMPer : "Ingrese un codigo",
                    apePMPer : "Campo obligatorio",
                    apeMMPer : "Campo obligatorio",
                    nomMPer : "Campo obligatorio",
                    fechNacMPer : "Campo obligatorio",
                    idTipPerMPer : "Campo obligatorio",
                    idTipDocMPer : "Campo obligatorio",
                    nDocMPer : "Campo obligatorio",
                    //estMPer = {required:true},
                    fecIngMPer : "Campo obligatorio"
                }
            });

            //FORMULARIO USUARIO
            $("#form_nuevo_usuario").validate({
                debug: false,
                rules: {
                    id_idMPer      : { required: true },
                    id_username     : { required: true },
                    id_fecIngreso     : { required: true},
                    id_tipoUsuario    : { required: true},
                    id_password    : { required: true,equalTo:"#id_password2" },
                   
                },
                messages: {
                    id_idMPer      : "Seleccione un personal",
                    id_username     : "Ing. el nombre de usuario",
                    id_fecIngreso     : "Seleccione una fecha",
                    id_tipoUsuario    : "Seleccione tipo de usuario",
                    id_password    : "Las contraseñas no coinciden",
                    
                    
                }
            });

            //FORMULARIO DE LOGUEO
            $("#frmLogueo").validate({
                debug: false,
                rules: {
                    username: { required: true, minlength: 2},
                    password: { required: true, minlength: 2}
                    
                },
                messages: {
                    username: "Campo obligatorio",
                    password: "Campo obligatorio"
                    
                   
                }
            });

            //FORMULARIO USUARIO
            $("#frmUsuario").validate({
                debug: false,
                //FORMULARIO USUARIO
                rules: {
                    idMPer      : { required: true },
                    logMUsu     : { required: true },
                    claMUsu     : { required: true, minlength: 8 },
                    claMUsu2    : { required: true, minlength: 8, equalTo:"#claMUsu" },
                    permMUsu    : { required: true },
                    estMUsu     : { required: true },
                    fecIngMUsu  : { required: true }
                    
                },
                messages: {
                    idMPer      : "Seleccione un personal",
                    idMUsu      : "Seleccione un personal",
                    logMUsu     : "Ing. el nombre de usuario",
                    claMUsu     : "Ing. una contraseña",
                    claMUsu2    : "Confirme contraseña",
                    permMUsu    : "Seleccione los permisos del usuario",
                    estMUsu     : "Seleccione un estado",
                    fecIngMUsu  : "Seleccione fecha"
                }
            });
            //FORMULARIO PROTOCOLO
            $("#frmProtocolo").validate({
                debug: false,
                rules:{
                    docInter    : { required: true},
                    nomMProt    : { required: true},
                    descMProt   : { required: true},
                    fecEntMProt : { required: true},
                    idTipFormEntMProt : { required: true},
                    idTipDocGen : { required: true},
                },
                messages:{
                    docInter    : "Seleccione la procedencia del documento",
                    nomMProt    : "Ingrese el nombre del protocolo",
                    descMProt   : "Ingrese la descripción del protocolo",
                    fecEntMProt : "Seleccione la fecha de entrega del protocolo",
                    idTipFormEntMProt : "Seleccione el formato de entrega del protocolo",
                    idTipDocGen : "Seleccion el formato del documento generado",
                }


            });
            $("#frmDetalleProtocolo").validate({
                debug: false,
                rules:{
                    nomDProt    : { required:true},
                    idTipDocDProt: { required:true},
                    ubiFisDProt : { required:true},
                },
                messages:{
                    nomDProt    : "Ingrese el nombre del documento",
                    idTipDocDProt: "Seleccione el tipo de documento",
                    ubiFisDProt : "Seleccione la ubicación",
                }
            });
            $("#frmConvenio").validate({
                debug: false,
                rules:{
                    idConv      : { required: true},
                    nomMProy    : { required: true},
                    idTipProMProy: { required: true},
                    idSector    : { required: true},
                    idBanco     : { required: true},
                    numCtaInterMProy: { required: true},
                    fecFirmaMProy: { required: true},

                    montInvFipMProy: { required: true},
                    montInvCliMProy: { required: true},
                    montTInvRealFipMProy: { required: true},
                    montTInvRealCliMProy: { required: true},

                },
                messages:{
                    idConv      : "Seleccione la convocatoria",
                    nomMProy    : "Ingrese el nombre del convenio",
                    idTipProMProy: "Seleccione el tipo de convenio",
                    idSector    : "Seleccione el sector",
                    idBanco     : "Seleccione el banco",
                    numCtaInterMProy: "Ingrese el código de cuenta interbancaria",
                    fecFirmaMProy: "Seleccione la fecha de firma del convenio",

                    montInvFipMProy: "Campo Requerido",
                    montInvCliMProy: "Campo Requerido",
                    montTInvRealFipMProy: "Campo Requerido",
                    montTInvRealCliMProy: "Campo Requerido",
                }
            });

            $("#frmColaborador").validate({
                debug: false,
                rules:{
                    idMPer      : { required: true},
                    idTipoCargoProy    : { required: true},
                    fecFirmaMCol: { required: true},
                    fecIniMCol    : { required: true},
                    fecFinMCol     : { required: true},
                    montoMCol: { required: true},
                    montoMenMCol: { required: true},

                   

                },
                messages:{
                    idMPer      : "Seleccione personal",
                    idTipoCargoProy    : "Seleccione cargo",
                    fecFirmaMCol: "Ingrese fecha",
                    fecIniMCol    : "Ingrese fecha",
                    fecFinMCol     : "Ingrese fecha",
                    montoMCol: "Ingrese monto",
                    montoMenMCol: "Ingrese monto",

                  
                }
            });

            $("#frmModificatoria").validate({
                debug: false,
                rules:{
                    idTipDocDProy      : { required: true},
                    descDProy    : { required: true},
                    fecFirmaDProy: { required: true},
                    fecIniDProy    : { required: true},
                    fecFinDProy     : { required: true},
                    montAportFIPDProy: { required: true},
                    montAportCliDProy: { required: true},
                    montAportOtrDProy: { required: true},

                   

                },
                messages:{
                    idTipDocDProy      : "Seleccione documento",
                    descDProy    : "Ingrese descripción",
                    fecFirmaDProy: "Ingrese fecha",
                    fecIniDProy    : "Ingrese fecha",
                    fecFinDProy     : "Ingrese fecha",
                    montAportFIPDProy: "Ingrese monto",
                    montAportCliDProy: "Ingrese monto",
                    montAportOtrDProy: "Ingrese monto",

                  
                }
            });

        });