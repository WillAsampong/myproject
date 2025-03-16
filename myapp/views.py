# myapp/views.py

from django.shortcuts import render 
from .forms import ContactForm 

def contact(request): 
    if request.method == 'POST': 
        form = ContactForm(request.POST) 
        if form.is_valid(): 
            # Process the form data 
            success_message = "Form submitted successfully!" 
            return render(request, 'myapp/success.html', {'success_message': success_message}) 
    else: 
        form = ContactForm() 
        return render(request, 'myapp/contact.html', {'form': form})
