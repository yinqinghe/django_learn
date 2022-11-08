/*
 * @Author: 殷清贺 987746808@qq.com
 * @Date: 2022-10-28 17:26:16
 * @LastEditors: 殷清贺 987746808@qq.com
 * @LastEditTime: 2022-10-29 22:49:08
 * @FilePath: \HTMLd:\C#\python\Django\django_2022\bms\static\js\auth_list.js
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
function add(id) {
    document.getElementById('all_light').style.display = 'block';
    document.getElementById('contes').style.display = 'block';
    document.getElementById('error').style.display = 'block';

    console.log('add',id);
    content = document.getElementById('name'+id).innerHTML;
    console.log(content);
    document.getElementById('name').value = content
    document.getElementById('sex').value = document.getElementById('sex'+id).innerHTML;
    document.getElementById('age').value = document.getElementById('age'+id).innerHTML;
    document.getElementById('tel').value = document.getElementById('tel' + id).innerHTML;
    document.getElementById('id').value = document.getElementById('id'+id).innerHTML;
    

    console.log(document.getElementById('name').innerHTML)
}
function disappear() {
    document.getElementById('all_light').style.display = 'none';
    document.getElementById('contes').style.display = 'none';
    document.getElementById('error').style.display = 'none';

    console.log('add');
}

function dele(id) {
      var xhttp = new XMLHttpRequest();
    cookie = document.cookie.split(";");
    for (var i = 0; i < cookie.length; i++) {
        var temp = cookie[i].split("=");
        if (temp[0] == "csrftoken")
            csrf = temp[1];
            break;
    }
    console.log(csrf)
    console.log(id);
    xhttp.open("POST", "/drop_author/", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.setRequestHeader("X-CSRFToken",csrf);
    xhttp.send("fname=Bill&id=" + id);

    xhttp.onreadystatechange = function () {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            console.log(xhttp.statusText)
        }
    }
}