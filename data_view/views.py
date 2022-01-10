from django.db import connection
from django.shortcuts import render
import pandas as pd
import json
from data_view.models import immo_bienny
from .models import Contact
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Sum, Max, Min, Avg, StdDev
from django.db.models.aggregates import StdDev
from django.views.generic import ListView
def immo_list (request):
    posts = str(immo_bienny.objects.exclude(balcony=True).query)
    #post = immo_bienny.objects.all().aggregate(Sum('prix_m2_ttc').query)
    
    df = pd.read_sql_query(posts, connection)
    
    df['prix_m2_ttc'] = df.prix_m2_ttc.replace(',','.', regex=True).values
    df['prix_m2_ttc'] = pd.to_numeric(df['prix_m2_ttc'], downcast = "float")
    
    #df['prix_m2_ttc'] = df['prix_m2_ttc'].astype()
    #df.prix_m2_ttc = df.prix_m2_ttc.astype(float)
    total_rows = len(df.id)
    bien_immo = total_rows + 1
    json_records = df.reset_index(). to_json(orient = 'records')
    data = []
    data = json.loads(json_records)

    sd = df.groupby('ville')['prix_m2_ttc'].mean()
    mean_records = sd.reset_index().to_json(orient ='records')
    mean = []
    mean = json.loads(mean_records)

    st = df.groupby('ville')['prix_m2_ttc'].std()
    std_records = st.reset_index().to_json(orient ='records')
    std = []
    std = json.loads(std_records)

    d= df.describe()
    smy_records = d.reset_index().to_json(orient ='records')
    describe = []
    describe = json.loads(smy_records)
    

   
    print(posts)
    print(connection.queries)
    if request.method=="POST":
        contact= Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact_number=request.POST.get('contact_number')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.message=message
        contact.contact_number=contact_number
        contact.save()
        return HttpResponse("<h1> THANKS FOR CONTACTING US</h1>")
    if request.method=="POST":
        fromdate= request.POST.get('fromdate')
        todate=request.POST.get('todate')
        searchresult=immo_bienny.objects.raw('select * from immo_bienny where joindate between "'+fromdate+'" and "'+todate+'"')
        return render(request, 'index.html', {"data":searchresult})
    else:
        displaydata=immo_bienny.objects.all()

    if request.method=="POST":
        exterieur= request.POST.get('exterieur')
        typologie=request.POST.get('typologie')
        garden=request.POST.get('garden')
        parking=request.POST.get('parking')
        searchresult1=immo_bienny.objects.raw('select * from immo_bienny where exterieur= "'+exterieur+'" and typologie="'+typologie+'" and garden="'+garden+'"and parking="'+parking+'"')
        return render(request, 'index.html', {"immo_bienny":searchresult1})
    else:
        displa=immo_bienny.objects.raw('select * from immo_bienny')


    return render(request, 'index.html', {'posts': data, 'bien_immo':bien_immo, 'mean':mean, 'std':std, "date":displaydata, "immo_bienny": displa})

# Create your views here.
# def viewdata(request):
#     results = immo_bienny.objects.all()
#     return render(request, 'index.html', {"data":results})

# def stat(request):
#     data = immo_bienny.objects.aggregate(sum=Sum('prix_m2_TTC'), max=Max('prix_m2_TTC'), min=Min('prix_m2_TTC'), avg=Avg('prix_m2_TTC'))
# # #         return data
#     #print(data)
#     return render(request, 'index.html', {"data":data})


# from django.shortcuts import render
# from data_view.models import immo_bien1
# from django.db.models import Sum

# # Create your views here.
# from .models import Csv
# from django.shortcuts import render

# # Create your views here.
# from .forms import CsvModelForm
# import csv
# from .models import Csv
# from django.contrib.auth.models import User
# #from . import views

# from .forms import CsvModelForm
# import csv
# from .models import Csv
# from django.contrib.auth.models import User
# from django.db.models import Sum, Max, Min, Avg, StdDev
# from django.db.models.aggregates import StdDev
# from django.views.generic import ListView
# #from django.http import HttpResponse
# #create your views here.

# def upload_file_view(request):
#     form =CsvModelForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#         form = CsvModelForm()
#         obj = Csv.objects.get(activated=False)
#         with open(obj.file_name.path, 'r') as f:
#             reader = csv.reader(f)
          

#             for i, row in enumerate(reader):
#                 if i==1:
#                     pass
#                 else:
#                     row = "".join(row)
#                     row = row.replace(" ", "_")
#                     row = row.replace(";", " ")
#                     row = row.split()
#                     #print(row)
#                     #print(type(row))

#                     immo_bien1.objects.create(
#                     #id =row[0],
#                     id_lot=row[1], 
#                     nb_piece=row[2], 
#                     typologie=row[3], 
#                     prix_tva_reduite=row[4],
#                     prix_tva_normale=row[5], 
#                     prix_HT =row[6], 
#                     prix_m2_HT =row[7], 
#                     prix_m2_TTC=row[8], 
#                     surface=row[9], 
#                     etage=row[10], 
#                     orientation=row[11],
#                     exterieur=row[12], 
#                     balcony=row[13],
#                     garden=row[14], 
#                     parking=row[15], 
#                     nom_programme= row[16], 
#                     ville=row[17], 
#                     departement=row[18], 
#                     date_fin_programme=row[19], 
#                     adresse_entiere=row[20],
#                     promoteur=row[21], 
#                     date_extraction=row[22])
#                 #row=row+1

#                     #def example(request):
#     #_count=immo_bien.o
#     # bjects.count()
#     #data=immo_bien.objects.all().aggregate(sum=Sum('prix_m2_TTC'), max=Max('prix_m2_TTC'), min=Min('prix_m2_TTC'), avg=Avg('prix_m2_TTC'),   )

#     #return render(request, 'basic_html', {"data":data})
                    
#             obj.activated = True
#             obj.save()
#     return render(request, "upload_csv/upload.html", {'form': form})

# # class Example(ListView):
    
# #     model = immo_bien
# #     template_name = "basic.html"
    
# #     def get_context_data(self, *args, **kwargs):
# #         context = super(Example, self).get_context_data(*args, **kwargs)
# #         context['Avg_prix_m2_TTC/ville'] = immo_bien.objects.values('ville').annotate(avg=Avg('prix_m2_TTC').order_by())
# #         return context  

# #     def example(request):
# #     #_count=immo_bien.o
# #     # bjects.count()
# #         data=immo_bien.objects.all().aggregate(sum=Sum('prix_m2_TTC'), max=Max('prix_m2_TTC'), min=Min('prix_m2_TTC'), avg=Avg('prix_m2_TTC'))
# #         return data
#     #return HttpResponse('drop a file here')
#     #form =CsvModelForm(request.POST or None, request.FILES or None)s