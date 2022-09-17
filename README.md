
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

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `uid`      | `string` | **Required**. uid of user to fetch |



