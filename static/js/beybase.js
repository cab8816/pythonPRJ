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

function deleteobj() {
    if (confirm("确定要删除吗11?")) {

        return true;
    } else {
        return false;
    }
}
// 为什么要调出开发模式，因为官方对于Disable cache功能是这样解释的：Disable cache(while DevTools is open)
// 也就是调出开发模式时，选择Disable cache才会清除缓存。
// Chrome官方推荐使用如下快捷键，就可以不使用页面缓存进行刷新
//
// Windows和Linux操作系统: Shift+F5 或 Ctrl+Shift+R
// Mac OS: Cmd+Shft+R
