//get average sentiment of weekdays

//map
function(doc) {
    if (doc['created_at']) {
      week = doc.created_at.split(" ");
      weekday = week[0];
      emit(weekday, doc['sentiment']);
    }
}

//reduce
function(keys, values, rereduce) {
    if (!rereduce){
        var length = values.length
            return [sum(values) / length, length]
    }else{
        var length = sum(values.map(function(v){return v[1]}))
        var avg_sentiment = sum(values.map(function(v){
        return v[0] * (v[1] / length)
    }))
    return [avg_sentiment, length]
    }
}
