// get average sentiment group by suburb
//map
function (doc) {
  if(doc["sa2_name"] != null){
    var suburb = doc["sa2_name"];
    var sentiment = doc["sentiment"];
    if(sentiment > 0){
      emit([suburb, "positive"], 1)
    } else if(sentiment < 0){
      emit([suburb, "negative"], 1)
    }
    else{
      emit([suburb, "neutral"], 1)
    }
  }


}
//reduce
function (keys, values, rereduce) {
  if (rereduce) {
    return sum(values);
  } else {
    return values.length;
  }
}
