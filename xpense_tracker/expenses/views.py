from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, authenticate, login, logout

from .models import Expense
from django.db.models import Sum
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Sum
from .models import UserProfile
from .decorators import *



@login_required
def dashboard(request):
    one_month_ago = datetime.now() - timedelta(days=30)
    expenses = Expense.objects.filter(user=request.user, date__gte=one_month_ago).order_by('date')
    
    expenses_by_date = expenses.values('date').annotate(total_amount=Sum('amount'))

    labels = [expense['date'].strftime('%Y-%m-%d') for expense in expenses_by_date]
    amounts = [float(expense['total_amount']) for expense in expenses_by_date]  # Convert Decimal to float
    

    if hasattr(request.user, 'income_set'):
        current_income = request.user.income_set.all().aggregate(Sum('amount'))['amount__sum']
    else:
        current_income = 1

    # Calculate total expense
    total_expense = expenses.aggregate(total=Sum('amount'))['total']
    total_expense = total_expense if total_expense else 0  # Handle None value
    total_expense_percentage = round((-total_expense/current_income * 100),2)

    available_balance = current_income - total_expense
    available_balance_percentage = round((available_balance/current_income * 100), 2)


    if hasattr(request.user, 'userprofile'):
        selected_currency = request.user.userprofile.currency
    else:
        selected_currency = 'INR'

    

    
    context = {
        'labels': labels,
        'amounts': amounts,
        'username': request.user.username,
        'total_expense': total_expense,
        'available_balance': available_balance,
        'selected_currency': selected_currency,
        'available_balance_percentage' : available_balance_percentage,
        'total_expense_percentage' : total_expense_percentage,
        'current_income' : current_income,
    }
    return render(request, 'expenses/index.html', context)



# views.py
from .forms import ExpenseForm
from django.http import JsonResponse

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ExpenseForm()
    return render(request, 'index.html', {'form': form})

from .forms import IncomeForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = IncomeForm()
    return render(request, 'index.html', {'form': form})



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.shortcuts import redirect
from django.contrib.auth import get_user_model, authenticate, login, logout

User = get_user_model()

@csrf_exempt
def remove_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            user.delete()
            logout(request)
            return JsonResponse({'success': True, 'message': 'User deleted successfully.'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid username or password.'})
    return JsonResponse({'success': False, 'message': 'Invalid request.'})



def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "expenses/login.html", {'message': 'Invalid username or password.'})
    else:
        message = None
        if 'message' in request.session:
            message = request.session.pop('message')

        return render(request, "expenses/login.html", {'message': message})
# def UserLogout(request):
#     logout(request)
#     return redirect('login_page')
def register_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register_page')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return redirect('register_page')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully. You can now log in.")
            return redirect('login_page')
    else:
        return render(request, "expenses/register.html")

def account_view(request):
    username = request.user.username
    return render(request, 'expenses/account.html', {'username': username})

from django.contrib.auth.models import User
from .models import UserProfile  # Import your UserProfile model

@login_required
def settings_page(request):
    if request.method == 'POST':
        selected_currency = request.POST.get('currency')
        # Check if the user has a profile
        if hasattr(request.user, 'userprofile'):
            # Update existing profile
            request.user.userprofile.currency = selected_currency
            request.user.userprofile.save()
        else:
            # Create a new profile
            UserProfile.objects.create(user=request.user, currency=selected_currency)
        return redirect('dashboard')
    else:
        username = request.user.username 

        if hasattr(request.user, 'userprofile'):
            selected_currency = request.user.userprofile.currency
        else:
            selected_currency = 'INR'
        context = {'username': username, 'selected_currency': selected_currency,}
        return render(request, 'expenses/settings.html', context)


from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse

def contact_page(request):
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Construct email message
        email_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"

        # Send email
        send_mail(
            'Contact Form Submission',
            email_message,
            settings.EMAIL_HOST_USER,  # From email address
            ['jayantpatil07092003@gmail.com'],  # To email address (change to your preferred email)
            fail_silently=False,
        )

        # Redirect after successful form submission
        return HttpResponseRedirect('/contact/')   # Assuming 'success' is the name of your success URL pattern
    else:
        # Render contact form page
        username = request.user.username 
        return render(request, 'expenses/contact.html', {'username': username})


@login_required
def transaction_page(request):
    username = request.user.username 
    transactions = Expense.objects.filter(user=request.user).order_by('-date')

    if hasattr(request.user, 'userprofile'):
        selected_currency = request.user.userprofile.currency
    else:
        selected_currency = 'INR'

    context = {'username': username, 'transactions': transactions, 'selected_currency': selected_currency,}

    return render(request, 'expenses/transaction.html', context)


from datetime import datetime, timedelta
from django.utils.timezone import now, timedelta
from django.db.models import Sum
from django.db.models import Avg, Sum, Max
from datetime import datetime

def analysis_page(request):
    if request.method == 'GET':
        user = request.user
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')



        if start_date and end_date:
            try:
                start_date = datetime.strptime(start_date, '%Y-%m-%d')
                end_date = datetime.strptime(end_date, '%Y-%m-%d')
            except ValueError:
                # Handle invalid date format here
                pass
        else:
            # Default to 30 days ago
            end_date = datetime.now()
            start_date = end_date - timedelta(days=30)

        start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = end_date.replace(hour=23, minute=59, second=59, microsecond=999999)


        analysis = Expense.calculate_analysis(user, start_date, end_date)
        
        context = {
            'average_expense': analysis.get('average_expense'),
            'daily_average_expense': analysis.get('daily_average_expense'),
            'max_expense': analysis.get('max_expense'),
            'max_expense_day': analysis.get('max_expense_day'),
            'max_expense_category': analysis.get('max_expense_category'),
            'max_expense_name': analysis.get('max_expense_name'),
            'start_date': start_date,
            'end_date': end_date
        }
        
        expenses = Expense.objects.filter(user=request.user, date__range=(start_date, end_date)).order_by('date')

        # Aggregate expenses data by category and sum up the total amount
        expenses_by_category = expenses.values('category').annotate(total_amount=Sum('amount'))

        if hasattr(request.user, 'userprofile'):
            selected_currency = request.user.userprofile.currency
        else:
            selected_currency = 'INR'

        # Prepare data for chart
        labels = []
        amounts = []

        # Combine expenses with the same category
        for expense in expenses_by_category:
            category = expense['category']
            total_amount = float(expense['total_amount'])

            # If the category already exists in labels, add the amount to the existing category
            if category in labels:
                index = labels.index(category)
                amounts[index] += total_amount
            # Otherwise, add the category and its amount to the lists
            else:
                labels.append(category)
                amounts.append(total_amount)

        # Pass data to template
        context.update({
            'labels': labels,
            'amounts': amounts,
            'username': request.user.username,
            'selected_currency': selected_currency,
            'start_date': start_date.strftime('%Y-%m-%d'),
            'end_date': end_date.strftime('%Y-%m-%d'),
        })

        return render(request, 'expenses/analysis.html', context)




from django.http import JsonResponse
from .models import Expense
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

@login_required
def expenses_data(request):
    data = list(Expense.objects.filter(user=request.user)
                .values('category')
                .annotate(total_amount=Sum('amount'))
                .order_by('-total_amount'))

    categories = [entry['category'] for entry in data]
    amounts = [entry['total_amount'] for entry in data]

    return JsonResponse({
        'labels': categories,
        'data': amounts,
    })
    
