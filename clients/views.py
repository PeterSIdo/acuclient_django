from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from bson.objectid import ObjectId
from .utils import get_mongodb_connection
import uuid

clients_collection = get_mongodb_connection()


clients_collection.update_many(
    {"sessions": {"$type": "string"}},
    {"$set": {"sessions": []}}
)



#login_required
def index(request):
    search_query = request.GET.get('search', '')
    if search_query:
        clients = clients_collection.find({
            "$or": [
                {"name": {"$regex": search_query, "$options": "i"}},
                {"condition": {"$regex": search_query, "$options": "i"}}
            ]
        })
    else:
        clients = clients_collection.find()
    clients = [{**client, 'id': str(client['_id'])} for client in clients]
    return render(request, 'clients/index.html', {'clients': clients, 'search_query': search_query})

#login_required
def add_client(request):
    if request.method == 'POST':
        client = {
            "id": str(uuid.uuid4()), # Generate a unique 
            "name": request.POST.get('name'),
            "date_of_birth": request.POST.get('date_of_birth'),
            "address": request.POST.get('address'),
            "phone": request.POST.get('phone'),
            "email": request.POST.get('email'),
            "condition": request.POST.get('condition'),
            "session_record": request.POST.get('session_record'),
            "sessions": []  # Ensure sessions is initialized as an array
        }
        clients_collection.insert_one(client)
        messages.success(request, "Client added successfully!")
        return redirect('index')
    return render(request, 'clients/add_client.html')

#login_required
def edit_client(request, client_id):
    client = clients_collection.find_one({"_id": ObjectId(client_id)})
    if not client:
        messages.error(request, "Client not found.")
        return redirect('index')
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'add_session':
            new_session = {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "notes": request.POST.get('new_session_notes')
            }
            clients_collection.update_one(
                {"_id": ObjectId(client_id)},
                {"$push": {"sessions": new_session}}
            )
            messages.success(request, "New session added successfully!")
            
        elif action == 'update_client':
            updated_client = {
                "name": request.POST.get('name'),
                "date_of_birth": request.POST.get('date_of_birth'),
                "address": request.POST.get('address'),
                "phone": request.POST.get('phone'),
                "email": request.POST.get('email'),
                "condition": request.POST.get('condition'),
                "session_record": request.POST.get('session_record'),
                "sessions": client.get('sessions', [])  # Ensure sessions remains an array
            }
            clients_collection.update_one(
                {"_id": ObjectId(client_id)}, 
                {"$set": updated_client}
            )
            messages.success(request, "Client updated successfully!")
            return redirect('index')
            
        return redirect('edit_client', client_id=client_id)
    return render(request, 'clients/edit_client.html', {'client': client})

#login_required
def delete_client(request, client_id):
    if request.method == 'POST':
        clients_collection.delete_one({"_id": ObjectId(client_id)})
        messages.success(request, "Client deleted successfully!")
    return redirect('index')

#login_required
def view_client(request, client_id):
    client = clients_collection.find_one({"_id": ObjectId(client_id)})
    if not client:
        messages.error(request, "Client not found.")
        return redirect('view_client', client_id=client_id)
    return render(request, 'clients/view_client.html', {'client': client})
