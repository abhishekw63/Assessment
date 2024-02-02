# code .
# python -m venv venv_tops_project
# cd .\(tab_key)
# pip install django
# created .gitignore file
# installed extension: python django django_template prettier cobalt2

#django-admin startproject ecommerce
#python manage.py startapp ecommerceapp

'''
->registering ecommerceapp in settings.py to installed_apps
->need to land at some html page  for localhost:8000 instead of the installed worked succcessfully messagge therefore configuiring url.py of ecommerce
    add a new path and redirecting it to ecommerceapp
->created urls.py of ecommerceapp and imported views module.
->created index view.
->created templates folder at project level.
    index.html
->DIRS': ['templates'], registering templates folder

#enabled mouse wheel zoom by clicking checkbox in settings.py
#pressing ctrl d will copy same statement below it
#can change copy line down setting in keyboard shortcuts.

->navigatig to getbootstrap.com
    -copied include bs' css and js code ffrom official docs
    -completely replacing index.html with copied code
    -link is associated with css loading.
        -every line of code would executed in our project.
        -same for script.
    -script is associated with js loading.
->index.html
    -copying navbar code
        -<a class="navbar-brand" href="/">Abhi's Outlet</a>  (-/ is equal to ' ')
        -a class="nav-link active" aria-current="page" href="/">Home</a>
        -<li class="nav-item">
                <a class="nav-link" href="/contact">Contact us</a>
              </li>  #changes from link to contact us
        -copied same snippet for about us. (href=/about)
        -deleting dropdown and disable list and disabled list.
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Dropdown
                </a>
                <ul class="dropdown-menu">
                  <li><a class="dropdown-item" href="#">Action</a></li>
                  <li><a class="dropdown-item" href="#">Another action</a></li>
                  <li><hr class="dropdown-divider"></li>
                  <li><a class="dropdown-item" href="#">Something else here</a></li>
                </ul>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled" aria-disabled="true">Disabled</a>
              </li>
        -changed href="/"> to dynamic url
            <a class="nav-link active" aria-current="page" href="{% url 'index' %}">Home</a>
        -<a class="navbar-brand" href="{% url 'index' %}">Abhi's Outlet</a>
        -<nav class="navbar navbar-expand-lg bg-body-tertiary"> changed.
        -we want same navbar for contact us and about us.
        
->created contact and about view and assigned url for it.
->creating base.html
    -inserted title block and body block
    -extended to all html files wherever required.
->navigating bootstrapmade.com/demo/tempo and downloading template
    -integrating this frontend into our project.
->replacing index.html with downloaded index.hhtml
    -pasting it alone wont work because we have static file as well.
        -such as js,jquery,img etc.
    -create static folder beside templates and paste assest folder into it.
->need to modified index.html as per requirement.
->localhost:8000 would load without static files.
    -   import os
        STATICFILES_DIRS=[
        os.path.join(BASE_DIR,'static')
        ]
    -STATICFILES_DIRS is a setting that specifies additional directories from   which Django should collect static files.
    In your provided code, it indicates that the 'static' folder, located at the project level (os.path.join(BASE_DIR,'static')), should be included when collecting static files.
    -STATIC_URL:It represents the URL prefix where Django will look for static files when rendering a template
    -STATICFILES_DIRS specifies where to find static files in your project.
    -STATIC_URL specifies the base URL to serve these static files.
    -i.e
        <link rel="stylesheet" type="text/css" href="{% static 'styles.css' %}">
        This uses the STATIC_URL setting to construct the correct URL for the static file.
    -in summary:
        -STATICFILES_DIRS specifies where to find static files in your project.
        STATIC_URL is useful for generating dynamic URL tags in Django templates.
    -in index.html replace assests with static/assests using ctrl +h
    -if we have exisiting css and want to remove that cache go for ctrl shift r that is basically hard reload and it will take new css.
->make a copy of index.html to copy.html so that we dont lose original.
->making blank base.html and copied data of copy.html to base.html
->modifying base.html:
    -{% block title %}{% endblock title %}
    -<meta content="ecommerce website which delievered products in 1 hour" name="description">
    -<meta content="ecommerce," name="amazon,flipkart,selling products">
    -<h1>Jutsu Cart</h1>
    -class is associated with css that is defined by .xyz
        particular styling code is written for it.
    -removed:
        <li><a href="index.html#services">Services</a></li>
          <li><a href="index.html#portfolio">Portfolio</a></li>
          <li><a href="index.html#team">Team</a></li>
    -removed:
        <li class="dropdown has-dropdown"><a href="#"><span>Deep Dropdown</span> <i class="bi bi-chevron-down"></i></a>
                <ul class="dd-box-shadow">
                  <li><a href="#">Deep Dropdown 1</a></li>
                  <li><a href="#">Deep Dropdown 2</a></li>
                  <li><a href="#">Deep Dropdown 3</a></li>
                  <li><a href="#">Deep Dropdown 4</a></li>
                  <li><a href="#">Deep Dropdown 5</a></li>
                </ul>
              </li>
                <li><a href="#">Dropdown 2</a></li>
              <li><a href="#">Dropdown 3</a></li>
              <li><a href="#">Dropdown 4</a></li>
Selectively wrtiting from now onwards.

->copied portfolio section to index.html.
->created new app for handling authentication.
->nothing to render while hitting logout function. just redirection is needed.
->change auth to authcart. apply changes wherever is required.
    -in apps.py too.
->creating baseauth.html file in authetication.
->

        
'''

