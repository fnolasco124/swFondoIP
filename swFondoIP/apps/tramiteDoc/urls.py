from django.conf.urls import patterns, include, url
#from .views import inicio_view, Personal_View, Usuario_View, Cliente_View, Proyecto_View, ListaPersonal_View, ListaCliente_View,ListaUsuario_View, ListaProyecto_View, formulario, DerivacionUsuario, ListaMTabla_View, Tabla_View, DTabla_View, ListaDTabla_View, Adenda_View, Bandeja_View, Protocolo_View, LocalizarProtocolo_View, BusquedaOCR_View, DetalleProtocolo_View, Enviados_View, BusquedaAjax_View, DetalleProtocoloAjax_View, Observados_View, ObservarAjax_View, MaestroProtocoloAjax_View
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns =  patterns('swFondoIP.apps.tramiteDoc.views',
	#url(r'^inicio/$', inicio_view.as_view(), name ='vista_inicio'),
	url(r'^$', Login_View.as_view(), name ='Login_View'),
	url(r'^logout/$', Logout_View.as_view(), name ='Logout_View'),
	#url(r'^inicio/$', 'inicio_view', name ='vista_inicio'),
	url(r'^administracion/personal/nuevo/$', Personal_View.as_view(), name ='vista_personal'),
	url(r'^administracion/uejecutora/nuevo/$', Cliente_View.as_view(), name ='vista_Nuevo_UEjecutora'),
	
	url(r'^administracion/personal/$', ListaPersonal_View.as_view(), name ='vista_Personal'),
	url(r'^administracion/uejecutoras/$', ListaCliente_View.as_view(), name ='vista_UEjecutora'),
	url(r'^administracion/usuarios/$', ListaUsuario_View.as_view(), name ='vista_Usuario'),
	url(r'^administracion/derivacion/$', DerivacionUsuario.as_view(), name ='vista_Derivacion'),
	url(r'^administracion/tablasmaestro/$', ListaMTabla_View.as_view(), name ='vista_TablasMaestro'),
	url(r'^administracion/modificar/password/$', ModificarPasswordAjax_View.as_view()),
	url(r'^sistema/listaDTablas/$', ListaDTabla_View.as_view(), name ='vista_lstDTabla'),
	url(r'^sistema/tablas/$', Tabla_View.as_view(), name ='vista_tabla'),
	url(r'^sistema/dtablas/$', DTabla_View.as_view(), name ='vista_dtabla'),
	
	# MENU DE TRAMITE DOCUMENTARIO
	
	url(r'^tramite/protocolo/$', Protocolo_View.as_view(), name ='vista_Protocolo'),
	url(r'^tramite/convenios/page/(?P<pagina>.*)/$', ListaProyecto_View.as_view(), name ='vista_Convenios'),
	url(r'^tramite/bandeja/page/(?P<pagina>.*)/$', Bandeja_View.as_view(), name ='vista_Bandeja'),
	url(r'^tramite/localizar/$', LocalizarProtocolo_View.as_view(), name ='vista_LocalizarProtocolo'),
	url(r'^tramite/proyecto/nuevo$', Proyecto_View.as_view(), name ='vista_Convenio'),
	url(r'^tramite/modificatoria/(?P<proyecto>.*)/$', Modificatorias_View.as_view(), name ='vista_lstModificatorias'),
	url(r'^tramite/colaborador/(?P<proyecto>.*)/$', Colaboradores_View.as_view(), name ='vista_lstColaboradores'),
	url(r'^tramite/detalleprotocolo/(?P<idpr>[A-Z]{2}\d{4}.\d{8})/$', DetalleProtocolo_View.as_view(), name ='vista_detalleProtocolo'),
	url(r'^supervision/presupuesto/$',ConveniosSupervisor_View.as_view(), name='vista_Convenio_Supervisor'),
	url(r'^supervision/presupuesto/(?P<proyecto>.*)/$',SupervisarProyecto_View.as_view(), name='vista_Supervisar_Proyecto'),


	url(r'^uejecutora/cargar/$',CargarPresupuesto_View.as_view(), name='vista_Cargar_Presupuesto'),
	url(r'^uejecutora/presupuesto/$',Presupuesto_View.as_view(), name='vista_Presupuesto'),
	
	#url(r'^tramitedoc/enviados/$', Enviados_View.as_view(), name ='vista_protocolosEnviados'),
	#url(r'^tramitedoc/observados/$', Observados_View.as_view(), name ='vista_protocolosObservados'),
	
	
	url(r'^tramitedoc/busquedaAjax/$', BusquedaAjax_View.as_view()),
	url(r'^tramitedoc/maestroProtocoloAjax/$', MaestroProtocoloAjax_View.as_view()),
	url(r'^tramitedoc/maestroConvenioAjax/$', MaestroConvenioAjax_View.as_view()),
	url(r'^tramitedoc/colaboradoresConvenioAjax/$', ColaboradoresConvenioAjax_View.as_view()),
	url(r'^tramitedoc/modificatoriasConvenioAjax/$', ModificatoriasConvenioAjax_View.as_view()),
	url(r'^tramitedoc/maestroPersonalAjax/$', MaestroPersonalAjax_View.as_view()),

	url(r'^tramitedoc/localizarPorProtocoloAjax/$', LocalizarPorProtocoloAjax_View.as_view()),
	url(r'^tramitedoc/localizarPorProyectoAjax/$', LocalizarPorProyectoAjax_View.as_view()),
	url(r'^tramitedoc/localizarPorUnidadEjecutoraAjax/$', LocalizarPorUnidadEjecutoraAjax_View.as_view()),
	url(r'^tramitedoc/localizarPorReferenciaAjax/$', LocalizarPorReferenciaAjax_View.as_view()),
	url(r'^tramitedoc/localizarPorFechaAjax/$', LocalizarPorFechaAjax_View.as_view()),
	url(r'^tramitedoc/listaDepartamentoAjax/$', ListaDepartamentoAjax_View.as_view()),
	url(r'^tramitedoc/listaProvinciaAjax/$', ListaProvinciaAjax_View.as_view()),
	url(r'^tramitedoc/listaDistritoAjax/$', ListaDistritoAjax_View.as_view()),

	url(r'^tramitedoc/tipoPersonalAjax/$', TipoPersonalAjax_View.as_view()),

	url(r'^tramitedoc/registrarColaboradorAjax/$', RegistrarColaboradorAjax_View.as_view()),

	url(r'^tramitedoc/usuarioAjax/$', UsuarioAjax_View.as_view()),
	url(r'^tramitedoc/busquedaDetalleProtocolo/$', DetalleProtocoloAjax_View.as_view()),
	url(r'^tramitedoc/observarProtocolo/$', ObservarAjax_View.as_view()),
	
	#url(r'^tramite/formulario/$', formulario.as_view(), name ='vista_formulario'),
	
	url(r'^tramitedoc/formulario/$', Formulario_View.as_view(), name ='nuevo'),
	#url(r'^tramite/prueba/$', Proyecto2_View.as_view(), name ='vista_proyecto2'),
	url(r'^ajax/editar_usuario/$',EditarUsuario_View.as_view(),name="usuarioAjax"),


	#url(r'^appwebfip/ajax/eliminar_registro/$', EliminarRegistroAjax_View.as_view()),

	## Seccion ajax
	url(r'^ajax/eliminar_registro/$', EliminarRegistroAjax_View.as_view()),

	)