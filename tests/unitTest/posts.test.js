const postsController = require('../../controllers/postController')

test('add like to a post', () => {
     req={
         postId:1
     }

     expected={
        "post": {
            "id": 1,
            "title": "Post 1",
            "description": "Post 1 description",
            "likes": 1
        }
     }

     result=postsController.addLike(req)
     expect(result == expected)
  });


test('remove like to a post', () => {
    req={
        postId:2
    }

    expected={
       "post": {
           "id": 2,
           "title": "Post 1",
           "description": "Post 1 description",
           "likes": 2
       }
    }

    result=postsController.subtractLike(req)
    expect(result == expected)
 });

 test('get all posts', () => {
    expected=[
        {
            "id": 1,
            "title": "Post 1",
            "description": "Post 1 description",
            "likes": 0
        },
        {
            "id": 2,
            "title": "Post 2",
            "description": "Post 2 description",
            "likes": 3
        },
        {
            "id": 4,
            "title": "Post 3",
            "description": "Post 3 description",
            "likes": 0
        },
        {
            "id": 4,
            "title": "Post 4",
            "description": "Post 4 description",
            "likes": 0
        }
    ]

    result=postsController.subtractLike(req)
    expect(result == expected)
 });