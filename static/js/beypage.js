<!-- 动态刷新验证码js -->
$(document).ready(function () {
    $('.captcha').click(function () {
        $.getJSON("/myapp/refresh_captcha/", function (result) {
            $('#id_captcha').attr('src', result['image_url']);
            $('#id_captcha_0').val(result['hashkey'])
        });
    });
});

function createXMLHttpRequest() {
    var xmlHttp;
    try {
        xmlHttp = new XMLHttpRequest();
    } catch (e) {
        try {
            // 适用于IE6
            xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
        } catch (e) {
            try {
                // 适用于IE5.5，以及IE更早版本
                xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
            } catch (e) {

            }
        }

    }

    return xmlHttp;
}

function func1(self) {
    var username = self.value;
    var xmlhttp = createXMLHttpRequest();
    xmlhttp.open("POST", "/myapp/ajax_checkuser/", true);
    xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xmlhttp.send("username=" + username);

    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState === 4 && xmlhttp.status === 200) {
            var s = xmlhttp.responseText
            if (s === "1") {
                document.getElementById("error").innerHTML = "用户名已经注册!";
                document.getElementById("submitid1").disabled="disabled";
            }
            if(s==="0"){
                document.getElementById("error").innerHTML = "";
                document.getElementById("submitid1").removeAttribute('disabled');
            }
        }
    }
}
