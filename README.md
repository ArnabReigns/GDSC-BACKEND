
# GDSC BACKEND

An API made for GDSC TIU website


## Features

- User Authentication
- Session Managemenet
- Blogs


## API Reference

### Authentication

#### Get all users

```
  GET /api/accounts/
```

#### Get all members

```
  GET /api/accounts/memeber/
```
#### Get all students
```
  GET /api/accounts/student/
```
#### Get all admin
```
  GET /api/accounts/admin/
```

#### Get user

```
  GET /api/accounts/{uid}
```
parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `uid`      | `string` | **Required**. uid of the user |

#### Get current user

```
  GET /api/accounts/currentuser/
```

#### Register User

```
  POST /api/accounts/register/
```

| data | Type     | Description                       |
| -------- | ------- | -------------------------------- |
| `name`      | `string` | **Required** |
| `email`      | `string` | **Required** |
| `password`      | `string` | **Required** |
| `gender`      | `string` | **Required**|
| `batch`      | `string` | **Required** |
| `stream`      | `string` | **Required** |
| `college_id`      | `number` | **Required**|
| `phone_number`      | `string` | **Required**|
| `linkedin_id`      | `string` | **Optional** |
| `github_id`      | `string` | **Optional** |

#### Login User

```
  POST /api/accounts/login/
```

| data | Type     | Description                       |
| -------- | ------- | -------------------------------- |
| `email`      | `string` | **Required** |
| `password`      | `string` | **Required** |

## Authorisation

Endpoints are protected with **Token Authentication**.
so you have to be a authorised user to get information from the database.
There are two ways to do it.

**1. Http Only Cookie ( Recomended ) :** Whenever a user successfully
log in, the uuid of the user will be autometically saved in
a http only cookie. you have to just send the cookies with the request.

Like in **Axios**, use :  `withCredentials: true`

```javascript
import 'axios';

axios
  .get(
    '/cookie-auth-protected-route',
    { withCredentials: true } // this should be added
  )
  .then(res => res.data)
  .catch(err => { /* not hit since no 401 */ })
  
```

**2. Authorization Header :** You can save the uuid of the logged in user
and pass the token in the header as `Token` with the request. But as it is
not secure to save the Token in local storages or cookie, it is
not the recomended way.

```javascript
import 'axios';

const token = '..your token..'

axios.get(url, {
  //...data
}, {
  headers: {
    'Token': `${token}` 
  }
})
  
```
