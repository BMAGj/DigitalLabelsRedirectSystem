// This JavaScript Document NEEEEDDDDDDSSSS TO FOLLOW NAMAING FORMAT OR DOESNT WORK ITS DYNAMIC AS LONG AS THAT IS STATIC (Life works on contradictions and compromise, shame i know)

var request = new XMLHttpRequest();

// (Javascript finds its filepath saves as 'me') 


var me;
(function(){ 
    var scripts = document.getElementsByTagName('script'); 
    me = scripts[ scripts.length-1 ].src; 
}());


//  (converts to string and sets transfer variable to hold data in replacing routine)

me = me.toString()
console.log(me) 
var transfer1 = "insert something witty and pointless in here"

me2 = me 


var arr = UpperCaseArray(me2);

function UpperCaseArray(input) {
    var result = input.replace(/([A-Z]+)/g, ",$1").replace(/^,/, "");
    return result.split(",");
}

me3 = arr.pop();
me4 = me3 
me4 = me4.replace(".js","");
console.log(me3)
console.log(me4)
// Finds JSON From its own name through replacements 


var transfer1 = me2.replace(".js",".json");
console.log(transfer1)
var transfer2 = transfer1.replace("/" + me4 + "/", "/");
var transfer3 = transfer2.replace()


me = transfer2


 // variable check 


// JSON Request 
function Get(me){
   var Httpreq = new XMLHttpRequest(); // a new request
   Httpreq.open("GET",me,false);
   Httpreq.send(null);
   return Httpreq.responseText;          
}

var json_obj = JSON.parse(Get(me));



link = json_obj.Location.toString()

  window.location = link;
  