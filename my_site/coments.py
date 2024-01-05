'''
Planning the data models:
    -Author to Post (one to many)
    -Post to Tag (Many to Many)
    
    -Author:
        First_name
        Last_name
        Email_address
    
    -Post:
        Title
        Excerpt
        Image Name
        Date
        Slug
        Content
    
    -Tag:
        Caption
        
Adding a Post model:
    -db.index is automatically set True though we can save it too
    -Unique true also implies  index

Author model one to many:
    -The ForeignKey field should be added to the model that represents the "many" side of the relationship.
        this case, since one author can have multiple posts, the ForeignKey field should be added to the Post model. 
       
        This is because each post will have a reference to its author.
        each Post instance will have a reference to its author through the author field,
        and you can access the posts of a particular author using the related_name="posts" attribute.
        
        The related_name="posts" attribute in the ForeignKey field is used to set the reverse relation from Author to Post.
        So, the related_name essentially allows you to navigate from the "one" side of the relationship (Author) to the "many" side (Post) more conveniently
    
Tag model many to many:
    -can add relation from both side. here we are adding from post perspetive
    -created tag model with caption field
    
Registering models for admin:
    -imported models in admin.py and registered models

Migrations and admin login:
    -in author field added null=True 
        author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
        
        The null=True parameter is essential in this context. 
        It specifies that the author field in the Post model can be set to NULL (i.e., have no associated Author). 
        If you remove null=True, it means that every Post must have a valid Author.
        If you try to save a Post without providing a valid Author instance, it will raise an integrity error.

        By setting null=True,
        you allow for situations where a Post doesn't necessarily have an associated Author, 
        and the author field can be set to NULL. 
        This is especially useful when you have existing Post instances and 
        you want to introduce the Author field without requiring it for all existing records.

        In summary, 
        the null=True parameter allows flexibility in the database schema, 
        permitting instances of the Post model to exist without an associated Author.

   -Creating superuser: id:admin and pwd:admin 
Adding Data via admin:
    -all field is required and emailid field also have validation
    -how author object should look like? -> def __str__
    -added three tag
    -slug is not auto populated make it later and created 2 post.
    
Configuiring the Admin panel:
    -created class in admin.py named PostAdmin  (for changing Post display in admin panel and also applied filters)
    -register PostAdmin
    -Slug should be autofilled/pre-populated
    -add prepopulated field
    -now data should come from database instead of from dummy data

Fetching Posts for starting page:
    -use models and get data from there
    -can use order by on all or filter
    -we can get all data from database then apply order by and then take slice of it too. but it would be very inefficient because fetching all data and slicing just 3 post
        -however django is smart. it will create long sql query and take that slice into consideration
        -django does not support negative indexing here . but there is already descending order of date
    -solve error variabledoesnot exist. image_name field in model and post.image was different in post.html
All post & single post pages:
    -displaying all post is straightforward ->all_posts =Post.objects.all().order_by('-date')
    -Now working on post detail
    -slug on rhs is the property and lhs is the name we are receiving.using shorcut get_object_or_404 instead of render+exception handlings
    -same error of image.
   

Using Author & tags Data:
    -we also have a tag and author model.
    -lets make name clickable-turn this into link
    -also show tag of posts
    -trasnfrom name into anchor tag with mailto std html syntax
    -after applying css (summary address) in post-detail do empty cache and hard reload after inspect
    -{{tag}} would also work because of str method
    -{% for tag in post.tags%} wont work because its not list of tags its object and allow us to drill into object.
        In Django, a manager is a class attribute of a Django model that provides a convenient interface for querying the database. 
        Managers allow you to retrieve, create, update, and delete records in the database using a higher-level API.
        In the context of many-to-many relationships, when you define a many-to-many field in your model, Django automatically creates a manager to handle the operations related to that relationship. 
        This manager is an instance of the django.db.models.Manager class.

        For example, in your Post model:
        tags = models.ManyToManyField(Tag)
        The tags attribute is a manager for the many-to-many relationship between Post and Tag. 
        When you access post.tags in your views or templates, you're actually working with this manager. 
        To get the actual tags, you need to use the .all() method of the manager to retrieve all related objects.
        Managers provide a high-level API for working with your models, and they help abstract away some of the complexity of database queries.
    -modified css for class tag and again empty cache and hard reload

Summary:
    -
    
    
14 Course Project: Building a blog,form files and sessions:

Module Introduction:
    -Adding a comment section with forms.
        so users/non logged in users can leave comment.
    -Add a read later feature with sessions.
        mark post as read later and we have a new page on our website where we can view all those marked posts.
    -Add a file uploads
        we always just type in the image name and we then rely on that image being pre stored in our source code in the end.
        and thats not realistic. 

Adding an imagefield to post model:
    -starting with fileuploads because that will require to change to our post model.
        and we will then have to update or recreate all our posts because of that
    -go to post model and change image field there.
        instead of storing the image name as text i wanna store as a file(though path name will be stored),
        image=models.ImageField(upload_to='posts') #it should be inside uploads folder
        create a uploads folder on root level.
        need to configure project little bit for uploads/posts/...
        add media_root
        add media_url (which will then define actual url)
            how url will look like for accessing that data. we are going with files.
        install pillow package
            so that imagefield works correctly
        now model has been adjusted so run migrations.
        error:we are trying to add non nullable field image to post without a default.
            we do have existing posts and they might not have images
            adding a null=true
    -error:
        VariableDoesNotExist at /
        Failed lookup for key [image_name] in <Post: Post object (3)>
        the pro is we are still trying to access the image name but that field doesnt exist anymore.
         <img src="{% static "blog/images/"|add:post.image_name %}" alt="{{ post.title}}"/> 
        visit admin panel look image field 
        lets update exisiting post by picking a file     
        
Serving uploaded files:
    -if we trying to upload through admin panel we indeed get images in uploads folder.
    -can delete this images folder in static because we are not using it anymore.
    -updating other post as well.
    -now lets make sure that we serve those uploaded images.
    -when it comes to serving images, we have couple of things to do.
        in blog folder of templates we have to change how we want to display them.
        in post.html we are using static tag.
            interpolate value here. {{post.image.url}}
            we do have couple of nested properties, this url property which gives us the URL to that image
            can ommit load static too.
        do similar modification to other templates.
    -dont delete static folder because there is abhi's image.and it is static image which is hard coded.
        it is part of our source code and not dynamically generated.
    -uploaded images are not being served.
        because out of the box django doesnot provide access to your enitre file system here to the outside world.
        so if we want to serve files from one of folders we explicitly have to tell django
            url configuration
            import static and append it to urlpatterns
            get both value from settings by importing settings
            now images would be back
              
Converting views to class based:
    -changing function based view to class based view
    -overhaul of starting_page fn:
        can use extends to view class and get method but it will make lengthy
        instead using listview
        call classmethod upon view in urlpatterns
        we have to careful with post model because we are querying. so need to override euryset method.
        limit that queryset as did in fn.
        ther also ordering (order by in fn)
            can also add more filter after (-date),...
        data will be provided to template under the name of posts.i.e. context object_name
    -conversion of post fn:
        only difference from above is we dont take slice but take all
        no need to override queryset because we are not limiting anything like that.
    -conversion of post_detail view:
        using specialized view detaileview and import it
        we need to make sure that data from model fetch by slug.
            it is supported by detail by detailview out of the box.
            django will automatically search item by slug.
        it will automatically raise 404 error
        need to override get context data for visible tags.
            we can get access to post by self.object
            we can access all fields of models by self.object.tags.all()
            return updated context
        DetailView automatically retrieves the object for you based on the URL parameters, including slug,
        and makes it available in the view as self.object.
    
Adding a comment model:
    -every post should have comment and every user should be able to comment.
    -so we need a new model.
    -every post can have multiple comment but every comment will belong nto only one post. 
        so it will be one to many relation.
    -setting a comments model.
        user_name
        user_email
        text
        post as foreign key to post model. also set related name so on a given post we can access all comments.
    -comments model has been prepare so need to add a form so user facing front end can add comments.
    -setup a form below {{post.content|linebreaks}}
        when it comes to creating a form ,
        we can create it from scratch on our own, collect and validate the data on our own,
        or we can use built in django-support.   
Adding a comment form:
    -since we in the end wanna fetch data for this comment,
        it would make sense to simply create a model form that is based on,
        comment model. 
    -create forms.py file and create modelform
        here we dont want to include post field because this post field,
        should not be set by user.
        user should see user_name,email and text field.
        post field should be set by us autmotically.
        overwriting label name because django will automatically infer name from model.
    -now we want to make sure that this form is passed into template.
    -import commentsform in views.py
    -create a form and passed it to template.
        create a button 
        
Styling comment form:
    -now making this form prettier.
    -we dont want to outpuit form like this,instead we want to gain full control over,
        how it is being outputted.
    -starting by adding a div here and giving a class form-control
    -then outputting different parts of my individual controls.
        so looping through all the controls.
    -we can create a separate css file but here we are applying in post-detail.
    -we also want to style overall form so giving a id to form.
    -empty catch and hard reload after applying css.
    -Adding a title above form
    -changing to section instead of div
    -add Id to overall section from form.
    
Handling Comment form submission:
    -adding csrf token
    -adding a form action and set a url to which our request should be sent,
        when the form is submitted.
        we are setting same page as url and also add dynamic segment i.e. post.slug
    -currently haven way of handling incoming post request.
    -so for adding a more custom logic  and i dont want to use detailview,
        to just return to about details about post.
        so inheritng generic view.
    -modification to SinglePostView
        adding a get and post method
        fetch model with slug
        slug is part of url in html so gettint that in post method.
        commit=false whem doing that calling save will not hit database ,\
        but instead create a new model instance.
        and we can still edit the comment before saving to the db
    -check server side validation by removing required.
    -      
    
Comment Form validation Styles:
    -working on how we present errors
    -i.e if you removed required and try to submit then we are jumping on same page, instead of showing error box.
    -saving the comment failed as error box.
        giving a red background.
        changing label color.
        change how list of error is presented.
    -we have errorlist class for css.
    -conditionally add css class to div class='form-control' 
        add if tag to check whether form is valid or not.
    -to show error box check overall form has any error.
    -we can utilize the fact that our comment form section has an ID of comment form,
        and we can therefore link to that.
        so we can add a link in our alertbox.
        add hash symbol and use id.
    
Outputting Comments:
    -we want to show comments that belong to post and that is above this comment form.
    -need to fetch comment related to that post.
    -we already have comment model that points at post
    -on a given post we can use the comments property to fetch all the comments related to that post.
    -pass as context in get and post method.
    -render comments in template.
    -adding a new section for comments.
    -need to work on order of comment.
        any comment added at last should be rendered first like LIFO.
    -showing latest comment at top.
        we could edit our model by adding a date field.
        but we will be use id which is automatically addded for comment. this id is automatically incrementing,
        so newer comment will have higher ID.
        post.comments.all().order_by('-id')
    -now working on styling.
    
Styling the comments:
    -target comments id of section to post-detail.css
    -for styling individual comment
        #comments ul{}
        #comments li{}
   
Comment admin:
    -as a owner of this page i want to allow me to administer this comments.
    -in admin panel comments are not manageble by me.
    -users can leave comments, but i want toedit or delete comment.
    -register comment model in admin.py
    -we can control how they are displayed here by adding commentadmin class.
    -user_name is displayed but we can also manage post object beside it as name.
        overwrite str method of post model.
        how post should displayed if we needed as string.
    -adding a read later feature top of the every post which allow us to save a post for reading it later
    -we should also add a new new page where we can view all those saved posts.
        
Read Later Starting Setup:
    -
    
Managing Read later via session:
    -
    
Read later page & styling:
    -
    
Finishing Read later Feauture:
    -for this we need information whether a post is on the list 
    -go to singlepageview and we wanna know about whether this post is saved in our sessions or not.
    -

15 Deployment

Deployment considerations:
    -moving from development to deployment.
    -choose db:
        sqlite might work but might be slow or be erased (depends on hosting provider).
    -Adjust settings:
        adjust config for chosen hosting provider,disable development-only settings.
    -collect static files:
        static files are not served autmatically (just like user uploads)
    -Handle static & uploaded files serving:
        static files are not served autmatically (just like user uploads)
    -chose a host and deploy:
        also dive into host-specific docs + examples
Which Database:
    -sql or nosql:
    -sql:
        prefer sql because djuango's model system supports sit.
        mysql,postgres
Django and webserver:
    -django is python based web framework.
    -it knows how to work with incoming requests and create responses.
    -it does not listen for incoming request or handle any other server tasks.
    -python manage.py runserver in development.
    -wsgi vs asgi(know difference).  
        entry point for incoming requests.
        need to installed dedicated web server.
    
Serving static files:
    -django does not serve static or uploaded files automatically.
    -python manage.py runserver is a development only server which handles
        static files serving.
    -configure django to serve such files via urls.py
        good for small sites not performance optimized though.
    -configure web server to serve static files and django app
        sane server and device but separate processes, better for performance.\
    -use dedicated service/server for static and uploaded files
        intial setup is more complex but offers best performance
Choosing hosting provider:
    -djangoocean.
        search and they showed how to deploy a django app on they service.
    - we will use AWS.
   
Getting started & revisiting settings:
    -debug=false
    -allowed hosts will be added later.
    
Collecting static files:
    -for serving static files in production we need to colelct them.
    -static_root=base_dir/'staticfiles'
        move all static files in one folder and start serve them.
    -can merge static_root with media_root because at the end i i just static files.
        but there would be security problem.
        if we have js files which runs in the browser and which can execute code in the browser.
        if we have shared static folder where user uploads go into as well,
        users can a find a way of uploading thier own js with malicious code into ,
        that static folder and you would start serving  it.
    -python manage.py collectstatic
        all the static files will be copied into that folder.
        
Serving static files:
    -repeat same settings as media url in urls.py
    
A note about migrations:
    -making sure of all runnning migrations.
    
Locking in dependencies:
    -django package and pillow package
    -need to make sure that those dependencies are installed on the host we are going,
        to deploy our application to.host should has those package.
    -most python hosting providers support a special txt which simply lists the dependencies,
        you need.
        requirements.txt
        can populate this file mannually.
        letting python do for us
        python3 -m pip freeze  > requirements.txt
        there would be lot of unuse dependeincies.
    -create venev and install project specific requirements in that project only.
    -create venv inside of your project then vs code will detect it.
    -installing only crucial packages
        pip -m install Django Pillow
        now running requirements.txt will have less dependeicies
    -:\Django_projects\my_site>python -m venv django_my_site 
    -C:\Django_projects\my_site>c:/Django_projects/my_site/django_my_site/Scripts/activate.bat
    (django_my_site) C:\Django_projects\my_site>
    (automatically done by editor)
    -python -m pip install Django Pillow
    -(django_my_site) C:\Django_projects\my_site>python -m pip freeze > requirements.txt 
        asgiref==3.7.2
        Django==5.0.1
        pillow==10.2.0
        sqlparse==0.4.4
        tzdata==2023.4
        
Using environment vaariables:
    -allowed hosts options need to be populated
        all the domains which basically should be able to send request to this django applications,
        i.e hosting address of server which will host this appn in the end.
    -env variables allows us to use placeholder here and then a define a value,
        for the given environment variable so for that plcaeholder name.
    -from os import getenv
        this has nothing to do with venv . this is diffnt concept.
    -get_env('app_host') -> name is of our choice.
    -later we need to make sure that we provide value for app_host.
    -make sure that secret key shoudn't expose to public.
        use getenv there as well with some identifier
        we are not doing here 
    -debug=getenv('is_development',True)
        we will pass value false when we are in production.
    
Deploying with elastic beanstalk:
    -we are going to use server call elastic beanstalk.
    -application->upload your codes.
        need to combine those folders in zip files.
        create .ebextensions folder
            thats the folder specificaly for elastic beansstalk.
            in that add django.config file
                option_ settings:
                    aws:elasticbeanstalk:container:python:
                        WSGipath:my_site.wsgi:application
                        (my_site folder has wsgi.py files)
                        (we are pointing at this file here 
                        basically telling ebs that this will be
                        our entry file to which any requests should
                        be forwarded.)
                        (appn_key is also there.)
        save and creating a zip file
    -dont zip entire project folder
        mannually select one by one.
        not static folder,venv,.ebex..,
    -upload that zip file 
    -set environment propertis.
        name            value
        is_production   true #wrong is_development  false
        app_host        xxx(placeholder ,dummy here)
            that should be the actual domain for this application,
            so the domain which will be used for hosting this application.
            the problem is that in this case ,i dont know yet,
            but that will be only the case when we deploy this for the,
            first time.
    -domain is not added to allowed hosts and we need to add it.(without http or slashes)
    
SSL & custom Domains:
    -for SSL we need to add load balancer.
    -this is not available in frer tier of AWS.
    -route53-> for registering and custom domain.
    
Connecting postgreSQL:
    -search django postgresql and dive into official docs.
    -need to install package psycopg..
        pip install psycopg2-binary
        update requirements.txt file by running freeze command.
    -update db settings in settings.py
    -aws provides built in RDS server
        master username and password for accessing db
    -make sure that django app can connect this db
        change to postgre from sqlite3
        set name:    user:   pwd:    host:   port:
        can also use env variable here to make sure that we are not exposing info to public.
            if we push it to github than we might want to use a env var here.
    -run migrations and migrate
        postgres is default name of db
    -we have brand new db and no superuser exist there.
    -start dev server and also add localhost to allowed host
        not want to run locally but on ebs so..
    -create a new zip file
        and upload that updated code by going aws console.
        
Serving static files separately:
    -returning static files without touching django would be efficient.
        using efficient approach.
    -ebs is not server, its a tool that sets a server for us.
    -elastic beanstalk>environments>djangoblog-env>confuguration
        proxy server: Nginx
    -create e new config in ebs.. folder named: static-files.config
        so this file will be picked up by ebs.
        making server serve that static files separately.
        we need to tell ebs  and nginx, for which kind of URLS,which kind of
        requests it should serve which folders.
        remove both static settings in django since we are not using django for that.
        added settings according to media url and static url names.
        option_settings:
            aws:elasticbranstalk:environment:proxy:staticfiles:
                /static:staticfiles
                /files:uploads
        create a zip file and again upload
    
serving static files via S3:
    -use a service called s3
    -create a new bucket
    -when we run collectstatic command and user upload image it should be then forwarded,
        into that bucket.
    -amazon s3->django-blog-course>edit static website hosting
        enable.
    -edit cross-origin resource sharing(ORS)
    -bucket policy
        making sure that requests can reach this bucket.
        need to publicly explicit public policy
        replace example-bucket with our name
    -IAM services
        a service that allows us to grant other users or appn, access to our AWS acc,
        or to services in this account.
        set a group name.
        attach policy.
    -pip install django-storages boto3
        the django storages packages allows us to change the way django handles local files,
        and boto 3 essentially the official AWS SDK for python,
        which allow us to communicate with AWS services programmatically from inside 
        python application
        run pip freeze to update
        register a new app storages 
    -need to add aws settings
        AWS-STORAGE-BUCKET_NAME= 'bucket_name'
        AWS_S3_REGION_NAME=
        AWS_ACCESS_KEY_ID=
        AWS_SECRET_ACCESS_KEY=
        AWS_S3_CUSTOM_DOMAIN=F'{AWS_STORAGE_BUCKET_NAME}.s3amazonaws.com'
        STATICFILES_STORAGE='storages.backends.s3boto3.S3Boto3Storage'
        run collectstatic 
            it will upload to bucketfolder instead of locally
        try runserver --nostatic
        
        tell django and python how to communicate  with our AWS acc,
        because we need to give django and python some information about our acc for it to connect successfully.
    -DEFAULT_FILE_STORAGE   

Moving files uploads to S3:
    -custom_storage.py
Summary:
 




'''