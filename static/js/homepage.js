function addMessage(color, message) {
    var box = document.getElementById("message_box");
    box.className = 'ui ' + color + ' message';
    box.innerText = message;
}
    
function onRequestCreate() {
    var 
        formData = new FormData();  
        image = document.getElementById("image"),
        dark = document.getElementById("is_dark"),
        submit = document.getElementById("submit");
        isDark = dark.checked,
        fileName = image.value;

    if (!fileName) {
        addMessage('red', "请选择图片");
        return false;
    } else if (!(fileName.endsWith('.jpg')) && !(fileName.endsWith('.jpeg'))) {
        addMessage('red', '只能对jpg进行转换');
        return false;
    }

    formData.append('image', image.files[0]);
    formData.append('dark', isDark);

    function ajax(method, url, data) {
        var request = new XMLHttpRequest();
        return new Promise(function(resolve, reject) {
            request.onreadystatechange = function() {
                if (request.readyState===1) {
                    submit.value = '正在上传..';
                }
                if (request.readyState===4) {
                    if (request.status === 200) {
                        resolve(request.responseText);
                    } else {
                        reject(request.status);
                    }
                }
            };
            request.open(method, url);
            request.send(formData);
        });
    }

    var post = ajax('POST', '/upload');
    post.then(function (text) {
        var contentPre = document.getElementById('content-pre');
        if (contentPre) {
            contentPre.innerText = text;
        } else {
            var 
                output = document.createElement('div'),
                pre = document.createElement('pre');
            output.className = "ui green message";
            pre.id = "content-pre";
            pre.innerText = text;
            output.appendChild(pre);
            content.appendChild(output);
        }
        addMessage('yellow', '成功');
        submit.value = '提交';
    }).catch(function(status) {
        addMessage('red', '失败');
        submit.value = '提交';
    });

    return false;
}
