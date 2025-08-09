1. Setup Project

  - projects ecomersprj

  - Cmats new app core

  - Install Apps in Settings

  - Configure Static and Media Files in settings and Urls.py

  - Create a new view, urla and template then runserve

  - Configure template inheritance and partials

2. Configure Admin Page, Superuser and partials

  - install Jazzmin (pip intall django-jazzmin)

  - Add jazzmin is INSTALLED APPS

  - Add Jazzmier Config Code in Settings.av

  - Create database Postgres

  - Login To admin sitting

3. Custom User Model

  - Create new app userauths

  - install apps in settings

  - create custom class User in models.py

  - add AUTH_USER_MODEL in settings.py

  - comment out django.contrib.admin and admin url in settings.py

  - run makemigrations and migrate 

  - create new superuser

  - register user  model in admin.py

  - login to admin with email and password

4. user Registration system

 - Create new form class UserRegisterForm(UserCreationForm): in forms.py

  - write view to register (def registerView(request):) user

  - Configure templates to show form

  - login to website from frontend



5. User Login System

 - Write view to login (def loginView(request):)

 - Configure templates to grab input filed

 - login website from frontend

6. User Logout System

  - Write view to logout (def logoutView(request):)

  - Configure URL

  - test the Feature

7. Alerts in Django

  - Grab Alert Seppet from Bootstrap (vertion 4)

  - Capy and Paste CDN

  - Write alert conditional statement in template

8. Django Context Processor for Template

  - Create noe file contex_process.py in core app 

  - install in setting.py TEMPLATES Section list as "core.context processors.default"

  - Now Add Core for context Processor

9. Product Model Structure

  - Create new Model Class and Add filed for product

  - Register Model in admin.py

10. 
  
  - Create logic to Display only featured Product in Home Page

  - Create new view list All the Active Product from the DB

  - configure URL and Template

11. Category List View

  - Create New view to List All active categories

  - Configure Urts.py and Template

12. Product Category List View

  - Create New view to List All The Active products from the DB depending on the category selected.

  - Configure Urts.py and Template

13. Product Detail View

  - Create New view to showcase the Details of a selected Product using pid

  - Configure Urts.py and Template

14. Product Rating and Review

 - Get all reviews in Product Detail and Lists them out in the Templates

 - Calculate the average rating of the product

style="color:rgb(194, 192, 192);"

<div class="product-grid row row-cols-2 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 row-cols-xl-4 g-4">
                    <!-- <div class="product-grid row row-cols-2 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 row-cols-xl-4"> -->
                    {% for v in vendor %}
                    <div class="col">
                      <div class="card_ven">
                        <div style="display: flex;justify-content: space-between;width:40%;">
                        <h3 class="card__title">{{v.title}}</h3>
                        <i class="fa-thin fa-wrench-simple"><img width="100px"  src="{% static "images/logo.png" %}" alt="">
                        </div>
                          <p class="card__content">{{v.description|truncatewords:10}}.</p>
                        <div class="card__date">April 15, 2022</div>
                        <div class="card__arrow">
                          <a href="{% url "productsforvendor" v.vid %}" class="button" ><i class="fa-solid fa-arrow-right"></i></a>
                        </div>
                      </div>
                    </div>
                    {% endfor %}
                  <!-- </div> -->
                  
                  

                </div>
                  



                    <style>

    .card_ven {
      --border-radius: 0.75rem;
      --primary-color: #7257fa;
      --secondary-color: #3c3852;
      width: 100%; /* بدل 210px */
      font-family: "Arial";
      padding: 1rem;
      cursor: pointer;
      border-radius: var(--border-radius);
      background: #f1f1f3;
      box-shadow: 0px 8px 16px 0px rgb(0 0 0 / 3%);
      position: relative;
    }
    

.card_ven > * + * {
  margin-top: 1.1em;
}

.card_ven .card__content {
  color: var(--secondary-color);
  font-size: 0.86rem;
}

.card_ven .card__title {
  padding: 0;
  font-size: 1.3rem;
  font-weight: bold;
}

.card_ven .card__date {
  color: #6e6b80;
  font-size: 0.8rem;
}

.card_ven .card__arrow {
  position: absolute;
  background: var(--primary-color);
  padding: 0.4rem;
  border-top-left-radius: var(--border-radius);
  border-bottom-right-radius: var(--border-radius);
  bottom: 0;
  right: 0;
  transition: 0.2s;
  display: flex;
  justify-content: center;
  align-items: center;
}

.card_ven svg {
  transition: 0.2s;
}

/* hover */
.card_ven:hover .card__title {
  color: var(--primary-color);
  text-decoration: underline;
}

.card_ven:hover .card__arrow {
  background: #111;
}

.card_ven:hover .card__arrow svg {
  transform: translateX(3px);
}
  </style>