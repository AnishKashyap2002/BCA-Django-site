$(document).ready(function () {
  $(".like").on("click", function (e) {
    e.preventDefault();
    var id = $(this).data("post-id");
    $.ajax({
      type: "get",
      url: "like-post/",
      data: {
        id: id,
      },
      dataType: "json",
      success: function (response) {
        let likes = response.likes.toString();
        console.log(likes);
        $("#like-count" + id).text(likes);
      },
    });
  });
});
