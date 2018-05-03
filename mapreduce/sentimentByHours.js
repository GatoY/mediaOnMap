//get average sentiment by 24 hours

//map 
function(doc) {
    if (doc['created_at']) {
      date_time = doc.created_at.split(" ");
      time = date_time[3];
      hour = (parseInt(time.split(":")[0]) + 10) % 24;
      emit(hour, doc['sentiment']);
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