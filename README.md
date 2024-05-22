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

<br>

## Endpoints

### Get anime list
~~~HTTP
GET anime/ HTTP
~~~
