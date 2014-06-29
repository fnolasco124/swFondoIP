#encoding:utf-8
from django import forms
from django.contrib.auth.models import User
from .models import *
import datetime

class MTablaForm(forms.ModelForm):
	class Meta:
		model = MTabla

class DTablaForm(forms.ModelForm):
	class Meta:
		model = DTabla

class MClienteForm(forms.ModelForm):
	class Meta:
		model = MCliente

class MProyectoForm(forms.ModelForm):
	class Meta:
		model = MProyecto
		fields = ('RutaPDFMProy','RutaPDFConvMProy','RutaPDFACMProy')

class MProyectoForm2(forms.ModelForm):
	class Meta:
		model = MProyecto
		

class MProtocoloForm(forms.ModelForm):
	class Meta:
		model = MProtocolo

class DProtocoloForm(forms.ModelForm):
	class Meta:
		model = DProtocolo
		fields = ('RutaPdfDProt',)

class DProyectoForm(forms.ModelForm):
	class Meta:
		model = DProyecto
		fields =('RutaPDFDProy',)

class MColaboradorForm(forms.ModelForm):
	class Meta:
		model = MColaborador
		fields =('RutaPDFMCol',)		

class CargaForm(forms.ModelForm):
	class Meta:
		model = CargaPresupuesto
		fields = ('doc_temp',)

lista_personal = MPersonal.objects.all().order_by("ApePMPer")
lista_clientes = MCliente.objects.all().order_by("NomMCli")

class UsuarioForm(forms.ModelForm):

	NIVEL_USUARIO = (('','Seleccione nivel de Usuario'),('0','Administrador'),('1','Usuario FIP'),('2','Supervisor'),('3','Unidad Ejecutora'))
	#lista_personal = MPersonal.objects.all().order_by("ApePMPer")
	#lista_clientes = MCliente.objects.all().order_by("NomMCli")
	PERSONAL = (('','Seleccione Personal'),)
	CLIENTE = (('','Seleccione UE'),('0','NO ES UE'))
	FECHA = datetime.datetime.today()
	for p in lista_personal:
		dato = ((p.IdMPer, p.ApePMPer+" "+p.ApeMMPer+", "+p.NomMPer),)
		PERSONAL += dato
	for c in lista_clientes:
		dato = ((c.IdMCli,c.NomMCli),)
		CLIENTE += dato
	
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de Usuario'}))
	password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'password','placeholder':'Password'}))
	fecIngreso = forms.DateField(initial = FECHA.strftime('%Y-%m-%d'), required=False, widget=forms.DateInput(attrs={'class':'form-control','type':'date', 'placeholder':'Fecha de ingreso'}))
	tipoUsuario = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=NIVEL_USUARIO)
	idMCli = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class':'form-control'}),choices=CLIENTE)
	idMPer = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class':'form-control'}),choices=PERSONAL)

	class Meta:
		model = User
		fields = ('username','password','fecIngreso','tipoUsuario','idMPer','idMCli')
		
class MPersonalForm(forms.ModelForm):
	lista_tipo_doc = DTabla.objects.filter(IdMTab__IdMTabla = '011')
	lista_areas = DTabla.objects.filter(IdMTab__IdMTabla = '008')
	lista_tipo_per = DTabla.objects.filter(IdMTab__IdMTabla = '022')
	FECHA = datetime.datetime.today()
	TIPO_PER = (('','Seleccione tipo personal'),)
	TIPO_DOC = (('','Seleccione tipo documento'),)
	AREAS = (('','Seleccione área'),)
	for p in lista_tipo_per:
		dato = ((p.pk, p.NomDTab),)
		TIPO_PER  += dato
	for p in lista_tipo_doc:
		dato = ((p.pk, p.NomDTab),)
		TIPO_DOC  += dato
	for p in lista_areas:
		dato = ((p.pk, p.NomDTab),)
		AREAS  += dato

	ApePMPer = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el apellido paterno'}))
	ApeMMPer = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el apellido materno'}))
	NomMPer = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese los nombres'}))
	FechNacMPer = forms.DateField(required=False,initial = FECHA.strftime('%Y-%m-%d'), widget=forms.DateInput(attrs={'class':'form-control','type':'date', 'placeholder':'Fecha de nacimiento'}))
	IdTipPerMPer = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class':'form-control'}),choices=TIPO_PER)
	IdTipDocMPer = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class':'form-control'}),choices=TIPO_DOC)
	NDocMPer = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese número de documento'}))
	FecIngMPer = forms.DateField(initial = FECHA.strftime('%Y-%m-%d'), widget=forms.DateInput(attrs={'class':'form-control','type':'date', 'placeholder':'Fecha de ingreso'}))
	Tel1MPer = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese telefono'}))
	Tel2MPer = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese telefono(opcional)'}))
	Email1MPer = forms.CharField(widget=forms.TextInput(attrs={'type':'email','class':'form-control','placeholder':'Ingrese email'}))
	Email2MPer = forms.CharField(required=False,widget=forms.TextInput(attrs={'type':'email','class':'form-control','placeholder':'Ingrese email(opcional)'}))
	IdArea = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class':'form-control'}),choices=AREAS)
	class Meta:
		model = MPersonal
		fields = ('ApePMPer','ApeMMPer','NomMPer','FechNacMPer','IdTipPerMPer','IdTipDocMPer','NDocMPer','FecIngMPer','Tel1MPer','Tel2MPer','Email1MPer','Email2MPer','IdArea')

class PresupuestoForm(forms.ModelForm):
	class Meta:
		model = PProyectos
		
