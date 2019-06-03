# pastebin
api end points
post structure 
</br>
{
"content":"",
"shared":"",
"private":"",
"public":""
}
</br>
 post http://127.0.0.1:8000/
 </br>
 delete {"id":id}
 </br>
 delete http://127.0.0.1:8000/
 </br>
 put
 {
 "id":id
 "content":content
 "shared":shared
 "private":private
 "public":public
 }
 </br>
 put http://127.0.0.1:8000/ </br>
 get http://127.0.0.1:8000/ </br>
 get private posts get http://127.0.0.1:8000/private </br>
 get public posts get http://127.0.0.1:8000/public </br>
