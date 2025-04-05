from django.shortcuts import render
from .models import Folder


# Create your views here.
def admin_dashboard_callback(request, context):
    documents_counts_per_folder = Folder.objects.get_documents_counts_per_folder()
    chart_labels, chart_data = list(documents_counts_per_folder.keys()), list(documents_counts_per_folder.values())
    context.update({
        "chart_title": "Documents per Folder",
        "chart_labels": chart_labels,
        "chart_data": chart_data,
    })
    return context
