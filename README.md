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
~~~
POST /users/signup/ HTTP
data: {
    "email": str,
    "password": str,
    "password2": str,
    "is_subscribed": bool
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
~~~
POST /users/token/ HTTP
data: {
    "email": str,
    "password": str
}
~~~

Example response
~~~
HTTP 200 OK
~~~
~~~JSON
{
    "refresh": "str",
    "access": "str"
}
~~~

<br>

### Refresh token

`AllowAny`
~~~
POST /users/token/refresh/ HTTP
data: {
    "refresh": str
}
~~~

Example response
~~~
HTTP 200 OK
~~~
~~~JSON
{
    "access": "str",
    "refresh": "str"
}
~~~

<br>

### Get anime list 

`IsAdminOrReadOnly`
~~~
GET /anime/ HTTP
~~~

Example response
~~~
HTTP 200 OK
~~~
~~~JSON
[
    {
        "id": 0,
        "rating": 0.0,
        "views": 0,
        "sudio": {
            "id": 0,
            "slug": "string"
        },
        "likes": 0,
        "title": "string",
        "alt_title": "string",
        "description": "string",
        "type": "string",
        "date_aired": "2024-05-22",
        "status": "string",
        "duration": "string",
        "cover": "string",
        "slug": "string",
        "genres": []
    }
]
~~~
<br>

### Create new anime
`IsAdminOrReadOnly`

~~~
POST /anime/ HTTP
headers: {
    Authorization: Bearer {your_token}
}
~~~

Example response
~~~
HTTP 201 CREATED
~~~
~~~JSON
{
    "id": 0,
    "rating": 0.0,
    "views": 0,
    "sudio": {
        "id": 0,
        "slug": "string"
    },
    "likes": 0,
    "title": "string",
    "alt_title": "string",
    "description": "string",
    "type": "string",
    "date_aired": "2024-05-22",
    "status": "string",
    "duration": "string",
    "cover": "string",
    "slug": "string",
    "genres": []
}
~~~

<br>

### Get anime detail
`IsAdminOrReadOnly`

~~~
GET /anime/{anime_id}/ HTTP
~~~

Example response
~~~
HTTP 200 OK
~~~
~~~JSON
{
    "id": 0,
    "rating": 0.0,
    "views": 0,
    "sudio": {
        "id": 0,
        "slug": "string"
    },
    "likes": 0,
    "title": "string",
    "alt_title": "string",
    "description": "string",
    "type": "string",
    "date_aired": "2024-05-22",
    "status": "string",
    "duration": "string",
    "cover": "string",
    "slug": "string",
    "genres": []
}
~~~

<br>

### Delete anime
`IsAdminOrReadOnly`

~~~
DELETE /anime/{anime_id}/ HTTP
headers: {
    Authorization: Bearer {your_token}
}
~~~

Example response
~~~
HTTP 204 NO CONTENT
~~~

<br>

### Update anime
`IsAdminOrReadOnly`

~~~
PATH, PUT /anime/{anime_id}/ HTTP
headers: {
    Authorization: Bearer {your_token}
}
data: {
    **new_data
}
~~~

Example response
~~~
HTTP 200 OK
~~~

~~~JSON
{
    "id": 0,
    "rating": 0.0,
    "views": 0,
    "sudio": {
        "id": 0,
        "slug": "string"
    },
    "likes": 0,
    "title": "string",
    "alt_title": "string",
    "description": "string",
    "type": "string",
    "date_aired": "2024-05-22",
    "status": "string",
    "duration": "string",
    "cover": "string",
    "slug": "string",
    "genres": []
}
~~~

<br>

### Get anime episodes

`AllowAny`
~~~
GET /anime/episodes/ HTTP
data: {
    anime: id
}
~~~

Example response
~~~
HTTP 200 OK
~~~

~~~JSON
[
    {
        "id": 0,
        "series_file": "path_to_file",
        "anime_id": 0
    }
]
~~~

