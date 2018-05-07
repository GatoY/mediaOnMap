//get average sentiment by 24 hours
//map
function(doc) {
    if (doc['created_at']) {
      var sentiment = doc.sentiment;
      var hour = doc.created_at.substring(11,13);
      if (sentiment > 0){
        var res = "positive";
      }
      else if(sentiment < 0){
        var res = "negative";
      }
      else{
        var res = "neutral";
      }


      emit([hour, res], 1);

    }
}
// function(doc) {
//     if (doc['created_at']) {
//       var sentiment = doc['sentiment'];
//       date_time = doc.created_at.split(" ");
//       time = date_time[3];
//       hour = (parseInt(time.split(":")[0]) + 10) % 24;
//       if (sentiment > 0){
//           var res = "positive";
//           emit([hour,res], 1)
//       }
//       else if(sentiment < 0){
//           var res = "negative";
//           emit([hour,res], 1)
//       }
//       else {
//           var res = "neutral";
//           emit([hour,res], 1)
//       }
//
//     }
// }

//reduce
function (keys, values, rereduce) {
  if (rereduce) {
    return sum(values);
  } else {
    return values.length;
  }
}



//
// //map
// function(doc) {
//     if (doc['created_at']) {
//       var date_time = doc.created_at.split(" ");
//       var time = date_time[3];
//       var hour = (parseInt(time.split(":")[0]) + 10) % 24;
//       emit(hour, doc['sentiment']);
//     }
// }
//
// //reduce
// function(keys, values, rereduce) {
//     if (!rereduce){
//         var length = values.length
//             return [sum(values) / length, length]
//     }else{
//         var length = sum(values.map(function(v){return v[1]}))
//         var avg_sentiment = sum(values.map(function(v){
//         return v[0] * (v[1] / length)
//     }))
//     return [avg_sentiment, length]
//     }
// }

