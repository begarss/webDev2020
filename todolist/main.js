
    document.getElementById('add').onclick = function(){
        var delo = document.getElementById('in').value;
        var checkbox = document.createElement('input');
        checkbox.type = "checkbox";
        var li = document.createElement('li');
        var label = document.createElement('label')
        label.marginLeft = "30pt";
        label.innerHTML=delo;
        li.appendChild(checkbox);
        li.appendChild(label);
        document.getElementById('myUl').appendChild(li);
        document.getElementById('in').value="";

        var btn = document.createElement('button');
        btn.className = 'btn';
        btn.innerHTML = '<i class="fas fa-trash"></i>';
        btn.style.height = "20pt";
        btn.style.width = "20pt";
        btn.style.float = "right";
        btn.style.padding = "0"
        li.appendChild(btn);
        
        btn.onclick = function(){
           /* li.removeChild(checkbox);
            li.removeChild(label);
            li.removeChild(btn);
            li.parentNode.removeChild(li);*/
            UL = document.getElementById("myUl");
            UL.removeChild(li);
        }
    
        checkbox.onclick = function(){
        if (checkbox.checked == true){
            label.style.textDecoration = "line-through";
        } else {
            label.style.textDecoration = "none";
        }
    }
    }   
       
    

    
    

    // function out(){
    //     var out="";
    //     for(var key in todoList){
    //         if(todoList[key].check==true){
    //             out+='<input type="checkbox" checked>';
    //         }else
    //         out+='<input type="checkbox">';

    //         out+=todoList[key].todo+'<br>';

    //     }
    //     var li = document.createElement('li');
    //     li.innerHTML=out;
    //     document.getElementById('myUl').appendChild(li);
        
    // }
