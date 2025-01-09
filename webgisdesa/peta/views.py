from django.shortcuts import render, redirect
from .models import Superhero
from django.contrib import messages

# view untuk read
def LihatSuperhero(request):
    semuaHero = Superhero.objects.all()

    context = {
        'Semua_Hero' : semuaHero,
    }

    return render (request, "peta/index.html", context)

# view untuk create
def createSuperhero (request):
    return render(request, 'peta/create.html')

def simpan(request):
    if request.method == "POST":
        hero = Superhero()
        hero.nama = request.POST.get('nama')
        hero.lat = request.POST.get('lat')
        hero.long = request.POST.get('long')
        hero.asosiasi = request.POST.get('asosiasi')
        hero.save()
        messages.success(request, "Superhero baru berhasil ditambahkan")
        return redirect('peta:create')  # Sesuaikan dengan nama URL untuk peta/create
    else:
        return render(request, 'peta/create.html')
    """ hero = Superhero() # nama kelas di models.py
    hero.nama = request.POST.get('nama') # nama kolom di models.py
    hero.lat = request.POST.get('lat')
    hero.long = request.POST.get('long')
    hero.asosiasi = request.POST.get('asosiasi')
    hero.save()
    messages.success(request, "Superhero baru berhasil ditambahkan")
    
    return redirect('/peta/create') """ 
    # return render(request, 'peta/create.html')

# view untuk delete

def deleteSuperhero(request, id):
    hero = Superhero.objects.get(id = id)
    hero.delete()
    messages.success(request, "Superhero berhasil dihapus")
    return redirect('/peta')

# view untuk UPDATE
def updateSuperhero(request, id):
    hero = Superhero.objects.get(id = id)
    return render(request, 'peta/update.html', {'hero':hero})

def update(request, id):
    hero = Superhero.objects.get(id = id)
    hero.nama = request.POST.get('nama') #nama kolom di models.py
    hero.lat = request.POST.get('lat')
    hero.long = request.POST.get('long')
    hero.asosiasi = request.POST.get('asosiasi')
    hero.save()
    messages.success(request, "Superher berhasil diupdate")
    return redirect('/peta')