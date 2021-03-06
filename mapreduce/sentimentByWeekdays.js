/**
 * ======================= COMP90024 TEAM 16 =======================

 889545   Yu Liu          yul22       yul22@student.unimelb.edu.au
 875095   Jize Dong       jized       jized@student.unimelb.edu.au
 911764   Minsheng Wang   minshengw   minshengw@student.unimelb.edu.au
 890742   Minglun Zhang   minglunz    minglunz@student.unimelb.edu.au
 905084   Xingping Ding   xingpingd   xingpingd@student.unimelb.edu.au

 ==================================================================== */

//get average sentiment of weekdays

//map
function (doc) {
    if (doc['created_at']) {
        var sentiment = doc['sentiment'];
        week = doc.created_at.split(" ");
        weekday = week[0];
        if (sentiment > 0) {
            var res = "positive";
            emit([weekday, res], 1)
        }
        else if (sentiment < 0) {
            var res = "negative";
            emit([weekday, res], 1)
        }
        else {
            var res = "neutral";
            emit([weekday, res], 1)
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


// //map
// function(doc) {
//     if (doc['created_at']) {
//       week = doc.created_at.split(" ");
//       weekday = week[0];
//       emit(weekday, doc['sentiment']);
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
