# Account Service
    Denne microservice håndterer brugerkonti, herunder registrering, autentificering og profiladministration.
    Den behandler login, logout, passwordhåndtering og brugerroller.


## Installation

1. Clone dette repository:

```bash
   git clone https://github.com/ITAKEA/account_service.git

   cd account_service

   docker build -t account_service .

   docker run -it --rm -p 5000:5000 account_service
```
2. pull docker image fra DockerHub

```
    docker run -it --rm -p 5000:5000 -v ${PWD}:/home/data clbo/account_service:latest

```

## API Endpoints

### Registrer en ny Bruger

- **URL:** `/profile`
- **Method:** `POST`
- **Request Body:** JSON

  ```json
  {
      "username": "username",
      "password": "password"
  }
  ```

- **Response:**

  - **201 Created:** User registered successfully
  - **400 Bad Request:** Username and password are required or User already exists

### View Profile

- **URL:** `/profile`
- **Method:** `GET`
- **Headers:** 

  `Authorization: username`

- **Response:**

  - **200 OK:** Returns user profile data
  - **401 Unauthorized:** User not logged in
  - **404 Not Found:** User not found

### Edit Profile

- **URL:** `/profile`
- **Method:** `PUT`
- **Response:** `201 Created`

*(Bemærk: Dette endpoint opdaterer i øjeblikket ikke nogen data og returnerer et pladsholderrespons.)*

### Login

- **URL:** `/login`
- **Method:** `POST`
- **Request Body:** JSON

  ```json
  {
      "username": "username",
      "password": "password"
  }
  ```

- **Response:**

  - **200 OK:** Login successful. Sets `Authorization` header in the response.
  - **401 Unauthorized:** Invalid username or password

### Logout

- **URL:** `/logout`
- **Method:** `POST`
- **Response:** `201 Created`

*(Bemærk: Dette endpoint returnerer i øjeblikket et pladsholderrespons og er ikke fuldt implementeret.)*

## Notes

Appen bruger i øjeblikket en liste i hukommelsen til at gemme brugerdata, hvilket bør ændres til en database som SQLite til produktionsbrug.

username bruges som autorisationstoken i headers, men denne metode er ikke sikker og bør erstattes med standard autentifikationspraksis som JWT i en reel applikation.

## License

MIT License
   