'''
->python -m venv bloodbank_venv
->\bloodbank_venv\Scripts\activate
->pip install -r requirements.txt
->pip install Pillow
->python manage.py makemigrations
->python manage.py migrate
->python manage.py createsuperuser
->asgiref==3.2.7
    -ASGI (Asynchronous Server Gateway Interface) is like a set of rules or guidelines that allow web servers to communicate with web applications.
    - Imagine it as a common language that both the server and your web application speak to understand each other.
    -Now, asgiref is a specific implementation of these rules. It's like a practical example or a ready-to-use version of ASGI that developers can use in their Python projects.
    -In conclusion,ASGI (Asynchronous Server Gateway Interface) is a specification for asynchronous web servers to communicate with web applications. Asgiref is a reference implementation of ASGI.
->Django==3.0.5
->django-widget-tweaks==1.4.8
    -Django Widget Tweaks is like a toolbox for Django templates. In web development with Django, templates are used to create the HTML structure of your pages. When you're working with forms in these templates (like getting user input), Django Widget Tweaks provides extra tools or functions to make your life easier.
    -Imagine you're building a form, and you want more control over how the form elements (like text fields or buttons) are displayed on your web page. Django Widget Tweaks steps in to help with that. It offers high-level helper functions, which are like pre-built tools, allowing you to customize the appearance of these form elements without writing a lot of complex code.
    -In conclusion,Django Widget Tweaks is a set of high-level template helper functions for Django, which allows for more flexibility in working with form widgets in templates. 
->pytz==2020.1
    -Pytz is a Python library for working with time zones. 
->sqlparse==0.3.1
    -Sqlparse is like a language interpreter but for SQL (Structured Query Language). In the world of Python programming, it's a module or tool that helps your program understand and work with SQL statements more effectively.
    -The primary job of sqlparse is to look at SQL statements (commands that interact with databases) written in your Python code and help your program understand them better. It can do things like breaking down complex SQL queries into understandable parts, formatting them nicely for readability, and even analyzing them to extract useful information.
    -In conclusion,Sqlparse is a non-validating SQL parser module for Python. It provides support for parsing, formatting, and analyzing SQL statement
        -Non validating refer to the fact that it doesnt rigourously check correctness of SQL.
        - sqlparse is more focused on helping you understand and work with SQL statements rather than ensuring that they strictly conform to a predefined SQL standard. 
->In Django, the User model (which represents user data in the database) is typically accessed as User. However, when dealing with an actual user instance associated with a request, the convention is to use request.user rather than request.User
->donor:donor1 and pwd:admin
->patient:patient1 and pwd:admin

->All urls descriptions:
/admin/: Django admin interface.
/donor/ and /patient/: Include URLs from the 'donor' and 'patient' apps.
/: Home view.
/logout: Logout view using Django's LogoutView.
/afterlogin: After login view.
/adminlogin: Admin login view using Django's LoginView.
/admin-dashboard: Admin dashboard view.
/admin-blood: Admin blood view.
/admin-donor: Admin donor view.
/update-donor/<int:pk>: Update donor view for a specific donor.
/delete-donor/<int:pk>: Delete donor view for a specific donor.
/admin-request: Admin request view.
/update-patient/<int:pk>: Update patient view for a specific patient.
/delete-patient/<int:pk>: Delete patient view for a specific patient.
/admin-donation: Admin donation view.
/approve-donation/<int:pk>: Approve donation view for a specific donation.
/reject-donation/<int:pk>: Reject donation view for a specific donation.
/admin-request-history: Admin request history view.
/update-approve-status/<int:pk>: Update approve status view for a specific request.
/update-reject-status/<int:pk>: Update reject status view for a specific request.

-> home view:
the home_view function checks for existing instances of the Stock model.
If there are no instances, it creates instances for various blood groups (A+, A-, B+, B-, AB+, AB-, O+, O-).
If the user is authenticated, it redirects them to the 'afterlogin' URL.
If the user is not authenticated or after redirection, it renders the 'blood/index.html' template.
The view aims to ensure the presence of stock instances for blood groups and handles user redirection based on authentication status.

->after login view:
After a user logs in:
If the user is identified as a donor, it redirects them to the 'donor/donor-dashboard' URL.
If the user is identified as a patient, it redirects them to the 'patient/patient-dashboard' URL.
If the user is not identified as a donor or patient, it assumes they are an admin and redirects them to the 'admin-dashboard' URL.
This view simplifies the redirection logic based on user types (donor, patient, or admin) after successful login.

->is_donor(user):
user: This parameter represents a user object. In the context of Django, it's typically an instance of the User model provided by Django's authentication system. The User model is often extended or customized in projects to include additional fields or relationships.

user.groups: This accesses the groups associated with the user. In Django's authentication system, users can be assigned to one or more groups. Groups are a way to categorize users and assign permissions to multiple users at once.

.filter(name='DONOR'): This filters the groups to include only those with the name 'DONOR'. It checks if the user is part of the group named 'DONOR'.

.exists(): This checks if there is at least one group with the name 'DONOR' in the filtered queryset. If at least one such group exists, the function returns True, indicating that the user is considered a donor; otherwise, it returns False.

->admin dashboard view:
@login_required(login_url='adminlogin')
This decorator ensures that the view can only be accessed by authenticated users. If a user is not authenticated, they will be redirected to the 'adminlogin' URL

totalunit = models.Stock.objects.aggregate(Sum('unit'))
the aggregate function is calculating the sum of the 'unit' field across all instances of the Stock model. The key in the result dictionary is automatically generated based on the aggregation function used, and in this case, it is 'unit__sum'.

Alternatively, we can use the annotate method with the Sum aggregation directly in the query. 
from django.db.models import Sum
totalunit = models.Stock.objects.all().aggregate(unit_sum=Sum('unit'))

Gross_unit is an alias for the result key, and you can customize it as needed.
Sum(F('unit')) represents the sum of the 'unit' field.
The use of F('unit') inside the Sum function ensures that you are referencing the actual field in the model. This is especially useful in more complex queries where you might want to perform aggregations or calculations based on the values of specific fields.
from django.db.models import Sum, F
totalunit = models.Stock.objects.all().aggregate(Gross_unit=Sum(F('unit')))

->admin blood view:
@login_required(login_url='adminlogin')
This is a decorator that ensures the user is authenticated before accessing the admin_blood_view. If not authenticated, it redirects to the login page specified by login_url.

dict: This is a Python dictionary used to store various data that will be passed to the template.

'bloodForm': forms.BloodForm(): It initializes an instance of the BloodForm form, which is used to handle blood-related form submissions.

'A1', 'A2', ..., 'O2': These are keys representing different blood groups, and their corresponding values are instances of the Stock model retrieved from the database based on the blood group.

Form Submission Handling (request.method == 'POST'):

A check is performed to see if the request method is POST, indicating a form submission.

If the submitted form (bloodForm) is valid, the blood group and unit are extracted from the form's cleaned data.

The corresponding Stock instance in the database is retrieved based on the blood group.

The unit of the retrieved Stock instance is updated with the submitted unit value from the form.

The changes are saved to the database.

Finally, a redirection (HttpResponseRedirect) to the 'admin-blood' URL is triggered.

Rendering the Template:

If the request method is not POST (GET request or initial rendering), the dict is passed as context to the 'blood/admin_blood.html' template for rendering.

->admin update view:
in Django, when saving a model instance to the database using the save() method, the commit parameter is used to control whether the changes should be immediately saved to the database or not.

Steps:

Fetch Donor and User Instances:
Retrieve the existing Donor and User instances based on the provided primary key (pk).
Initialize Forms:

Create instances of the donor and user forms.
userForm = DonorUserForm(instance=user)
donorForm = DonorForm(request.FILES, instance=donor)

Display Forms in Template:
Pass the forms as context to be displayed in the template.

Form Submission (POST Request):
If the request method is POST:
Reinitialize the forms with the submitted data.
Validate the forms (is_valid()).
If both forms are valid:
Save the user data, ensuring the password is updated (userForm.save()).
Save the donor data with commit set to False.
Associate the donor with the user (donor.user = user).
Save the donor instance to the database (donor.save()).
Redirect to the admin donor view (redirect('admin-donor')).

Rendering the Template:
If the request method is not POST or the forms are not valid, render the template with the forms.

Additional Notes:
The use of commit=False allows for additional processing before saving to the database.
The user's password is updated explicitly after saving (user.set_password(user.password)).
The Donor model has a foreign key relationship with the User model.


'''