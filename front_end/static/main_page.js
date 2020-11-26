var ele1 = document.getElementById("show_items_display");
var ele2 = document.getElementById("add_item_display");
var ele3 = document.getElementById("show_user_information_display");

ele1.style.display = 'none';
ele2.style.display = 'none';
ele3.style.display = 'none';

function show_items() {
    console.log("show_items()");
    var oReq = new XMLHttpRequest();
    oReq.open("GET", "/api/get_all_auction_items");
	oReq.addEventListener("load", get_all_auction_items_message);
    oReq.send();
}


function add_item() {
    console.log("add_item()");
    var item_name = document.getElementById("item_name").value;
    var item_start_time = document.getElementById("item_start_time").value;
    var item_end_time = document.getElementById("item_end_time").value;
    var item_category = document.getElementById("item_category").value;
    var item_start_bidding_price = document.getElementById("item_start_bidding_price").value;
    var item_buyout_price = document.getElementById("item_buyout_price").value;
    var user_key =   localStorage.getItem("user_key");
    console.log("user key is: " + user_key);
    var oReq = new XMLHttpRequest();
    oReq.open("PUT", "/api/add_item");
    // oReq.addEventListener("load", add_item_);
    oReq.send(JSON.stringify({
                "name": item_name,
                "start_time": item_start_time,
                "end_time": item_end_time,
                "category": item_category,
                "start_bidding_price": item_start_bidding_price,
                "buyout_price": item_buyout_price,
                "user_key": user_key}));
}

function get_all_auction_items_message() {
	console.log(this.responseText);
    var text =  this.responseText;
    var obj = JSON.parse(text);
    var all_auction_items = document.getElementById("inner_show_items_display");
    while(all_auction_items.firstChild){
        all_auction_items.removeChild(all_auction_items.firstChild);
    }

    for(var i in obj) {
        var one_row = obj[i];
        console.log(one_row)
        var wrapper = document.createElement('div');

        wrapper.setAttribute('class','container darker');

        var p = document.createElement('p');
        p.innerHTML = "name: " + one_row["name"] + "<br></br>start_bidding_price: " +  one_row["start_bidding_price"] + 
                      "<br></br>buyout_price: " + one_row["buyout_price"] + 
                      "<br></br>start_time: " +  one_row["start_time"] + "<br></br>end_time: " +  one_row["end_time"] +
                      "<br></br>category: " +  one_row["category"] ;
        
        // If the user key equals to current user key, the user can modify or delete the item


        wrapper.appendChild(p);
        all_auction_items.appendChild(wrapper);
    }

    show_items_display();
}

function search_item_by_category() {
    console.log("search_item_by_category()");
    var oReq = new XMLHttpRequest();
    oReq.open("POST", "/api/get_auction_items_by_category");
    var search_item = document.getElementById("search_item").value;
	oReq.addEventListener("load", get_all_auction_items_message);
    oReq.send(JSON.stringify({'category':search_item}));
}

function search_item_by_keyword() {
    console.log("search_item_by_keyword()");
    // var oReq = new XMLHttpRequest();
    // oReq.open("GET", "/api/get_auction_items_by_category");
    // var search_item = localStorage.getItem("search_item");
	// oReq.addEventListener("load", logout_message);
    // oReq.send(JSON.stringify({'category':search_item}));
}

function show_user_information() {
    console.log("show_user_information()");
    var user_information = document.getElementById("show_user_information_display");
    user_information.innerHTML = "<label>email: "+  localStorage.getItem("user_email") + " </label>" + 
                                 "<br></br> <label>update email: </label> <input id=\"modify_email\"></input> <button onclick=\"modify_email();\">update email</button>" +
                                 " <br></br> <label>update password: </label> <input id=\"modify_password\"></input> <button onclick=\"modify_password();\">update password</button> ";
    show_user_information_display();
}

function logout() {
    console.log("logout()");
    var oReq = new XMLHttpRequest();
    oReq.open("POST", "/api/logout");
    var user_key = localStorage.getItem("user_key");
	oReq.addEventListener("load", logout_message);
    oReq.send(JSON.stringify({'id':parseInt(user_key)}));
    
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

function logout_message() {
    console.log(this.responseText);
    location.replace("/");
}

function modify_email() {
    console.log("show_items()");
    var oReq = new XMLHttpRequest();
    oReq.open("POST", "/api/update_email");
    var email = document.getElementById("modify_email").value;
    var user_key = localStorage.getItem("user_key");
	oReq.addEventListener("load", modify_email_message);
    oReq.send(JSON.stringify({'email':email, 'id':parseInt(user_key)}));
    localStorage.setItem("user_email",email);
    show_user_information();
}

function modify_email_message() {
    console.log(this.responseText);

}

function modify_password() {
    console.log("show_items()");
    var oReq = new XMLHttpRequest();
    oReq.open("POST", "/api/update_password");
    var password = document.getElementById("modify_password").value;
    var user_key = localStorage.getItem("user_key");
	oReq.addEventListener("load", modify_password_message);
    oReq.send(JSON.stringify({'password':password, 'id':parseInt(user_key)}));
}

function modify_password_message() {
    console.log(this.responseText);
    
}


function show_items_display() {
    ele1.style.display = 'block';
    ele2.style.display = 'none';
    ele3.style.display = 'none';
}

function add_item_display() {
    ele1.style.display = 'none';
    ele2.style.display = 'block';
    ele3.style.display = 'none';
    // setInterval(request_message, 500);
    // handle_creator_invite();
    // history.pushState({},"","/chat/"+chat_id);
}

function show_user_information_display() {
    ele1.style.display = 'none';
    ele2.style.display = 'none';
    ele3.style.display = 'block';

}
