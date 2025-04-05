from django.contrib import admin, messages
from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse
from unfold.admin import ModelAdmin, StackedInline
from unfold.decorators import action
from .models import Folder, Document


class DocumentInline(StackedInline):
    model = Document
    tab = True
    extra = 0


class FolderAdmin(ModelAdmin):
    inlines = [DocumentInline]
    list_display = ["name", "description"]
    actions_detail = ['count_documents']

    @action(description="Count documents", url_path="change-detail-action", icon="person")
    def count_documents(self, request: HttpRequest, object_id: int):
        folder = Folder.objects.get(pk=object_id)
        doc_count = folder.documents.count()
        messages.info(request, f"Folder '{folder.name}' has {doc_count} document(s).")
        return redirect(
            reverse("admin:app_main_folder_change", args=[folder.id])
        )


class DocumentAdmin(ModelAdmin):
    pass


# Register your models here.
admin.site.register(Folder, FolderAdmin),
admin.site.register(Document, DocumentAdmin)
