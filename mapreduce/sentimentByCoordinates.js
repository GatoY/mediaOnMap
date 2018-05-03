// get average sentiment group by different coordinates
//map
function (doc) {
  if(doc['geo']['coordinates']){
    var coordinates = doc['geo']['coordinates'];
    var sentiment = doc['sentiment'];
  }
  emit(coordinates, sentiment);
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

