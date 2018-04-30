$(function () {
    var myChart = echarts.init(document.getElementById('main'));

    // 指定图表的配置项和数据
    var option = {
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
    };


    // var option = {
    //     xAxis: {
    //         type: 'category',
    //         data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    //     },
    //     yAxis: {
    //         type: 'value'
    //     },
    //     series: [{
    //         data: [820, 932, 901, 934, 1290, 1330, 1320],
    //         type: 'line'
    //     }]
    // };


    // var option = {
    //     title: {
    //         text: '堆叠区域图'
    //     },
    //     tooltip: {
    //         trigger: 'axis',
    //         axisPointer: {
    //             type: 'cross',
    //             label: {
    //                 backgroundColor: '#6a7985'
    //             }
    //         }
    //     },
    //     legend: {
    //         data: ['邮件营销', '联盟广告', '视频广告', '直接访问', '搜索引擎']
    //     },
    //     toolbox: {
    //         feature: {
    //             saveAsImage: {}
    //         }
    //     },
    //     grid: {
    //         left: '3%',
    //         right: '4%',
    //         bottom: '3%',
    //         containLabel: true
    //     },
    //     xAxis: [
    //         {
    //             type: 'category',
    //             boundaryGap: false,
    //             data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    //         }
    //     ],
    //     yAxis: [
    //         {
    //             type: 'value'
    //         }
    //     ],
    //     series: [
    //         {
    //             name: '邮件营销',
    //             type: 'line',
    //             stack: '总量',
    //             areaStyle: { normal: {} },
    //             data: [120, 132, 101, 134, 90, 230, 210]
    //         },
    //         {
    //             name: '联盟广告',
    //             type: 'line',
    //             stack: '总量',
    //             areaStyle: { normal: {} },
    //             data: [220, 182, 191, 234, 290, 330, 310]
    //         },
    //         {
    //             name: '视频广告',
    //             type: 'line',
    //             stack: '总量',
    //             areaStyle: { normal: {} },
    //             data: [150, 232, 201, 154, 190, 330, 410]
    //         },
    //         {
    //             name: '直接访问',
    //             type: 'line',
    //             stack: '总量',
    //             areaStyle: { normal: {} },
    //             data: [320, 332, 301, 334, 390, 330, 320]
    //         },
    //         {
    //             name: '搜索引擎',
    //             type: 'line',
    //             stack: '总量',
    //             label: {
    //                 normal: {
    //                     show: true,
    //                     position: 'top'
    //                 }
    //             },
    //             areaStyle: { normal: {} },
    //             data: [820, 932, 901, 934, 1290, 1330, 1320]
    //         }
    //     ]
    // };


    myChart.setOption(option);

})