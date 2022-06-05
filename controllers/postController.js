"use strict";

const posts = [{
  id: 1,
  title: "Post 1",
  description: "Post 1 description",
  likes: 0
},
{
  id: 2,
  title: "Post 2",
  description: "Post 2 description",
  likes: 3
},{
  id: 4,
  title: "Post 3",
  description: "Post 3 description",
  likes: 0
},{
  id: 4,
  title: "Post 4",
  description: "Post 4 description",
  likes: 0
}]

exports.addLike = async function (req, res){
    try {
      //Find selected post
      const id = posts.findIndex(el => {   return el.id == req.body.postId})
      if(id < 0) {
        return res.status(400).send('Post not found');
      } else {
        posts[id].likes ++;
        return res.status(500).json({
          post: posts[id]
        });
      }
       
      
    } catch (error) {

      return res.status(500).send(error);

    }
}

exports.subtractLike = async function (req, res){
  try {
    //Find selected post
    const id = posts.findIndex(el => {   return el.id == req.body.postId})
    
    if(id < 0) {
      return res.status(400).send('Post not found');
    } else {
      if(posts[id].likes > 0) posts[id].likes --;
      return res.status(500).json({
        post: posts[id]
      });
    }
     
    
  } catch (error) {

    return res.status(500).send(error);

  }
}

exports.allPost = async function (req, res) {
  try {
    return res.status(200).json(posts)

  } catch (error) {

    return res.status(500).send(error);

  }
}

