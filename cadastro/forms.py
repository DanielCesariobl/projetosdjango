from django.forms import ModelForm 
from .models import Marca, Cliente, Modelo, Veiculo

class MarcaForm(ModelForm):
   class Meta:
    model = Marca
    fields = '__all__'

class ClienteForm(ModelForm):
   class Meta:
    model = Cliente
    fields = '__all__'    

class ModeloForm(ModelForm):
   class Meta:
      model = Modelo 
      fields = '__all__'   

class VeiculoForm(ModelForm):
   class Meta:
      model = Veiculo
      fields = '__all__'      