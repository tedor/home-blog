from django import forms

class PictureByCategory(forms.Widget):
    def render(self, name, value, attrs=None):
        return '1234'
