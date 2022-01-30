
# Blog Website

This is a complete ready to deploy ```django``` based blog website with an integrated ```sqlite3```database 
and an admin panel. In admin panel the blogger can create ```n``` number of categories 
and attach the written blog to the appropriate category and maintain the collection 
of all the blogs by their categories.

This default editor in the admin panel has been changed to ```Ck Editor``` which
gives maximum facility to the blogger to add images in between the blog, custom headers
insert tables, insert emotes, text highlighter,etc.


## DEMO

[![Demo](https://img.youtube.com/vi/UQYrLCLS2bY/0.jpg)](https://www.youtube.com/watch?v=UQYrLCLS2bY)



## Deployment

To deploy this project on localhost run

```bash
    python3 manage.py runserver
```
The default web server runs on port ```8000```.If you want to change the port number
run:
```
python3 manage.py runserver <port number>
Ex: python3 manage.py runserver 1234

```

## In case of models.py modification:

Run the following commands:

```
python3 manage.py makemigrations
python3 manage.py migrate

```


### Social Media:
- [@linkedin](https://www.linkedin.com/in/devarapalli-jaya-shankar-kumar-530464230/)
- [@twitter](https://twitter.com/MrJayashankar)

