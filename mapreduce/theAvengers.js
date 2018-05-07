// The avengers

//map
function(doc){
    var keywords = ["Iron Man", "Gamora", "Star-Lord","Thanos", "Thor", "avenger", "Hulk", "Captain America", "Black Widow", "Doctor Strange", "War Machine", "Groot", "Spider-Man", "Rocket Racoon", "Black Panther", "Vision", "Scarlet Witch", "Falcon", "White Wolf", "Loki","Drax the Destroyer","Nebula"];
    var text = doc.text.toLowerCase();
    for(i in keywords) {
        if(text.search(keywords[i].toLowerCase()) > -1){
            if(doc.sentiment > 0){
                emit([keywords[i], "positive"], 1);
            }
            else if(doc.sentiment < 0){
              emit([keywords[i], "negative"], 1);
            }
            else{
              emit([keywords[i], "neutral"], 1);
            }
        }
    }

}

//reduce
function(key,values,rereduce){
    return sum(values);
}