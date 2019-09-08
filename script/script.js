//create new element on todo list
function newElement () {
    let li = document.createElement("li");
    let inputValue = document.querySelector(".add__input").value;
    let t=document.createTextNode(inputValue);
    li.appendChild(t);

    if (inputValue==='')  {
        alert ("You cannot add empty task!");
    } else {
        document.querySelector(".toDo__list").appendChild(li);
    }
    document.querySelector(".add__input").value="";

    //add close button
    let span = document.createElement("SPAN");
    let txt = document.createTextNode("\u00D7");
    span.className="close";
    span.appendChild(txt);
    li.appendChild(span);

    let close = document.getElementsByClassName("close");
    for (let i=0;i<close.length; i++) {
        close[i].onclick = function () {
        let div=this.parentElement;
        div.style.display= "none";
    }
}

}

//checked task
let list = document.querySelector(".toDo__list");
list.addEventListener('click', function (ev) {
    if (ev.target.tagName === "LI") {
        document.querySelector(".done__list").appendChild(ev.target);
    }
})

//create close button
let myList = document.getElementsByTagName("LI");
for (let i = 0; i<myList.length; i++) {
    let span = document.createElement("SPAN");
    let txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    myList[i].appendChild(span);
}

//click close button to delete elements
let close = document.getElementsByClassName("close");
for (let i=0;i<close.length; i++) {
    close[i].onclick = function () {
        let div=this.parentElement;
        div.style.display= "none";
    }
}

//trigger button on enter click
let input = document.querySelector(".add__input");
input.addEventListener("keyup", function(event) {
if (event.keyCode === 13) {
    document.querySelector(".add--submit").click();
}
});