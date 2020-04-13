$("button").click(function() {
  $(this).attr("disabled", "disabled");
  $(this).css("cursor", "not-allowed");

  var a = $.ajax({
    url: "keyfinder_ajax/",

    type: "POST",

    data: {
      url: $("input[name=url]", "form").val(),

      csrfmiddlewaretoken: window.CSRF_TOKEN
    },

    dataType: "json"
  });
  a.done(function(json) {
    $("button").removeAttr("disabled");
    $("button").removeAttr("cursor");

    if (json.keywords) {
      $("h5").css("display", "block");

      if (json.related) {
        for (var i of json.related.keys()) {
          $("related-url").append("<p>" + json.related.i + "</p>");

          for (var j in json.related.i) {
            $("related").append("<li>" + j.name + "</li>");
          }
        }
      }
    }
  });

  a.fail(function(json) {
    $("button").removeAttr("disabled");
    $("button").removeAttr("cursor");
  });
});
