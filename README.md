# Heppi 🌻

Heppi is a social media site where users can share what made them smile that day.

To install, run:

```
git clone https://github.com/gracejiang/heppi
cd heppi
pip install -r requirements.txt
python3 manage.py runserver
```



## Video Demo Here

https://youtu.be/slZFT6iNvLY



## Code Organization

The code is organized the following way:

* ```heppi/```
  * ```settings.py```: Project configurations
  * ```urls.py```: All the valid URLs for this project. This is where the routing from URL to views takes place.
* ```main/```
  * ```static/```: Where all the static files are stored.
    * ```css/```: Any and all CSS files for webpage styling.
    * ```pics/```: Images used on the website.
  * ```templates/```: Where the HTML files are. These are the files that control what the user sees.
  * ```admin.py```: Where to add in custom models to edit on the /admin routing.
  * ```models.py```: All the models for this project. The main models I defined were: 
    * **Post**: A user's post
    * **Profile**: An extension of the built in Django User class
  * ```views.py```: The meat of this project tbh. Where all the logic happened between connecting the views with the models.