// get average sentiment group by suburb
//map
function (doc) {
  if(doc["sa2_name"] != null){
    var suburb = doc["sa2_name"];
    var sentiment = doc["sentiment"];
    emit(suburb, sentiment);
  }


}
//reduce
function(keys, values, rereduce) {
    if (!rereduce){
        var length = values.length
        return [sum(values) / length, length]
    }else{
        var length = sum(values.map(function(v){return v[1]}))
        var avg = sum(values.map(function(v){
        return v[0] * (v[1] / length)
    }))
    return [avg, length]
    }
}

