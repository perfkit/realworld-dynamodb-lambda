```
DELETE /__TESTUTILS__/purge
```
```
200 OK

"Purged all data!"
```
# Article
```
POST /users

{
  "user": {
    "email": "author-9q4czo@email.com",
    "username": "author-9q4czo",
    "password": "password"
  }
}
```
```
200 OK

{
  "user": {
    "email": "author-9q4czo@email.com",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImF1dGhvci05cTRjem8iLCJpYXQiOjE2MTM5NTkwNzgsImV4cCI6MTYxNDEzMTg3OH0.PuNngvvQ5AFgCsCd1Pk6MlSVj9dvbozNxnQU39stDek",
    "username": "author-9q4czo",
    "bio": "",
    "image": ""
  }
}
```
```
POST /users

{
  "user": {
    "email": "authoress-oepvov@email.com",
    "username": "authoress-oepvov",
    "password": "password"
  }
}
```
```
200 OK

{
  "user": {
    "email": "authoress-oepvov@email.com",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImF1dGhvcmVzcy1vZXB2b3YiLCJpYXQiOjE2MTM5NTkwNzgsImV4cCI6MTYxNDEzMTg3OH0.hnjmTi9xQNZBBm5FAQfMPHK39zcVDcvM10vzAPipCAo",
    "username": "authoress-oepvov",
    "bio": "",
    "image": ""
  }
}
```
```
POST /users

{
  "user": {
    "email": "non-author-3q62pg@email.com",
    "username": "non-author-3q62pg",
    "password": "password"
  }
}
```
```
200 OK

{
  "user": {
    "email": "non-author-3q62pg@email.com",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im5vbi1hdXRob3ItM3E2MnBnIiwiaWF0IjoxNjEzOTU5MDc4LCJleHAiOjE2MTQxMzE4Nzh9.PdFDfQm_THPlo7sHJEtgEvm28FZnQ7OVSKyUROvlUSQ",
    "username": "non-author-3q62pg",
    "bio": "",
    "image": ""
  }
}
```
## Create
### should create article
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description",
    "body": "body"
  }
}
```
```
200 OK

{
  "article": {
    "slug": "title-ucbf9i",
    "title": "title",
    "description": "description",
    "body": "body",
    "createdAt": 1613959078503,
    "updatedAt": 1613959078503,
    "author": {
      "username": "author-9q4czo",
      "bio": "",
      "image": "",
      "following": false
    },
    "tagList": [],
    "favorited": false,
    "favoritesCount": 0
  }
}
```
### should create article with tags
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description",
    "body": "body",
    "tagList": [
      "tag_a",
      "tag_b"
    ]
  }
}
```
```
200 OK

{
  "article": {
    "slug": "title-fbhyhu",
    "title": "title",
    "description": "description",
    "body": "body",
    "createdAt": 1613959078543,
    "updatedAt": 1613959078543,
    "author": {
      "username": "author-9q4czo",
      "bio": "",
      "image": "",
      "following": false
    },
    "tagList": [
      "tag_a",
      "tag_b"
    ],
    "favorited": false,
    "favoritesCount": 0
  }
}
```
### should disallow unauthenticated user
```
POST /articles

{}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Must be logged in."
    ]
  }
}
```
### should enforce required fields
```
POST /articles

{}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Article must be specified."
    ]
  }
}
```
```
POST /articles

{
  "article": {}
}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "title must be specified."
    ]
  }
}
```
```
POST /articles

{
  "article": {
    "title": "title"
  }
}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "description must be specified."
    ]
  }
}
```
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description"
  }
}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "body must be specified."
    ]
  }
}
```
## Get
### should get article by slug
```
GET /articles/title-ucbf9i
```
```
200 OK

{
  "article": {
    "createdAt": 1613959078503,
    "author": {
      "username": "author-9q4czo",
      "bio": "",
      "image": "",
      "following": false
    },
    "description": "description",
    "title": "title",
    "body": "body",
    "slug": "title-ucbf9i",
    "updatedAt": 1613959078503,
    "tagList": [],
    "favoritesCount": 0,
    "favorited": false
  }
}
```
### should get article with tags by slug
```
GET /articles/title-fbhyhu
```
```
200 OK

{
  "article": {
    "tagList": [
      "tag_a",
      "tag_b"
    ],
    "createdAt": 1613959078543,
    "author": {
      "username": "author-9q4czo",
      "bio": "",
      "image": "",
      "following": false
    },
    "description": "description",
    "title": "title",
    "body": "body",
    "slug": "title-fbhyhu",
    "updatedAt": 1613959078543,
    "favoritesCount": 0,
    "favorited": false
  }
}
```
### should disallow unknown slug
```
GET /articles/vk7y2
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Article not found: [vk7y2]"
    ]
  }
}
```
## Update
### should update article
```
PUT /articles/title-fbhyhu

{
  "article": {
    "title": "newtitle"
  }
}
```
```
200 OK

{
  "article": {
    "tagList": [
      "tag_a",
      "tag_b"
    ],
    "createdAt": 1613959078543,
    "author": {
      "username": "author-9q4czo",
      "bio": "",
      "image": "",
      "following": false
    },
    "description": "description",
    "title": "newtitle",
    "body": "body",
    "slug": "title-fbhyhu",
    "updatedAt": 1613959078543,
    "favoritesCount": 0,
    "favorited": false
  }
}
```
```
PUT /articles/title-fbhyhu

{
  "article": {
    "description": "newdescription"
  }
}
```
```
200 OK

{
  "article": {
    "tagList": [
      "tag_a",
      "tag_b"
    ],
    "createdAt": 1613959078543,
    "author": {
      "username": "author-9q4czo",
      "bio": "",
      "image": "",
      "following": false
    },
    "description": "newdescription",
    "title": "newtitle",
    "body": "body",
    "slug": "title-fbhyhu",
    "updatedAt": 1613959078543,
    "favoritesCount": 0,
    "favorited": false
  }
}
```
```
PUT /articles/title-fbhyhu

{
  "article": {
    "body": "newbody"
  }
}
```
```
200 OK

{
  "article": {
    "tagList": [
      "tag_a",
      "tag_b"
    ],
    "createdAt": 1613959078543,
    "author": {
      "username": "author-9q4czo",
      "bio": "",
      "image": "",
      "following": false
    },
    "description": "newdescription",
    "title": "newtitle",
    "body": "newbody",
    "slug": "title-fbhyhu",
    "updatedAt": 1613959078543,
    "favoritesCount": 0,
    "favorited": false
  }
}
```
### should disallow missing mutation
```
PUT /articles/title-fbhyhu

{}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Article mutation must be specified."
    ]
  }
}
```
### should disallow empty mutation
```
PUT /articles/title-fbhyhu

{
  "article": {}
}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "At least one field must be specified: [title, description, article]."
    ]
  }
}
```
### should disallow unauthenticated update
```
PUT /articles/title-fbhyhu

{
  "article": {
    "title": "newtitle"
  }
}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Must be logged in."
    ]
  }
}
```
### should disallow updating non-existent article
```
PUT /articles/foo-title-fbhyhu

{
  "article": {
    "title": "newtitle"
  }
}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Article not found: [foo-title-fbhyhu]"
    ]
  }
}
```
### should disallow non-author from updating
```
PUT /articles/title-fbhyhu

{
  "article": {
    "title": "newtitle"
  }
}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Article can only be updated by author: [author-9q4czo]"
    ]
  }
}
```
## Favorite
### should favorite article
```
POST /articles/title-ucbf9i/favorite

{}
```
```
200 OK

{
  "article": {
    "createdAt": 1613959078503,
    "author": {
      "username": "author-9q4czo",
      "bio": "",
      "image": "",
      "following": false
    },
    "description": "description",
    "title": "title",
    "body": "body",
    "slug": "title-ucbf9i",
    "updatedAt": 1613959078503,
    "favoritedBy": [
      "non-author-3q62pg"
    ],
    "favoritesCount": 1,
    "tagList": [],
    "favorited": true
  }
}
```
```
GET /articles/title-ucbf9i
```
```
200 OK

{
  "article": {
    "createdAt": 1613959078503,
    "author": {
      "username": "author-9q4czo",
      "bio": "",
      "image": "",
      "following": false
    },
    "description": "description",
    "title": "title",
    "body": "body",
    "favoritesCount": 1,
    "slug": "title-ucbf9i",
    "updatedAt": 1613959078503,
    "tagList": [],
    "favorited": true
  }
}
```
### should disallow favoriting by unauthenticated user
```
POST /articles/title-ucbf9i/favorite

{}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Must be logged in."
    ]
  }
}
```
### should disallow favoriting unknown article
```
POST /articles/title-ucbf9i_foo/favorite

{}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Article not found: [title-ucbf9i_foo]"
    ]
  }
}
```
### should unfavorite article
```
DELETE /articles/title-ucbf9i/favorite
```
```
200 OK

{
  "article": {
    "createdAt": 1613959078503,
    "author": {
      "username": "author-9q4czo",
      "bio": "",
      "image": "",
      "following": false
    },
    "description": "description",
    "title": "title",
    "body": "body",
    "favoritesCount": 0,
    "slug": "title-ucbf9i",
    "updatedAt": 1613959078503,
    "tagList": [],
    "favorited": false
  }
}
```
## Delete
### should delete article
```
DELETE /articles/title-ucbf9i
```
```
200 OK

{}
```
```
GET /articles/title-ucbf9i
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Article not found: [title-ucbf9i]"
    ]
  }
}
```
### should disallow deleting by unauthenticated user
```
DELETE /articles/foo
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Must be logged in."
    ]
  }
}
```
### should disallow deleting unknown article
```
DELETE /articles/foobar
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Article not found: [foobar]"
    ]
  }
}
```
### should disallow deleting article by non-author
```
DELETE /articles/title-fbhyhu
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Article can only be deleted by author: [author-9q4czo]"
    ]
  }
}
```
## List
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description",
    "body": "body",
    "tagList": [
      "g0gn2r",
      "tag_0",
      "tag_mod_2_0",
      "tag_mod_3_0"
    ]
  }
}
```
```
200 OK

{
  "article": {
    "slug": "title-l3hb20",
    "title": "title",
    "description": "description",
    "body": "body",
    "createdAt": 1613959079387,
    "updatedAt": 1613959079387,
    "author": {
      "username": "authoress-oepvov",
      "bio": "",
      "image": "",
      "following": false
    },
    "tagList": [
      "g0gn2r",
      "tag_0",
      "tag_mod_2_0",
      "tag_mod_3_0"
    ],
    "favorited": false,
    "favoritesCount": 0
  }
}
```
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description",
    "body": "body",
    "tagList": [
      "rt9tda",
      "tag_1",
      "tag_mod_2_1",
      "tag_mod_3_1"
    ]
  }
}
```
```
200 OK

{
  "article": {
    "slug": "title-t8euxc",
    "title": "title",
    "description": "description",
    "body": "body",
    "createdAt": 1613959079451,
    "updatedAt": 1613959079451,
    "author": {
      "username": "author-9q4czo",
      "bio": "",
      "image": "",
      "following": false
    },
    "tagList": [
      "rt9tda",
      "tag_1",
      "tag_mod_2_1",
      "tag_mod_3_1"
    ],
    "favorited": false,
    "favoritesCount": 0
  }
}
```
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description",
    "body": "body",
    "tagList": [
      "7v0ge2",
      "tag_2",
      "tag_mod_2_0",
      "tag_mod_3_2"
    ]
  }
}
```
```
200 OK

{
  "article": {
    "slug": "title-1qrdcc",
    "title": "title",
    "description": "description",
    "body": "body",
    "createdAt": 1613959079494,
    "updatedAt": 1613959079494,
    "author": {
      "username": "authoress-oepvov",
      "bio": "",
      "image": "",
      "following": false
    },
    "tagList": [
      "7v0ge2",
      "tag_2",
      "tag_mod_2_0",
      "tag_mod_3_2"
    ],
    "favorited": false,
    "favoritesCount": 0
  }
}
```
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description",
    "body": "body",
    "tagList": [
      "3ei9nl",
      "tag_3",
      "tag_mod_2_1",
      "tag_mod_3_0"
    ]
  }
}
```
```
200 OK

{
  "article": {
    "slug": "title-6k7lii",
    "title": "title",
    "description": "description",
    "body": "body",
    "createdAt": 1613959079533,
    "updatedAt": 1613959079533,
    "author": {
      "username": "author-9q4czo",
      "bio": "",
      "image": "",
      "following": false
    },
    "tagList": [
      "3ei9nl",
      "tag_3",
      "tag_mod_2_1",
      "tag_mod_3_0"
    ],
    "favorited": false,
    "favoritesCount": 0
  }
}
```
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description",
    "body": "body",
    "tagList": [
      "26iaze",
      "tag_4",
      "tag_mod_2_0",
      "tag_mod_3_1"
    ]
  }
}
```
```
200 OK

{
  "article": {
    "slug": "title-bi9kwd",
    "title": "title",
    "description": "description",
    "body": "body",
    "createdAt": 1613959079568,
    "updatedAt": 1613959079568,
    "author": {
      "username": "authoress-oepvov",
      "bio": "",
      "image": "",
      "following": false
    },
    "tagList": [
      "26iaze",
      "tag_4",
      "tag_mod_2_0",
      "tag_mod_3_1"
    ],
    "favorited": false,
    "favoritesCount": 0
  }
}
```
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description",
    "body": "body",
    "tagList": [
      "a7fqkf",
      "tag_5",
      "tag_mod_2_1",
      "tag_mod_3_2"
    ]
  }
}
```
```
200 OK

{
  "article": {
    "slug": "title-th8bh8",
    "title": "title",
    "description": "description",
    "body": "body",
    "createdAt": 1613959079599,
    "updatedAt": 1613959079599,
    "author": {
      "username": "author-9q4czo",
      "bio": "",
      "image": "",
      "following": false
    },
    "tagList": [
      "a7fqkf",
      "tag_5",
      "tag_mod_2_1",
      "tag_mod_3_2"
    ],
    "favorited": false,
    "favoritesCount": 0
  }
}
```
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description",
    "body": "body",
    "tagList": [
      "nyqg9p",
      "tag_6",
      "tag_mod_2_0",
      "tag_mod_3_0"
    ]
  }
}
```
```
200 OK

{
  "article": {
    "slug": "title-ro2dbv",
    "title": "title",
    "description": "description",
    "body": "body",
    "createdAt": 1613959079622,
    "updatedAt": 1613959079622,
    "author": {
      "username": "authoress-oepvov",
      "bio": "",
      "image": "",
      "following": false
    },
    "tagList": [
      "nyqg9p",
      "tag_6",
      "tag_mod_2_0",
      "tag_mod_3_0"
    ],
    "favorited": false,
    "favoritesCount": 0
  }
}
```
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description",
    "body": "body",
    "tagList": [
      "5c0ko",
      "tag_7",
      "tag_mod_2_1",
      "tag_mod_3_1"
    ]
  }
}
```
```
200 OK

{
  "article": {
    "slug": "title-1qw6jr",
    "title": "title",
    "description": "description",
    "body": "body",
    "createdAt": 1613959079652,
    "updatedAt": 1613959079652,
    "author": {
      "username": "author-9q4czo",
      "bio": "",
      "image": "",
      "following": false
    },
    "tagList": [
      "5c0ko",
      "tag_7",
      "tag_mod_2_1",
      "tag_mod_3_1"
    ],
    "favorited": false,
    "favoritesCount": 0
  }
}
```
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description",
    "body": "body",
    "tagList": [
      "hacmgy",
      "tag_8",
      "tag_mod_2_0",
      "tag_mod_3_2"
    ]
  }
}
```
```
200 OK

{
  "article": {
    "slug": "title-7r2kee",
    "title": "title",
    "description": "description",
    "body": "body",
    "createdAt": 1613959079675,
    "updatedAt": 1613959079675,
    "author": {
      "username": "authoress-oepvov",
      "bio": "",
      "image": "",
      "following": false
    },
    "tagList": [
      "hacmgy",
      "tag_8",
      "tag_mod_2_0",
      "tag_mod_3_2"
    ],
    "favorited": false,
    "favoritesCount": 0
  }
}
```
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description",
    "body": "body",
    "tagList": [
      "a2dixx",
      "tag_9",
      "tag_mod_2_1",
      "tag_mod_3_0"
    ]
  }
}
```
```
200 OK

{
  "article": {
    "slug": "title-d4my63",
    "title": "title",
    "description": "description",
    "body": "body",
    "createdAt": 1613959079699,
    "updatedAt": 1613959079699,
    "author": {
      "username": "author-9q4czo",
      "bio": "",
      "image": "",
      "following": false
    },
    "tagList": [
      "a2dixx",
      "tag_9",
      "tag_mod_2_1",
      "tag_mod_3_0"
    ],
    "favorited": false,
    "favoritesCount": 0
  }
}
```
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description",
    "body": "body",
    "tagList": [
      "usln1y",
      "tag_10",
      "tag_mod_2_0",
      "tag_mod_3_1"
    ]
  }
}
```
```
200 OK

{
  "article": {
    "slug": "title-mt7nti",
    "title": "title",
    "description": "description",
    "body": "body",
    "createdAt": 1613959079726,
    "updatedAt": 1613959079726,
    "author": {
      "username": "authoress-oepvov",
      "bio": "",
      "image": "",
      "following": false
    },
    "tagList": [
      "usln1y",
      "tag_10",
      "tag_mod_2_0",
      "tag_mod_3_1"
    ],
    "favorited": false,
    "favoritesCount": 0
  }
}
```
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description",
    "body": "body",
    "tagList": [
      "dv3sr8",
      "tag_11",
      "tag_mod_2_1",
      "tag_mod_3_2"
    ]
  }
}
```
```
200 OK

{
  "article": {
    "slug": "title-lhi34v",
    "title": "title",
    "description": "description",
    "body": "body",
    "createdAt": 1613959079748,
    "updatedAt": 1613959079748,
    "author": {
      "username": "author-9q4czo",
      "bio": "",
      "image": "",
      "following": false
    },
    "tagList": [
      "dv3sr8",
      "tag_11",
      "tag_mod_2_1",
      "tag_mod_3_2"
    ],
    "favorited": false,
    "favoritesCount": 0
  }
}
```
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description",
    "body": "body",
    "tagList": [
      "6iwbo9",
      "tag_12",
      "tag_mod_2_0",
      "tag_mod_3_0"
    ]
  }
}
```
```
200 OK

{
  "article": {
    "slug": "title-b50en4",
    "title": "title",
    "description": "description",
    "body": "body",
    "createdAt": 1613959079770,
    "updatedAt": 1613959079770,
    "author": {
      "username": "authoress-oepvov",
      "bio": "",
      "image": "",
      "following": false
    },
    "tagList": [
      "6iwbo9",
      "tag_12",
      "tag_mod_2_0",
      "tag_mod_3_0"
    ],
    "favorited": false,
    "favoritesCount": 0
  }
}
```
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description",
    "body": "body",
    "tagList": [
      "bisjqj",
      "tag_13",
      "tag_mod_2_1",
      "tag_mod_3_1"
    ]
  }
}
```
```
200 OK

{
  "article": {
    "slug": "title-3yi0em",
    "title": "title",
    "description": "description",
    "body": "body",
    "createdAt": 1613959079794,
    "updatedAt": 1613959079794,
    "author": {
      "username": "author-9q4czo",
      "bio": "",
      "image": "",
      "following": false
    },
    "tagList": [
      "bisjqj",
      "tag_13",
      "tag_mod_2_1",
      "tag_mod_3_1"
    ],
    "favorited": false,
    "favoritesCount": 0
  }
}
```
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description",
    "body": "body",
    "tagList": [
      "gi34eg",
      "tag_14",
      "tag_mod_2_0",
      "tag_mod_3_2"
    ]
  }
}
```
```
200 OK

{
  "article": {
    "slug": "title-muaeed",
    "title": "title",
    "description": "description",
    "body": "body",
    "createdAt": 1613959079820,
    "updatedAt": 1613959079820,
    "author": {
      "username": "authoress-oepvov",
      "bio": "",
      "image": "",
      "following": false
    },
    "tagList": [
      "gi34eg",
      "tag_14",
      "tag_mod_2_0",
      "tag_mod_3_2"
    ],
    "favorited": false,
    "favoritesCount": 0
  }
}
```
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description",
    "body": "body",
    "tagList": [
      "ir7631",
      "tag_15",
      "tag_mod_2_1",
      "tag_mod_3_0"
    ]
  }
}
```
```
200 OK

{
  "article": {
    "slug": "title-dbnb9u",
    "title": "title",
    "description": "description",
    "body": "body",
    "createdAt": 1613959079841,
    "updatedAt": 1613959079841,
    "author": {
      "username": "author-9q4czo",
      "bio": "",
      "image": "",
      "following": false
    },
    "tagList": [
      "ir7631",
      "tag_15",
      "tag_mod_2_1",
      "tag_mod_3_0"
    ],
    "favorited": false,
    "favoritesCount": 0
  }
}
```
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description",
    "body": "body",
    "tagList": [
      "aqbb17",
      "tag_16",
      "tag_mod_2_0",
      "tag_mod_3_1"
    ]
  }
}
```
```
200 OK

{
  "article": {
    "slug": "title-t1e72e",
    "title": "title",
    "description": "description",
    "body": "body",
    "createdAt": 1613959079868,
    "updatedAt": 1613959079868,
    "author": {
      "username": "authoress-oepvov",
      "bio": "",
      "image": "",
      "following": false
    },
    "tagList": [
      "aqbb17",
      "tag_16",
      "tag_mod_2_0",
      "tag_mod_3_1"
    ],
    "favorited": false,
    "favoritesCount": 0
  }
}
```
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description",
    "body": "body",
    "tagList": [
      "gpfuw4",
      "tag_17",
      "tag_mod_2_1",
      "tag_mod_3_2"
    ]
  }
}
```
```
200 OK

{
  "article": {
    "slug": "title-gx4nsk",
    "title": "title",
    "description": "description",
    "body": "body",
    "createdAt": 1613959079892,
    "updatedAt": 1613959079892,
    "author": {
      "username": "author-9q4czo",
      "bio": "",
      "image": "",
      "following": false
    },
    "tagList": [
      "gpfuw4",
      "tag_17",
      "tag_mod_2_1",
      "tag_mod_3_2"
    ],
    "favorited": false,
    "favoritesCount": 0
  }
}
```
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description",
    "body": "body",
    "tagList": [
      "bqttji",
      "tag_18",
      "tag_mod_2_0",
      "tag_mod_3_0"
    ]
  }
}
```
```
200 OK

{
  "article": {
    "slug": "title-hhfysh",
    "title": "title",
    "description": "description",
    "body": "body",
    "createdAt": 1613959079923,
    "updatedAt": 1613959079923,
    "author": {
      "username": "authoress-oepvov",
      "bio": "",
      "image": "",
      "following": false
    },
    "tagList": [
      "bqttji",
      "tag_18",
      "tag_mod_2_0",
      "tag_mod_3_0"
    ],
    "favorited": false,
    "favoritesCount": 0
  }
}
```
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description",
    "body": "body",
    "tagList": [
      "j22qs8",
      "tag_19",
      "tag_mod_2_1",
      "tag_mod_3_1"
    ]
  }
}
```
```
200 OK

{
  "article": {
    "slug": "title-k8owok",
    "title": "title",
    "description": "description",
    "body": "body",
    "createdAt": 1613959079947,
    "updatedAt": 1613959079947,
    "author": {
      "username": "author-9q4czo",
      "bio": "",
      "image": "",
      "following": false
    },
    "tagList": [
      "j22qs8",
      "tag_19",
      "tag_mod_2_1",
      "tag_mod_3_1"
    ],
    "favorited": false,
    "favoritesCount": 0
  }
}
```
### should list articles
```
GET /articles
```
```
200 OK

{
  "articles": [
    {
      "tagList": [
        "j22qs8",
        "tag_19",
        "tag_mod_2_1",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079947,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-k8owok",
      "updatedAt": 1613959079947,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "bqttji",
        "tag_18",
        "tag_mod_2_0",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079923,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-hhfysh",
      "updatedAt": 1613959079923,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "gpfuw4",
        "tag_17",
        "tag_mod_2_1",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079892,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-gx4nsk",
      "updatedAt": 1613959079892,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "aqbb17",
        "tag_16",
        "tag_mod_2_0",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079868,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-t1e72e",
      "updatedAt": 1613959079868,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "ir7631",
        "tag_15",
        "tag_mod_2_1",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079841,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-dbnb9u",
      "updatedAt": 1613959079841,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "gi34eg",
        "tag_14",
        "tag_mod_2_0",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079820,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-muaeed",
      "updatedAt": 1613959079820,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "bisjqj",
        "tag_13",
        "tag_mod_2_1",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079794,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-3yi0em",
      "updatedAt": 1613959079794,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "6iwbo9",
        "tag_12",
        "tag_mod_2_0",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079770,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-b50en4",
      "updatedAt": 1613959079770,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "dv3sr8",
        "tag_11",
        "tag_mod_2_1",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079748,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-lhi34v",
      "updatedAt": 1613959079748,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "tag_10",
        "tag_mod_2_0",
        "tag_mod_3_1",
        "usln1y"
      ],
      "createdAt": 1613959079726,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-mt7nti",
      "updatedAt": 1613959079726,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "a2dixx",
        "tag_9",
        "tag_mod_2_1",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079699,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-d4my63",
      "updatedAt": 1613959079699,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "hacmgy",
        "tag_8",
        "tag_mod_2_0",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079675,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-7r2kee",
      "updatedAt": 1613959079675,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "5c0ko",
        "tag_7",
        "tag_mod_2_1",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079652,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-1qw6jr",
      "updatedAt": 1613959079652,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "nyqg9p",
        "tag_6",
        "tag_mod_2_0",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079622,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-ro2dbv",
      "updatedAt": 1613959079622,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "a7fqkf",
        "tag_5",
        "tag_mod_2_1",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079599,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-th8bh8",
      "updatedAt": 1613959079599,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "26iaze",
        "tag_4",
        "tag_mod_2_0",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079568,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-bi9kwd",
      "updatedAt": 1613959079568,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "3ei9nl",
        "tag_3",
        "tag_mod_2_1",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079533,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-6k7lii",
      "updatedAt": 1613959079533,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "7v0ge2",
        "tag_2",
        "tag_mod_2_0",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079494,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-1qrdcc",
      "updatedAt": 1613959079494,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "rt9tda",
        "tag_1",
        "tag_mod_2_1",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079451,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-t8euxc",
      "updatedAt": 1613959079451,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "g0gn2r",
        "tag_0",
        "tag_mod_2_0",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079387,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-l3hb20",
      "updatedAt": 1613959079387,
      "favoritesCount": 0,
      "favorited": false
    }
  ]
}
```
### should list articles with tag
```
GET /articles?tag=tag_7
```
```
200 OK

{
  "articles": [
    {
      "tagList": [
        "5c0ko",
        "tag_7",
        "tag_mod_2_1",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079652,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-1qw6jr",
      "updatedAt": 1613959079652,
      "favoritesCount": 0,
      "favorited": false
    }
  ]
}
```
```
GET /articles?tag=tag_mod_3_2
```
```
200 OK

{
  "articles": [
    {
      "tagList": [
        "gpfuw4",
        "tag_17",
        "tag_mod_2_1",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079892,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-gx4nsk",
      "updatedAt": 1613959079892,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "gi34eg",
        "tag_14",
        "tag_mod_2_0",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079820,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-muaeed",
      "updatedAt": 1613959079820,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "dv3sr8",
        "tag_11",
        "tag_mod_2_1",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079748,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-lhi34v",
      "updatedAt": 1613959079748,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "hacmgy",
        "tag_8",
        "tag_mod_2_0",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079675,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-7r2kee",
      "updatedAt": 1613959079675,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "a7fqkf",
        "tag_5",
        "tag_mod_2_1",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079599,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-th8bh8",
      "updatedAt": 1613959079599,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "7v0ge2",
        "tag_2",
        "tag_mod_2_0",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079494,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-1qrdcc",
      "updatedAt": 1613959079494,
      "favoritesCount": 0,
      "favorited": false
    }
  ]
}
```
### should list articles by author
```
GET /articles?author=authoress-oepvov
```
```
200 OK

{
  "articles": [
    {
      "tagList": [
        "bqttji",
        "tag_18",
        "tag_mod_2_0",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079923,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-hhfysh",
      "updatedAt": 1613959079923,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "aqbb17",
        "tag_16",
        "tag_mod_2_0",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079868,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-t1e72e",
      "updatedAt": 1613959079868,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "gi34eg",
        "tag_14",
        "tag_mod_2_0",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079820,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-muaeed",
      "updatedAt": 1613959079820,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "6iwbo9",
        "tag_12",
        "tag_mod_2_0",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079770,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-b50en4",
      "updatedAt": 1613959079770,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "tag_10",
        "tag_mod_2_0",
        "tag_mod_3_1",
        "usln1y"
      ],
      "createdAt": 1613959079726,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-mt7nti",
      "updatedAt": 1613959079726,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "hacmgy",
        "tag_8",
        "tag_mod_2_0",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079675,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-7r2kee",
      "updatedAt": 1613959079675,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "nyqg9p",
        "tag_6",
        "tag_mod_2_0",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079622,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-ro2dbv",
      "updatedAt": 1613959079622,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "26iaze",
        "tag_4",
        "tag_mod_2_0",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079568,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-bi9kwd",
      "updatedAt": 1613959079568,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "7v0ge2",
        "tag_2",
        "tag_mod_2_0",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079494,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-1qrdcc",
      "updatedAt": 1613959079494,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "g0gn2r",
        "tag_0",
        "tag_mod_2_0",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079387,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-l3hb20",
      "updatedAt": 1613959079387,
      "favoritesCount": 0,
      "favorited": false
    }
  ]
}
```
### should list articles favorited by user
```
GET /articles?favorited=non-author-3q62pg
```
```
200 OK

{
  "articles": []
}
```
### should list articles by limit/offset
```
GET /articles?author=author-9q4czo&limit=2
```
```
200 OK

{
  "articles": [
    {
      "tagList": [
        "j22qs8",
        "tag_19",
        "tag_mod_2_1",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079947,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-k8owok",
      "updatedAt": 1613959079947,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "gpfuw4",
        "tag_17",
        "tag_mod_2_1",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079892,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-gx4nsk",
      "updatedAt": 1613959079892,
      "favoritesCount": 0,
      "favorited": false
    }
  ]
}
```
```
GET /articles?author=author-9q4czo&limit=2&offset=2
```
```
200 OK

{
  "articles": [
    {
      "tagList": [
        "ir7631",
        "tag_15",
        "tag_mod_2_1",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079841,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-dbnb9u",
      "updatedAt": 1613959079841,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "bisjqj",
        "tag_13",
        "tag_mod_2_1",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079794,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-3yi0em",
      "updatedAt": 1613959079794,
      "favoritesCount": 0,
      "favorited": false
    }
  ]
}
```
### should list articles when authenticated
```
GET /articles
```
```
200 OK

{
  "articles": [
    {
      "tagList": [
        "j22qs8",
        "tag_19",
        "tag_mod_2_1",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079947,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-k8owok",
      "updatedAt": 1613959079947,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "bqttji",
        "tag_18",
        "tag_mod_2_0",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079923,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-hhfysh",
      "updatedAt": 1613959079923,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "gpfuw4",
        "tag_17",
        "tag_mod_2_1",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079892,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-gx4nsk",
      "updatedAt": 1613959079892,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "aqbb17",
        "tag_16",
        "tag_mod_2_0",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079868,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-t1e72e",
      "updatedAt": 1613959079868,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "ir7631",
        "tag_15",
        "tag_mod_2_1",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079841,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-dbnb9u",
      "updatedAt": 1613959079841,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "gi34eg",
        "tag_14",
        "tag_mod_2_0",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079820,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-muaeed",
      "updatedAt": 1613959079820,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "bisjqj",
        "tag_13",
        "tag_mod_2_1",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079794,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-3yi0em",
      "updatedAt": 1613959079794,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "6iwbo9",
        "tag_12",
        "tag_mod_2_0",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079770,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-b50en4",
      "updatedAt": 1613959079770,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "dv3sr8",
        "tag_11",
        "tag_mod_2_1",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079748,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-lhi34v",
      "updatedAt": 1613959079748,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "tag_10",
        "tag_mod_2_0",
        "tag_mod_3_1",
        "usln1y"
      ],
      "createdAt": 1613959079726,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-mt7nti",
      "updatedAt": 1613959079726,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "a2dixx",
        "tag_9",
        "tag_mod_2_1",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079699,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-d4my63",
      "updatedAt": 1613959079699,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "hacmgy",
        "tag_8",
        "tag_mod_2_0",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079675,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-7r2kee",
      "updatedAt": 1613959079675,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "5c0ko",
        "tag_7",
        "tag_mod_2_1",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079652,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-1qw6jr",
      "updatedAt": 1613959079652,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "nyqg9p",
        "tag_6",
        "tag_mod_2_0",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079622,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-ro2dbv",
      "updatedAt": 1613959079622,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "a7fqkf",
        "tag_5",
        "tag_mod_2_1",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079599,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-th8bh8",
      "updatedAt": 1613959079599,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "26iaze",
        "tag_4",
        "tag_mod_2_0",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079568,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-bi9kwd",
      "updatedAt": 1613959079568,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "3ei9nl",
        "tag_3",
        "tag_mod_2_1",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079533,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-6k7lii",
      "updatedAt": 1613959079533,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "7v0ge2",
        "tag_2",
        "tag_mod_2_0",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079494,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-1qrdcc",
      "updatedAt": 1613959079494,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "rt9tda",
        "tag_1",
        "tag_mod_2_1",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079451,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-t8euxc",
      "updatedAt": 1613959079451,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "g0gn2r",
        "tag_0",
        "tag_mod_2_0",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079387,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": false
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-l3hb20",
      "updatedAt": 1613959079387,
      "favoritesCount": 0,
      "favorited": false
    }
  ]
}
```
### should disallow multiple of author/tag/favorited
```
GET /articles?tag=foo&author=bar
```
```
GET /articles?author=foo&favorited=bar
```
```
GET /articles?favorited=foo&tag=bar
```
## Feed
### should get feed
```
GET /articles/feed
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Only one of these can be specified: [tag, author, favorited]"
    ]
  }
}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Only one of these can be specified: [tag, author, favorited]"
    ]
  }
}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Only one of these can be specified: [tag, author, favorited]"
    ]
  }
}
```
```
200 OK

{
  "articles": []
}
```
```
POST /profiles/authoress-oepvov/follow

{}
```
```
200 OK

{
  "profile": {
    "username": "authoress-oepvov",
    "bio": "",
    "image": "",
    "following": true
  }
}
```
```
GET /articles/feed
```
```
200 OK

{
  "articles": [
    {
      "tagList": [
        "bqttji",
        "tag_18",
        "tag_mod_2_0",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079923,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-hhfysh",
      "updatedAt": 1613959079923,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "aqbb17",
        "tag_16",
        "tag_mod_2_0",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079868,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-t1e72e",
      "updatedAt": 1613959079868,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "gi34eg",
        "tag_14",
        "tag_mod_2_0",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079820,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-muaeed",
      "updatedAt": 1613959079820,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "6iwbo9",
        "tag_12",
        "tag_mod_2_0",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079770,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-b50en4",
      "updatedAt": 1613959079770,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "tag_10",
        "tag_mod_2_0",
        "tag_mod_3_1",
        "usln1y"
      ],
      "createdAt": 1613959079726,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-mt7nti",
      "updatedAt": 1613959079726,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "hacmgy",
        "tag_8",
        "tag_mod_2_0",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079675,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-7r2kee",
      "updatedAt": 1613959079675,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "nyqg9p",
        "tag_6",
        "tag_mod_2_0",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079622,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-ro2dbv",
      "updatedAt": 1613959079622,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "26iaze",
        "tag_4",
        "tag_mod_2_0",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079568,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-bi9kwd",
      "updatedAt": 1613959079568,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "7v0ge2",
        "tag_2",
        "tag_mod_2_0",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079494,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-1qrdcc",
      "updatedAt": 1613959079494,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "g0gn2r",
        "tag_0",
        "tag_mod_2_0",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079387,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-l3hb20",
      "updatedAt": 1613959079387,
      "favoritesCount": 0,
      "favorited": false
    }
  ]
}
```
```
POST /profiles/author-9q4czo/follow

{}
```
```
200 OK

{
  "profile": {
    "username": "author-9q4czo",
    "bio": "",
    "image": "",
    "following": true
  }
}
```
```
GET /articles/feed
```
```
200 OK

{
  "articles": [
    {
      "tagList": [
        "j22qs8",
        "tag_19",
        "tag_mod_2_1",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079947,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-k8owok",
      "updatedAt": 1613959079947,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "bqttji",
        "tag_18",
        "tag_mod_2_0",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079923,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-hhfysh",
      "updatedAt": 1613959079923,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "gpfuw4",
        "tag_17",
        "tag_mod_2_1",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079892,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-gx4nsk",
      "updatedAt": 1613959079892,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "aqbb17",
        "tag_16",
        "tag_mod_2_0",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079868,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-t1e72e",
      "updatedAt": 1613959079868,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "ir7631",
        "tag_15",
        "tag_mod_2_1",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079841,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-dbnb9u",
      "updatedAt": 1613959079841,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "gi34eg",
        "tag_14",
        "tag_mod_2_0",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079820,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-muaeed",
      "updatedAt": 1613959079820,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "bisjqj",
        "tag_13",
        "tag_mod_2_1",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079794,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-3yi0em",
      "updatedAt": 1613959079794,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "6iwbo9",
        "tag_12",
        "tag_mod_2_0",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079770,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-b50en4",
      "updatedAt": 1613959079770,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "dv3sr8",
        "tag_11",
        "tag_mod_2_1",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079748,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-lhi34v",
      "updatedAt": 1613959079748,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "tag_10",
        "tag_mod_2_0",
        "tag_mod_3_1",
        "usln1y"
      ],
      "createdAt": 1613959079726,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-mt7nti",
      "updatedAt": 1613959079726,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "a2dixx",
        "tag_9",
        "tag_mod_2_1",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079699,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-d4my63",
      "updatedAt": 1613959079699,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "hacmgy",
        "tag_8",
        "tag_mod_2_0",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079675,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-7r2kee",
      "updatedAt": 1613959079675,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "5c0ko",
        "tag_7",
        "tag_mod_2_1",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079652,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-1qw6jr",
      "updatedAt": 1613959079652,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "nyqg9p",
        "tag_6",
        "tag_mod_2_0",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079622,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-ro2dbv",
      "updatedAt": 1613959079622,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "a7fqkf",
        "tag_5",
        "tag_mod_2_1",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079599,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-th8bh8",
      "updatedAt": 1613959079599,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "26iaze",
        "tag_4",
        "tag_mod_2_0",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079568,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-bi9kwd",
      "updatedAt": 1613959079568,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "3ei9nl",
        "tag_3",
        "tag_mod_2_1",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079533,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-6k7lii",
      "updatedAt": 1613959079533,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "7v0ge2",
        "tag_2",
        "tag_mod_2_0",
        "tag_mod_3_2"
      ],
      "createdAt": 1613959079494,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-1qrdcc",
      "updatedAt": 1613959079494,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "rt9tda",
        "tag_1",
        "tag_mod_2_1",
        "tag_mod_3_1"
      ],
      "createdAt": 1613959079451,
      "author": {
        "username": "author-9q4czo",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-t8euxc",
      "updatedAt": 1613959079451,
      "favoritesCount": 0,
      "favorited": false
    },
    {
      "tagList": [
        "g0gn2r",
        "tag_0",
        "tag_mod_2_0",
        "tag_mod_3_0"
      ],
      "createdAt": 1613959079387,
      "author": {
        "username": "authoress-oepvov",
        "bio": "",
        "image": "",
        "following": true
      },
      "description": "description",
      "title": "title",
      "body": "body",
      "slug": "title-l3hb20",
      "updatedAt": 1613959079387,
      "favoritesCount": 0,
      "favorited": false
    }
  ]
}
```
### should disallow unauthenticated feed
```
GET /articles/feed
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Must be logged in."
    ]
  }
}
```
## Tags
### should get tags
```
GET /tags
```
```
200 OK

{
  "tags": [
    "tag_10",
    "tag_mod_2_0",
    "tag_mod_3_1",
    "usln1y",
    "nyqg9p",
    "tag_6",
    "tag_mod_3_0",
    "ir7631",
    "tag_15",
    "tag_mod_2_1",
    "bisjqj",
    "tag_13",
    "rt9tda",
    "tag_1",
    "dv3sr8",
    "tag_11",
    "tag_mod_3_2",
    "7v0ge2",
    "tag_2",
    "tag_a",
    "tag_b",
    "a2dixx",
    "tag_9",
    "bqttji",
    "tag_18",
    "5c0ko",
    "tag_7",
    "j22qs8",
    "tag_19",
    "6iwbo9",
    "tag_12",
    "a7fqkf",
    "tag_5",
    "26iaze",
    "tag_4",
    "hacmgy",
    "tag_8",
    "aqbb17",
    "tag_16",
    "g0gn2r",
    "tag_0",
    "3ei9nl",
    "tag_3",
    "gpfuw4",
    "tag_17",
    "gi34eg",
    "tag_14"
  ]
}
```
# Comment
```
POST /users

{
  "user": {
    "email": "author-u0xqfr@email.com",
    "username": "author-u0xqfr",
    "password": "password"
  }
}
```
```
200 OK

{
  "user": {
    "email": "author-u0xqfr@email.com",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImF1dGhvci11MHhxZnIiLCJpYXQiOjE2MTM5NTkwODEsImV4cCI6MTYxNDEzMTg4MX0.E8155uyFsWtWg-jQ7KB5llIFVoSLKdrSvzPOeB0o2Tk",
    "username": "author-u0xqfr",
    "bio": "",
    "image": ""
  }
}
```
```
POST /users

{
  "user": {
    "email": "commenter-hk1xiz@email.com",
    "username": "commenter-hk1xiz",
    "password": "password"
  }
}
```
```
200 OK

{
  "user": {
    "email": "commenter-hk1xiz@email.com",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNvbW1lbnRlci1oazF4aXoiLCJpYXQiOjE2MTM5NTkwODEsImV4cCI6MTYxNDEzMTg4MX0.ka3A9Cs0dI3LJ5ypY-6QL-pYPTvR749rDZva-fRlrN4",
    "username": "commenter-hk1xiz",
    "bio": "",
    "image": ""
  }
}
```
```
POST /articles

{
  "article": {
    "title": "title",
    "description": "description",
    "body": "body"
  }
}
```
```
200 OK

{
  "article": {
    "slug": "title-blom0i",
    "title": "title",
    "description": "description",
    "body": "body",
    "createdAt": 1613959081163,
    "updatedAt": 1613959081163,
    "author": {
      "username": "author-u0xqfr",
      "bio": "",
      "image": "",
      "following": false
    },
    "tagList": [],
    "favorited": false,
    "favoritesCount": 0
  }
}
```
## Create
### should create comment
```
POST /articles/title-blom0i/comments

{
  "comment": {
    "body": "test comment ya5lvd"
  }
}
```
```
200 OK

{
  "comment": {
    "id": "fcab6087-0764-4dbe-985c-02d119264c81",
    "slug": "title-blom0i",
    "body": "test comment ya5lvd",
    "createdAt": 1613959081188,
    "updatedAt": 1613959081188,
    "author": {
      "username": "commenter-hk1xiz",
      "bio": "",
      "image": "",
      "following": false
    }
  }
}
```
```
POST /articles/title-blom0i/comments

{
  "comment": {
    "body": "test comment 5u736i"
  }
}
```
```
200 OK

{
  "comment": {
    "id": "662b714f-5689-419c-9647-addef92ecf13",
    "slug": "title-blom0i",
    "body": "test comment 5u736i",
    "createdAt": 1613959081225,
    "updatedAt": 1613959081225,
    "author": {
      "username": "commenter-hk1xiz",
      "bio": "",
      "image": "",
      "following": false
    }
  }
}
```
```
POST /articles/title-blom0i/comments

{
  "comment": {
    "body": "test comment g33iex"
  }
}
```
```
200 OK

{
  "comment": {
    "id": "2b3fcc44-ae9b-49fe-9fdf-15cf0f4426aa",
    "slug": "title-blom0i",
    "body": "test comment g33iex",
    "createdAt": 1613959081263,
    "updatedAt": 1613959081263,
    "author": {
      "username": "commenter-hk1xiz",
      "bio": "",
      "image": "",
      "following": false
    }
  }
}
```
```
POST /articles/title-blom0i/comments

{
  "comment": {
    "body": "test comment sj46h7"
  }
}
```
```
200 OK

{
  "comment": {
    "id": "3de0b514-6f4a-43e8-9fa7-6faef952aa1d",
    "slug": "title-blom0i",
    "body": "test comment sj46h7",
    "createdAt": 1613959081360,
    "updatedAt": 1613959081360,
    "author": {
      "username": "commenter-hk1xiz",
      "bio": "",
      "image": "",
      "following": false
    }
  }
}
```
```
POST /articles/title-blom0i/comments

{
  "comment": {
    "body": "test comment p4p48a"
  }
}
```
```
200 OK

{
  "comment": {
    "id": "39caafdd-9f33-4c0d-814b-5428963d4916",
    "slug": "title-blom0i",
    "body": "test comment p4p48a",
    "createdAt": 1613959081410,
    "updatedAt": 1613959081410,
    "author": {
      "username": "commenter-hk1xiz",
      "bio": "",
      "image": "",
      "following": false
    }
  }
}
```
```
POST /articles/title-blom0i/comments

{
  "comment": {
    "body": "test comment dwmtn"
  }
}
```
```
200 OK

{
  "comment": {
    "id": "950b73f5-3324-47e7-8628-2b5205518a8b",
    "slug": "title-blom0i",
    "body": "test comment dwmtn",
    "createdAt": 1613959081448,
    "updatedAt": 1613959081448,
    "author": {
      "username": "commenter-hk1xiz",
      "bio": "",
      "image": "",
      "following": false
    }
  }
}
```
```
POST /articles/title-blom0i/comments

{
  "comment": {
    "body": "test comment 8ca0u1"
  }
}
```
```
200 OK

{
  "comment": {
    "id": "909344a3-9740-46e9-bf71-aa921be93481",
    "slug": "title-blom0i",
    "body": "test comment 8ca0u1",
    "createdAt": 1613959081484,
    "updatedAt": 1613959081484,
    "author": {
      "username": "commenter-hk1xiz",
      "bio": "",
      "image": "",
      "following": false
    }
  }
}
```
```
POST /articles/title-blom0i/comments

{
  "comment": {
    "body": "test comment v7pbq6"
  }
}
```
```
200 OK

{
  "comment": {
    "id": "e998e58d-f543-49ef-b2ee-42b0f39cfe0f",
    "slug": "title-blom0i",
    "body": "test comment v7pbq6",
    "createdAt": 1613959081516,
    "updatedAt": 1613959081516,
    "author": {
      "username": "commenter-hk1xiz",
      "bio": "",
      "image": "",
      "following": false
    }
  }
}
```
```
POST /articles/title-blom0i/comments

{
  "comment": {
    "body": "test comment v4i246"
  }
}
```
```
200 OK

{
  "comment": {
    "id": "dcf7aff9-3ca2-4983-976c-3086e0d35bdc",
    "slug": "title-blom0i",
    "body": "test comment v4i246",
    "createdAt": 1613959081548,
    "updatedAt": 1613959081548,
    "author": {
      "username": "commenter-hk1xiz",
      "bio": "",
      "image": "",
      "following": false
    }
  }
}
```
```
POST /articles/title-blom0i/comments

{
  "comment": {
    "body": "test comment ysf7ht"
  }
}
```
```
200 OK

{
  "comment": {
    "id": "0c2394c6-d3ef-4f47-b2bd-214638dbbc05",
    "slug": "title-blom0i",
    "body": "test comment ysf7ht",
    "createdAt": 1613959081582,
    "updatedAt": 1613959081582,
    "author": {
      "username": "commenter-hk1xiz",
      "bio": "",
      "image": "",
      "following": false
    }
  }
}
```
### should disallow unauthenticated user
```
POST /articles/title-blom0i/comments

{}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Must be logged in."
    ]
  }
}
```
### should enforce comment body
```
POST /articles/title-blom0i/comments

{}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Comment must be specified."
    ]
  }
}
```
### should disallow non-existent article
```
POST /articles/foobar/comments

{
  "comment": {
    "body": "test comment trri80"
  }
}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Article not found: [foobar]"
    ]
  }
}
```
## Get
### should get all comments for article
```
GET /articles/title-blom0i/comments
```
```
200 OK

{
  "comments": [
    {
      "createdAt": 1613959081448,
      "id": "950b73f5-3324-47e7-8628-2b5205518a8b",
      "body": "test comment dwmtn",
      "slug": "title-blom0i",
      "author": {
        "username": "commenter-hk1xiz",
        "bio": "",
        "image": "",
        "following": false
      },
      "updatedAt": 1613959081448
    },
    {
      "createdAt": 1613959081263,
      "id": "2b3fcc44-ae9b-49fe-9fdf-15cf0f4426aa",
      "body": "test comment g33iex",
      "slug": "title-blom0i",
      "author": {
        "username": "commenter-hk1xiz",
        "bio": "",
        "image": "",
        "following": false
      },
      "updatedAt": 1613959081263
    },
    {
      "createdAt": 1613959081516,
      "id": "e998e58d-f543-49ef-b2ee-42b0f39cfe0f",
      "body": "test comment v7pbq6",
      "slug": "title-blom0i",
      "author": {
        "username": "commenter-hk1xiz",
        "bio": "",
        "image": "",
        "following": false
      },
      "updatedAt": 1613959081516
    },
    {
      "createdAt": 1613959081582,
      "id": "0c2394c6-d3ef-4f47-b2bd-214638dbbc05",
      "body": "test comment ysf7ht",
      "slug": "title-blom0i",
      "author": {
        "username": "commenter-hk1xiz",
        "bio": "",
        "image": "",
        "following": false
      },
      "updatedAt": 1613959081582
    },
    {
      "createdAt": 1613959081484,
      "id": "909344a3-9740-46e9-bf71-aa921be93481",
      "body": "test comment 8ca0u1",
      "slug": "title-blom0i",
      "author": {
        "username": "commenter-hk1xiz",
        "bio": "",
        "image": "",
        "following": false
      },
      "updatedAt": 1613959081484
    },
    {
      "createdAt": 1613959081548,
      "id": "dcf7aff9-3ca2-4983-976c-3086e0d35bdc",
      "body": "test comment v4i246",
      "slug": "title-blom0i",
      "author": {
        "username": "commenter-hk1xiz",
        "bio": "",
        "image": "",
        "following": false
      },
      "updatedAt": 1613959081548
    },
    {
      "createdAt": 1613959081360,
      "id": "3de0b514-6f4a-43e8-9fa7-6faef952aa1d",
      "body": "test comment sj46h7",
      "slug": "title-blom0i",
      "author": {
        "username": "commenter-hk1xiz",
        "bio": "",
        "image": "",
        "following": false
      },
      "updatedAt": 1613959081360
    },
    {
      "createdAt": 1613959081410,
      "id": "39caafdd-9f33-4c0d-814b-5428963d4916",
      "body": "test comment p4p48a",
      "slug": "title-blom0i",
      "author": {
        "username": "commenter-hk1xiz",
        "bio": "",
        "image": "",
        "following": false
      },
      "updatedAt": 1613959081410
    },
    {
      "createdAt": 1613959081188,
      "id": "fcab6087-0764-4dbe-985c-02d119264c81",
      "body": "test comment ya5lvd",
      "slug": "title-blom0i",
      "author": {
        "username": "commenter-hk1xiz",
        "bio": "",
        "image": "",
        "following": false
      },
      "updatedAt": 1613959081188
    },
    {
      "createdAt": 1613959081225,
      "id": "662b714f-5689-419c-9647-addef92ecf13",
      "body": "test comment 5u736i",
      "slug": "title-blom0i",
      "author": {
        "username": "commenter-hk1xiz",
        "bio": "",
        "image": "",
        "following": false
      },
      "updatedAt": 1613959081225
    }
  ]
}
```
## Delete
### should delete comment
```
DELETE /articles/title-blom0i/comments/fcab6087-0764-4dbe-985c-02d119264c81
```
```
200 OK

{}
```
### only comment author should be able to delete comment
```
DELETE /articles/title-blom0i/comments/662b714f-5689-419c-9647-addef92ecf13
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Only comment author can delete: [commenter-hk1xiz]"
    ]
  }
}
```
### should disallow unauthenticated user
```
DELETE /articles/title-blom0i/comments/662b714f-5689-419c-9647-addef92ecf13
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Must be logged in."
    ]
  }
}
```
### should disallow deleting unknown comment
```
DELETE /articles/title-blom0i/comments/foobar_id
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Comment ID not found: [foobar_id]"
    ]
  }
}
```
# User
## Create
### should create user
```
POST /users

{
  "user": {
    "email": "user1-0.v9b5xff4a0h@email.com",
    "username": "user1-0.v9b5xff4a0h",
    "password": "password"
  }
}
```
```
200 OK

{
  "user": {
    "email": "user1-0.v9b5xff4a0h@email.com",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXIxLTAudjliNXhmZjRhMGgiLCJpYXQiOjE2MTM5NTkwODEsImV4cCI6MTYxNDEzMTg4MX0.DswTa-bI3uUyQPDbfAeQzmw8IyNdSDvVk14HgInteLA",
    "username": "user1-0.v9b5xff4a0h",
    "bio": "",
    "image": ""
  }
}
```
### should disallow same username
```
POST /users

{
  "user": {
    "email": "user1-0.v9b5xff4a0h@email.com",
    "username": "user1-0.v9b5xff4a0h",
    "password": "password"
  }
}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Username already taken: [user1-0.v9b5xff4a0h]"
    ]
  }
}
```
### should disallow same email
```
POST /users

{
  "user": {
    "username": "user2",
    "email": "user1-0.v9b5xff4a0h@email.com",
    "password": "password"
  }
}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Email already taken: [user1-0.v9b5xff4a0h@email.com]"
    ]
  }
}
```
### should enforce required fields
```
POST /users

{}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "User must be specified."
    ]
  }
}
```
```
POST /users

{
  "user": {
    "foo": 1
  }
}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Username must be specified."
    ]
  }
}
```
```
POST /users

{
  "user": {
    "username": 1
  }
}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Email must be specified."
    ]
  }
}
```
```
POST /users

{
  "user": {
    "username": 1,
    "email": 2
  }
}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Password must be specified."
    ]
  }
}
```
## Login
### should login
```
POST /users/login

{
  "user": {
    "email": "user1-0.v9b5xff4a0h@email.com",
    "password": "password"
  }
}
```
```
200 OK

{
  "user": {
    "email": "user1-0.v9b5xff4a0h@email.com",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXIxLTAudjliNXhmZjRhMGgiLCJpYXQiOjE2MTM5NTkwODEsImV4cCI6MTYxNDEzMTg4MX0.DswTa-bI3uUyQPDbfAeQzmw8IyNdSDvVk14HgInteLA",
    "username": "user1-0.v9b5xff4a0h",
    "bio": "",
    "image": ""
  }
}
```
### should disallow unknown email
```
POST /users/login

{
  "user": {
    "email": "0.0j5hmjnpon1s",
    "password": "somepassword"
  }
}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Email not found: [0.0j5hmjnpon1s]"
    ]
  }
}
```
### should disallow wrong password
```
POST /users/login

{
  "user": {
    "email": "user1-0.v9b5xff4a0h@email.com",
    "password": "0.t640egxn8qg"
  }
}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Wrong password."
    ]
  }
}
```
### should enforce required fields
```
POST /users/login

{}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "User must be specified."
    ]
  }
}
```
```
POST /users/login

{
  "user": {}
}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Email must be specified."
    ]
  }
}
```
```
POST /users/login

{
  "user": {
    "email": "someemail"
  }
}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Password must be specified."
    ]
  }
}
```
## Get
### should get current user
```
GET /user
```
```
200 OK

{
  "user": {
    "email": "user1-0.v9b5xff4a0h@email.com",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXIxLTAudjliNXhmZjRhMGgiLCJpYXQiOjE2MTM5NTkwODEsImV4cCI6MTYxNDEzMTg4MX0.DswTa-bI3uUyQPDbfAeQzmw8IyNdSDvVk14HgInteLA",
    "username": "user1-0.v9b5xff4a0h",
    "bio": "",
    "image": ""
  }
}
```
### should disallow bad tokens
```
GET /user
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Token not present or invalid."
    ]
  }
}
```
```
GET /user
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Token not present or invalid."
    ]
  }
}
```
```
GET /user
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Token not present or invalid."
    ]
  }
}
```
```
GET /user
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Token not present or invalid."
    ]
  }
}
```
## Profile
### should get profile
```
GET /profiles/user1-0.v9b5xff4a0h
```
```
200 OK

{
  "profile": {
    "username": "user1-0.v9b5xff4a0h",
    "bio": "",
    "image": "",
    "following": false
  }
}
```
### should disallow unknown username
```
GET /profiles/foo_0.ub7xot3olh
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "User not found: [foo_0.ub7xot3olh]"
    ]
  }
}
```
### should follow/unfollow user
```
POST /users

{
  "user": {
    "username": "followed_user",
    "email": "followed_user@mail.com",
    "password": "password"
  }
}
```
```
200 OK

{
  "user": {
    "email": "followed_user@mail.com",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImZvbGxvd2VkX3VzZXIiLCJpYXQiOjE2MTM5NTkwODIsImV4cCI6MTYxNDEzMTg4Mn0.zh2G5BxlJGxRrLrW5Ji6AtousHj2h-qSirC0pqliK4Y",
    "username": "followed_user",
    "bio": "",
    "image": ""
  }
}
```
```
POST /profiles/followed_user/follow
```
```
200 OK

{
  "profile": {
    "username": "followed_user",
    "bio": "",
    "image": "",
    "following": true
  }
}
```
```
POST /profiles/followed_user/follow
```
```
200 OK

{
  "profile": {
    "username": "followed_user",
    "bio": "",
    "image": "",
    "following": true
  }
}
```
```
GET /profiles/followed_user
```
```
200 OK

{
  "profile": {
    "username": "followed_user",
    "bio": "",
    "image": "",
    "following": true
  }
}
```
```
GET /profiles/followed_user
```
```
200 OK

{
  "profile": {
    "username": "followed_user",
    "bio": "",
    "image": "",
    "following": false
  }
}
```
```
POST /users

{
  "user": {
    "username": "user2-0.ytfkkc8y9gs",
    "email": "user2-0.ytfkkc8y9gs@mail.com",
    "password": "password"
  }
}
```
```
200 OK

{
  "user": {
    "email": "user2-0.ytfkkc8y9gs@mail.com",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXIyLTAueXRma2tjOHk5Z3MiLCJpYXQiOjE2MTM5NTkwODIsImV4cCI6MTYxNDEzMTg4Mn0.rcPUEawRO00y60kRw1MtbVYvu6p5DFSR-91ThAj2sPg",
    "username": "user2-0.ytfkkc8y9gs",
    "bio": "",
    "image": ""
  }
}
```
```
POST /profiles/followed_user/follow
```
```
200 OK

{
  "profile": {
    "username": "followed_user",
    "bio": "",
    "image": "",
    "following": true
  }
}
```
```
DELETE /profiles/followed_user/follow
```
```
200 OK

{
  "profile": {
    "username": "followed_user",
    "bio": "",
    "image": "",
    "following": false
  }
}
```
```
DELETE /profiles/followed_user/follow
```
```
200 OK

{
  "profile": {
    "username": "followed_user",
    "bio": "",
    "image": "",
    "following": false
  }
}
```
```
DELETE /profiles/followed_user/follow
```
```
200 OK

{
  "profile": {
    "username": "followed_user",
    "bio": "",
    "image": "",
    "following": false
  }
}
```
### should disallow following with bad token
```
POST /profiles/followed_user/follow
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Token not present or invalid."
    ]
  }
}
```
## Update
### should update user
```
PUT /user

{
  "user": {
    "email": "updated-user1-0.v9b5xff4a0h@email.com"
  }
}
```
```
200 OK

{
  "user": {
    "username": "user1-0.v9b5xff4a0h",
    "email": "updated-user1-0.v9b5xff4a0h@email.com",
    "image": "",
    "bio": "",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXIxLTAudjliNXhmZjRhMGgiLCJpYXQiOjE2MTM5NTkwODEsImV4cCI6MTYxNDEzMTg4MX0.DswTa-bI3uUyQPDbfAeQzmw8IyNdSDvVk14HgInteLA"
  }
}
```
```
PUT /user

{
  "user": {
    "password": "newpassword"
  }
}
```
```
200 OK

{
  "user": {
    "username": "user1-0.v9b5xff4a0h",
    "email": "updated-user1-0.v9b5xff4a0h@email.com",
    "image": "",
    "bio": "",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXIxLTAudjliNXhmZjRhMGgiLCJpYXQiOjE2MTM5NTkwODEsImV4cCI6MTYxNDEzMTg4MX0.DswTa-bI3uUyQPDbfAeQzmw8IyNdSDvVk14HgInteLA"
  }
}
```
```
PUT /user

{
  "user": {
    "bio": "newbio"
  }
}
```
```
200 OK

{
  "user": {
    "username": "user1-0.v9b5xff4a0h",
    "bio": "newbio",
    "image": "",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXIxLTAudjliNXhmZjRhMGgiLCJpYXQiOjE2MTM5NTkwODEsImV4cCI6MTYxNDEzMTg4MX0.DswTa-bI3uUyQPDbfAeQzmw8IyNdSDvVk14HgInteLA"
  }
}
```
```
PUT /user

{
  "user": {
    "image": "newimage"
  }
}
```
```
200 OK

{
  "user": {
    "username": "user1-0.v9b5xff4a0h",
    "image": "newimage",
    "bio": "newbio",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXIxLTAudjliNXhmZjRhMGgiLCJpYXQiOjE2MTM5NTkwODEsImV4cCI6MTYxNDEzMTg4MX0.DswTa-bI3uUyQPDbfAeQzmw8IyNdSDvVk14HgInteLA"
  }
}
```
### should disallow missing token/email in update
```
PUT /user
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Token not present or invalid."
    ]
  }
}
```
```
PUT /user

{}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "User must be specified."
    ]
  }
}
```
### should disallow reusing email
```
POST /users

{
  "user": {
    "email": "user2-0.8kz6v3nf7r5@email.com",
    "username": "user2-0.8kz6v3nf7r5",
    "password": "password"
  }
}
```
```
200 OK

{
  "user": {
    "email": "user2-0.8kz6v3nf7r5@email.com",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXIyLTAuOGt6NnYzbmY3cjUiLCJpYXQiOjE2MTM5NTkwODIsImV4cCI6MTYxNDEzMTg4Mn0.dNGhSR-EAmppwlHfNr5ed0zEby_NaBczm_hz06ZdYO8",
    "username": "user2-0.8kz6v3nf7r5",
    "bio": "",
    "image": ""
  }
}
```
```
PUT /user

{
  "user": {
    "email": "user2-0.8kz6v3nf7r5@email.com"
  }
}
```
```
422 Unprocessable Entity

{
  "errors": {
    "body": [
      "Email already taken: [user2-0.8kz6v3nf7r5@email.com]"
    ]
  }
}
```
# Util
## Ping
### should ping
```
GET /ping
```
```
200 OK

{
  "pong": "2021-02-22T01:58:02.531Z",
  "AWS_REGION": "us-east-1",
  "DYNAMODB_NAMESPACE": "dev"
}
```
