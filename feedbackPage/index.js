var chart_config = function(location){
    return{
        type: "realtimeline",
        renderAt: location,
        width: "100%",
        height: "60%",
        dataFormat: "json",
        dataSource: {
        chart: {
            caption: "Current Consumed By The Motor",
            numdisplaysets: "10",
            labeldisplay: "rotate",
            showRealTimeValue: "1",
            theme: "fusion",  
            thousandSeparator: ",",
            formatnumberscale:"0",
            plotToolText: "$label<br>Current: <b>$dataValue mA</b>",
            setAdaptiveYMin: "100"
        },
        categories: [{
                category: [{}]
            }
        ],
        dataset: [{}]
        },
    };
}

function generateGraph(){
    FusionCharts.ready(function() {
        chart1.render();
        chart2.render();
        chart3.render();
        chart4.render();
        chart5.render();
        chart6.render();
     });
}

function requestData(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          updateCharts(this.responseText);
        }
    };
    xhttp.open("GET", "update", true);
    xhttp.send();
}

function updateCharts(respText){
    respObj = JSON.parse(respText);
    chart1.feedData("&label=" + respObj.motor1.time + "&value=" + respObj.motor1.value);
    chart2.feedData("&label=" + respObj.motor2.time + "&value=" + respObj.motor2.value);
    chart3.feedData("&label=" + respObj.motor3.time + "&value=" + respObj.motor3.value);
    chart4.feedData("&label=" + respObj.motor4.time + "&value=" + respObj.motor4.value);
    chart5.feedData("&label=" + respObj.motor5.time + "&value=" + respObj.motor5.value);
    chart6.feedData("&label=" + respObj.motor6.time + "&value=" + respObj.motor6.value);
}
/*
    '{"motor1" : { "time" : 1, "value" : 50}, "motor2" : { "time" : 1, "value" : 50}}'
*/

var chart1 = new FusionCharts(chart_config("motor1-chart"));
var chart2 = new FusionCharts(chart_config("motor2-chart"));
var chart3 = new FusionCharts(chart_config("motor3-chart"));
var chart4 = new FusionCharts(chart_config("motor4-chart"));
var chart5 = new FusionCharts(chart_config("motor5-chart"));
var chart6 = new FusionCharts(chart_config("motor6-chart"));
generateGraph();




// strData = "&label=" + 4 + "&value=" + 10000;
// chart1.feedData(strData)