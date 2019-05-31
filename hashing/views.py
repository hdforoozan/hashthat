from django.shortcuts import render, redirect
from .forms import HashForm
from .models import Hash
import hashlib

def home(request):
	if request.method == 'POST':
		print(request.POST['text'])
		print(request.POST['submit'])
		filled_form = Hash(request.POST['text'],request.POST['submit'])
		if filled_form.is_valid():
			text = filled_form.cleaned_data['text']
			text_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
			try:
				Hash.objects.get(Hash=text_hash)
			except Hash.DoesNotExist:
				Hash1 = Hash()
				Hash1.text = text
				Hash1.Hash = text_hash
				Hash1.save()
			return redirect('Hash',Hash=text_hash)

	form  = HashForm()
	return render(request, 'hashing/home.html', {'form':form})

def Hash(request, hash1):
	Hash1 = Hash.objects.get(Hash=hash1)
	return render(request, 'hashing/hash.html', {'Hash':Hash1})