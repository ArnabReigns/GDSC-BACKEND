
# GDSC BACKEND

An API made for GDSC TIU website


## Features

- User Authentication
- Session Managemenet
- Blogs


## API Reference

### Authentication

#### Get all users

```http
  GET /api/accounts/
```

#### Get all members

```http
  GET /api/accounts/memeber/
```
#### Get all students
```http
  GET /api/accounts/student/
```
#### Get all admin
```http
  GET /api/accounts/admin/
```

#### Get user

```http
  GET /api/accounts/{uid}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `uid`      | `string` | **Required**. uid of user to fetch |



