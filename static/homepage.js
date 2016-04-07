function addMessage(color, message) {
    var box = document.getElementById("message_box");
    box.className = 'ui ' + color + ' message';
    box.innerText = message;
}
    
function onRequestCreate() {
    var 
        image = document.getElementById("image"),
        dark = document.getElementById("is_dark"),
        isDark = dark.checked,
        fileName = image.value;

    if (!fileName) {
        addMessage('red', "请选择图片");
        return false;
    } else if (!(fileName.endsWith('.jpg')) && !(fileName.endsWith('.jpeg'))) {
        addMessage('red', '只能对jpg进行转换');
        return false;
    }

    var formData = new FormData();  
    formData.append('image', image.files[0]);
    formData.append('dark', isDark);
    
    function stateChange() {
        if (xhr.readyState==1) {
            var submit = document.getElementById("submit");
            submit.value = '正在上传..';
        };

        if (xhr.readyState==4) {
            if (xhr.status==200) {// 200 = OK
                var contentPre = document.getElementById('content-pre');
                if (contentPre) {
                    contentPre.innerText = xhr.responseText;
                } else {
                    // 创建输出div并输出
                    var output = document.createElement('div');
                    var pre = document.createElement('pre');
                    output.className = "ui green message";
                    pre.id = "content-pre";
                    pre.innerText = xhr.responseText ;
                    output.appendChild(pre);
                    content.appendChild(output);
                }

                addMessage('yellow', '成功');
                // 清空上一次图片url按钮
                image.value = '';
                var submit = document.getElementById("submit");
                submit.value = '提交';
            } else {
                addMessage('red', '失败');
                image.value = '';
                var submit = document.getElementById("submit");
                submit.value = '提交';
            }
        }
    }

    var xhr = new XMLHttpRequest(); 
    xhr.onreadystatechange=stateChange;
    xhr.open("POST", "/upload");
    xhr.send(formData);
    return false;
}
