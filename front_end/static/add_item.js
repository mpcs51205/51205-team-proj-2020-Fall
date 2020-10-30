function add_item() {
     var oReq = new XMLHttpRequest();
    oReq.open("POST", "/api/add_item");
    var item_name = document.getElementById("add_item").value;
    oReq.send(JSON.stringify({
                "item_name": item_name}));
    console.log(item_name);
}


