# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MTabla'
        db.create_table(u'tramiteDoc_mtabla', (
            ('IdMTabla', self.gf('django.db.models.fields.CharField')(max_length=4, primary_key=True)),
            ('NomMTabla', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('AbrMTabla', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('PropMTabla', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('EstMTabla', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
        ))
        db.send_create_signal(u'tramiteDoc', ['MTabla'])

        # Adding model 'DTabla'
        db.create_table(u'tramiteDoc_dtabla', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('IdDTab', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('IdMTab', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tramiteDoc.MTabla'], db_column='idMTabla')),
            ('NomDTab', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('AbrDTab', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('AbrOpDTab', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('FactDTab', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('IndDTab', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('IdRefDTab', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('PropDTab', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('EstDTab', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
        ))
        db.send_create_signal(u'tramiteDoc', ['DTabla'])

        # Adding model 'MPersonal'
        db.create_table(u'tramiteDoc_mpersonal', (
            ('IdMPer', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key=True)),
            ('ApePMPer', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('ApeMMPer', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('NomMPer', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('FechNacMPer', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('IdTipPerMPer', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('IdTipDocMPer', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('NDocMPer', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('EstMPer', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('FecIngMPer', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('Tel1MPer', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('Tel2MPer', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('Email1MPer', self.gf('django.db.models.fields.EmailField')(max_length=254, blank=True)),
            ('Email2MPer', self.gf('django.db.models.fields.EmailField')(max_length=254, blank=True)),
            ('IdArea', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
        ))
        db.send_create_signal(u'tramiteDoc', ['MPersonal'])

        # Adding model 'MCliente'
        db.create_table(u'tramiteDoc_mcliente', (
            ('IdMCli', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key=True)),
            ('NomMCli', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('IdTipMCli', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('IdTipInstMCli', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('DirMCli', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('IdPaisMCli', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('IdRegMCli', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('IdDepMCli', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('IdProvMCli', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('IdDistMCli', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('RefMCli', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('Tel1MCli', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('Tel2MCli', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('Tel3MCli', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('Email1MCli', self.gf('django.db.models.fields.EmailField')(max_length=300, null=True, blank=True)),
            ('FecIngMCli', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('EstMCli', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
        ))
        db.send_create_signal(u'tramiteDoc', ['MCliente'])

        # Adding model 'MProyecto'
        db.create_table(u'tramiteDoc_mproyecto', (
            ('IdMProy', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key=True)),
            ('IdMCli', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tramiteDoc.MCliente'], null=True, db_column='IdMCli', blank=True)),
            ('NomMProy', self.gf('django.db.models.fields.CharField')(max_length=700, null=True, blank=True)),
            ('FecEntMProy', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('FecEntRealMProy', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('FecIniMProy', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('FecIniRealMProy', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('FecFinMProy', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('FecFinRealMProy', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('MontInvCliMProy', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=15, decimal_places=2, blank=True)),
            ('MontInvFipMProy', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=15, decimal_places=2, blank=True)),
            ('MontTotMProy', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=15, decimal_places=2, blank=True)),
            ('MontTInvRealCliMProy', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=15, decimal_places=2, blank=True)),
            ('MontTInvRealFipMProy', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=15, decimal_places=2, blank=True)),
            ('MontTInvRealOtrMProy', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=15, decimal_places=2, blank=True)),
            ('MontTotRealMProy', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=15, decimal_places=2, blank=True)),
            ('IdTipProMProy', self.gf('django.db.models.fields.CharField')(default='0', max_length=5, null=True, blank=True)),
            ('EstMProy', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('FecIngMProy', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('IdEstMProy', self.gf('django.db.models.fields.CharField')(default='0', max_length=5, null=True, blank=True)),
            ('IdSector', self.gf('django.db.models.fields.CharField')(default='0', max_length=5, null=True, blank=True)),
            ('IdBanco', self.gf('django.db.models.fields.CharField')(default='0', max_length=5, null=True, blank=True)),
            ('NumCtaInterMProy', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('MontTotAdeCliMProy', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=15, decimal_places=2, blank=True)),
            ('MontTotAdeFipMProy', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=15, decimal_places=2, blank=True)),
            ('MontTotAdeOtrMProy', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=15, decimal_places=2, blank=True)),
            ('MontTotAdeTotMProy', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=15, decimal_places=2, blank=True)),
            ('IdConv', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('TiempoMProy', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('PorcTotAdeMProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('RutaPDFMProy', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('RutaPDFConvMProy', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('RutaOCRConvMProy', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('RutaOCRMProy', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('RutaPDFACMProy', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('RutaOCRACMProy', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('EstCierreMProy', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
        ))
        db.send_create_signal(u'tramiteDoc', ['MProyecto'])

        # Adding model 'MProtocolo'
        db.create_table(u'tramiteDoc_mprotocolo', (
            ('IdMProt', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key=True)),
            ('IdMProy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tramiteDoc.MProyecto'], null=True, db_column='IdMProy', blank=True)),
            ('IdMCli', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('NomMProt', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('DescMProt', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('FecEntMProt', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('FecEntRealMProt', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('IdTipFormEntMProt', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('IdRefMProt', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('IdTipDocGen', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('EstMProt', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('DocInter', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
        ))
        db.send_create_signal(u'tramiteDoc', ['MProtocolo'])

        # Adding model 'DProtocolo'
        db.create_table(u'tramiteDoc_dprotocolo', (
            ('IdDProt', self.gf('django.db.models.fields.CharField')(max_length=35, primary_key=True)),
            ('IdMProt', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tramiteDoc.MProtocolo'], db_column='IdMProt')),
            ('NomDProt', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('IdTipDocDProt', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('UbLogDProt', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('UbiFisDProt', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('IdPerDProt', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('RutaPdfDProt', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('RutaOcrDProt', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('EstDProt', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
        ))
        db.send_create_signal(u'tramiteDoc', ['DProtocolo'])

        # Adding model 'DProyecto'
        db.create_table(u'tramiteDoc_dproyecto', (
            ('IdDProy', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key=True)),
            ('IdMProy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tramiteDoc.MProyecto'], db_column='IdMProy')),
            ('FecIniDProy', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('FecFinDProy', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('FecFirmaDProy', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('MontAportFIPDProy', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2, blank=True)),
            ('MontAportCliDProy', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2, blank=True)),
            ('MontAportOtrDProy', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2, blank=True)),
            ('IdTipDocDProy', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('DescDProy', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('RutaPDFDProy', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('RutaOcrDProy', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('EstDProy', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
        ))
        db.send_create_signal(u'tramiteDoc', ['DProyecto'])

        # Adding model 'MColaborador'
        db.create_table(u'tramiteDoc_mcolaborador', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('IdMPer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tramiteDoc.MPersonal'], null=True, db_column='IdMPer', blank=True)),
            ('IdMProy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tramiteDoc.MProyecto'], null=True, db_column='IdMProy', blank=True)),
            ('IdTipoCargoProy', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('FecIniMCol', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 6, 3, 0, 0), null=True, blank=True)),
            ('FecFinMCol', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 6, 3, 0, 0), null=True, blank=True)),
            ('FecFirmaMCol', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 6, 3, 0, 0), null=True, blank=True)),
            ('TiempoMCol', self.gf('django.db.models.fields.CharField')(default=0, max_length=50, null=True, blank=True)),
            ('MontoMCol', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=15, decimal_places=2, blank=True)),
            ('MontoMenMCol', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=15, decimal_places=2, blank=True)),
            ('EstMCol', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('EstActMCol', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('RutaPDFMCol', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('RutaOCRMCol', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'tramiteDoc', ['MColaborador'])

        # Adding model 'MUsuarioDer'
        db.create_table(u'tramiteDoc_musuarioder', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('IdUsuOri', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('IdUsuDer', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('EstDer', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
        ))
        db.send_create_signal(u'tramiteDoc', ['MUsuarioDer'])

        # Adding model 'Bandeja'
        db.create_table(u'tramiteDoc_bandeja', (
            ('IdBandeja', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('IdMUsuEnv', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('IdMUsuRec', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('IdMProt', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('NomMUsuEnv', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('NomMUsuRec', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('CliBProt', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('ProyBProt', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('FecEnv', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('FecRec', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('FecSist', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('MenBProt', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('EstBProt', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('EstAccion', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('EstObservado', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('ObsProt', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('IdProtRef', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
        ))
        db.send_create_signal(u'tramiteDoc', ['Bandeja'])

        # Adding model 'CClientes'
        db.create_table(u'tramiteDoc_cclientes', (
            ('IdCCli', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key=True)),
            ('IdMCli', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tramiteDoc.MCliente'], db_column='IdMCli', blank=True)),
            ('ApePCCli', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('ApeMCCli', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('NomCCli', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('IdTipDocCCli', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('NumDocCCli', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('EstCCli', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('Tel1CCli', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('Tel2CCli', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('Email1CCli', self.gf('django.db.models.fields.EmailField')(max_length=254, blank=True)),
            ('Email2CCli', self.gf('django.db.models.fields.EmailField')(max_length=254, blank=True)),
        ))
        db.send_create_signal(u'tramiteDoc', ['CClientes'])

        # Adding model 'SClientes'
        db.create_table(u'tramiteDoc_sclientes', (
            ('IdSCli', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key=True)),
            ('IdMCli', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tramiteDoc.MCliente'], max_length=30, db_column='IdMCli', blank=True)),
            ('NomSCli', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('IdTipSCli', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('DirSCli', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('IdPaisSCli', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('IdRegSCli', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('IdDepSCli', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('IdProvSCli', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('IdDistSCli', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('RefSCli', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('Tel1SCli', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('Tel2SCli', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('Tel3SCli', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('Email1SCli', self.gf('django.db.models.fields.EmailField')(max_length=254, blank=True)),
        ))
        db.send_create_signal(u'tramiteDoc', ['SClientes'])

        # Adding model 'PProyectos'
        db.create_table(u'tramiteDoc_pproyectos', (
            ('IdPProy', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key=True)),
            ('IdMProy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tramiteDoc.MProyecto'], null=True, blank=True)),
            ('NroPartPProy', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('IdNivPartPProy', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('DescPProy', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('TitPProy', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('NroPartPerPProy', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('IdUnidMed', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('CantPProy', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CostUnitPProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('CostTotPProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('FFFipPProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('FFCliPProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('FFOtrosPProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('PFFFipPProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('PFFCliPProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('PFFOtrosPProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('FinPProy', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('VerPProy', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('EstPProy', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('FecIngPProy', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('IdUsuCreaPProy', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('FecModPProy', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('IdUsuModPProy', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('CostEjePProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('CostSalPProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('IdMotCierrePProy', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('PorcCostEjePProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('BorradorPProy', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('EstPresPProy', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('EstEvalPProy', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('EstValidPProy', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('EstAprobPProy', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('EstModPProy', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
        ))
        db.send_create_signal(u'tramiteDoc', ['PProyectos'])

        # Adding model 'CargaPresupuesto'
        db.create_table(u'tramiteDoc_cargapresupuesto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('doc_temp', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'tramiteDoc', ['CargaPresupuesto'])

        # Adding model 'CPProyectos'
        db.create_table(u'tramiteDoc_cpproyectos', (
            ('IdCPProy', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('IdPProy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tramiteDoc.PProyectos'], null=True, blank=True)),
            ('MesCPProy', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('MesCCPProy', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('AnioCCPProy', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('MontoEjeCPProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('PorcEjeCProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('VerCProy', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('SVerCProy', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('EstCProy', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('EstModifCProy', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('MontoEjeFipCPProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('PorcEjeFipCPProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('MontoEjeCliCPProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('PorcEjeCliCPProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('MontoRealCPProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('PorcRealCPProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('MontoRealFipCPProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('PorcRealFipCPProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('MontoRealCliCPProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('PorcRealCliCPProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('MontoDifEjecRealCPProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('PorcDifEjecRealCPProy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('EstVisCPProy', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
        ))
        db.send_create_signal(u'tramiteDoc', ['CPProyectos'])


    def backwards(self, orm):
        # Deleting model 'MTabla'
        db.delete_table(u'tramiteDoc_mtabla')

        # Deleting model 'DTabla'
        db.delete_table(u'tramiteDoc_dtabla')

        # Deleting model 'MPersonal'
        db.delete_table(u'tramiteDoc_mpersonal')

        # Deleting model 'MCliente'
        db.delete_table(u'tramiteDoc_mcliente')

        # Deleting model 'MProyecto'
        db.delete_table(u'tramiteDoc_mproyecto')

        # Deleting model 'MProtocolo'
        db.delete_table(u'tramiteDoc_mprotocolo')

        # Deleting model 'DProtocolo'
        db.delete_table(u'tramiteDoc_dprotocolo')

        # Deleting model 'DProyecto'
        db.delete_table(u'tramiteDoc_dproyecto')

        # Deleting model 'MColaborador'
        db.delete_table(u'tramiteDoc_mcolaborador')

        # Deleting model 'MUsuarioDer'
        db.delete_table(u'tramiteDoc_musuarioder')

        # Deleting model 'Bandeja'
        db.delete_table(u'tramiteDoc_bandeja')

        # Deleting model 'CClientes'
        db.delete_table(u'tramiteDoc_cclientes')

        # Deleting model 'SClientes'
        db.delete_table(u'tramiteDoc_sclientes')

        # Deleting model 'PProyectos'
        db.delete_table(u'tramiteDoc_pproyectos')

        # Deleting model 'CargaPresupuesto'
        db.delete_table(u'tramiteDoc_cargapresupuesto')

        # Deleting model 'CPProyectos'
        db.delete_table(u'tramiteDoc_cpproyectos')


    models = {
        u'tramiteDoc.bandeja': {
            'CliBProt': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'EstAccion': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'EstBProt': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'EstObservado': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'FecEnv': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'FecRec': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'FecSist': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'IdBandeja': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'IdMProt': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'IdMUsuEnv': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'IdMUsuRec': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'IdProtRef': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'MenBProt': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'Meta': {'object_name': 'Bandeja'},
            'NomMUsuEnv': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'NomMUsuRec': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ObsProt': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'ProyBProt': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        },
        u'tramiteDoc.cargapresupuesto': {
            'Meta': {'object_name': 'CargaPresupuesto'},
            'doc_temp': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'tramiteDoc.cclientes': {
            'ApeMCCli': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'ApePCCli': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'Email1CCli': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'blank': 'True'}),
            'Email2CCli': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'blank': 'True'}),
            'EstCCli': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'IdCCli': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'IdMCli': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tramiteDoc.MCliente']", 'db_column': "'IdMCli'", 'blank': 'True'}),
            'IdTipDocCCli': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'Meta': {'object_name': 'CClientes'},
            'NomCCli': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'NumDocCCli': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'Tel1CCli': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'Tel2CCli': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'tramiteDoc.cpproyectos': {
            'AnioCCPProy': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'EstCProy': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'EstModifCProy': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'EstVisCPProy': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'IdCPProy': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'IdPProy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tramiteDoc.PProyectos']", 'null': 'True', 'blank': 'True'}),
            'MesCCPProy': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'MesCPProy': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'CPProyectos'},
            'MontoDifEjecRealCPProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'MontoEjeCPProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'MontoEjeCliCPProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'MontoEjeFipCPProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'MontoRealCPProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'MontoRealCliCPProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'MontoRealFipCPProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'PorcDifEjecRealCPProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'PorcEjeCProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'PorcEjeCliCPProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'PorcEjeFipCPProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'PorcRealCPProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'PorcRealCliCPProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'PorcRealFipCPProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'SVerCProy': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'VerCProy': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'tramiteDoc.dprotocolo': {
            'EstDProt': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'IdDProt': ('django.db.models.fields.CharField', [], {'max_length': '35', 'primary_key': 'True'}),
            'IdMProt': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tramiteDoc.MProtocolo']", 'db_column': "'IdMProt'"}),
            'IdPerDProt': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'IdTipDocDProt': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'Meta': {'object_name': 'DProtocolo'},
            'NomDProt': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'RutaOcrDProt': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'RutaPdfDProt': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'UbLogDProt': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'UbiFisDProt': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'})
        },
        u'tramiteDoc.dproyecto': {
            'DescDProy': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'EstDProy': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'FecFinDProy': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'FecFirmaDProy': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'FecIniDProy': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'IdDProy': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'IdMProy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tramiteDoc.MProyecto']", 'db_column': "'IdMProy'"}),
            'IdTipDocDProy': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'DProyecto'},
            'MontAportCliDProy': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'MontAportFIPDProy': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'MontAportOtrDProy': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'RutaOcrDProy': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'RutaPDFDProy': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'tramiteDoc.dtabla': {
            'AbrDTab': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'AbrOpDTab': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'EstDTab': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'FactDTab': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'IdDTab': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'IdMTab': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tramiteDoc.MTabla']", 'db_column': "'idMTabla'"}),
            'IdRefDTab': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'IndDTab': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'Meta': {'object_name': 'DTabla'},
            'NomDTab': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'PropDTab': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'tramiteDoc.mcliente': {
            'DirMCli': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Email1MCli': ('django.db.models.fields.EmailField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'EstMCli': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'FecIngMCli': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'IdDepMCli': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'IdDistMCli': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'IdMCli': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'IdPaisMCli': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'IdProvMCli': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'IdRegMCli': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'IdTipInstMCli': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'IdTipMCli': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'MCliente'},
            'NomMCli': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'RefMCli': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Tel1MCli': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'Tel2MCli': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'Tel3MCli': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'tramiteDoc.mcolaborador': {
            'EstActMCol': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'EstMCol': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'FecFinMCol': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 6, 3, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'FecFirmaMCol': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 6, 3, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'FecIniMCol': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 6, 3, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'IdMPer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tramiteDoc.MPersonal']", 'null': 'True', 'db_column': "'IdMPer'", 'blank': 'True'}),
            'IdMProy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tramiteDoc.MProyecto']", 'null': 'True', 'db_column': "'IdMProy'", 'blank': 'True'}),
            'IdTipoCargoProy': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'MColaborador'},
            'MontoMCol': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'MontoMenMCol': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'RutaOCRMCol': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'RutaPDFMCol': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'TiempoMCol': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'tramiteDoc.mpersonal': {
            'ApeMMPer': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'ApePMPer': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'Email1MPer': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'blank': 'True'}),
            'Email2MPer': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'blank': 'True'}),
            'EstMPer': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'FecIngMPer': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'FechNacMPer': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'IdArea': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'IdMPer': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'IdTipDocMPer': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'IdTipPerMPer': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'Meta': {'object_name': 'MPersonal'},
            'NDocMPer': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'NomMPer': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'Tel1MPer': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'Tel2MPer': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'tramiteDoc.mprotocolo': {
            'DescMProt': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'DocInter': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'EstMProt': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'FecEntMProt': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'FecEntRealMProt': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'IdMCli': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'IdMProt': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'IdMProy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tramiteDoc.MProyecto']", 'null': 'True', 'db_column': "'IdMProy'", 'blank': 'True'}),
            'IdRefMProt': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'IdTipDocGen': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'IdTipFormEntMProt': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'Meta': {'object_name': 'MProtocolo'},
            'NomMProt': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'tramiteDoc.mproyecto': {
            'EstCierreMProy': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'EstMProy': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'FecEntMProy': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'FecEntRealMProy': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'FecFinMProy': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'FecFinRealMProy': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'FecIngMProy': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'FecIniMProy': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'FecIniRealMProy': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'IdBanco': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'IdConv': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'IdEstMProy': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'IdMCli': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tramiteDoc.MCliente']", 'null': 'True', 'db_column': "'IdMCli'", 'blank': 'True'}),
            'IdMProy': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'IdSector': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'IdTipProMProy': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'MProyecto'},
            'MontInvCliMProy': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'MontInvFipMProy': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'MontTInvRealCliMProy': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'MontTInvRealFipMProy': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'MontTInvRealOtrMProy': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'MontTotAdeCliMProy': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'MontTotAdeFipMProy': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'MontTotAdeOtrMProy': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'MontTotAdeTotMProy': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'MontTotMProy': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'MontTotRealMProy': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'NomMProy': ('django.db.models.fields.CharField', [], {'max_length': '700', 'null': 'True', 'blank': 'True'}),
            'NumCtaInterMProy': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'PorcTotAdeMProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'RutaOCRACMProy': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'RutaOCRConvMProy': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'RutaOCRMProy': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'RutaPDFACMProy': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'RutaPDFConvMProy': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'RutaPDFMProy': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'TiempoMProy': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'tramiteDoc.mtabla': {
            'AbrMTabla': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'EstMTabla': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'IdMTabla': ('django.db.models.fields.CharField', [], {'max_length': '4', 'primary_key': 'True'}),
            'Meta': {'object_name': 'MTabla'},
            'NomMTabla': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'PropMTabla': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'})
        },
        u'tramiteDoc.musuarioder': {
            'EstDer': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'IdUsuDer': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'IdUsuOri': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'Meta': {'object_name': 'MUsuarioDer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'tramiteDoc.pproyectos': {
            'BorradorPProy': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'CantPProy': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CostEjePProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'CostSalPProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'CostTotPProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'CostUnitPProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'DescPProy': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'EstAprobPProy': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'EstEvalPProy': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'EstModPProy': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'EstPProy': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'EstPresPProy': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'EstValidPProy': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'FFCliPProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'FFFipPProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'FFOtrosPProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'FecIngPProy': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'FecModPProy': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'FinPProy': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'IdMProy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tramiteDoc.MProyecto']", 'null': 'True', 'blank': 'True'}),
            'IdMotCierrePProy': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'IdNivPartPProy': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'IdPProy': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'IdUnidMed': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'IdUsuCreaPProy': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'IdUsuModPProy': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'PProyectos'},
            'NroPartPProy': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'NroPartPerPProy': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'PFFCliPProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'PFFFipPProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'PFFOtrosPProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'PorcCostEjePProy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'TitPProy': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'VerPProy': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'tramiteDoc.sclientes': {
            'DirSCli': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'Email1SCli': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'blank': 'True'}),
            'IdDepSCli': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'IdDistSCli': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'IdMCli': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tramiteDoc.MCliente']", 'max_length': '30', 'db_column': "'IdMCli'", 'blank': 'True'}),
            'IdPaisSCli': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'IdProvSCli': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'IdRegSCli': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'IdSCli': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'IdTipSCli': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'Meta': {'object_name': 'SClientes'},
            'NomSCli': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'RefSCli': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'Tel1SCli': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'Tel2SCli': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'Tel3SCli': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['tramiteDoc']