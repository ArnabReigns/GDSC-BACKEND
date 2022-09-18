
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
| `uid`      | `string` | **Required**. Full name of the user |

#### Get logged in user

```
  GET /api/accounts/currentuser/
```

#### Register User

```
  POST /api/accounts/register/
```

| data | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required** |
| `email`      | `string` | **Required** |
| `gender`      | `string` | **Required**|
| `batch`      | `string` | **Required** |
| `stream`      | `string` | **Required** |
| `college_id`      | `number` | **Required**|
| `phone_number`      | `string` | **Required**|
| `linkedin_id`      | `string` | **Optional** |
| `github_id`      | `string` | **Optional** |
