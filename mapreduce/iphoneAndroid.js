//find the total numbers of iphone and android users

//map
function(doc) {
    var source = doc.source;
    if(source.search("Android") > -1)
        emit("Android",1);
    if(source.search("iPhone") > -1)
        emit("iPhone",1);
}
//reduce
function(key,values,rereduce){
    return sum(values);
}


//example result
//

// {"rows":[
// {"key":"Android","value":4686},
// {"key":"iPhone","value":12849}
// ]}