from django.contrib import admin
from content.models import MindStream, Picture

class PictureAdmin(admin.ModelAdmin):
    actions = ['delete_model']

    def get_actions(self, request):
        actions = super(PictureAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def delete_model(self, request, obj):
        for o in obj.all():
            o.delete()
    delete_model.short_description = "Delete items"


admin.site.register(MindStream)
admin.site.register(Picture, PictureAdmin)