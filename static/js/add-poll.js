$(document).ready(function () {
  $("#add").click(function (e) {
    e.preventDefault();

    let n = parseInt($("#count").val());

    
      let temp = "";

    for (let i = 0; i < n; i++) {
      temp += `<label > Value no ${i + 1} </label><br>
<input type="text" class = 'choices form-control' required><br>`;
    }

    $(".options").html(temp);
    
  });

  $("#submit").on("click", function (e) {
    e.preventDefault();

    let title = $("#title").val();
    console.log(title)

    let temp = "";

    let elements = document.getElementsByClassName("choices");

    console.log("Fuck");

    for (let i = 0; i < elements.length; i++) {
      temp += elements[i].value + ',';
    }

    if (temp === ""){
      alert('Invalid Entry')
    }
    else{
      console.log(temp);
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    $.ajax({
      headers: {'X-CSRFToken': csrftoken},
      type: "POST",
      url: "/add-poll",

      data: {
        title: title,
        choices: temp,
      },
      success: function (response) {
        if(response === 'success'){
          location.replace("/polls")
        }
        else{
          console.log('Invalid Data')
        }
      },
    });
    }
  });
});
