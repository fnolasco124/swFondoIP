#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404

from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator
from .forms  import MPersonalForm, MClienteForm, MProyectoForm, MTablaForm, DTablaForm, DProyectoForm, MProtocoloForm, DProtocoloForm, MColaboradorForm, MProyectoForm2,CargaForm, UsuarioForm

#from .models import MCliente, MPersonal, MUsuario, MProyecto, MTabla, DTabla, DProyecto, Bandeja, MProyecto, MUsuarioDer, DProtocolo, MProtocolo
from .models import *
from .decorators import access_permission

from django.views.generic import View, ListView, TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.core import serializers

import datetime
import os
import django
import re
import decimal
from decimal import *
import json



class Login_View(TemplateView):
	def get(self, request, *args, **kwargs):
		return render_to_response('tramite/index.html',context_instance=RequestContext(request))
	
	def post(self,request, *args, **kwargs):
		username = request.POST['username']
		password = request.POST['password']
		usuario = authenticate(username=username,password=password)
		if usuario is not None and usuario.is_active:
			login(request,usuario)
			if int(request.user.tipoUsuario) == 3:
				return HttpResponseRedirect('/uejecutora/cargar')
			else:
				return HttpResponseRedirect('/tramite/bandeja/page/1')
		else:
			mensaje = "Sus datos son incorrectos o el usuario no esta activo"
			return render_to_response('tramite/index.html',{'mensaje':mensaje},context_instance=RequestContext(request))

class Logout_View(TemplateView):
	def get(self,request):
		logout(request)
		return HttpResponseRedirect('/')

def enviarCorreo(mensajea,destino,html_content):
        try:
                asunto = "Recepcion de protocolo"
                mensaje = mensajea
                origen = "wffip@fondoitaloperuano.org"
                msg = EmailMultiAlternatives(asunto,mensaje,origen,[destino])
                msg.attach_alternative(html_content,"text/html")
                msg.send()
        except Exception, e:
                print 'Errores en el servidor de correos'

def enviarCorreo2(mensajea,destino):
	asunto = "Recepcion de protocolo"
	mensaje = mensajea
	origen = "fnolasco@fondoitaloperuano.org"
	
	send_mail(asunto,mensaje,origen,[destino])
	
class Personal_View(FormView):
	#template_name = 'tramite/frmPersonal.html'
	#form_class = MPersonalForm
	error = ""
	@method_decorator(access_permission([0,]))
	@method_decorator(login_required(login_url='/'))
	def get(self,request):
		lstTipoDoc = DTabla.objects.filter(IdMTab__IdMTabla='011')
		lstAreas = DTabla.objects.filter(IdMTab__IdMTabla='008')
		lstTipPersonal = DTabla.objects.filter(IdMTab__IdMTabla='022')
		ctx = {'lstTipoDoc':lstTipoDoc,'lstAreas':lstAreas,'lstTipPersonal':lstTipPersonal}
		return render_to_response('tramite/frmPersonal.html',ctx,context_instance=RequestContext(request))

	def generarCodigo(self):
		anio = datetime.date.today().strftime("%Y")
		if (MPersonal.objects.count()==0):
			anio = datetime.date.today().strftime("%Y")
			codigo = 'PE'+anio+'-00000001'

		else:
			obj = MPersonal.objects.last()
			cod = obj.IdMPer
			num = cod[7:]
			num = int(num)
			num = num + 1
			can = len(str(num))
			dif = 8-can
			codigo = ''
			codigo = '0'*dif
			codigo = 'PE'+ anio + '-' + codigo + str(num)
		return codigo
	
	def post(self, request, *args, **kwargs):
		print 'aki'
		form = MPersonalForm(request.POST) # A form bound to the POST data
		try:

			if form.is_valid():
				add = form.save(commit= False)
				add.EstMPer = 1
				add.IdMPer = self.generarCodigo()
				add.save()
				message= {'mensaje':'Personal registrado, los datos ingresados son correctos.'}
				return HttpResponse(json.dumps(message),mimetype='application/json')
			else:
				message= {'mensaje':'Los datos ingresados no son correctos!. Intente nuevamente.'}
				return HttpResponse(json.dumps(message),mimetype='application/json')
		except Exception, e:
			message = {'mensaje':e}
			return HttpResponse(json.dumps(message),mimetype='application/json')
		

class Cliente_View(FormView):
	template_name = 'tramite/form_cliente.html'
	form_class = MClienteForm
	error = ""
	@method_decorator(access_permission([0,1]))
	@method_decorator(login_required(login_url='/'))
	def get(self,request, *args, **kwargs):
		lstPais = DTabla.objects.filter(IdMTab__IdMTabla='001')
		lstRegion = DTabla.objects.filter(IdMTab__IdMTabla='002')
		lstTipo = DTabla.objects.filter(IdMTab__IdMTabla = '015')
		#lstDepartamento = DTabla.objects.filter(idMTab__idMTabla='003')
		#lstProvincia = DTabla.objects.filter(idMTab__idMTabla='004')
		#lstDistrito = DTabla.objects.filter(idMTab__idMTabla='005')
		lista = MCliente.objects.all()
		ctx = {'lista':lista,'error':self.error,'lstPais':lstPais,'lstRegion':lstRegion,'lstTipo':lstTipo}
		return render_to_response('tramite/form_cliente.html',ctx,context_instance=RequestContext(request))

	def post(self, request, *args, **kwargs):
		try:
			obj = MCliente()
			if (MCliente.objects.count() == 0):
				obj.IdMCli = 'CL2014-00000001'
			else:
				obj.IdMCli = self.generarCodigo()
			
			obj.NomMCli = request.POST['nomMCli']
			obj.IdTipMCli = request.POST['idTipMCli']
			obj.IdTipInstMCli = request.POST['idTipInstMCli']
			obj.DirMCli = request.POST['dirMCli']		
			obj.IdPaisMCli = request.POST['idPaisMCli']
			obj.IdRegMCli = request.POST['idRegMCli']
			obj.IdDepMCli = request.POST['idDepMCli']
			obj.IdProvMCli = request.POST['idProvMCli']
			obj.IdDistMCli = request.POST['idDistMCli']
			obj.RefMCli = request.POST['refMCli']
			obj.Tel1MCli = request.POST['tel1MCli']
			obj.Tel2MCli = request.POST['tel2MCli']
			obj.Tel3MCli = request.POST['tel3MCli']
			obj.FechCreaMCli = timezone.now()
			obj.EstMCli = '1'
			obj.FecIngMCli = timezone.now()
			obj.Email1MCli = request.POST['emailMCli']
				#obj.idUsuCreaMCli = '1'
			obj.save()
				#print obj
				#return HttpResponseRedirect('/')
			return HttpResponseRedirect('/administracion/ujecutoras/')
		except Exception, e:
			print e
		return self.get(request)

	def generarCodigo(self):

		obj = MCliente.objects.last()
		cod = obj.IdMCli
		num = cod[7:]
		num = int(num)
		num = num + 1
		can = len(str(num))
		dif = 8-can
		codigo = ''
		codigo = '0'*dif
		
		codigo = 'CL2014'+ '-' + codigo + str(num)

		return codigo
				
class Proyecto_View(TemplateView):
	def generarCodigo(self):
		if (MProyecto.objects.count()==0):
			#print convo
			codigo = 'CV2014-00000001'
		else:
			anio = datetime.datetime.today().year
			anio = str(anio)
			obj = MProyecto.objects.last()
			cod = obj.IdMProy
			num = cod[7:]
			num = int(num)
			num = num + 1
			can = len(str(num))
			dif = 8-can
			codigo = ''
			codigo = '0'*dif
			codigo = 'CV'+anio+ '-' + codigo + str(num)
		return codigo

	@method_decorator(access_permission([0,1]))
	@method_decorator(login_required(login_url='/'))
	def get(self,request,*args, **kwargs):
		lstBancos = DTabla.objects.filter(IdMTab__IdMTabla='007')
		lstSector = DTabla.objects.filter(IdMTab__IdMTabla='010')
		lista = MProyecto.objects.all()
		listaUE = MCliente.objects.all()
		lstPersonal = MPersonal.objects.all()
		cabecera = []
		form = MProyectoForm()
		frm = MColaboradorForm()
		ctx = {'lista':lista, 'listFields':cabecera, 'listaUE':listaUE,'form':form,'lstPersonal':lstPersonal,'frm':frm,'lstBancos':lstBancos,'lstSector':lstSector}
		return render_to_response('tramite/form_convenio.html',ctx, context_instance=RequestContext(request))
	
	def post(self, request, *args, **kwargs):
		
		try:
			form = MProyectoForm(request.POST,request.FILES) # A form bound to the POST data
			if form.is_valid():
				print 'es valido aki'
				add = form.save(commit=False)
				cod = self.generarCodigo()
				add.IdMProy = cod
					
					#c = request.POST['idMCli']
				add.IdMCli = MCliente.objects.get(IdMCli=request.POST['idMCli'])				
				print add.IdMCli
				if (request.POST['nomMProy']!=''):
					add.NomMProy = request.POST['nomMProy']
				
				if (request.POST['idTipProMProy']!=''):
					add.IdTipProMProy = request.POST['idTipProMProy']
					
				add.EstMProy = '1'
				if (request.POST['fecEntMProy']!=''):
					add.FecEntMProy = datetime.datetime.strptime(request.POST['fecEntMProy'],'%Y-%m-%d')

				if(request.POST['fecEntRealMProy']!=''):
					add.FecEntRealMProy = datetime.datetime.strptime(request.POST['fecEntRealMProy'],'%Y-%m-%d')
					
				if(request.POST['fecIniMProy']!=''):
					add.FecIniMProy = datetime.datetime.strptime(request.POST['fecIniMProy'],'%Y-%m-%d')
					
				if(request.POST['fecIniRealMProy']!=''):
					add.FecIniRealMProy = datetime.datetime.strptime(request.POST['fecIniRealMProy'],'%Y-%m-%d')
					
				if(request.POST['fecFinMProy']!=''):
					add.FecFinMProy = datetime.datetime.strptime(request.POST['fecFinMProy'],'%Y-%m-%d')
					
				if(request.POST['fecFinRealMProy']!=''):
					add.FecFinRealMProy = datetime.datetime.strptime(request.POST['fecFinRealMProy'],'%Y-%m-%d')

				if(request.POST['montInvCliMProy']!=''):
					add.MontInvCliMProy = decimal.Decimal(request.POST['montInvCliMProy'])
					
				if(request.POST['montInvFipMProy']!=''):
					add.MontInvFipMProy = decimal.Decimal(request.POST['montInvFipMProy'])
					
				if(request.POST['montTotMProy']!=''):
					add.MontTotMProy = decimal.Decimal(request.POST['montTotMProy'])
					
				if(request.POST['montTInvRealCliMProy']!=''):
					add.MontTInvRealCliMProy = decimal.Decimal(request.POST['montTInvRealCliMProy'])

				if(request.POST['montTInvRealFipMProy']!=''):
					add.MontTInvRealFipMProy = decimal.Decimal(request.POST['montTInvRealFipMProy'])
					
				if(request.POST['montTotRealMProy']!=''):
					add.MontTotRealMProy = decimal.Decimal(request.POST['montTotRealMProy'])
					
				add.FecIngMProy = timezone.now()

				if(request.POST['idEstMProy']):
					add.IdEstMProy = request.POST['idEstMProy']
					# Desde aki
				if(request.POST['idSector']!=''):
					add.IdSector = request.POST['idSector']
					
				if(request.POST['idBanco']!=''):
					add.IdBanco = request.POST['idBanco']
					
				if(request.POST['montTotAdeCliMProy']!=''):
					add.MontTotAdeCliMProy = decimal.Decimal(request.POST['montTotAdeCliMProy'])
					
				if(request.POST['numCtaInterMProy']!=''):
					add.NumCtaInterMProy = request.POST['numCtaInterMProy']

				if(request.POST['montTotAdeFipMProy']!=''):
					add.MontTotAdeFipMProy = decimal.Decimal(request.POST['montTotAdeFipMProy'])

				if(request.POST['montTotAdeTotMProy']!=''):
					add.MontTotAdeTotMProy = decimal.Decimal(request.POST['montTotAdeTotMProy'])

				if(request.POST['idConv']!=''):
					add.IdConv = request.POST['idConv']
					
				add.TiempoMProy = request.POST['tiempoMProy']
					
				add.PorcTotAdeMProy = decimal.Decimal('1')
					
				add.EstCierreMProy = '0'

				add.save()
			else:
				print 'El formulario no es correcto'
			return HttpResponseRedirect('/tramite/convenios/page/1/')
		except Exception, e:
			error = e
			print error
		return self.get(request)
		
class ListaPersonal_View(TemplateView):
	@method_decorator(access_permission([0,]))
	@method_decorator(login_required(login_url='/'))
	def get(self, request, *args, **kwargs):
		lista = MPersonal.objects.all()
		frm = MPersonalForm()
		ctx = {'lista':lista,'frm':frm}
		return render_to_response('tramite/lista_personal.html',ctx, context_instance=RequestContext(request))

	def post(self, request, *args, **kwargs):
		print 'aki'
		form = MPersonalForm(request.POST) # A form bound to the POST data
		try:

			if form.is_valid():
				add = form.save(commit= False)
				add.EstMPer = 1
				add.IdMPer = self.generarCodigo()
				add.save()
				last_personal = []
				last_personal.append(MPersonal.objects.last())
				data = serializers.serialize('json', last_personal)
				message= {'mensaje':'Personal registrado, los datos ingresados son correctos.','usuario':last_personal}
				return HttpResponse(data,mimetype='application/json')
			else:
				message= {'mensaje':'Los datos ingresados no son correctos!. Intente nuevamente.'}
				return HttpResponse(json.dumps(message),mimetype='application/json')
		except Exception, e:
			message = {'mensaje':e}
			return HttpResponse(json.dumps(message),mimetype='application/json')

	def generarCodigo(self):
		anio = datetime.date.today().strftime("%Y")
		if (MPersonal.objects.count()==0):
			anio = datetime.date.today().strftime("%Y")
			codigo = 'PE'+anio+'-00000001'

		else:
			obj = MPersonal.objects.last()
			cod = obj.IdMPer
			num = cod[7:]
			num = int(num)
			num = num + 1
			can = len(str(num))
			dif = 8-can
			codigo = ''
			codigo = '0'*dif
			codigo = 'PE'+ anio + '-' + codigo + str(num)
		return codigo

class ListaCliente_View(TemplateView):
	@method_decorator(access_permission([0,1]))
	@method_decorator(login_required(login_url='/'))
	def get(self,request,*args, **kwargs):
		lista = MCliente.objects.all()
		ctx = {'lista':lista,}
		return render_to_response('tramite/lista_unidad_ejecutora.html',ctx, context_instance=RequestContext(request))

class ListaUsuario_View(TemplateView):
	@method_decorator(access_permission([0,]))
	@method_decorator(login_required(login_url='/'))
	def get(self,request,*args, **kwargs):
		lista = User.objects.all().order_by("-pk")
		form = UsuarioForm()
		ctx = {'lista':lista,'form':form}
		return render_to_response('tramite/lista_usuario.html',ctx, context_instance=RequestContext(request))
	def post(self, request, *args, **kwargs):
		form = UsuarioForm(request.POST) # A form bound to the POST data
		#try:
		if form.is_valid():
			add = form.save(commit=False)
			add.set_password(add.password)
			o_per = MPersonal.objects.get(IdMPer = add.idMPer)
			add.last_name = '%s %s' %(o_per.ApePMPer, o_per.ApeMMPer)
			add.first_name = o_per.NomMPer
			add.email = o_per.Email1MPer
			add.save()
			last_user = User.objects.last()
			message= {'username':last_user.username,'last_name':last_user.last_name, 'first_name':last_user.first_name, 'tipoUsuario':last_user.tipoUsuario, 'fecIngreso':str(last_user.fecIngreso),'id':last_user.pk}
			#data = serializers.serialize('json', last_user)	
			return HttpResponse(json.dumps(message),mimetype='application/json')
			#return HttpResponse(data,mimetype='application/json')
		else:
			message= {'mensaje':'Los datos ingresados no son correctos!. Intente nuevamente.'}
			return HttpResponse(json.dumps(message),mimetype='application/json')
		#except Exception, e:
		#	message = {'mensaje':e}
		#	return HttpResponse(json.dumps(message),mimetype='application/json')
		
class ListaProyecto_View(TemplateView):
	@method_decorator(access_permission([0,1]))
	@method_decorator(login_required(login_url='/'))
	def get(self,request,pagina):
		pr = MProyecto()
		lst = MProyecto.objects.filter(EstMProy='1').order_by("-IdMProy")
		
		paginator = Paginator(lst,15)
		try:
			page=int(pagina)
		except:
			page=1
		
		try:
			lista = paginator.page(page)
		except (EmptyPage,InvalidPage):
			lista = paginator.page(paginator.num_pages)

		cabecera = pr.get_nombreCampos()
		ctx = {'lista':lista, 'listFields':cabecera,'nomTabla':'Registro de Convenios'}
		return render_to_response('tramite/lista_convenio.html',ctx, context_instance=RequestContext(request))

class ListaMTabla_View(TemplateView):
	@method_decorator(access_permission([0,]))
	@method_decorator(login_required(login_url='/'))
	def get(self,request,*args, **kwargs):
		lista = MTabla.objects.all()
		ctx = {'lista':lista,}
		return render_to_response('tramite/tablas_maestro.html',ctx, context_instance=RequestContext(request))

class ListaDTabla_View(TemplateView):
	@method_decorator(access_permission([0,]))
	@method_decorator(login_required(login_url='/'))
	def get(self,request,*args, **kwargs):
		pr = DTabla()
		lista = DTabla.objects.all()
		#print lista
		cabecera = pr.get_nombreCampos()
		ctx = {'lista':lista, 'listFields':cabecera,'nomTabla':'Tablas del sistema (detalle)'}
		return render_to_response('tramite/lstDTabla.html',ctx, context_instance=RequestContext(request))

# ESTA CLASE SE PUEDE ELIMINAR
class formulario(FormView):
	@method_decorator(login_required(login_url='/'))
	def get(self,request,*args,**kwargs):
		form = MProyectoForm()
		ctx = {'form':form}
		return render_to_response('tramite/formulario.html',ctx, context_instance=RequestContext(request))

class DerivacionUsuario(TemplateView):
	@method_decorator(access_permission([0,]))
	@method_decorator(login_required(login_url='/'))
	def get(self,request,*error):
		pr = MUsuarioDer()
		lstDeriva = MUsuarioDer.objects.all()
		lista = []
		lstPk = []
	
		for item in lstDeriva:
			lstPk.append(int(item.pk))
			lista.append([str((MUsuario.objects.get(pk=int(item.IdUsuOri))).IdMUsu.username),str((MUsuario.objects.get(pk=int(item.IdUsuDer))).IdMUsu.username)])
		 
		
		cabecera = pr.get_nombreCampos()
		ctx = {'lista':lista,'lstPk':lstPk}
		return render_to_response('tramite/derivacion_usuario.html',ctx,context_instance=RequestContext(request))

	def post(self, request, *args, **kwargs):
		pass

class Tabla_View(FormView):
	template_name = 'tramite/frmTabla.html'
	form_class = MTablaForm
	error = ""
	@method_decorator(access_permission([0,]))
	@method_decorator(login_required(login_url='/'))
	def get(self,request,*error):
		#lista = MTabla.objects.all()
		print 'Estamos en el get'
		return render_to_response('tramite/frmTabla.html',context_instance=RequestContext(request))

	def post(self, request, *args, **kwargs):
		try:
			obj = MTabla()


			obj.IdMTabla = request.POST['idMTab']
			obj.NomMTabla = request.POST['nomMTab']
			obj.AbrMTabla = request.POST['abrMTab']
			obj.PropMTabla = request.POST['propMTab']
			obj.EstMTabla = request.POST['estMTab']

			
			#obj.fecIngMCli = timezone.now()
			#obj.idUsuCreaMCli = '1'
			obj.save()
			#print obj
			#return HttpResponseRedirect('/')
			print 'Estamos en el post'
			return HttpResponseRedirect('/sistema/listaTablas/')
		except Exception, e:
			error = e
			print error
		return self.get(request)

class DTabla_View(FormView):
	template_name = 'tramite/frmDTabla.html'
	form_class = DTablaForm
	error = ""
	@method_decorator(access_permission([0,]))
	@method_decorator(login_required(login_url='/'))
	def get(self,request,*error):
		lista = DTabla.objects.all()
		cod = '5'
		return render_to_response('tramite/frmDTabla.html',{'lista':lista,'cod':cod},context_instance=RequestContext(request))

	def post(self, request, *args, **kwargs):
		#try:
			obj = DTabla()


			obj.IdMTabla = MTabla.objects.get(pk=request.POST['idMTabla'])
			obj.IdDTabla = '000'
			obj.NomDTabla = request.POST['nomDTabla']
			obj.AbrDTabla = request.POST['abrDTabla']
			obj.AbrOptDTabla = obj.abrDTabla
			obj.PropDTabla = request.POST['propDTabla']
			obj.IdRefDTabla = request.POST['idRefDTabla']

			
			#obj.fecIngMCli = timezone.now()
			#obj.idUsuCreaMCli = '1'
			obj.save()
			#print obj
			#return HttpResponseRedirect('/')
			return HttpResponseRedirect('/tramite/listaDTablas/')
		#except Exception, e:
		#	error = e
		#	print error
		#return self.get(request)

class Modificatorias_View(TemplateView):
	def generarCodigo(self):
		anio = datetime.date.today().strftime("%Y")
		if (DProyecto.objects.count()==0):
			anio = datetime.date.today().strftime("%Y")
			codigo = 'MC'+anio+'-00000001'

		else:
			obj = DProyecto.objects.last()
			cod = obj.IdDProy
			num = cod[7:]
			num = int(num)
			num = num + 1
			can = len(str(num))
			dif = 8-can
			codigo = ''
			codigo = '0'*dif
			codigo = 'MC'+ anio + '-' + codigo + str(num)
		return codigo

	@method_decorator(access_permission([0,1]))
	@method_decorator(login_required(login_url='/'))
	def get(self,request,*args, **kwargs):
		proyecto = kwargs['proyecto']
		print proyecto
		try:
			objMP = MProyecto.objects.get(IdMProy=proyecto)

			lista = DProyecto.objects.filter(IdMProy__IdMProy=proyecto)
			lstTipAdenda = DTabla.objects.filter(IdMTab__IdMTabla="021")
			form = DProyectoForm()
			ctx = {'lista':lista, 'form':form,'objMP':objMP,'lstTipAdenda':lstTipAdenda}
			return render_to_response('tramite/modificatoria_convenio.html',ctx, context_instance=RequestContext(request))
		except Exception, e:
			print e

	def post(self, request, *args, **kwargs):
		cod  = ""	
		try:
			form = DProyectoForm(request.POST,request.FILES) # A form bound to the POST data
			if form.is_valid():
				print 'Modificatoria valida'
				cod = request.POST['codProyecto']
				objProy = MProyecto.objects.get(IdMProy=cod)

				#print objProy
						#print 'este es el codigo %s' %(cod)
				add = form.save(commit=False)
				add.IdDProy = self.generarCodigo()
				add.IdMProy = MProyecto.objects.get(IdMProy=cod)

				add.FecIniDProy = datetime.datetime.strptime(request.POST['fecIniDProy'],'%Y-%m-%d')
				add.FecFinDProy = datetime.datetime.strptime(request.POST['fecFinDProy'],'%Y-%m-%d')
				add.FecFirmaDProy = datetime.datetime.strptime(request.POST['fecFirmaDProy'],'%Y-%m-%d')
				add.MontAportFIPDProy = request.POST['montAportFIPDProy']
				add.MontAportCliDProy = request.POST['montAportCliDProy']
				add.MontAportOtrDProy = request.POST['montAportOtrDProy']
					
					#Actualizar el aporte de las modificatorias en el proyecto
					#objProy.montTotAdeTotMProy = Decimal(objProy.montTotAdeCliMProy) + Decimal(objProy.montTotAdeFipMProy) + Decimal(objProy.montTotAdeOtrMProy)
				
				montTotAdeCliMProy =  objProy.MontTotAdeCliMProy
				montTotAdeFipMProy = objProy.MontTotAdeFipMProy
				montTotAdeOtrMProy = objProy.MontTotAdeOtrMProy
				totalAde = 0.0
				print type(str(request.POST['montAportCliDProy']))
				objProy.MontTotAdeCliMProy = float(montTotAdeCliMProy) + float(request.POST['montAportCliDProy'])
				objProy.MontTotAdeFipMProy = float(montTotAdeFipMProy) + float(request.POST['montAportFIPDProy'])
				objProy.MontTotAdeOtrMProy = float(montTotAdeOtrMProy) + float(request.POST['montAportOtrDProy'])
				totalAde = objProy.MontTotAdeCliMProy + objProy.MontTotAdeFipMProy + objProy.MontTotAdeOtrMProy
				objProy.MontTotAdeTotMProy = totalAde
				
					#Fin de actualizacion
				objProy.save()
				add.EstDProy = '1' # MODIFICAR PARA QUE SE EXCLUYA DEL CAMPO
				add.IdTipDocDProy = request.POST['idTipDocDProy']
				add.DescDProy = request.POST['descDProy']
							#add.rutaPDFDProy = request.POST['rutaPDFDProy']
						
				add.save()
						#return HttpResponseRedirect('/tramitedoc/listaModificatoria/%s' %(cod))	
			else:
				print 'El formulario no es valido'	
				#return HttpResponseRedirect('/tramitedoc/listaModificatoria/%s' %(cod))	
		except Exception, e:
			print e
			self.error = "Sucedio un error al momento de guardar"	
		return HttpResponseRedirect('/tramite/modificatoria/%s' %(cod))	

class Colaboradores_View(TemplateView):
	def generarCodigo(self):
		anio = datetime.date.today().strftime("%Y")
		if (MColaborador.objects.count()==0):
			anio = datetime.date.today().strftime("%Y")
			codigo = 'CC'+anio+'-00000001'

		else:
			obj = DProyecto.objects.last()
			cod = obj.idDProy
			num = cod[7:]
			num = int(num)
			num = num + 1
			can = len(str(num))
			dif = 8-can
			codigo = ''
			codigo = '0'*dif
			codigo = 'CC'+ anio + '-' + codigo + str(num)
		return codigo

	@method_decorator(access_permission([0,1]))
	@method_decorator(login_required(login_url='/'))
	def get(self,request,*args, **kwargs):
		proyecto = kwargs['proyecto']
		print proyecto + 'esto'
		try:
			objMP = MProyecto.objects.get(IdMProy=proyecto)
			lista = MColaborador.objects.filter(IdMProy__IdMProy=proyecto)
			lstPersonal = MPersonal.objects.exclude(IdTipPerMPer='2')
			form = MColaboradorForm()
			ctx = {'lista':lista, 'form':form,'objMP':objMP,'lstPersonal':lstPersonal}
			return render_to_response('tramite/colaborador_convenio.html',ctx, context_instance=RequestContext(request))
		except Exception, e:
			print e

	def post(self, request, *args, **kwargs):
		cod  = ""
		try:
			form = MColaboradorForm(request.POST,request.FILES) # A form bound to the POST data
			if form.is_valid():
				print 'Colaborador valido'
				add = form.save(commit=False)
				add.IdMProy = MProyecto.objects.get(IdMProy=request.POST['codProyecto'])
				cod  = request.POST['codProyecto']
				codPer = request.POST['idMPer']
				objMPer = MPersonal.objects.get(IdMPer=codPer)
				add.IdMPer = objMPer
					
				if (objMPer.IdTipPerMPer == '0'):
					add.IdTipoCargoProy = request.POST['idTipoCargoProy']
					add.FecIniMCol = datetime.datetime.strptime(request.POST['fecIniMCol'],'%Y-%m-%d')
					add.FecFinMCol = datetime.datetime.strptime(request.POST['fecFinMCol'],'%Y-%m-%d')
					add.TiempoMCol = request.POST['tiempoMCol']
					add.FecFirmaMCol = datetime.datetime.strptime(request.POST['fecIniMCol'],'%Y-%m-%d')
					add.MontoMCol = request.POST['montoMCol']
					add.MontoMenMCol = request.POST['montoMenMCol']

				add.EstMCol = '1'
				add.EstActMCol = '1'
				add.save()
			else:
				print 'no es valido'
			
		except Exception, e:
			print e
			self.error = "Sucedio un error al momento de guardar"
		
		return HttpResponseRedirect('/tramite/colaborador/%s' %(cod))
	
class Bandeja_View(ListView):
	@method_decorator(access_permission([0,1,2]))
	@method_decorator(login_required(login_url='/'))
	def get(self,request,pagina=1):
		pr = Bandeja()
		usuario = request.user.pk
		print usuario
		lista = Bandeja.objects.filter(IdMUsuRec=usuario).order_by('-IdBandeja')
		paginator = Paginator(lista,8)
		try:
			page=int(pagina)
		except:
			page=1
		
		try:
			bandejas = paginator.page(page)
		except (EmptyPage,InvalidPage):
			bandejas = paginator.page(paginator.num_pages)
		
		listaUsuario = User.objects.all()
				
		ctx = {'lista':lista,'listaUsuario':listaUsuario,'bandejas':bandejas}
		return render_to_response('tramite/bandeja_protocolo.html',ctx, context_instance=RequestContext(request))
	
	def post(self,request,*args,**kwargs):
		destino = request.POST['txtDestino']
		protocolo = request.POST['txtProtocolo']
		#observacion = request.POST['txtObservacion']
		mensaje = request.POST['txtMensaje']
		
		codUsuarioEnvio = request.user.pk
		envx = request.user.username
		
		lstCodProt = protocolo.split(',')
		lstCodDest = destino.split(',')
		observacion = mensaje
		estObs = request.POST['protObservado']

		
		if (lstCodProt[0]!= '' and lstCodDest[0]!=''):
			for p in lstCodProt:
				obj = Bandeja.objects.get(IdBandeja=p)
				obj.EstAccion = "1"
				obj.save()
				print obj.EstAccion
				for d in lstCodDest:
					codUsuarioRecepcion = d
					usuario = User.objects.get(pk=d)
					print "ES EL PRIMER OBJ"
					print obj
					print "FIN DEL PRIMERO BOJECT"
					regProtocoloEnBandeja(obj, codUsuarioEnvio, codUsuarioRecepcion,usuario.username,observacion,mensaje,estObs,envx)
			
		else:
			print 'No existen destinatarios o protocolos para registrar'

		return self.get(request)

	def observado(self, cod):
		obj = Bandeja.objects.get(idBandeja=cod)
		if (obj.EstObservado == '1'):
			return 'Se encuentra observado'
		else:
			return 'No esta observado'

class Enviados_View(ListView):
	def get(self,request,*args,**kwargs):
		pr = Bandeja()
		usuario = request.user.pk
		print "Usuario actual %s con codigo %s" %(request.user.username, request.user.pk)
		lista = Bandeja.objects.filter(idMUsuREc=usuario, estAccion='1')
		print lista
		listaUsuario = User.objects.all()
		cabecera = pr.get_nombreCampos()
		ctx = {'lista':lista, 'listFields':cabecera,'nomTabla':'Protocolos Enviados', 'listaUsuario':listaUsuario}
		return render_to_response('tramite/lstEnviados.html',ctx, context_instance=RequestContext(request))
	def post(self,request,*args,**kwargs):
		
		for d in destino:
			for p in protocolo:
				prot = Bandeja.objects.get(pk=p)
				protocolo = prot.IdMProt
				clie = MCliente.objects.get(pk=prot.IdMCli)
				cliente = clie.NomMCli
				proy = MProyecto.objects.get(pk=prot.IdMProy)
				referencia = prot.EdRefMProt
				proyecto = proy.NomMProy
				regProtocoloEnBandeja(protocolo,enviadoPor,d,usuario,cliente,referencia, proyecto,observacion,mensaje)

		
		return self.get(request)		

class Protocolo_View(TemplateView):
	@method_decorator(login_required(login_url='/'))
	@method_decorator(access_permission([0,1,2]))
	def get(self,request,*args,**kwargs):
		lista = MProyecto.objects.all()
		usuario = request.user.pk
		lstTipoDoc = DTabla.objects.filter(IdMTab__IdMTabla='012')
		listaProtocolo = Bandeja.objects.filter(IdMUsuRec=usuario,EstAccion ='0')
		fecha = datetime.datetime.today()
		
		ctx = {'lista':lista, 'listaProtocolo':listaProtocolo,'lstTipoDoc':lstTipoDoc,'fechaActual':fecha}

		return render_to_response('tramite/form_protocolo.html',ctx, context_instance=RequestContext(request))

	def post(self, request, *args, **kwargs):
		pr = MProtocolo()
		cliente = ""
		proyecto = ""
		data = []

		#print 'Codigo de la referencia : %s' %(request.POST['idRefMProt'])
					
		if (request.POST['idMProy']!= ''):
			obj = MProyecto.objects.get(IdMProy=request.POST['idMProy'])
			pr.IdMProy= MProyecto.objects.get(IdMProy=request.POST['idMProy'])
			pr.idMCli = obj.IdMCli.IdMCli
			cliente = obj.IdMCli.NomMCli
			proyecto = pr.IdMProy.NomMProy

		if (request.POST['idRefMProt'] != ''):
			pr.IdRefMProt = request.POST['idRefMProt']
			
			
		try:
			pr.NomMProt= request.POST['nomMProt']
			pr.DescMProt= request.POST['descMProt']
			pr.FecEntMProt= datetime.datetime.strptime(request.POST['fecEntMProt'],'%Y-%m-%d')  
			pr.FecEntRealMProt= timezone.now()
			pr.IdTipFormEntMProt= request.POST['idTipFormEntMProt']		
			pr.IdTipDocGen= request.POST['idTipDocGen']
			pr.DocInter = request.POST['docInter']
			pr.EstMProt = '1'
			anio = str(datetime.date.today().strftime("%Y"))
			pr.IdMProt = self.generarCodigo(anio)	
			pr.save()
			protocolo = pr.IdMProt
			codUsuario = request.user.pk
			usuario = request.user.username
			referencia = pr.IdRefMProt	
			self.registrarProtocoloEnBandeja(protocolo,cliente,codUsuario,usuario,proyecto,referencia)	
			data =  {'idMProt': pr.IdMProt}
			print 'Se ha grabado un nuevo archivo'
				#return render_to_response('tramite/lstDetalleProtocolo.html', data ,context_instance=RequestContext(request))
			return HttpResponseRedirect('/tramite/detalleprotocolo/%s' %(pr.IdMProt))		
		except Exception, e:
			print e
			data = {'error':e}
			return render_to_response('tramite/form_protocolo.html', data ,context_instance=RequestContext(request))
		
		
		

	def generarCodigo(self, convo):

		if (MProtocolo.objects.count()==0):
			print convo
			codigo = 'PR2014-00000001'
		else:
			obj = MProtocolo.objects.last()
			cod = obj.IdMProt
			num = cod[7:]
			num = int(num)
			num = num + 1
			can = len(str(num))
			dif = 8-can
			codigo = ''
			codigo = '0'*dif
			convocatoria = convo.split()
			print convocatoria
			codigo = 'PR'+ convocatoria[0] + '-' + codigo + str(num)
		return codigo

	def registrarProtocoloEnBandeja(self, protocolo,cliente,codUsuario,usuario,proyecto,referencia):
		bd = Bandeja()
		print proyecto
		codigo = ''
		if Bandeja.objects.count() > 0:
			band = Bandeja.objects.last()
			cod = band.IdBandeja
			print cod
			num = cod[7:]
			num = int(num)
			num = num + 1
			can = len(str(num))
			dif = 8-can
			codigo = ''
			codigo = '0'*dif
			codigo = 'BD'+ '2014' + '-' + codigo + str(num)

		else:
			codigo = 'BD2014-00000001'

		bd.IdBandeja = codigo
		bd.IdMUsuEnv = codUsuario
		bd.IdMUsuRec = codUsuario
		bd.IdMProt = protocolo
		bd.FecEnv = timezone.now()
		bd.FecRec = timezone.now()
		bd.FecSist = timezone.now()
		bd.MenBProt = ''
		bd.EstBProt = '1' #Estado del BProt, cuando es 1 está activo, si es 0 esta eliminado logicamente
		bd.EstAccion = '0' #Cambia de valor a 1 cuando el protocolo esta enviado
		bd.EstObservado = '0' #Cambia de valor a 1 cuando el protocolo esta observado
		bd.ObsProt = ''
		bd.NomMUsuEnv = usuario
		bd.NomMUsuREc = usuario
		bd.CliBProt = cliente
		bd.ProyBProt = proyecto
		bd.IdProtRef = referencia
		bd.save()
	
class LocalizarProtocolo_View(ListView):
	@method_decorator(access_permission([0,1]))
	@method_decorator(login_required(login_url='/'))
	def get(self,request):
		return render_to_response('tramite/frmLocalizarProt.html',context_instance=RequestContext(request))
	
	def post(self,request):
		codProtocolo = ""
		proyecto = ""
		cliente = ""
		fecInicio = ""
		fecFin = ""
		referencia = ""
		if (request.POST['codProtocolo'] != ""):
			codProtocolo = request.POST['codProtocolo']
		if(request.POST['nomConvenio'] != ""):
			proyecto = (request.POST['nomConvenio'])
		if(request.POST['cliente'] != ""):
			cliente = request.POST['cliente']
		if(request.POST['inicio'] != ""):
			fecInicio = request.POST['inicio']
		else:
			fecInicio = '2000-01-01'
		if(request.POST['fin'] != ""):
			fecFin = request.POST['fin']
		else:
			fecFin = timezone.now()
		if(request.POST['referencia'] != ""):
			referencia = request.POST['referencia']

		lstFiltro = Bandeja.objects.filter(IdMProt__contains=codProtocolo, ProyBProt__contains=proyecto.upper(), CliBProt__contains= cliente.upper(), FecSist__range=(fecInicio,fecFin)).order_by('-FecSist')
		ctx = {'lista':lstFiltro}
		return render_to_response('tramite/frmLocalizarProt.html',ctx,context_instance=RequestContext(request))
			
class Observados_View(ListView):
	@method_decorator(login_required(login_url='/'))
	def get(self,request,*args,**kwargs):
		pr = Bandeja()
		usuario = request.user.pk
		#print "Usuario actual %s con codigo %s" %(request.user.username, request.user.pk)
		lista = Bandeja.objects.filter(IdMUsuREc=usuario, EstAccion='0', EstObservado='1' ).order_by('-IdMProt')
		listaUsuario = User.objects.all()
		
		cabecera = pr.get_nombreCampos()
		ctx = {'lista':lista, 'listFields':cabecera,'nomTabla':'Protocolos Observados'}
		return render_to_response('tramite/bandejaProt.html',ctx, context_instance=RequestContext(request))

class BusquedaAjax_View(TemplateView):
	
	def get(self,request,*args,**kwargs):
		print 'Busqueda ajax_view'
		protocolo = request.GET['protocolo']
		print protocolo 
		
		try:
			print 'esto es el protocolo %s' %(protocolo)
			lista = Bandeja.objects.filter(IdMProt__contains=protocolo, EstAccion='0').order_by('-IdBandeja')
			data = serializers.serialize('json', lista)
				
		except Exception, e:
			print e
		return HttpResponse(data, mimetype='application/json')

class DetalleProtocoloAjax_View(TemplateView):
	
	def get(self,request,*args,**kwargs):
		print 'Lista de detalles protocolo'
		protocolo = request.GET['protocolo']
		#print protocolo 
		
		try:
			
			lista = DProtocolo.objects.filter(IdMProt__IdMProt=protocolo)
			
			data = serializers.serialize('json', lista)
			#print lista
			
		except Exception, e:
			print e
		return HttpResponse(data, mimetype='application/json')

class ObservarProtocoloAjax_View(TemplateView):

	def get(self,request,*args,**kwargs):
		protocolo = request.GET['protocolo']
		lstCod = obtenerNumeros(protocolo)
				
		try:
			for cod in lstCod:
				lstobj = Bandeja.objects.filter()
				
			
			
		except Exception, e:
			print e
		return HttpResponse(data, mimetype='application/json')

class DetalleProtocolo_View(TemplateView):
	template_name = 'tramite/detalle_protocolo.html'
	
	def generarCodigo(self):
		anio = datetime.date.today().strftime("%Y")
		if (DProtocolo.objects.count()==0):
			anio = datetime.date.today().strftime("%Y")
			codigo = 'DP'+anio+'-00000001'

		else:
			obj = DProtocolo.objects.last()
			cod = obj.IdDProt
			num = cod[7:]
			num = int(num)
			num = num + 1
			can = len(str(num))
			dif = 8-can
			codigo = ''
			codigo = '0'*dif
			codigo = 'DP'+ anio + '-' + codigo + str(num)
		return codigo
	@method_decorator(access_permission([0,1]))
	@method_decorator(login_required(login_url='/'))
	def get(self, request,*args,**kwargs):
		idProtocolo = kwargs['idpr']

		try:
			#lstUsuario = MUsuario.objects.all()
			#lstArea = DTabla.objects.filter()
			objMP = MProtocolo.objects.get(IdMProt=idProtocolo)
			pr = DProtocolo()
			lista = DProtocolo.objects.filter(IdMProt__IdMProt=idProtocolo)
			lstAreas = DTabla.objects.filter(IdMTab__IdMTabla='008')
			lstFormato = DTabla.objects.filter(IdMTab__IdMTabla='013')
			cabecera = pr.get_nombreCampos()
			form = DProtocoloForm()
			ctx = {'lista':lista,'listFields':cabecera,'nomTabla':'Detalle Protocolo', 'form':form,'objMP':objMP,'lstFormato':lstFormato,'lstAreas':lstAreas}
			return render_to_response('tramite/detalle_protocolo.html',ctx, context_instance=RequestContext(request))
			
		except Exception, e:
			raise
		

	def post(self,request,*args,**kwargs):
		cod = ""
		try:
			
			form = DProtocoloForm(request.POST,request.FILES) # A form bound to the POST data
			if form.is_valid():
				print 'es valido'

				add = form.save(commit=False)
				add.IdDProt = self.generarCodigo()
				add.IdMProt = MProtocolo.objects.get(IdMProt=request.POST['codProtocolo'])
				cod  = request.POST['codProtocolo']
				add.NomDProt = request.POST['nomDProt']
				add.IdTipDocDProt = request.POST['idTipDocDProt']
				add.UbiLogDProt = request.user.pk
				add.UbiFisDProt = request.POST['ubiFisDProt']
				add.IdPerDProt = '1'
				add.EstDProt = '1'
				add.save()
			else:
				print 'no es valido'
			
		except Exception, e:
			print e
			self.error = "Sucedio un error al momento de guardar"
		
		return HttpResponseRedirect('/tramite/detalleprotocolo/%s' %(cod))

def obtenerNumeros(cad):
	lstId = cad
	lst   = []
	band  = True
	
	while lstId != ",":
		lst.append(re.search(r'\D*(\d*)',lstId).groups()[0])
		lstId = re.sub(r'^\D*(\d*)',',',lstId)
	return lst

def regProtocoloEnBandeja(obj, codUsuarioEnvio, codUsuarioRecepcion, usuario, observacion='', mensaje='',estObs='0',envx=''):
	
	mensajeCorreo = ""
	print codUsuarioRecepcion
	
	codigo = ''
	if Bandeja.objects.count() > 0:
		band = Bandeja.objects.last()
		cod = band.IdBandeja
		print cod
		num = cod[7:]
		num = int(num)
		num = num + 1
		can = len(str(num))
		dif = 8-can
		codigo = ''
		codigo = '0'*dif
		
		codigo = 'BD'+ '2014' + '-' + codigo + str(num)
	else:
		codigo = 'BD2014-00000001'

	idProt = obj.IdMProt
	objProtocolo = MProtocolo.objects.get(IdMProt=idProt)
	if(estObs=="1"):
		mensajeCorreo= "Protocolo observado." 


	cliente = obj.CliBProt
	referencia = obj.IdProtRef
	proyecto = obj.ProyBProt
	observacion= ''
	objUser = User.objects.get(pk=codUsuarioRecepcion)
	correUsuario = objUser.email
	IdMProy = ""
	NomMProy = ""
	

	try:
		mensajeCorreo += "<body style='font-family:Arial;font-size:8px;'><h3>Ha recibido un protocolo con los siguientes datos:</h3> <h4>Nro de Protocolo:%s</h4><h4>Unidad Ejecutora:%s</h4><h4>Nro de Convenio:%s</h4><h4>Nombre del Convenio:%s</h4><h4>Enviado por:%s</h4><h4>Mensaje:%s</h4><br><br><br>---------------------------<br><h5 style='color:#FF0000'>Por favor no responder a este correo</h5></body>" %(idProt,cliente,objProtocolo.idMProy.idMProy,objProtocolo.idMProy.nomMProy,envx,mensaje)
	except Exception, e:
		mensajeCorreo += "<body style='font-family:Arial;font-size:8px;'><h3>Ha recibido un protocolo con los siguientes datos:</h3> <h4>Nro de Protocolo:%s</h4><h4>Unidad Ejecutora:%s</h4><h4>Nro de Convenio:No Existe</h4><h4>Nombre del Convenio:No Existe</h4><h4>Enviado por:%s</h4>><h4>Mensaje: %s</h4><br><br><br>---------------------------<br><h5 style='color:#FF0000'>Por favor no responder a este correo</h5></body>" %(idProt,cliente,envx,mensaje)
	finally:
		pass

	
	bd = Bandeja()

	bd.IdBandeja = codigo
	bd.IdMUsuEnv = codUsuarioEnvio
	bd.IdMUsuRec = codUsuarioRecepcion
	bd.IdMProt = idProt
	bd.FecEnv = timezone.now()
	bd.FecRec = timezone.now()
	bd.FecSist = timezone.now()
	bd.MenBProt = mensaje
	bd.EstBProt = '1' #Estado del BProt, cuando es 1 está activo, si es 0 esta eliminado logicamente
	bd.EstAccion = '0' #Cambia de valor a 1 cuando el protocolo esta enviado
	bd.EstObservado = estObs #Cambia de valor a 1 cuando el protocolo esta observado
	bd.ObsProt = observacion
	bd.NomMUsuEnv = envx
	bd.NomMUsuREc = usuario
	bd.CliBProt = cliente
	bd.ProyBProt = proyecto
	bd.IdProtRef = referencia
	bd.save()

	html_content = mensajeCorreo
	enviarCorreo(mensajeCorreo,correUsuario,html_content)
	
class ConveniosSupervisor_View(TemplateView):
	@method_decorator(access_permission([0,2]))
	def get(self, request, *args, **kwargs):
		IdMPer = request.user.idMPer
		lista_proyectos = MColaborador.objects.filter(IdMPer__IdMPer = IdMPer)
		lista = []
		for item in lista_proyectos:
			lista.append(item.IdMProy)
		ctx = {'lista':lista}
		return render_to_response('tramite/supervision_convenio.html',ctx, context_instance=RequestContext(request))

class CargarPresupuesto_View(TemplateView):
	@method_decorator(access_permission([0,3]))
	@method_decorator(login_required(login_url='/'))
	def get(self, request, *args, **kwargs):
		id_tipoUsuario = request.user.tipoUsuario
		
		if int(id_tipoUsuario) != 3:
			msj = 'Ud no puede cargar presupuestos.'
			ctx = {'mensaje':msj}
		else:
			id_cliente = request.user.idMCli
			proy = MProyecto.objects.filter(IdMCli__IdMCli= id_cliente).order_by('-IdConv')
			if len(proy) > 0 :
				proy = proy[0]			
				lista_p = PProyectos.objects.filter(IdMProy__IdMProy = proy.IdMProy)
				if len(lista_p) > 0:
					msj = 'Ya existe un presupuesto, si desea cargar un nuevo presupuesto contacte al supervisor asignado.'
					ctx = {'mensaje':msj}
				else:
					form = CargaForm()
					ctx = {'form': form}
			else:
				msj = 'No existe ningun convenio registrado con esta Unidad Ejecutora.'
				ctx = {'mensaje':msj}

		return render_to_response('tramite/form_presupuesto.html', ctx,context_instance=RequestContext(request))
		
	def post(self, request, *args, **kwargs):
		from .proceso import Presupuesto
		msj = ""
		filename = ""
		n_meses = 0
		try:
			
			form = CargaForm(request.POST,request.FILES) # A form bound to the POST data
			if form.is_valid():
				add = form.save(commit=False)
				add.save()
				msj = 'El archivo fue subido con exito'
			else:
				msj = 'El formulario no es valido'
		
		except Exception, e:
				#print e
			msj = "Sucedio un error al momento de guardar"
		
		errores = []
		datos = []
		query = Presupuesto()
		filename = CargaPresupuesto.objects.last()
		filename = str(filename.doc_temp)
		filename = filename.split('/')
		filename = filename[-1]

		hasname = query.inicio(filename)
		le = []
		ld = []
		if hasname:
			resultado = query.procesar_pres()
			cant_meses = int(query.duracion_proyecto())
			filas_resultados = query.get_lista_fni
			lista_resultados = query.get_lista_resultados
			valido = resultado[0]
			datos = resultado[1]
			errores = resultado[2]
			self.guardar_presupuesto(request, filas_resultados,lista_resultados,datos)
		if len(errores)>2:
			le = errores[:-2]
		elif len(errores)<3:
			ld = datos
			
		n_meses = 5
		rango = range(1,cant_meses+1)
		ctx = {'msj':msj,'errores':le,'n_meses':n_meses,'datos':datos,'lista_resul':lista_resultados,'rango':rango}
		return render_to_response('tramite/form_presupuesto.html', ctx,context_instance=RequestContext(request))

	def guardar_presupuesto(self,request, fni, desc_fni, datoPres):
	
		id_cliente = request.user.idMCli
		proy = MProyecto.objects.filter(IdMCli__IdMCli= id_cliente, EstMProy = 1).order_by('-IdConv')
		proy = proy[0]
		FECHA = datetime.datetime.today()
		index = 1
		for p in datoPres:
			
			pres = PProyectos()
			cod_pres = self.generar_Codigo()
			pres.IdPProy = cod_pres
			
			
			pres.IdMProy = proy
			pres.NroPartPProy = p['partida']
			pres.IdNivPartPProy = p['nivel']
			pres.TitPProy = p['tit']
			pres.DescPProy = p['desc']
			pres.NroPartPerProy = self.pertenece_a(p['partida'])
			pres.IdUnidMed = p['um']
			try:
				pres.CantPProy = int(p['cant'])	
			except ValueError as ve:
				pres.CantPProy = 0.0
			except Exception, e:
				pres.CantPProy = 0.0
			try:
				pres.CostUnitPProy = float(p['cu'])
			except Exception, e:
				pres.CostUnitPProy = 0.0
			try:
				pres.CostTotPProy = float(p['ct'])
			except Exception, e:
				pres.CostTotPProy = 0.0
			try:
				pres.FFFipPProy = float(p['ifip'])
			except Exception, e:
				pres.FFFipPProy = 0.0
			try:
				pres.FFCliPProy = float(p['iue'])
			except Exception, e:
				pres.FFCliPProy = 0.0
			try:
				pres.FFOtrosPProy = float(p['iotros'])
			except Exception, e:
				pres.FFOtrosPProy = 0.0
			try:
				ct =  float(p['ct'])
			except ValueError as ve:
				ct = 0.0
			try:
				ifip =  float(p['ifip'])
				pres.PFFFipPProy = (ifip * 100)/ct
			except ValueError as ve:
				ifip = 0.0
			except ZeroDivisionError as dz:
				pres.PFFFipPProy = 0
			try:
				iue =  float(p['iue'])
				pres.PFFCliPProy = (iue * 100)/ct
			except ValueError as ve:
				iue = 0.0
			except ZeroDivisionError as dz:
				pres.PFFCliPProy = 0.0
			try:
				iotros =  float(p['iotros'])
				pres.PFFOtrosPProy = (iotros * 100)/ct
			except ValueError as ve:
				iotros = 0.0
			except ZeroDivisionError as dz:
				pres.PFFOtrosPProy = 0.0

			pres.FinPProy = '0'
			pres.VerPProy = '0'
			pres.EstPProy = '1'
			pres.FecIngPProy = FECHA.strftime('%Y-%m-%d')
			
			pres.IdUsuCreaPProy = request.user.id
			
			pres.IdUsuModPProy = ''
			pres.CostEjePProy = 0.0
			pres.CostSalPProy = 0.0
			pres.IdMotCierrePProy = '0'
			pres.PorCostEjePProy = 0.0
			pres.BorradorPProy = '1'
			pres.EstPresPProy = '0'
			pres.EstEvalPProy = '0'
			pres.EstValidPProy = '0'
			pres.EstAprobPProy = '0'
			pres.EstModifPProy = '0'
			
			mes = proy.FecIniRealMProy 
			anio = mes.strftime('%Y')
			anio = int(anio)
			mes_ini = mes.strftime('%m')
			mes_ini = int(mes_ini)
			mes_c = 1
			
			pres.save()
			index = index + 1
			i=1
			x=0
			for m in p['cant_meses']:

				cpp = CPProyectos()
				cpp.IdPProy = pres
				cpp.MesCPProy = mes_c
				cpp.MesCCPProy = mes_ini
				cpp.AnioCCPProy = anio
				cpp.MontoEjecCPProy = 0
				cpp.PorcEjecCPProy = 0
				cpp.VerCPProy = 0
				cpp.SVerCPProy = 0
				cpp.EstCPProy = 1
				cpp.EstModifCPProy = 0
				cpp.MontoEjeFipCPProy = 0
				cpp.PorcEjeFipCPProy = 0
				cpp.MontoEjeCliCPProy = 0
				cpp.PorcEjeCliCPProy = 0
				cpp.MontoRealCPProy = 0
				cpp.PorcRealCPProy = 0
				if (x%2 == 0):
					cpp.MontoRealFipCPProy = m
					cpp.PorcRealFipCPProy = 0
					cpp.MontoRealCliCPProy = 0
					cpp.PorcRealCliCPProy = 0
				else :
					cpp.MontoRealFipCPProy = 0
					cpp.PorcRealFipCPProy = 0
					cpp.MontoRealCliCPProy = m
					cpp.PorcRealCliCPProy = 0

				cpp.MontoDifEjecRealCPProy = 0
				cpp.PorcDifEjecRealCPProy = 0
				cpp.EstVisCPProy = 0
				if (mes_ini == 12):
					mes_ini = 1
				if (i %2 == 0):
					mes_ini += 1
					mes_c += 1

				cpp.save()
				i += 1
				x += 1

	def pertenece_a(self, partida):
		val_part = partida.split(',')
		if (len(val_part) == 1):
			return partida
		else:
			val_part = val_part[:-1]
			pertence = '.'.join(val_part)
			return pertence

	def generar_Codigo(self):
		if (PProyectos.objects.count() == 0):
			#print convo
			codigo = 'PRES2014-00000001'
		else:
			anio = datetime.datetime.today().year
			anio = str(anio)
			obj = PProyectos.objects.last()
			cod = obj.IdPProy
			num = cod[-8:]
			num = int(num)
			num = num + 1
			can = len(str(num))
			dif = 8-can
			codigo = ''
			codigo = '0'*dif
			codigo = 'PRES'+anio+ '-' + codigo + str(num)
		return codigo

class ObservarAjax_View(TemplateView):
	def get(self,request,*args,**kwargs):
		protocolo = request.GET['protocolo']
		usuario = request.GET['usuario']
		
		lstObservado = Bandeja.objects.filter(IdMProt=protocolo, IdMUsuEnv =usuario, EstAccion='0')
		for obj in lstObservado:
			obj.EstObservado = '1'
			obj.save()


		objBand = lstObservado[0]
		objBand.EstAccion = "0"
		codUsuarioEnvio = request.user.pk
		codUsuarioRecepcion = usuario
		nomUsuario = request.user.username
		observacion = ""
		mensaje = "El protocolo ha sido observado"
		
		regProtocoloEnBandeja(obj, codUsuarioEnvio, codUsuarioRecepcion,nomUsuario,observacion,mensaje)

		lista = Bandeja.objects.filter(IdMProt=protocolo, IdMUsuEnv =usuario, EstAccion='1')
		bd = Bandeja()

		data = serializers.serialize('json', lista)		
			
		
		return HttpResponse(data, mimetype='application/json')

class MaestroProtocoloAjax_View(TemplateView):
	def get(self,request,*args,**kwargs):
		protocolo = request.GET['protocolo']
		#print "para maestro protocolo %s" %(protocolo)
		try:
			lista = MProtocolo.objects.filter(IdMProt=protocolo)[:1]
			print lista
			data = serializers.serialize('json', lista)
			
		except Exception, e:
			print e
		return HttpResponse(data, mimetype='application/json')

class UsuarioAjax_View(TemplateView):
	def get(self,request,*args,**kwargs):
		
		try:
			lstUsuarios = User.objects.all()
			#data = serializers.serialize('json',lstUsuarios,fields('pk','username','first_name','last_name'))	
			data = serializers.serialize('json',lstUsuarios)	
			
		except Exception, e:
			print e
		return HttpResponse(data,mimetype='application/json')

class MaestroConvenioAjax_View(TemplateView):
	def get(self,request,*args,**kwargs):
		convenio = request.GET['convenio']
		#print "para maestro convenio %s" %(convenio)
		try:
			lista = MProyecto.objects.filter(IdMProy=convenio)[:1]
			#print lista
			data = serializers.serialize('json', lista)
			
		except Exception, e:
			print e
		return HttpResponse(data, mimetype='application/json')
		
class ColaboradoresConvenioAjax_View(TemplateView):
	def get(self,request,*args,**kwargs):
		convenio = request.GET['convenio']
		#print "para colaboradores convenio %s" %(convenio)
		try:
			lista = MColaborador.objects.filter(IdMProy__IdMProy=convenio)
			#lista = list(MColaborador.objects.filter(idMProy__idMProy=convenio))+ list(MPersonal.objects.all())
			#print lista
			data = serializers.serialize('json', lista, use_natural_keys=True)	
		except Exception, e:
			print e
		return HttpResponse(data, mimetype='application/json')

class ModificatoriasConvenioAjax_View(TemplateView):
	def get(self,request,*args,**kwargs):
		convenio = request.GET['convenio']
		#print "para modificatorias convenio %s" %(convenio)
		try:
			lista = DProyecto.objects.filter(IdMProy__IdMProy=convenio)
			#print lista
			data = serializers.serialize('json', lista)
			
		except Exception, e:
			print e
		return HttpResponse(data, mimetype='application/json')

class MaestroPersonalAjax_View(TemplateView):
	def get(self,request,*args,**kwargs):
		convenio = request.GET['convenio']
		print "para personal convenio %s" %(convenio)
		try:
			lista = MPersonal.objects.all()
			#print lista
			#data = serializers.serialize('json', lista,fields('idMPer','apePMPer','nomMPer'))
			data = serializers.serialize('json', lista)
			
		except Exception, e:
			print e
		return HttpResponse(data, mimetype='application/json')

class LocalizarPorProtocoloAjax_View(TemplateView):
	def get(self,request, *args, **kwargs):

		protocolo = request.GET['protocolo']
		nombre = request.GET['nombre']
		cliente = request.GET['cliente']
		#fecinicio = request.GET['fecinicio']
		#fecfin = request.GET['fecfin']
		referencia = request.GET['referencia']
		
		try:
			#print 'esto es el protocolo %s' %(protocolo)
			#lista = Bandeja.objects.filter( estAccion='0',idMProt__contains=protocolo, proyBProt__contains=nombre.upper(), cliBProt__contains= cliente.upper(), fecSist__range=(fecinicio,fecfin)).order_by('-idBandeja')
			lista = Bandeja.objects.filter(IdMProt__contains=protocolo, ProyBProt__contains=nombre.upper(), CliBProt__contains= cliente.upper()).order_by('-IdBandeja')
			#lista = Bandeja.objects.filter(idMProt__contains=protocolo, estAccion='0').order_by('-idBandeja')
			data = serializers.serialize('json', lista)
				
		except Exception, e:
			print e
		return HttpResponse(data, mimetype='application/json')

class LocalizarPorProyectoAjax_View(TemplateView):
	def get(self,request,*args,**kwargs):
		#print 'Busqueda ajax_view'
		proyecto = request.GET['protocolo']
		#print protocolo 
		
		try:
			#print 'esto es el protocolo %s' %(protocolo)
			#lstFiltro = Bandeja.objects.filter(idMProt__contains=protocolo, proyBProt__contains=proyecto.upper(), cliBProt__contains= cliente.upper(), fecSist__range=(fecInicio,fecFin)).order_by('-fecSist')
			lista = Bandeja.objects.filter(ProyBProt__contains=proyecto, EstAccion='0').order_by('-IdBandeja')
			print lista
			data = serializers.serialize('json', lista)
				
		except Exception, e:
			print e
		return HttpResponse(data, mimetype='application/json')

class LocalizarPorUnidadEjecutoraAjax_View(TemplateView):
	def get(self,request,*args,**kwargs):
		#print 'Busqueda ajax_view'
		cliente = request.GET['cliente']
		#print protocolo 
		
		try:
			#print 'esto es el protocolo %s' %(protocolo)
			lista = Bandeja.objects.filter(CliBProt__contains=cliente, EstAccion='0').order_by('-IdBandeja')
			data = serializers.serialize('json', lista)
				
		except Exception, e:
			print e
		return HttpResponse(data, mimetype='application/json')

class LocalizarPorReferenciaAjax_View(TemplateView):
	def get(self,request,*args,**kwargs):
		#print 'Busqueda ajax_view'
		referencia = request.GET['referencia']
		#print protocolo 
		
		try:
			#print 'esto es el protocolo %s' %(protocolo)
			lista = Bandeja.objects.filter(IdProtRef__contains=referencia, EstAccion='0').order_by('-IdBandeja')
			data = serializers.serialize('json', lista)
				
		except Exception, e:
			print e
		return HttpResponse(data, mimetype='application/json')

class LocalizarPorFechaAjax_View(TemplateView):
	def get(self,request,*args,**kwargs):

		fecha = request.GET['fecha']
		anio = datetime.datetime.now().year
		mes = datetime.datetime.now().month
		dia= datetime.datetime.now().day
		datafec = fecha.split('-')	#print protocolo 
		lista = []
		
		if (len(datafec) == 3):
			print "en 3"
			# Existe año mes y dia
			if(len(datafec[0]) == 4):
				anio = int(datafec[0])
			#else:
			#	anio = datetime.datetime.now().year

			if(len(datafec[1]) == 2):
				mes = int(datafec[1])
				dia = int(datafec[2])
			#else:
			#	mes = datetime.datetime.now().month
			#	dia = datetime.datetime.now().day

			lista = Bandeja.objects.filter(FecEnv__year=anio,FecEnv__month=mes,FecEnv__day=dia, EstAccion='0').order_by('-IdBandeja')

		elif (len(datafec) == 2):
			print "en 2"
			if(len(datafec[0]) == 4):
				anio = int(datafec[0])
			#else:
			#	anio = datetime.datetime.now().year

			if(len(datafec[1]) == 2):
				mes = int(datafec[1])
			#else:
			#	mes = datetime.datetime.now().month

			lista = Bandeja.objects.filter(FecEnv__year=anio,FecEnv__month=mes, EstAccion='0').order_by('-IdBandeja')
		
		elif (len(datafec) == 1):
			print "en 1"
			if(len(datafec[0]) == 4):
				anio = int(datafec[0])
				lista = Bandeja.objects.filter(FecEnv__year=anio, EstAccion='0').order_by('-IdBandeja')
			#else:
			#	anio = datetime.datetime.now().year
			#	lista = Bandeja.objects.filter(fecEnv__year=anio, estAccion='0').order_by('-idBandeja')

			if(len(datafec[0]) == 2):
				mes = int(datafec[0])
				lista = Bandeja.objects.filter(FecEnv__month=mes, EstAccion='0').order_by('-IdBandeja')
			#else:
			#	mes = datetime.datetime.now().month
			#	lista = Bandeja.objects.filter(fecEnv__month=mes, estAccion='0').order_by('-idBandeja')


			
		try:
		
			#lista = Bandeja.objects.filter(fecEnv__contains=fecha, estAccion='0').order_by('-idBandeja')
			data = serializers.serialize('json', lista)
				
		except Exception, e:
			print e

		return HttpResponse(data, mimetype='application/json')
		
		#return self.get(request)

class RegistrarColaboradorAjax_View(TemplateView):
	def get(self,request,*args,**kwargs):
		if request.is_ajax() :
			col = MColaborador()
			es = request.GET["esto"]
			print es  
			obj = MPersonal.objects.get(pk=4)
			col.IdMPer = obj
			obj2 = MProyecto.objects.get(pk=5)
			col.IdMProy = obj2
			col.IdTipoCargoProy = '1'
			col.FecIniMCol = '2014-12-12' #datetime.datetime.now()
			col.FecFinMCol = '2014-12-12' #datetime.datetime.now()
			col.FecFirmaMCol = '2014-12-12'
			col.TiempoMCol = '5'
			col.MontoMCol = 2
			col.MontoMenMCol =5 
			col.EstMCol = '1'
			col.EstActMCol = '1'
			col.RutaPDFMCol = request.GET["archivo"]
			col.RutaOCRMCol = request.GET["archivo"]
			col.save()
		msj={'status':'esto es para ti json'}
		return HttpResponse(json.dumps(msj),mimetype='application/json')

class ListaDepartamentoAjax_View(TemplateView):
	def get(self,request,*args,**kwargs):
		idregion = request.GET['idregion']
		obj = DTabla.objects.get(pk =idregion)			
		region = obj.IdDTab
		print region
		try:
			#print 'esto es el protocolo %s' %(protocolo)
			lstDepartamento = DTabla.objects.filter(IdMTab__IdMTabla='003',IdRefDTab=region).order_by('NomDTab')
			data = serializers.serialize('json', lstDepartamento)
				
		except Exception, e:
			print e
		return HttpResponse(data, mimetype='application/json')

class ListaProvinciaAjax_View(TemplateView):
	def get(self,request,*args,**kwargs):
		iddepa = request.GET['iddepa']
		obj = DTabla.objects.get(pk =iddepa)			
		departamento = obj.IdDTab
			
		try:
			#print 'esto es el protocolo %s' %(protocolo)
			lstPronvincia = DTabla.objects.filter(IdMTab__IdMTabla='004', IdRefDTab=departamento).order_by('NomDTab')
			data = serializers.serialize('json', lstPronvincia)
				
		except Exception, e:
			print e
		return HttpResponse(data, mimetype='application/json')

class ListaDistritoAjax_View(TemplateView):
	def get(self,request,*args,**kwargs):
		idprov = request.GET['idprov']
		obj = DTabla.objects.get(pk =idprov)			
		provincia = obj.IdDTab
			
		try:
			#print 'esto es el protocolo %s' %(protocolo)
			lstDistrito = DTabla.objects.filter(IdMTab__IdMTabla='005',IdRefDTab=provincia).order_by('NomDTab')
			data = serializers.serialize('json', lstDistrito)
				
		except Exception, e:
			print e
		return HttpResponse(data, mimetype='application/json')

class TipoPersonalAjax_View(TemplateView):
	def get(self,request,*args,**kwargs):
		codMPer = request.GET['codPer']
		objPersonal = MPersonal.objects.get(IdMPer = codMPer)
		mensaje = ""
		if (objPersonal.EstMPer == '0'):
			mensaje = {'status':'True'}
		else:
			mensaje = {'status':'False'}
		return HttpResponse(json.dumps(mensaje), mimetype='application/json')

"""
class Presupuesto_View(TemplateView):
	@method_decorator(access_permission([0,1]))
	@method_decorator(login_required(login_url='/'))
	def get(self, request, *args, **kwargs):
		form = CargaForm()
		ctx = {'form':form}
		return render_to_response('tramite/formPresupuesto.html',ctx,context_instance=RequestContext(request))
	def post(self, request, *args, **kwargs):
		from .proceso import Presupuesto
		msj = ""
		filename = ""
		n_meses = 0
		try:
			
			form = CargaForm(request.POST,request.FILES) # A form bound to the POST data
			if form.is_valid():
				add = form.save(commit=False)
				filename = str(add.doc_temp)
				add.save()
				msj = 'El archivo fue subido con exito'
			else:
				msj = 'El formulario no es valido'
			print msj
		except Exception, e:
			print e
			msj = "Sucedio un error al momento de guardar"
		

		query = Presupuesto()
		hasname = query.inicio(filename)
		le = []
		ld = []
		if hasname:
			resultado = query.procesar_pres()
			valido = resultado[0]
			datos = resultado[1]
			errores = resultado[2]
		if len(errores)>2:
			le = errores[:-2]
		elif len(errores)<3:
			ld = datos
		n_meses = 5
		ctx = {'msj':msj,'errores':le,'n_meses':n_meses,'datos':datos}
		print 'Se encontraron %s errores en el archivo' %(len(le))

		return render_to_response('tramite/formPresupuesto.html',ctx,context_instance=RequestContext(request))
	
"""

class Formulario_View(TemplateView):
	def get(self,request,*args,**kwargs):
		form = Formulario()
		ctx = {'form':form}
		return render_to_response('tramite/nuevo.html',ctx, context_instance=RequestContext(request))

class EditarUsuario_View(TemplateView):
	def get(self,request,*args,**kwargs):
		cod = request.GET['id']
		
		usuario = User.objects.get(pk=cod)
		print usuario
		data = serializers.serialize('json', usuario)
		return HttpResponse(data, mimetype='application/json')

class ModificarPasswordAjax_View(TemplateView):
	def get(self, request, *args, **kwargs):
		pass1 = request.GET['pass1']
		try:
			usuario = User.objects.get(username = request.user.username)
			usuario.set_password(pass1)
			usuario.save()
			message= {'mensaje':'El password ha sido actualizado correctamente!.'}
			return HttpResponse(json.dumps(message),mimetype='application/json')
		except Exception, e:
			message= {'mensaje':e}
		return HttpResponse(json.dumps(message),mimetype='application/json')

class Presupuesto_View(TemplateView):
	@method_decorator(access_permission([0,3]))
	@method_decorator(login_required(login_url='/'))
	def get(self, request, *args, **kwargs):
		tipo_usuario = request.user.tipoUsuario
		
		if int(tipo_usuario) == 3 :
			id_cliente = request.user.idMCli
			proy = MProyecto.objects.filter(IdMCli__IdMCli= id_cliente, EstMProy = 1).order_by('-FecIngMProy')
			id_proy = proy[0].IdMProy
			nombre_proyecto = proy[0].NomMProy 
			nombre_cliente =  proy[0].IdMCli.NomMCli
			convenio = proy[0].IdMProy
			presupuesto_proyecto = PProyectos.objects.filter(IdMProy__IdMProy = id_proy)
			lista = []
			rango = 0
			for pp in presupuesto_proyecto:
				dic_dp = {}
				dic_dp['IdPProy'] = pp.IdPProy
				dic_dp['partida'] = pp.NroPartPProy
				dic_dp['tit'] = pp.TitPProy
				dic_dp['desc'] = pp.DescPProy
				dic_dp['um'] = pp.IdUnidMed
				dic_dp['cant'] = pp.CantPProy
				dic_dp['cu'] = pp.CostUnitPProy
				dic_dp['ct'] = pp.CostTotPProy
				dic_dp['ifip'] = pp.FFFipPProy
				dic_dp['iue'] = pp.FFCliPProy
				dic_dp['iotros'] = pp.FFOtrosPProy
				dic_dp['pifip'] = pp.PFFOtrosPProy
				dic_dp['piue'] = pp.PFFCliPProy
				dic_dp['piotros'] = pp.PFFOtrosPProy
				lista_meses = []
				detalle_pres = CPProyectos.objects.filter(IdPProy__IdPProy = pp.IdPProy)
				index = 0
				for cp in detalle_pres:
					print index
					if (index%2==0):
						lista_meses.append(cp.MontoRealFipCPProy)
					else:
						lista_meses.append(cp.MontoRealCliCPProy)
					index += 1
				
				dic_dp['cant_meses'] = lista_meses
				rango = len(lista_meses)

				lista.append(dic_dp)

			rango = rango/2
			rango = range(1, rango+1)
			
			self.imprimir(lista)

			ctx = {'proyecto':nombre_proyecto,'cliente':nombre_cliente,'datos':lista,'rango':rango,'convenio':convenio}
		else:
			ctx = {'msg':'No existe presupuesto.'}
		
		return render_to_response('tramite/presupuesto.html', ctx, context_instance= RequestContext(request))

	def imprimir(self, datos):
		for row in datos:
			print row['partida']
			print row['tit']
			print row['desc']
			print row['um']
			print row['cant']
			print row['cu']
			print row['ct']
			print row['ifip']
			print row['cant_meses']
	def post(self, request, *args, **kwargs):
		pass
		
class EliminarRegistroAjax_View(TemplateView):
	def get(self, request, *args, **kwargs):
		lst = request.GET['lista_codigos']
		print lst
		try:
			modelo = request.GET['modelo']
			lista_codigos = request.GET['lista_codigos']
			lista_modelos = {'0':User, '1':MTabla, '2':DTabla, '3': DProyecto,'4': MPersonal, '5': MColaborador, '6':MCliente, '7':MProyecto, '8':MProtocolo, '9':DProtocolo, '10': Bandeja, '11': PProyectos, '12': CPProyectos} 
			"""
			for cod in lista_codigos:
				eval('model.objects.get(pk=codigo).delete()',{'model':lista_modelos[modelo],'codigo':cod})	

			msj = "True"
			"""
			msj = "Se han eliminado %s registros." %(len(lista_codigos))
		except Exception, e:
			msj = str(e)
		except DoesNotExist as de:
			msj = "False 2"
		finally:
			message= {'mensaje':msj}
			return HttpResponse(json.dumps(message),mimetype='application/json')


class SupervisarProyecto_View(TemplateView):
	def get(self, request, proyecto):
		current_p = proyecto
		lista = PProyectos.objects.filter(IdMProy__IdMProy = current_p, EstPProy=1)
		if len(lista) > 0 :
			proy = MProyecto.objects.get(IdMProy = current_p, EstMProy = 1)
			id_proy = proy.IdMProy
			nombre_proyecto = proy.NomMProy 
			nombre_cliente =  proy.IdMCli.NomMCli
			convenio = proy.IdMProy
			presupuesto_proyecto = PProyectos.objects.filter(IdMProy__IdMProy = current_p)
			lista = []
			rango = 0
			for pp in presupuesto_proyecto:
				dic_dp = {}
				dic_dp['IdPProy'] = pp.IdPProy
				dic_dp['partida'] = pp.NroPartPProy
				dic_dp['tit'] = pp.TitPProy
				dic_dp['desc'] = pp.DescPProy
				dic_dp['um'] = pp.IdUnidMed
				dic_dp['cant'] = pp.CantPProy
				dic_dp['cu'] = pp.CostUnitPProy
				dic_dp['ct'] = pp.CostTotPProy
				dic_dp['ifip'] = pp.FFFipPProy
				dic_dp['iue'] = pp.FFCliPProy
				dic_dp['iotros'] = pp.FFOtrosPProy
				dic_dp['pifip'] = pp.PFFOtrosPProy
				dic_dp['piue'] = pp.PFFCliPProy
				dic_dp['piotros'] = pp.PFFOtrosPProy
				lista_meses = []
				detalle_pres = CPProyectos.objects.filter(IdPProy__IdPProy = pp.IdPProy)
				index = 0
				for cp in detalle_pres:
					print index
					if (index%2==0):
						lista_meses.append(cp.MontoRealFipCPProy)
					else:
						lista_meses.append(cp.MontoRealCliCPProy)
					index += 1
				
				dic_dp['cant_meses'] = lista_meses
				rango = len(lista_meses)

				lista.append(dic_dp)

			rango = rango/2
			rango = range(1, rango+1)
			
			#self.imprimir(lista)

			ctx = {'proyecto':nombre_proyecto,'cliente':nombre_cliente,'datos':lista,'rango':rango,'convenio':convenio}
			
		else :
			form = CargaForm()
			ctx = {'form': form, 'mensaje':'El proyecto no cuenta con un presupuesto','proyecto':current_p}
		return render_to_response('tramite/pres_proyecto.html', ctx, context_instance = RequestContext(request))
	
	def post(self, request, *args, **kwargs):
		from .proceso import Presupuesto
		msj = ""
		filename = ""
		n_meses = 0
		proyecto = ""
		try:
			
			form = CargaForm(request.POST,request.FILES) # A form bound to the POST data
			proyecto = request.POST['proyecto']
			if form.is_valid():
				add = form.save(commit=False)
				add.save()
				msj = 'El archivo fue subido con exito'
			else:
				msj = 'El formulario no es valido'
		
		except Exception, e:
				#print e
			msj = "Sucedio un error al momento de guardar"
		c_p = MProyecto.objects.get(IdMProy = proyecto)
		nombre_proyecto = c_p.NomMProy 
		nombre_cliente =  c_p.IdMCli.NomMCli
		convenio = c_p.IdMProy

		errores = []
		datos = []
		query = Presupuesto()
		filename = CargaPresupuesto.objects.last()
		filename = str(filename.doc_temp)
		filename = filename.split('/')
		filename = filename[-1]

		hasname = query.inicio(filename)
		le = []
		ld = []
		if hasname:
			resultado = query.procesar_pres()
			cant_meses = int(query.duracion_proyecto())
			filas_resultados = query.get_lista_fni
			lista_resultados = query.get_lista_resultados
			valido = resultado[0]
			datos = resultado[1]
			errores = resultado[2]

			
		if len(errores)>2:
			le = errores[:-2]
			ctx = {'errores':le}
			return render_to_response('tramite/pres_proyecto.html', ctx, context_instance=RequestContext(request))
		elif len(errores)<3:
			ld = datos
			self.guardar_presupuesto(request, filas_resultados,lista_resultados,datos,proyecto)
			n_meses = 5
			rango = range(1,cant_meses+1)
			ctx = {'datos':datos,'lista_resul':lista_resultados,'rango':rango, 'proyecto':nombre_proyecto,'cliente':nombre_cliente, 'convenio':convenio}
			return render_to_response('tramite/pres_proyecto.html', ctx,context_instance=RequestContext(request))

	def guardar_presupuesto(self,request, fni, desc_fni, datoPres, proyecto):
	
		proy = MProyecto.objects.get(IdMProy= proyecto, EstMProy = 1)
		FECHA = datetime.datetime.today()
		index = 1
		for p in datoPres:
			
			pres = PProyectos()
			cod_pres = self.generar_Codigo()
			pres.IdPProy = cod_pres
			
			
			pres.IdMProy = proy
			pres.NroPartPProy = p['partida']
			pres.IdNivPartPProy = p['nivel']
			pres.TitPProy = p['tit']
			pres.DescPProy = p['desc']
			pres.NroPartPerProy = self.pertenece_a(p['partida'])
			pres.IdUnidMed = p['um']
			try:
				pres.CantPProy = int(p['cant'])	
			except ValueError as ve:
				pres.CantPProy = 0.0
			except Exception, e:
				pres.CantPProy = 0.0
			try:
				pres.CostUnitPProy = float(p['cu'])
			except Exception, e:
				pres.CostUnitPProy = 0.0
			try:
				pres.CostTotPProy = float(p['ct'])
			except Exception, e:
				pres.CostTotPProy = 0.0
			try:
				pres.FFFipPProy = float(p['ifip'])
			except Exception, e:
				pres.FFFipPProy = 0.0
			try:
				pres.FFCliPProy = float(p['iue'])
			except Exception, e:
				pres.FFCliPProy = 0.0
			try:
				pres.FFOtrosPProy = float(p['iotros'])
			except Exception, e:
				pres.FFOtrosPProy = 0.0
			try:
				ct =  float(p['ct'])
			except ValueError as ve:
				ct = 0.0
			try:
				ifip =  float(p['ifip'])
				pres.PFFFipPProy = (ifip * 100)/ct
			except ValueError as ve:
				ifip = 0.0
			except ZeroDivisionError as dz:
				pres.PFFFipPProy = 0
			try:
				iue =  float(p['iue'])
				pres.PFFCliPProy = (iue * 100)/ct
			except ValueError as ve:
				iue = 0.0
			except ZeroDivisionError as dz:
				pres.PFFCliPProy = 0.0
			try:
				iotros =  float(p['iotros'])
				pres.PFFOtrosPProy = (iotros * 100)/ct
			except ValueError as ve:
				iotros = 0.0
			except ZeroDivisionError as dz:
				pres.PFFOtrosPProy = 0.0

			pres.FinPProy = '0'
			pres.VerPProy = '0'
			pres.EstPProy = '1'
			pres.FecIngPProy = FECHA.strftime('%Y-%m-%d')
			
			pres.IdUsuCreaPProy = request.user.id
			
			pres.IdUsuModPProy = ''
			pres.CostEjePProy = 0.0
			pres.CostSalPProy = 0.0
			pres.IdMotCierrePProy = '0'
			pres.PorCostEjePProy = 0.0
			pres.BorradorPProy = '1'
			pres.EstPresPProy = '0'
			pres.EstEvalPProy = '0'
			pres.EstValidPProy = '0'
			pres.EstAprobPProy = '0'
			pres.EstModifPProy = '0'
			
			mes = proy.FecIniRealMProy 
			anio = mes.strftime('%Y')
			anio = int(anio)
			mes_ini = mes.strftime('%m')
			mes_ini = int(mes_ini)
			mes_c = 1
			
			pres.save()
			index = index + 1
			i=1
			x=0
			for m in p['cant_meses']:

				cpp = CPProyectos()
				cpp.IdPProy = pres
				cpp.MesCPProy = mes_c
				cpp.MesCCPProy = mes_ini
				cpp.AnioCCPProy = anio
				cpp.MontoEjecCPProy = 0
				cpp.PorcEjecCPProy = 0
				cpp.VerCPProy = 0
				cpp.SVerCPProy = 0
				cpp.EstCPProy = 1
				cpp.EstModifCPProy = 0
				cpp.MontoEjeFipCPProy = 0
				cpp.PorcEjeFipCPProy = 0
				cpp.MontoEjeCliCPProy = 0
				cpp.PorcEjeCliCPProy = 0
				cpp.MontoRealCPProy = 0
				cpp.PorcRealCPProy = 0
				if (x%2 == 0):
					cpp.MontoRealFipCPProy = m
					cpp.PorcRealFipCPProy = 0
					cpp.MontoRealCliCPProy = 0
					cpp.PorcRealCliCPProy = 0
				else :
					cpp.MontoRealFipCPProy = 0
					cpp.PorcRealFipCPProy = 0
					cpp.MontoRealCliCPProy = m
					cpp.PorcRealCliCPProy = 0

				cpp.MontoDifEjecRealCPProy = 0
				cpp.PorcDifEjecRealCPProy = 0
				cpp.EstVisCPProy = 0
				if (mes_ini == 12):
					mes_ini = 1
				if (i %2 == 0):
					mes_ini += 1
					mes_c += 1

				cpp.save()
				i += 1
				x += 1

	def pertenece_a(self, partida):
		val_part = partida.split(',')
		if (len(val_part) == 1):
			return partida
		else:
			val_part = val_part[:-1]
			pertence = '.'.join(val_part)
			return pertence

	def generar_Codigo(self):
		if (PProyectos.objects.count() == 0):
			#print convo
			codigo = 'PRES2014-00000001'
		else:
			anio = datetime.datetime.today().year
			anio = str(anio)
			obj = PProyectos.objects.last()
			cod = obj.IdPProy
			num = cod[-8:]
			num = int(num)
			num = num + 1
			can = len(str(num))
			dif = 8-can
			codigo = ''
			codigo = '0'*dif
			codigo = 'PRES'+anio+ '-' + codigo + str(num)
		return codigo	
		

