/**
 * ======================= COMP90024 TEAM 16 =======================

 889545   Yu Liu          yul22       yul22@student.unimelb.edu.au
 875095   Jize Dong       jized       jized@student.unimelb.edu.au
 911764   Minsheng Wang   minshengw   minshengw@student.unimelb.edu.au
 890742   Minglun Zhang   minglunz    minglunz@student.unimelb.edu.au
 905084   Xingping Ding   xingpingd   xingpingd@student.unimelb.edu.au

 ==================================================================== */

// get average sentiment group by suburb
//map
function (doc) {
    if (doc["sa2_name"] != null) {
        var suburb = doc["sa2_name"];
        var sentiment = doc["sentiment"];
        if (sentiment > 0) {
            emit([suburb, "positive"], 1)
        } else if (sentiment < 0) {
            emit([suburb, "negative"], 1)
        }
        else {
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
