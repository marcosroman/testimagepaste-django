from django import forms#.ModelForm, forms.CharField, forms.HiddenInput
from django.forms import widgets
from . import models
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.core.files.base import ContentFile
import base64

# (1) https://stackoverflow.com/questions/43481931/how-to-upload-an-image-through-copy-paste-using-django-modelform#43502536

class PictureWidget(widgets.Widget):
    def render(self, name, value, attrs=None, renderer=None): # (2) https://stackoverflow.com/questions/52039654/django-typeerror-render-got-an-unexpected-keyword-argument-renderer
        # => eso de 'renderer=None' no estaba inicialmente en la referencia (1), se lo agrego porque me daba error sin eso (solucion sacada de referencia (2))
        print('rendering... value='+str(value))
        #if str(value) == '': # (esto saco porque value!='' siempre, es None (hasta ahora.. siempre)
        if value is None:
            html1 = "<img id='id_imagen' style='display:block' class='rounded float-left d-block'/>"
        else:
            html1 = "<img id='id_imagen' style='display:block' class='rounded float-left d-block' src='" + str(value) + "'/>"
        return mark_safe(html1)

class Formulario(forms.ModelForm):
    imagen_container = forms.CharField(required=False, widget=forms.HiddenInput())
    class Meta:
        model = models.Modelo
        fields = '__all__'
        widgets = {
            'imagen': PictureWidget(),
        }

    def save(self, commit=True):
        # check image_container data
        self.instance.imagen.delete(False)
        imgdata = self.cleaned_data['imagen_container'].split(',')
        try:
            ftype = imgdata[0].split(';')[0].split('/')[1]
            fname = slugify(self.instance.texto)
            self.instance.imagen.save('%s.%s' % (fname, ftype), ContentFile(base64.decodebytes(bytes(imgdata[1], 'utf-8'))))
        except:
            pass
        return super(Formulario, self).save(commit=commit)
