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
    var i;
    var xmlhttp = createXMLHttpRequest();
    xmlhttp.open("POST", "/myapp/showhctkxx/", true);
    xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xmlhttp.send("zbh=" + zbh);

    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState === 4 && xmlhttp.status === 200) {
            var xmldoc = xmlhttp.responseText;
            var x = $.parseXML(xmldoc)
            var obj = x.getElementsByTagName("object");

            $("#e2").empty();

            for (i = 0; i < obj.length; i++) {
                var tkhao = obj[i].getElementsByTagName("field")[0].childNodes[0].nodeValue;
                var tkneirong = obj[i].getElementsByTagName("field")[1].childNodes[0].nodeValue;
                $("#e2").append("<option value = " + tkhao + " >" + tkhao + " : " + tkneirong + " </option>");

            }


        }
    }
}

function selecthctk(self) {
    var txt = self.value;

    $("#id_tkhao").val(txt);
}

function deleteJob() {
    if (confirm("确定要删除吗?")) {

        return true;
    } else {
        return false;
    }
}
