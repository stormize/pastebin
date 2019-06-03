# pastebin
api end points
post structure 
{
"content":"",
"shared":"",
"private":"",
"public":""
}
 post http://127.0.0.1:8000/
 delete {"id":id}
 delete http://127.0.0.1:8000/
 put
 {
 "id":id
 "content":content
 "shared":shared
 "private":private
 "public":public
 }
 put http://127.0.0.1:8000/
 get http://127.0.0.1:8000/
 get private posts get http://127.0.0.1:8000/private
 get public posts get http://127.0.0.1:8000/public
