/**
 * ======================= COMP90024 TEAM 16 =======================

 889545   Yu Liu          yul22       yul22@student.unimelb.edu.au
 875095   Jize Dong       jized       jized@student.unimelb.edu.au
 911764   Minsheng Wang   minshengw   minshengw@student.unimelb.edu.au
 890742   Minglun Zhang   minglunz    minglunz@student.unimelb.edu.au
 905084   Xingping Ding   xingpingd   xingpingd@student.unimelb.edu.au

 ==================================================================== */


//traffic complaint number by hours


//map
function (doc) {
    var keywords = ["avenue", "street", "drive", "lane", "highway", "motoway", "freeway", "driveway", "cross", "traffic", "jam", "congestion", "controlflow", "sarl", "detour", "ave", "rd", "st", "ln", "dr", "way", "blvd", "road"];
    var words = doc.text.toLowerCase().split(" ");
    date_time = doc.created_at.split(" ");
    time = date_time[3];
    hour = time.split(":")[0];
    for (i in words) {
        if (keywords.indexOf(words[i]) > -1) {
            if (doc.sentiment < 0) {
                emit(hour, 1);
                break;
            }
        }
    }

}

//reduce
function (key, values, rereduce) {
    return sum(values);
}