
// $(document).ready(function () {
//     setInterval(function(){
//       var id = $('#used').val();
     
//         $.ajax({
//             type: "GET",
//             url: `/get-messages/${id}`,
            
//             success: function (response) {
//                 $('#messages').empty();

//                 console.log(response)

//                 for (key in response.messages){
//                 let temp = `<div class="feed p-2" >
//                 <div class="bg-white border mt-2 text-black " style = 'border-radius: 10px;'>
//                     <div>
//                         <div class="d-flex flex-row justify-content-between align-items-center p-2 border-bottom">

//                             <a href="{% url 'show-profile' ${response.messages[key].user_id} %">
//                             <div class="d-flex flex-row align-items-center feed-text px-2"><img class="rounded-circle" src="${response.messages[key].user.avatar.url}" width="45">
//                                 <div class="d-flex flex-column flex-wrap ml-2"><span class="font-weight-bold" style = "font-size: 25px;">${response.messages[key].user.username}

//                                     {% if ${response.messages[key].user.is_teacher} %}
                                    
//                                     <button type="button" class="btn btn-success">Teacher</button>
//                                     {% endif %}

//                                 </span><span class="text-black-50 time">{{${response.messages[key].date|timesince}} ago</span></div>
//                             </div>
//                         </a>

//                         </div>
//                     </div>
//                     <div class="p-2 px-3"><span>${response.messages[key].body}</span></div>


//                     {% if ${response.messages[key].image} %}
//                     <div class="feed-image p-2 px-3" ><img class="img-fluid img-responsive rounded" src="${response.messages[key].image.url}"></div>
//                     {% endif %}

                    
//                 </div>
                
                
//             </div>`

//             $('#messages').append(temp);

//         }
                
//             }
//         });
//     },
//     1000)
// });

