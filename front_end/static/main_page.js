function show_items() {
    console.log("show_items()");
    var oReq = new XMLHttpRequest();
    oReq.open("GET", "/api/get_all_auction_items");
	oReq.addEventListener("load", get_all_auction_items_success);
    oReq.send();
}


function add_item() {
    var oReq = new XMLHttpRequest();
    oReq.open("POST", "/api/add_item");
    var item_name = document.getElementById("add_item").value;
    oReq.send(JSON.stringify({
                "item_name": item_name}));
    console.log(item_name);
}

function get_all_auction_items_success() {
	console.log(this.responseText);
    // var text =  this.responseText;
    // var obj = JSON.parse(text);
    // var all_auction_items = document.getElementById("show_auction_items");
    // while(all_auction_items.firstChild){
    //     all_auction_items.removeChild(all_auction_items.firstChild);
    // }


    // for(var i in obj) {
    //     var one_row = obj[i];
    //     console.log(one_row)
    //     var wrapper = document.createElement('div');

    //     wrapper.setAttribute('class','container darker');

    //     var p = document.createElement('p');
    //     p.innerHTML = "key: " + one_row["key"] + " name: " + one_row["name"];
    //     wrapper.appendChild(p);
    //     all_auction_items.appendChild(wrapper);
    // }

}


function logout() {
    console.log("logout()");
    // var text = JSON.parse(this.responseText);
    // console.log(text);

    // // window.localStorage.setItem(window.chat_id + " session_token",this.responseText) ;
    // // window.localStorage.setItem(window.chat_id + " username",window.username) ;
    // location.replace("main_page");

    // if(text["login_code"] == "true") {
    //     console.log("login success");
    //     window.session_token = text["session_token"];
    //     window.username = text["username"];
    //     belay_display();
    // }
    // else {
    //     document.getElementById("login_error").innerText = "email or password not correct, please try again";
    // }

}