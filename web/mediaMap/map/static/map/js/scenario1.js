$(function () {

    function initMap() {
        var location = {lat: -37.8136, lng: 144.99758596};
        var mapCanvas = document.getElementById('map');
        var mapOptions = {
            center: location,
            zoom: 10,
            panControl: false,
            mapTypeId: google.maps.MapTypeId.ROADMAP,
        }
        var map = new google.maps.Map(mapCanvas, mapOptions);


        // var contentString = '<div class="info-window">' +
        //     '<h3>Info Window Content</h3>' +
        //     '<div class="info-content">' +
        //     '<p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. </p>' +
        //     '</div>' +
        //     '</div>';

    }

    google.maps.event.addDomListener(window, 'load', initMap);


    var chart1 = echarts.init(document.getElementById('chart1'), 'light').setOption({
        title: {
            text: 'ECharts demo'
        },
        tooltip: {},
        legend: {
            data: ['销量', '哈哈']
        },
        xAxis: {
            data: ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        },
        yAxis: {},
        series: [{
            name: '销量',
            type: 'bar',
            data: [5, 20, 36, 10, 10, 20]
        }, {
            name: '哈哈',
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

    var chart4 = echarts.init(document.getElementById('chart4')).setOption({
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b}: {c} ({d}%)"
        },
        legend: {
            orient: 'vertical',
            x: 'left',
            data: ['直接访问', '邮件营销', '联盟广告', '视频广告', '搜索引擎']
        },
        series: [
            {
                name: '访问来源',
                type: 'pie',
                radius: ['50%', '70%'],
                avoidLabelOverlap: false,
                label: {
                    normal: {
                        show: false,
                        position: 'center'
                    },
                    emphasis: {
                        show: true,
                        textStyle: {
                            fontSize: '30',
                            fontWeight: 'bold'
                        }
                    }
                },
                labelLine: {
                    normal: {
                        show: false
                    }
                },
                data: [
                    {value: 335, name: '直接访问'},
                    {value: 310, name: '邮件营销'},
                    {value: 234, name: '联盟广告'},
                    {value: 135, name: '视频广告'},
                    {value: 1548, name: '搜索引擎'}
                ]
            }
        ]
    });

});