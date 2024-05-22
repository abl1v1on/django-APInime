<div align="center">
    <img src="assets/logo(1).png" width="300"><br>
    <img src="https://skillicons.dev/icons?i=python,django" width="120"/>
    <h3>
        <storng>APInime</strong> is a web application that allows users to browse and rate anime. It is built using Django and Django REST Framework.
    </h3>
</div>
<br>

## Features

- Registration, authentication and authorization of users using JWT tokens.

- CRUD oprations over anime for administrators.

- List of anime with the ability to filter by some fields, the ability to get video files of series.

- Receive email notifications when new episodes are released if the user has liked the anime and agreed to receive the newsletter when registering.

- Commentary system.

- Filtering anime by title, genres, studio names (will be updated).

- Sorting anime by title, date aired (will be updated).

- Ability to give likes to your favorite anime.

<br><br>

## Endpoints


### Create new user

`AllowAny`
~~~HTTP
POST /users/signup/ HTTP
data: {
    "email": "str",
    "password": "str",
    "password2": "str",
    "is_subscribed": "bool"
}
~~~

Example response
~~~
HTTP 201 CREATED
~~~
~~~JSON
{
    "email": "your email",
    "is_subscribed": "is subscribed"
}
~~~

<br>

### Get JWT token

`AllowAny`
~~~HTTP
POST /users/token/ HTTP
data: {
    "email": str,
    "password": str
}
~~~

Example response
~~~HTTP
HTTP 200 OK
~~~
~~~JSON
{
    "refresh": str,
    "access": str
}
~~~

<br>

### Refresh token

`AllowAny`
~~~HTTP
POST /users/token/refresh/ HTTP
data: {
    "refresh": str
}
~~~

Example response
~~~HTTP
HTTP 200 OK
~~~
~~~JSON
{
    "access": str,
    "refresh": str
}
~~~

<br>

### Get anime list 

`IsAdminOrReadOnly`
~~~HTTP
GET /anime/ HTTP
~~~

Example response
~~~HTTP
HTTP 200 OK
~~~
~~~JSON
[
    {
        "id": int,
        "rating": float,
        "views": int,
        "sudio": {
            "id": int,
            "slug": str
        },
        "likes": int,
        "title": str,
        "alt_title": str,
        "description": str,
        "type": str,
        "date_aired": date,
        "status": str,
        "duration": str,
        "cover": str,
        "slug": str,
        "genres": list
    }
]
~~~
<br>

### Create new anime
`IsAdminOrReadOnly`

~~~HTTP
POST /anime/ HTTP
headers: {
    Authorization: Bearer {your_token}
}
~~~

Example response
~~~HTTP
HTTP 201 CREATED
~~~
~~~JSON
{
    "id": int,
    "rating": float,
    "views": int,
    "sudio": {
        "id": int,
        "slug": str
    },
    "likes": int,
    "title": str,
    "alt_title": str,
    "description": str,
    "type": str,
    "date_aired": date,
    "status": str,
    "duration": str,
    "cover": str,
    "slug": str,
    "genres": list
}
~~~

<br>

### Get anime detail
`IsAdminOrReadOnly`

~~~HTTP
GET /anime/{anime_id}/ HTTP
~~~

Example response
~~~HTTP
HTTP 200 OK
~~~
~~~JSON
{
    "id": int,
    "rating": float,
    "views": int,
    "sudio": {
        "id": int,
        "slug": str
    },
    "likes": int,
    "title": str,
    "alt_title": str,
    "description": str,
    "type": str,
    "date_aired": date,
    "status": str,
    "duration": str,
    "cover": str,
    "slug": str,
    "genres": list
}
~~~

<br>

### Delete anime
`IsAdminOrReadOnly`

~~~HTTP
DELETE /anime/{anime_id}/ HTTP
headers: {
    Authorization: Bearer {your_token}
}
~~~

Example response
~~~HTTP
HTTP 204 NO CONTENT
~~~

<br>

### Update anime
`IsAdminOrReadOnly`

~~~HTTP
PATH, PUT /anime/{anime_id}/ HTTP
headers: {
    Authorization: Bearer {your_token}
}
data: {
    **new_data
}
~~~

Example response
~~~HTTP
HTTP 200 OK
~~~

~~~JSON
{
    "id": int,
    "rating": float,
    "views": int,
    "sudio": {
        "id": int,
        "slug": str
    },
    "likes": int,
    "title": str,
    "alt_title": str,
    "description": str,
    "type": str,
    "date_aired": date,
    "status": str,
    "duration": str,
    "cover": str,
    "slug": str,
    "genres": list
}
~~~

<br>

### Get anime episodes

`AllowAny`
~~~HTTP
GET /anime/episodes/ HTTP
data: {
    anime: id
}
~~~

Example response
~~~HTTP
HTTP 200 OK
~~~

~~~JSON
[
    {
        "id": int,
        "series_file": str,
        "anime_id": int
    }
]
~~~

