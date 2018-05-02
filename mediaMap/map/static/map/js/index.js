$(function () {

    // var mapStyle = [
    //     {elementType: 'geometry', stylers: [{color: '#242f3e'}]},
    //     {elementType: 'labels.text.stroke', stylers: [{color: '#242f3e'}]},
    //     {elementType: 'labels.text.fill', stylers: [{color: '#746855'}]}, {
    //         'stylers': [{'visibility': 'off'}]
    //     }, {
    //         'featureType': 'landscape',
    //         'elementType': 'geometry',
    //         'stylers': [{'visibility': 'on'}, {'color': '#fcfcfc'}]
    //     }, {
    //         'featureType': 'water',
    //         'elementType': 'geometry',
    //         'stylers': [{'visibility': 'on'}, {'color': '#bfd4ff'}]
    //     }];

    function initMap() {
        var location = {lat: -37.8136, lng: 144.99758596};
        var mapCanvas = document.getElementById('map');
        var mapOptions = {
            center: location,
            zoom: 10,
            panControl: false,
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            // styles: mapStyle
            // styles: [
            //     {elementType: 'geometry', stylers: [{color: '#242f3e'}]},
            //     {elementType: 'labels.text.stroke', stylers: [{color: '#242f3e'}]},
            //     {elementType: 'labels.text.fill', stylers: [{color: '#746855'}]},
            //     {
            //         featureType: 'administrative.locality',
            //         elementType: 'labels.text.fill',
            //         stylers: [{color: '#d59563'}]
            //     },
            //     {
            //         featureType: 'poi',
            //         elementType: 'labels.text.fill',
            //         stylers: [{color: '#d59563'}]
            //     },
            //     {
            //         featureType: 'poi.park',
            //         elementType: 'geometry',
            //         stylers: [{color: '#263c3f'}]
            //     },
            //     {
            //         featureType: 'poi.park',
            //         elementType: 'labels.text.fill',
            //         stylers: [{color: '#6b9a76'}]
            //     },
            //     {
            //         featureType: 'road',
            //         elementType: 'geometry',
            //         stylers: [{color: '#38414e'}]
            //     },
            //     {
            //         featureType: 'road',
            //         elementType: 'geometry.stroke',
            //         stylers: [{color: '#212a37'}]
            //     },
            //     {
            //         featureType: 'road',
            //         elementType: 'labels.text.fill',
            //         stylers: [{color: '#9ca5b3'}]
            //     },
            //     {
            //         featureType: 'road.highway',
            //         elementType: 'geometry',
            //         stylers: [{color: '#38414e'}]
            //     },
            //     {
            //         featureType: 'road.highway',
            //         elementType: 'geometry.stroke',
            //         stylers: [{color: '#1f2835'}]
            //     },
            //     {
            //         featureType: 'road.highway',
            //         elementType: 'labels.text.fill',
            //         stylers: [{color: '#9ca5b3'}]
            //     },
            //     {
            //         featureType: 'transit',
            //         elementType: 'geometry',
            //         stylers: [{color: '#2f3948'}]
            //     },
            //     {
            //         featureType: 'transit.station',
            //         elementType: 'labels.text.fill',
            //         stylers: [{color: '#d59563'}]
            //     },
            //     {
            //         featureType: 'water',
            //         elementType: 'geometry',
            //         stylers: [{color: '#17263c'}]
            //     },
            //     {
            //         featureType: 'water',
            //         elementType: 'labels.text.fill',
            //         stylers: [{color: '#515c6d'}]
            //     },
            //     {
            //         featureType: 'water',
            //         elementType: 'labels.text.stroke',
            //         stylers: [{color: '#17263c'}]
            //     }
            // ]
        }
        var map = new google.maps.Map(mapCanvas, mapOptions);

        var markerImage = '../img/marker.png';

        var marker = new google.maps.Marker({
            position: location,
            map: map,
            icon: markerImage
        });

        var contentString = '<div class="info-window">' +
            '<h3>Info Window Content</h3>' +
            '<div class="info-content">' +
            '<p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. </p>' +
            '</div>' +
            '</div>';

        var infowindow = new google.maps.InfoWindow({
            content: contentString,
            maxWidth: 400
        });
        // map.data.loadGeoJson('../res/Melb_ad.geojson'); // TODO add geojson file
        // map.data.setStyle(function (feature) {
        //     return ({
        //         fillColor: feature.getProperty('color'),
        //         strokeWeight: 1
        //     });
        // });
        map.data.addListener('mouseup', function (event) {
            // event.feature.setProperty('state', 'hover');

            // TODO clear

            // document.getElementById('info-box').textContent =
            //     event.feature.getProperty('pos');
            // document.getElementById('info-box1').textContent =
            //     event.feature.getProperty('neg');
            // document.getElementById('info-box2').textContent =
            //     event.feature.getProperty('vic_loca_2');
            // document.getElementById('info-box3').textContent =
            //     event.feature.getProperty('score');
            // document.getElementById('info-box5').textContent =
            //     event.feature.getProperty('edu');
        });
        // marker.addListener('click', function () {
        //     infowindow.open(map, marker);
        // });

    }

    google.maps.event.addDomListener(window, 'load', initMap);


    var chart1 = echarts.init(document.getElementById('chart1'), 'light').setOption({
        title: {
            text: 'ECharts 入门示例'
        },
        tooltip: {},
        legend: {
            data: ['销量']
        },
        xAxis: {
            data: ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        },
        yAxis: {},
        series: [{
            name: '销量',
            type: 'bar',
            data: [5, 20, 36, 10, 10, 20]
        }]
    });

    var chart2 = echarts.init(document.getElementById('chart2')).setOption({
        xAxis: {
            type: 'category',
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
            type: 'value'
        },
        series: [{
            data: [820, 932, 901, 934, 1290, 1330, 1320],
            type: 'line'
        }]
    });

});