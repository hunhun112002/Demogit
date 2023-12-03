from django.views import View
from django.http import HttpResponse



class ItemListView(View):

    def get (self , request ) :
        items = ["items1", "items2", "items3"]
        return HttpResponse ("\n".join(items)) 

