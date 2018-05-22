/**
 * Created by viva on 30/3/18.
 */

    $("#submit").click(function (e) {
        var fname = $("#fname").val();
        var mno = $("#mno").val();
        var gen = $('input[name=gender]:checked').val();

        var datas = {
            "Name": fname,
            "Mobile_num": mno,
            "Gender": gen,
        };
        $.ajax({
            url: "/register",
            type: "post",
            data: datas,
            success: function (response) {

                // {#                                $("p").text(response);#}
                console.log("Response is " + JSON.stringify(response))
                console.log((response["name"]))
                // {#                var len = response.length;#}
                var txt = "";
                // {#                if (len > 0) {#}
                // {#                    for (var i = 0; i < len; i++) {#}
                // {#                        obje = response[i];#}
                txt += "<tr>  " +
                    "<td>" +
                    response["name"] +
                    "</td>" +
                    "<td>" +
                    response["Mobile_num"] +
                    "</td>" +
                    "<td>" +
                    response["Gender"] +
                    "<td>" +
                    "<button id='" + response["_id"] + "' class='botaoadd'>delete</button>" +
                    "</td>" +
                    "<td>" +
                    "<button id='" + response["_id"] + "' class='btupdate'>update</button>" +
                    "</td>" +
                    "</tr>";
                // {#                    }#}
                if (txt != "") {
                    $("#table").append(txt);
                }


                console.log(response["name"]);

            },
            error: function (response) {
                alert("error")
                //Do Something to handle error
            }
        });
    });


    $("#table").on("click", ".botaoadd", function (e) {
        $(this).parents("tr").remove();
        obid = $(this).attr('id')

        var d_delete = {
            "oid": obid,
            "action": "delete"
        }
        $.ajax({
            url: "/delete",
            type: "POST",
            data: d_delete,
            success: function (response) {
                console.log(response)

            },
            error: function (response) {
                console.log("error1")

            }

        });


        console.log(obid);
        // {#        alert($("#fname").text())#}
        // {#        #this is almost done you just have to pass the particular #}
        // {#        object in this function to remove that element#}


    });



