

$(document).ready(function () {

// 条款章节选择框点击

  $("#e1").change(function() {
     alert('点击select');
      showhctk(self);
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


function showhctk(self) {
    var zbh = self.value;
    var xmlhttp = createXMLHttpRequest();
    xmlhttp.open("POST", "/myapp/showhctkxx/", true);
    xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xmlhttp.send("zbh=" + zbh);

    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState === 4 && xmlhttp.status === 200) {
            var s = xmlhttp.responseText
            for (tk in s)
            {
                document.getElementById()
            }

            if(s==="0"){
                // document.getElementById("error").innerHTML = "";
                // document.getElementById("submitid1").removeAttribute('disabled');
            }
        }
    }
}
