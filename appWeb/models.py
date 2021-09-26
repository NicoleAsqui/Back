from django.db import models
#he puesto las tablas de estado como estado de cuenta
#no he corregido la tabla sugerencias que depende de usuario
#dni_empresa no la he puesto como clave primaria aunque en la base se encuentre de esa forma
# on_delete=models.CASCADE borra todos los elementos que dependan de la clase 
#se ha incluido en empresa una tabla para povincia y ciudad  a pesar que no esta en l base de datos 
# sector en empresa si se ha incluido en una tabla y  si se encuentra como tabla en la base de datos (discutir)
#no se ha incluido la tabla de tarjetas de pago 
class Rol(models.Model):
    id_rol = models.AutoField( primary_key=True) 
    nombre = models.CharField(max_length=45)  
    descripcion = models.CharField(max_length=45)  

class Estadocuenta(models.Model):
    id_estadocuenta = models.AutoField(primary_key=True) 
    estado_cuenta = models.CharField(max_length=45)  

class Estadocivil(models.Model):
    id_estadocivil = models.AutoField( primary_key=True) 
    estado_civil = models.CharField(max_length=45)  

class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    genero = models.CharField(max_length=45)  

class Provincia(models.Model):
    id_provincia = models.AutoField(primary_key=True) 
    provincia = models.CharField(max_length=45)  

class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True) 
    ciudad = models.CharField(max_length=45)  
    id_provincia = models.ForeignKey(Provincia, null= False, blank = False, on_delete=models.CASCADE) 

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True) 
    nombre_usuario = models.CharField(max_length=45)  
    contrasenia = models.CharField(max_length=16)
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    ciudad = models.ForeignKey(Ciudad, null= False, blank = False, on_delete=models.CASCADE) 
    provincia = models.ForeignKey(Provincia, null= False, blank = False, on_delete=models.CASCADE)  
    correo = models.CharField(max_length=60)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=80)
    genero = models.ForeignKey(Genero, null= False, blank = False, on_delete=models.CASCADE) 
    estado_cuenta = models.ForeignKey(Estadocuenta,null= False, blank = False, on_delete=models.CASCADE) 
    estado_civil = models.ForeignKey(Estadocivil, null= False, blank = False, on_delete=models.CASCADE) 
    id_rol = models.ForeignKey(Rol, null= False, blank = False, on_delete=models.CASCADE) 


class Tipodocumento(models.Model):
    id_tipodocumento = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)  

class Tipopersona(models.Model):
    id_tipopersona = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)  

class Actividadeconomica(models.Model):
    id_actividadeconomica = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)  

class Ramaactividad(models.Model):
    id_ramaactividad = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)  

class Sector(models.Model):
    id_sector = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)  

class Tipoempresa(models.Model):
    id_tipoempresa = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)  

class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True) 
    dni_empresa = models.CharField(max_length=45)  
    tipo_documento = models.ForeignKey(Tipodocumento,null= False, blank = False, on_delete=models.CASCADE) 
    tipo_persona = models.ForeignKey(Tipopersona,null= False, blank = False, on_delete=models.CASCADE) 
    nombre_comercial = models.CharField(max_length=60)
    actividad_economica = models.ForeignKey(Actividadeconomica,null= False, blank = False, on_delete=models.CASCADE) 
    rama_actividad = models.ForeignKey(Ramaactividad,null= False, blank = False, on_delete=models.CASCADE) 
    razon_social = models.CharField(max_length=60)
    tipo_empresa = models.ForeignKey(Tipoempresa,null= False, blank = False, on_delete=models.CASCADE) 
    provincia = models.ForeignKey(Provincia, null= False, blank = False, on_delete=models.CASCADE)  
    ciudad = models.ForeignKey(Ciudad, null= False, blank = False, on_delete=models.CASCADE) 
    sector = models.ForeignKey(Sector, null= False, blank = False, on_delete=models.CASCADE) 
    calle_principal = models.CharField(max_length=60)
    calle_secundaria = models.CharField(max_length=60)
    manzana = models.CharField(max_length=20)
    villa = models.CharField(max_length=20)
    referencia = models.CharField(max_length=60)
    telefono_oficina = models.CharField(max_length=20)
    correo = models.CharField(max_length=60)
    pagina_web = models.CharField(max_length=60)

class Representante(models.Model):
    id_representante = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario,null= False, blank = False, on_delete=models.CASCADE) 
    id_empresa = models.ForeignKey(Empresa,null= False, blank = False, on_delete=models.CASCADE) 
    estado_cuenta = models.ForeignKey(Estadocuenta,null= False, blank = False, on_delete=models.CASCADE) 
    