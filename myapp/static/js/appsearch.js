$(".store").each(function(){
    $(this).click(function(){
        if($(this).attr("id") == "play"){
            $(".app-store")
                .css("display" , "none")
                .delay(1000);

            $(".play-store")
                .css("display" , "inline")
                .delay(1000);
        } else{
            $(".play-store")
                .css("display" , "none")
                .delay(1000);

            $(".app-store")
                .css("display" , "inline")
                .delay(1000);
        }
    });
});

///////////////////////// AJAX ///////////////////////////////////

$("#run-ajax").click(function(){
    $(this).attr("disabled" , "disabled");
    $(this).css("cursor" , "not-allowed");
    $("#loading").css("display" , "inline");

    // $('.store').
    var opt = $("input[name=store]:checked" , "form").val();

    if(opt == "1"){
        var a = $.ajax({
            url : "ajax/" ,

            type : "POST" ,

            data : {
                store : "1" ,

                play_app : $("input[name=play_app]" , "form").val() ,

                csrfmiddlewaretoken : window.CSRF_TOKEN
            } ,

            dataType : "json"
        });

        a.done(function(json){

            $('.error-msg').css('display','none')

            $("input[name=play_app]" , "form").val("");

            $("#loading").css("display" , "none");

            $("#run-ajax").removeAttr("disabled");

            $("#run-ajax").css("cursor" , "default");

            $("#data").css("display" , "block");

            $("#appName").text(json.APP_NAME);

            $("#dev-name").text(json.DEV_NAME);

            $("#icon").attr("src" , json.ICON);

            $("#rating").text(json.RATING + " Rating");

            $("#reviews").text(json.REVIEWS + " Reviews");

            $("#downloads").text(json.DOWNLOADS + " Downloads");

            $("#discription").text(json.DISCRIPTION);
        });

        a.fail(function(json){

            $('#data').css('display','none')

            $("#loading").css("display" , "none");

            $("#run-ajax").removeAttr("disabled");

            $("#run-ajax").css("cursor" , "default");

            $(".error-msg").css("display" , "block");

            package = $("input[name=play_app]" , "form").val();

            $("input[name=play_app]" , "form").val("");

            $(".error-head").html(
                package + " package not found in <strong>Play Store</strong>"
            );

            $(".error-para").html(
                "<ul><li>Goto desired application in play store then package name is in the url followed by <code>id=</code></li></ul>"
            );
        });
    } else{
        var a = $.ajax({
            url : "ajax/" ,

            type : "POST" ,

            data : {
                store : "2" ,

                ios_app : $("input[name=ios_app]" , "form").val() ,

                ios_app_no : $("input[name=ios_app_no]" , "form").val() ,

                csrfmiddlewaretoken : window.CSRF_TOKEN
            } ,

            dataType : "json"
        });

        a.done(function(json){

            $("input[name=ios_app]" , "form").val("");

            $("input[name=ios_app_no]" , "form").val("");

            $("#loading").css("display" , "none");

            $("#run-ajax").removeAttr("disabled");

            $("#run-ajax").css("cursor" , "default");

            $("#data").css("display" , "block");

            $("#appName").text(json.APP_NAME);

            $("#dev-name").text(json.DEV_NAME);

            $("#icon").attr("src" , json.ICON);

            $("#rating").text(json.RATING + " Rating");

            $("#reviews").text(json.REVIEWS + " Reviews");

            $("#downloads").text('Downloads ' + json.DOWNLOADS);

            $("#discription").text(json.DISCRIPTION);
        });

        a.fail(function(json){


            $("#loading").css("display" , "none");

            $("#run-ajax").removeAttr("disabled");

            $("#run-ajax").css("cursor" , "default");

            $(".error-msg").css("display" , "block");

            appName = $("input[name=ios_app]" , "form").val();
            $("input[name=ios_app]" , "form").val("");

            appNo = $("input[name=ios_app_no]" , "form").val();
            $("input[name=ios_app_no]" , "form").val("");

            $("input[name=play_app]" , "form").val("");

            $(".error-head").html(
                appName + " app not found in <strong>App Store</strong>"
            );

            $(".error-para").html(
                `<ul><li>Goto desired application in app store then app name is in the url followed by <code>app/</code></li>.<br><li>Application number is the number followed by <code>/id</code></li></ul>`
            );
        });
    }
});
