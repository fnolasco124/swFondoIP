#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
from django.db import models
from django.contrib.auth.models import User
import datetime

# Agregamos los campos a la tabla usuario
TIPO_USUARIO = (
		('0', 'Administrador'),
		('1', 'Supervisor'),
		('2', 'Unidad Ejecutora'),
		('3', 'Usuario Fip'),
	)
User.add_to_class('idMPer',models.CharField(max_length=30))
User.add_to_class('tipoUsuario',models.CharField(max_length=2,choices=TIPO_USUARIO))
User.add_to_class('fecIngreso',models.DateField(default='2014-01-01'))
User.add_to_class('idMCli',models.CharField(max_length=30, default='0', blank=True))



ESTADO_REGISTRO = (
		('0','No Activo'),
		('1','Activo'),
	)

class MTabla(models.Model):
	IdMTabla = models.CharField(max_length=4, blank= True,primary_key=True)
	NomMTabla = models.CharField(max_length=80, blank= True)
	AbrMTabla = models.CharField(max_length=5, blank= True)
	PropMTabla = models.CharField(max_length=2, blank= True)
	EstMTabla = models.CharField(max_length=2, blank= True, choices=ESTADO_REGISTRO)

	def __unicode__(self):
		return '%s - %s' %(self.IdMTabla, self.NomMTabla)

	def get_nombreCampos(self):
		lstcab = ('Cód.','Descripción','Abreviatura','Prop',
			'Estado')
		return lstcab

	def natural_key(self):
		return '%s' %(self.NomMTab)

class DTabla(models.Model):
	IdDTab = models.CharField(max_length=5, blank= True, verbose_name="Código")
	IdMTab = models.ForeignKey(MTabla,db_column='idMTabla', verbose_name="Tabla Maestro")
	NomDTab = models.CharField(max_length=80, blank= True, verbose_name="Nombre")
	AbrDTab = models.CharField(max_length=5, null=True, blank= True, verbose_name="Abreviatura")
	AbrOpDTab = models.CharField(max_length=5, null=True, blank= True, verbose_name="Abreviatura Opcional")
	FactDTab = models.IntegerField(blank= True, verbose_name="Factor")
	IndDTab = models.IntegerField(blank= True, verbose_name="Ind")
	IdRefDTab = models.CharField(max_length=5, blank= True,verbose_name="Referencia")
	PropDTab = models.CharField(max_length=2,blank=True, verbose_name="Prop")
	EstDTab = models.CharField(max_length=2, blank= True, choices=ESTADO_REGISTRO)

	def __unicode__(self):
		return '%s' %(self.NomDTab)

	def get_nombreCampos(self):
		lstcab = ('Cód.','Nombre','Abreviatura',
			'Perteneca a','Requerido')
		return lstcab

	def natural_key(self):
		return '%s' %(self.NomDTab)

class MPersonal(models.Model):
	IdMPer = models.CharField(max_length=30,verbose_name="Codigo", primary_key=True)
	ApePMPer = models.CharField(max_length=80, verbose_name= "Apellido Paterno", blank= True)
	ApeMMPer = models.CharField(max_length=80, verbose_name= "Apellido Materno", blank= True)
	NomMPer = models.CharField(max_length=80, verbose_name= "Nombres", blank= True)
	FechNacMPer = models.DateField(verbose_name= "Fecha de Nacimiento", blank= True)
	IdTipPerMPer = models.CharField(max_length=5, verbose_name="Tipo Personal", blank= True)
	IdTipDocMPer = models.CharField(max_length=5, verbose_name="Tipo Documento", blank= True)
	NDocMPer = models.CharField(max_length=20, verbose_name="Numero de Documento", blank= True)
	EstMPer	= models.CharField(max_length=2, blank= True, choices=ESTADO_REGISTRO)
	FecIngMPer = models.DateField(verbose_name="Fecha de Ingreso", blank= True)
	Tel1MPer = models.CharField(max_length=20, blank=True,verbose_name="Telefono 1",)
	Tel2MPer = models.CharField(max_length=20, blank=True, verbose_name="Telefono 2(Opc)")
	Email1MPer = models.EmailField(max_length=254, blank=True, verbose_name="Email 1")
	Email2MPer = models.EmailField(max_length=254, blank=True, verbose_name="Email 2(Opc)")
	IdArea = models.CharField(max_length=5, verbose_name="Area", blank= True)
	def __unicode__(self):
		return '%s %s' %(self.NomMPer, self.ApePMPer)

	def get_nombreCampos(self):
		lstcab = ('Cód.','Apellidos y Nombres','F. de Nacim.',
			'Tipo de Pers.','Tipo de Doc.','Num. Doc.','Estado','F. de Ingreso')
		return lstcab

	def natural_key(self):
		return '%s %s' %(self.NomMPer, self.ApePMPer)

class MCliente(models.Model):
	IdMCli = models.CharField(max_length=30, verbose_name="Código",primary_key= True)
	NomMCli= models.CharField(max_length=300, blank= True, verbose_name="Nombre",null=True)
	IdTipMCli = models.CharField(max_length=5, blank= True, verbose_name="Tipo",null=True) # puede ser foreingKey
	IdTipInstMCli = models.CharField(max_length=5, blank= True, verbose_name="Tip. Insitución",null=True)
	DirMCli = models.CharField(max_length=100, blank= True, verbose_name="Dirección",null=True)
	IdPaisMCli = models.CharField(max_length=5, blank= True, verbose_name="País",null=True)
	IdRegMCli = models.CharField(max_length=5, blank= True, verbose_name="Región",null=True)
	IdDepMCli = models.CharField(max_length=5, blank= True, verbose_name="Departamento",null=True)
	IdProvMCli = models.CharField(max_length=5, blank= True, verbose_name="Provincia",null=True)
	IdDistMCli = models.CharField(max_length=5, blank= True, verbose_name="Distrito",null=True)
	RefMCli = models.CharField(max_length=200, blank= True, verbose_name="Referencia",null=True)
	Tel1MCli = models.CharField(max_length=20, blank= True, verbose_name="Teléfono 1",null=True)
	Tel2MCli = models.CharField(max_length=20, blank= True, verbose_name="Teléfono 2",null=True)
	Tel3MCli = models.CharField(max_length=20, blank= True, verbose_name="Teléfono 3",null=True)
	Email1MCli = models.EmailField(max_length=300, blank=True, verbose_name="Email Institucional",null=True)
	FecIngMCli = models.DateField(blank= True, verbose_name="Fecha de Ingreso",null=True)
	EstMCli = models.CharField(max_length=2, blank= True, choices=ESTADO_REGISTRO)

	def __unicode__(self):
		return '%s - %s' %(self.IdMCli, self.NomMCli)

	def get_nombreCampos(self):
		lstcab = ('COD','NOMBRE','TIPO','Instución','Dirección',
			'Región-Departamento-Provincia-Distrito','Referencia','Telefono Ref.')
		return lstcab
	def natural_key(self):
		return '%s' %(self.NomMCli)

class MProyecto(models.Model):

	def urlPdf(self, filename):
		ruta = 'protocolos/%s.pdf' %(self.IdMProy)
		return ruta

	def urlOcr(self, filename):
		ruta = 'ocr/%s.pdf' %(self.IdMProy)
		return ruta

	def urlPDFAC(self, filename):
		ruta = 'acPdf/%s.pdf' %(self.IdMProy)
		return ruta

	def urlOCRAC(self, filename):
		ruta = 'acOcr/%s.pdf' %(self.IdMProy)
		return ruta

	def urlPdfConv(self, filename):
		ruta = 'convPdf/%s.pdf' %(self.IdMProy)
		return ruta

	def urlOcrConv(self, filename):
		ruta = 'convOcr/%s.pdf' %(self.IdMProy)
		return ruta


	IdMProy = models.CharField(max_length=30, verbose_name="Código",primary_key= True)
	IdMCli = models.ForeignKey(MCliente,db_column='IdMCli', verbose_name="Cliente", null=True, blank=True)
	NomMProy = models.CharField(max_length=700, blank= True, verbose_name="Nombre", null=True)
	FecEntMProy = models.DateField(blank= True, verbose_name="Fecha de Entrega" , null=True)
	FecEntRealMProy = models.DateField(blank= True, verbose_name="Fecha de Entrega Real", null=True)
	FecIniMProy = models.DateField(blank= True, verbose_name="Fecha de Inicio" , null=True)
	FecIniRealMProy = models.DateField(blank= True, verbose_name="Fecha de Inicio Real", null=True)
	FecFinMProy = models.DateField(blank= True, verbose_name="Fecha Fin", null=True)
	FecFinRealMProy = models.DateField(blank= True, verbose_name="Fecha Fin Real",null=True)
	MontInvCliMProy = models.DecimalField(max_digits=15, decimal_places=2, blank= True, verbose_name="Inversión Cliente", null=True, default=0)
	MontInvFipMProy = models.DecimalField(max_digits=15, decimal_places=2, blank= True,verbose_name="Inversión FIP", null=True, default=0)
	MontTotMProy = models.DecimalField(max_digits=15, decimal_places=2, blank= True, verbose_name="Inversión Total", null=True, default=0)
	MontTInvRealCliMProy = models.DecimalField(max_digits=15, decimal_places=2, blank= True, verbose_name="Inversión Real Cliente", null=True, default=0)
	MontTInvRealFipMProy = models.DecimalField(max_digits=15, decimal_places=2, blank= True, verbose_name="Inversión Real FIP", null=True, default=0)
	MontTInvRealOtrMProy = models.DecimalField(max_digits=15, decimal_places=2, blank= True, verbose_name="Inversión Real Asociados", null=True, default=0)
	MontTotRealMProy = models.DecimalField(max_digits=15, decimal_places=2, blank= True, verbose_name="Inversión Real Total", null=True, default=0)
	IdTipProMProy = models.CharField(max_length=5, blank= True, verbose_name = "Tipo Proyecto", null=True,default='0')
	EstMProy = models.CharField(max_length=2,blank= True, verbose_name="Activo", null=True) 
	FecIngMProy = models.DateField(blank= True, verbose_name="Fecha de Ingreso", null=True)
	IdEstMProy = models.CharField(max_length=5, blank= True, verbose_name="Estado", null=True,default='0') 
	IdSector = models.CharField(max_length=5,blank=True, verbose_name="Sector", null=True,default='0')
	IdBanco = models.CharField(max_length=5,blank=True, verbose_name="Banco", null=True,default='0')
	NumCtaInterMProy = models.CharField(max_length=50, blank=True, verbose_name="Cuenta Corriente", null=True)
	MontTotAdeCliMProy = models.DecimalField(max_digits=15, decimal_places=2, blank=True, verbose_name="Monto Adendas Cliente", null=True, default=0)
	MontTotAdeFipMProy = models.DecimalField(max_digits=15, decimal_places=2, blank=True, verbose_name="Monto Adendas FIP", null=True, default=0)
	MontTotAdeOtrMProy = models.DecimalField(max_digits=15, decimal_places=2, blank=True, verbose_name="Monto Adendas Asociados", null=True, default=0)
	MontTotAdeTotMProy = models.DecimalField(max_digits=15, decimal_places=2, blank=True, verbose_name="Monto Total Adendas", null=True, default=0)
	IdConv = models.CharField(max_length=5, blank=True, verbose_name="Convocatoria", null=True)
	TiempoMProy = models.CharField(max_length=50, blank=True, verbose_name="Tiempo", null=True)
	PorcTotAdeMProy = models.DecimalField(max_digits=5, decimal_places=2, blank=True, verbose_name="Porcentaje de Adelanto", null=True)
	RutaPDFMProy = models.FileField(upload_to= urlPdf, verbose_name="PDF PROYECTO", null=True, blank=True)
	RutaPDFConvMProy = models.FileField(upload_to= urlPdfConv, verbose_name="PDF PROYECTO", null=True, blank=True)
	RutaOCRConvMProy = models.FileField(upload_to= urlOcrConv, verbose_name="PDF PROYECTO", null=True, blank=True)
	RutaOCRMProy = models.FileField(upload_to= urlOcr, verbose_name="OCR PROYECTO", null=True, blank=True)
	RutaPDFACMProy = models.FileField(upload_to= urlPDFAC, verbose_name="PDF AC", null=True, blank=True)
	RutaOCRACMProy = models.FileField(upload_to= urlOCRAC, verbose_name="OCR AC", null=True, blank=True)
	EstCierreMProy = models.CharField(max_length=2, blank= True, choices=ESTADO_REGISTRO)


	def __unicode__(self):
		return '%s - %s' %(self.IdMProy, self.NomMProy)

	def get_nombreCampos(self):
		lstcab = ('Cod.','Nombre','Unidad Ejecutora',
			'Fech. Inicio','Fech. FIn','Fech. Entrega')
		return lstcab

	def natural_key(self):
		return '%s' %(self.NomMProy)

class MProtocolo(models.Model):
	DOC_INTER = (
		('0','INTERNO'),
		('1','EXTERNO'),
	)

	IdMProt = models.CharField(max_length=30, verbose_name="Código",primary_key= True)
	IdMProy = models.ForeignKey(MProyecto,db_column='IdMProy', verbose_name="Convenio", blank=True, null=True)
	IdMCli = models.CharField(max_length=30, verbose_name="Cliente", blank = True)
	NomMProt = models.CharField(max_length=100, blank= True, verbose_name="Nombre")
	DescMProt = models.CharField(max_length=300, blank= True, verbose_name="Descripción")
	FecEntMProt = models.DateField(blank= True, verbose_name="Fecha de Entrega")
	FecEntRealMProt = models.DateField(blank= True, verbose_name="Fecha de Entrega Real")
	IdTipFormEntMProt = models.CharField(max_length=5,blank= True, verbose_name="Formato de Entrega") # Puede ser digital, fisico o ambos
	IdRefMProt = models.CharField(max_length=30, blank= True, verbose_name="Referencia")
	IdTipDocGen = models.CharField(max_length=5,blank= True, verbose_name="Documento Generado") # Informe, etc
	EstMProt = models.CharField(max_length=2, blank= True, choices=ESTADO_REGISTRO)
	DocInter = models.CharField(max_length=2, blank= True, choices=DOC_INTER)

	def __unicode__(self):
		return '%s - %s' %(self.IdMProt, self.NomMProt)

	def get_nombreCampos(self):
		lstcab = ('Cód.','Nombre','Descripción',
			'Fec. Entrega','F. Ent. Real','Formato','Estado')
		return lstcab
	def natural_key(self):
		return '%s' %(self.NomMProt)

class DProtocolo(models.Model):
	
	def urlPdf(self, filename):
		ruta = 'protocolos/%s.pdf' %(self.IdDProt)
		#ruta = 'protocolos/%s' %(filename)
		return ruta

	def urlOcr(self, filename):
		#ruta = 'ocr/%s' %(self.idDProt)
		ruta = 'ocr/%s' %(filename)
		return ruta


	IdDProt = models.CharField(max_length=35, verbose_name="Código",primary_key= True)
	IdMProt = models.ForeignKey(MProtocolo,db_column='IdMProt', verbose_name="Protocolo")
	NomDProt = models.CharField(max_length=100, blank= True, verbose_name="Nombre")
	IdTipDocDProt = models.CharField(max_length=5, blank= True, verbose_name="Tipo Documento")
	UbLogDProt = models.CharField(max_length=5, blank= True, verbose_name="Ubicación Lógica")
	UbiFisDProt = models.CharField(max_length=5, blank= True, verbose_name="Ubicación Física")
	IdPerDProt = models.CharField(max_length=30, blank= True, verbose_name="Persona que tiene documento físico") #Se ingresa solo en caso de fisicos
	RutaPdfDProt = models.FileField(upload_to= urlPdf, verbose_name="Ruta PDF", null = True, blank=True)
	RutaOcrDProt = models.FileField(upload_to= urlOcr, verbose_name="Ruta OCR", null = True, blank= True)
	EstDProt = models.CharField(max_length=2, blank= True, choices=ESTADO_REGISTRO)

	def __unicode__(self):
		return '%s' %(self.NomDProt)

	def get_nombreCampos(self):
		lstcab = ('Cód.','Nombre','PDF')
		return lstcab

	def natural_key(self):
		return '%s' %(self.NomDProt)

class DProyecto(models.Model):

	def urlPdf(self, filename):
		ruta = 'adendasPDF/%s.pdf' %(self.IdDProy)
		return ruta

	def urlOcr(self, filename):
		ruta = 'adendasOCR/%s.txt' %(self.IdDProy)
		return ruta

	IdDProy = models.CharField(max_length=30, verbose_name="Código",primary_key= True)
	IdMProy = models.ForeignKey(MProyecto,db_column='IdMProy', verbose_name="Proyecto")
	FecIniDProy = models.DateField(blank= True, verbose_name="Fecha de Inicio")
	FecFinDProy = models.DateField(blank= True, verbose_name="Fecha Final")
	FecFirmaDProy = models.DateField(blank= True, verbose_name="Fecha de Firma")
	MontAportFIPDProy = models.DecimalField(max_digits=15, decimal_places=2, blank= True, verbose_name="Aporte FIP")
	MontAportCliDProy = models.DecimalField(max_digits=15, decimal_places=2, blank= True, verbose_name="Aporte Cliente")
	MontAportOtrDProy = models.DecimalField(max_digits=15, decimal_places=2, blank= True, verbose_name="Aporte Asociados")
	IdTipDocDProy = models.CharField(max_length=5, blank=True, null= True, verbose_name="Tipo de documento")
	DescDProy = models.CharField(max_length=200, blank=True, null= True, verbose_name="Descripción")
	RutaPDFDProy = models.FileField(upload_to= urlPdf, verbose_name="Ruta PDF", blank=True, null=True)
	RutaOcrDProy =  models.FileField(upload_to= urlOcr, verbose_name="Ruta OCR", blank=True, null=True)
	EstDProy = models.CharField(max_length=2, blank= True, choices=ESTADO_REGISTRO)
	def __unicode__(self):
		return '%s' %(self.IdDProy)

	def get_nombreCampos(self):
		lstcab = ('Cód.','Descripción','Fec. Firma','Inv. FIP.',
			'Inv. U.E.','PDF.')
		return lstcab
	def natural_key(self):
		return '%s' %(self.DescDProy)

class MColaborador(models.Model):
	
	def urlPdf(self, filename):
		ruta = 'colaborador/%s.pdf' %(filename)
		return filename

	def urlOcr(self, filename):
		ruta = 'ocr/%s.txt' %(filename)
		return ruta

	IdMPer = models.ForeignKey(MPersonal,db_column='IdMPer',verbose_name="Personal", blank = True, null = True)
	IdMProy = models.ForeignKey(MProyecto,db_column='IdMProy',verbose_name="Proyecto", blank = True, null = True)
	IdTipoCargoProy = models.CharField(max_length=5, blank=True, verbose_name="Cargo", null = True)
	FecIniMCol = models.DateField(blank=True, verbose_name="Fecha de Inicio", null=True,default=datetime.datetime.today())
	FecFinMCol = models.DateField(blank=True, verbose_name="Fecha Final", null=True,default=datetime.datetime.today())
	FecFirmaMCol = models.DateField(blank=True, verbose_name="Fecha Firma", null=True,default=datetime.datetime.today())
	TiempoMCol = models.CharField(max_length=50, blank=True, verbose_name="Tiempo", null=True,default=0)
	MontoMCol = models.DecimalField(max_digits=15, decimal_places=2, blank= True, verbose_name="Pago Total", null=True,default=0)
	MontoMenMCol = models.DecimalField(max_digits=15, decimal_places=2, blank= True, verbose_name="Pago Mensual", null=True,default=0)
	EstMCol = models.CharField(max_length=2, blank = True, verbose_name="Activo", null=True)
	EstActMCol = models.CharField(max_length=2, blank= True, verbose_name="Estado actual", null=True)
	RutaPDFMCol = models.FileField(upload_to= urlPdf, verbose_name="Ruta PDF", blank= True, null=True)
	RutaOCRMCol = models.FileField(upload_to= urlOcr, verbose_name="Ruta OCR", blank = True, null = True)
	
	def __unicode__(self):
		return '%s' %(self.IdMPer)

	def get_nombreCampos(self):
		lstcab = ('Cód.','Apellidos y Nombres','Cargo','Inicio',
			'Fin','Inversión', 'PDF')
		return lstcab

	def natural_key(self):
		return '%s' %(self.IdMPer.NomMPer)

class MUsuarioDer(models.Model):
	IdUsuOri = models.CharField(max_length=5, blank=True)
	IdUsuDer = models.CharField(max_length=5, blank= True)
	EstDer = models.CharField(max_length=2, blank= True, choices=ESTADO_REGISTRO)

	def __unicode__(self):
		return '%s' %(self.IdUsuDer)

	def get_nombreCampos(self):
		lstcab = ('Usuario Origen','Usuario a Derivar')
		return lstcab

class Bandeja(models.Model):
	IdBandeja = models.CharField(max_length=50, verbose_name = "Código",primary_key= True)
	IdMUsuEnv = models.CharField(max_length=5, verbose_name="Enviado Por")
	IdMUsuRec =models.CharField(max_length=5, verbose_name="Recibido Por")
	IdMProt = models.CharField(max_length=30, blank= True, verbose_name="Protocolo")
	NomMUsuEnv = models.CharField(max_length=50, blank=True, verbose_name="Usuario Envio")
	NomMUsuRec = models.CharField(max_length=50,blank=True,verbose_name="Usuario Recepcion")
	CliBProt = models.CharField(max_length=500,blank=True, verbose_name="Cliente")
	ProyBProt = models.CharField(max_length=500,blank=True, verbose_name="Proyecto")
	FecEnv = models.DateField(blank= True, verbose_name="Fecha de Envio")
	FecRec = models.DateField(blank= True, verbose_name="Fecha de Recepción")
	FecSist = models.DateField(blank= True, verbose_name="Fecha del sistema")
	MenBProt = models.CharField(max_length=400, blank= True, verbose_name="Mensaje")
	EstBProt = models.CharField(max_length=2, blank= True, verbose_name="Activo")
	EstAccion = models.CharField(max_length=6, blank= True, verbose_name="Acción")
	EstObservado = models.CharField(max_length=2, blank= True, verbose_name="Observado")
	ObsProt = models.CharField(max_length=200, blank= True, verbose_name="Observación")
	IdProtRef = models.CharField(max_length=30, blank= True, verbose_name="Referencia")

	def __unicode__(self):
		return 'Recibido por %s, enviado por %s-%s, IdBandeja %s' %(self.IdMUsuRec, self.IdMUsuEnv, self.NomMUsuEnv, self.IdBandeja)

	def get_nombreCampos(self):
		lstcab = ('Protocolo','Convenio','Und. Ejecutora','Enviado Por','Fecha','Referencia')
		return lstcab

	def natural_key(self):
		return '%s' %(self.IdMUsuEnv.username,self.IdMUsuRec.username)

class CClientes(models.Model):
	IdCCli = models.CharField(max_length=30, verbose_name="Codigo",primary_key= True)
	IdMCli = models.ForeignKey(MCliente,db_column='IdMCli', blank=True, verbose_name="Codigo Cliente")
	ApePCCli = models.CharField(max_length=80, blank=True, verbose_name="Apellido Paterno")
	ApeMCCli = models.CharField(max_length=80, blank=True, verbose_name="Apellido Materno")
	NomCCli = models.CharField(max_length=80, blank=True, verbose_name="Nombres")
	IdTipDocCCli = models.CharField(max_length=5, blank=True, verbose_name="Tipo de Documento")
	NumDocCCli = models.CharField(max_length=20, blank=True, verbose_name="Numero de Documento")
	EstCCli = models.CharField(max_length=2,blank=True, verbose_name="Activo")
	Tel1CCli = models.CharField(max_length=20, blank=True, verbose_name="Telefono 1")
	Tel2CCli = models.CharField(max_length=20, blank=True, verbose_name="Telefono 2(opc)")
	Email1CCli = models.EmailField(max_length=254, blank=True, verbose_name="Email 1")
	Email2CCli = models.EmailField(max_length=254, blank=True, verbose_name="Email 2(Opc)")

	def __unicode__(self):
		return '%s - %s -%s ' %(self.IdMCli, self.IdCCli, self.NomCCli)

class SClientes(models.Model):
	IdSCli = models.CharField(max_length=30, verbose_name="Codigo",primary_key= True) 
	IdMCli = models.ForeignKey(MCliente,db_column='IdMCli',max_length=30, blank=True, verbose_name="Codigo Cliente")
	NomSCli = models.CharField(max_length=100, blank=True, verbose_name="Nombre")
	IdTipSCli = models.CharField(max_length=5, blank=True, verbose_name="Tipo")
	DirSCli = models.CharField(max_length=100, blank=True, verbose_name="Direccion")
	IdPaisSCli = models.CharField(max_length=5, blank=True, verbose_name="Pais")
	IdRegSCli = models.CharField(max_length=5, blank=True, verbose_name="Region")
	IdDepSCli = models.CharField(max_length=5, blank=True, verbose_name="Departamento")
	IdProvSCli = models.CharField(max_length=5, blank=True, verbose_name="Provincia")
	IdDistSCli = models.CharField(max_length=5, blank=True, verbose_name="Distrito")
	RefSCli = models.CharField(max_length=200, blank=True, verbose_name="Referencia")
	Tel1SCli = models.CharField(max_length=20, blank=True, verbose_name="Telefono 1")
	Tel2SCli = models.CharField(max_length=20, blank=True, verbose_name="Telefono 2(opc)")
	Tel3SCli = models.CharField(max_length=20, blank=True, verbose_name="Telefono 3(opc)")
	Email1SCli = models.EmailField(max_length=254, blank=True, verbose_name="Email")

	def __unicode__(self):
		return '%s %s' %(self.IdSCli, self.NomSCli)

class PProyectos(models.Model):
	IdPProy = models.CharField(max_length=30, primary_key= True, verbose_name="Codigo del Presupuesto", help_text="Ingrese codigo del presupuesto")
	IdMProy = models.ForeignKey(MProyecto, blank=True, null=True, verbose_name="Seleccione Convenio", help_text="Seleccione el convenio")
	NroPartPProy = models.CharField(max_length=40, blank=True, null=True, verbose_name="Numero de Partida", help_text="Ingrese el numero de partida")	
	IdNivPartPProy	= models.CharField(max_length=4, blank=True, null=True, verbose_name="Nivel de Partido", help_text="Seleccione el  nivel de partida")
	DescPProy = models.CharField(max_length=300, blank=True, null=True, verbose_name="Descripcion de la partida", help_text="Ingrese la descripción de la partida")
	TitPProy = models.CharField(max_length=300, blank=True, null=True, verbose_name="Descripcion de la partida", help_text="Ingrese el título de la partida")
	NroPartPerPProy = models.CharField(max_length=40, blank=True, null= True, verbose_name="Pertenece a ", help_text="Seleccione a que partida pertenece")
	IdUnidMed = models.CharField(max_length=4, blank=True, null=True, verbose_name="Unidad de medida", help_text="Seleccione unidad de medida")
	CantPProy = models.IntegerField(blank=True, null=True, verbose_name="Cantidad", help_text="Ingrese la cantidad")
	CostUnitPProy = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, verbose_name="Cantidad", help_text="Ingrese la cantidad")
	CostTotPProy = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null= True, verbose_name="Costo total",help_text="Costo total")
	FFFipPProy = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True,verbose_name="Financiamiento FIP",help_text="Financiamiento FIP")
	FFCliPProy = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, verbose_name="Financiamiento UE", help_text="Financiamiento UE")
	FFOtrosPProy = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null = True, verbose_name="Financiamiento Otros", help_text="Financiamiento Otros")
	PFFFipPProy = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True,verbose_name="Porcentaje Financiamiento FIP",help_text="Porcentaje Financiamiento FIP")
	PFFCliPProy = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, verbose_name="Porcentaje Financiamiento UE", help_text="Porcentaje Financiamiento UE")
	PFFOtrosPProy = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null = True, verbose_name="Porcentaje Financiamiento Otros", help_text="Porcentaje Financiamiento Otros")
	FinPProy = models.IntegerField(blank=True, null= True, verbose_name="", help_text="")
	VerPProy = models.IntegerField(blank=True, null= True, verbose_name="Versión", help_text="Versión")
	EstPProy = models.CharField(max_length=2,blank=True, null=True, verbose_name="Estado",help_text="Estado")
	FecIngPProy = models.DateField(blank=True, null=True, verbose_name="Fecha de Ingreso", help_text="Fecha de ingreso")
	IdUsuCreaPProy = models.CharField(max_length=30, blank=True, null=True, verbose_name="Creado por", help_text="Creado por")
	FecModPProy = models.DateField(blank=True, null=True, verbose_name="Fecha de modificacion", help_text="Fecha de modificacion")
	IdUsuModPProy = models.CharField(max_length=30, blank=True, null=True, verbose_name="Modificado por", help_text="Modificado por")
	CostEjePProy = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, verbose_name="Costo de ejecución", help_text="Ingrese el costo de ejecución")
	CostSalPProy = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, verbose_name="Saldo de la ejecución", help_text="Saldo de la ejecución")
	IdMotCierrePProy = models.CharField(max_length=4, blank=True, null=True, verbose_name="Motivo de cierre", help_text="Seleccione el motivo de cierre")
	PorcCostEjePProy = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Porcentaje de Costo de ejecución", help_text="Porcentaje de costo de ejecución")
	BorradorPProy = models.CharField(max_length=2, blank=True, null=True, verbose_name="Borrado", help_text="Borrador")
	EstPresPProy = models.CharField(max_length=2, blank=True, null=True, verbose_name="Estado", help_text="Estado")
	EstEvalPProy = models.CharField(max_length=2, blank=True, null=True, verbose_name="Estado", help_text="Estado")
	EstValidPProy = models.CharField(max_length=2, blank=True, null=True, verbose_name="Estado", help_text="Estado")
	EstAprobPProy = models.CharField(max_length=2, blank=True, null=True, verbose_name="Estado", help_text="Estado")
	EstModPProy = models.CharField(max_length=2, blank=True, null=True, verbose_name="Estado", help_text="Estado")

	def __unicode__(self):
		return '%s - %s' %(self.IdPProy, self.NroPartPProy)

class CargaPresupuesto(models.Model):
	def urlExcel(self, filename):
		ruta = 'presup/%s' %(filename)
		return ruta
	doc_temp = models.FileField(upload_to= urlExcel, verbose_name="Seleccionar Archivo", blank= True, null=True)

class CPProyectos(models.Model):
	IdCPProy = models.AutoField(primary_key=True)
	IdPProy = models.ForeignKey(PProyectos, blank= True, null= True, verbose_name="Proyecto", help_text="Proyecto")
	MesCPProy = models.IntegerField(blank= True, null= True, verbose_name="Mes nro", help_text="Mes nro")
	MesCCPProy = models.IntegerField(blank= True, null= True, verbose_name="Mes correlativo", help_text="Mes correlativo")
	AnioCCPProy = models.IntegerField(blank= True, null= True, verbose_name="Año correlativo", help_text="Año correlativo")
	MontoEjeCPProy = models.DecimalField(max_digits=15, decimal_places=2, blank= True, null= True, verbose_name="Monto ejecutado", help_text="Monto ejecutado")
	PorcEjeCProy = models.DecimalField(max_digits=15, decimal_places=2, blank= True, null=True, verbose_name="Porcentaje", help_text="Porcentaje")
	VerCProy = models.IntegerField(blank= True, null= True, verbose_name="Versión", help_text="Versión")
	SVerCProy = models.IntegerField(blank= True, null= True, verbose_name="S. Versión", help_text="S. Versión")
	EstCProy = models.CharField(max_length=2, blank= True, null= True, verbose_name="Estado", help_text="Estado")
	EstModifCProy = models.CharField(max_length=2, blank= True, null= True, verbose_name="Estado modificación", help_text="Estado modificación")
	MontoEjeFipCPProy = models.DecimalField(max_digits=15, decimal_places=2, blank= True, null= True, verbose_name="Monto ejecutado Fip")
	PorcEjeFipCPProy = models.DecimalField(max_digits=6, decimal_places=2, blank= True, null= True, verbose_name="Porc. ejecutado Fip")
	MontoEjeCliCPProy = models.DecimalField(max_digits=15, decimal_places=2, blank= True, null= True, verbose_name="Monto ejecutado UE")
	PorcEjeCliCPProy = models.DecimalField(max_digits=6, decimal_places=2, blank= True, null= True, verbose_name="Porc. ejecutado UE")
	MontoRealCPProy = models.DecimalField(max_digits=15, decimal_places=2, blank= True, null= True, verbose_name="Monto ejecutado Real")
	PorcRealCPProy = models.DecimalField(max_digits=6, decimal_places=2, blank= True, null= True, verbose_name="Porc. ejecutado Real")
	MontoRealFipCPProy = models.DecimalField(max_digits=15, decimal_places=2, blank= True, null= True, verbose_name="Monto ejecutado Real Fip")
	PorcRealFipCPProy = models.DecimalField(max_digits=6, decimal_places=2, blank= True, null= True, verbose_name="Porc. ejecutado Real Fip")
	MontoRealCliCPProy = models.DecimalField(max_digits=15, decimal_places=2, blank= True, null= True, verbose_name="Monto ejecutado Real UE")
	PorcRealCliCPProy = models.DecimalField(max_digits=6, decimal_places=2, blank= True, null= True, verbose_name="Porc. ejecutado Real UE")
	MontoDifEjecRealCPProy = models.DecimalField(max_digits=15, decimal_places=2, blank= True, null= True, verbose_name="Dif Monto ejecutado Real")
	PorcDifEjecRealCPProy = models.DecimalField(max_digits=6, decimal_places=2, blank= True, null= True, verbose_name="Dif Porc. ejecutado Real")
	EstVisCPProy = models.CharField(max_length=2, blank= True, null= True, verbose_name="Estado", help_text="Estado")

	def __unicode__(self):
		return 'Proyecto:%s | Partida: %s | Mes: %s| MesC: %s | MontoFip: %s | MontoUE: %s |' %(self.IdPProy.IdPProy, self.IdPProy.NroPartPProy, self.MesCPProy, self.MesCCPProy, self.MontoRealFipCPProy, self.MontoRealCliCPProy  )



