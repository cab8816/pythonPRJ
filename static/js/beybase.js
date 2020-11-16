// $(document).ready(function () {
//
// // 条款章节选择框点击
//
//     $("#e1").change(function () {
//
//
//     });
// });


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


function showhctk(self) {
    var zbh = self.value;
    var xmlhttp = createXMLHttpRequest();
    xmlhttp.open("POST", "/myapp/showhctkxx/", true);
    xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xmlhttp.send("zbh=" + zbh);

    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState === 4 && xmlhttp.status === 200) {
            var s = xmlhttp.responseText;
            ss = JSON.parse(s);
            alert(ss);

             $("#e2").append("<option value='1'>" + ss+ " </option>");

            // for (i = 0; i < s.length; i++)
            //     // for (tk in s)
            // {
            //     $("#e2").append("<option value='1'>" + s[i].childNodes[0].nodeValue + " </option>");
            // }


            if (s === "0") {
                // document.getElementById("error").innerHTML = "";
                // document.getElementById("submitid1").removeAttribute('disabled');
            }
        }
    }
}
