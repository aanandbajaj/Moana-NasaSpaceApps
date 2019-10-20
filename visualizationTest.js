//x = date
//y = height
var rawHeights = new Array();
var rawDates = new Array();
var dates = new Array();
var heights = new Array();
var tempSumHeight = 0;
var tempYear = 0;
var tempYearNext = 0;
var counter = 1;

d3.csv("/Data/SaltonSeaData.csv")
    .then(function (data) {
        for (var i = 0; i < data.length; i++) {
            rawHeights.push(parseFloat(data[i].Height));
            rawDates.push(parseInt(data[i].Date.substring(0, 4)));
        }

        //get average from each year
        tempSumHeight = 0;
        tempSumHeight = rawHeights[0];
        for (var i = 0; i < rawDates.length; i++) {
            //1992
            tempYear = rawDates[i];
            tempYearNext = rawDates[i + 1];

            //duplicate year
            if (tempYearNext == tempYear) {
                tempSumHeight = tempSumHeight + rawHeights[i + 1];
                counter++;

            } else {
                heights.push(tempSumHeight / counter);
                dates.push(tempYear);
                counter = 1;
                tempSumHeight = rawHeights[i + 1];
            }

        }
        //
        // console.log(heights);
        // TESTER = document.getElementById('tester');
        // Plotly.plot(TESTER, [{
        //     x: dates,
        //     y: heights
        // }], {
        //     margin: {
        //         t: 0
        //     }
        // });

        var arr = [];
        for (var i = 0; i < 10; i++) {
            arr.push(Array(10)
                .fill()
                .map(() => Math.random()));
        }
        var newArr = [];
        while (heights.length) newArr.push(heights.splice(0, 2));
        TESTER = document.getElementById('tester');

        var data = [{
            z: newArr,
            type: 'surface'
        }];

        var layout = {
            title: 'Salton Sea Water Levels (1992 to 2019)',
            autosize: false,
            width: 600,
            height: 600,
            margin: {
                l: 50,
                r: 50,
                b: 100,
                t: 100,
            }
        };

        console.log(newArr);
        Plotly.newPlot('tester', data, layout, {
            responsive: true
        });


    });


//slider
$(function () {
    $('#checkbox')
        .change(function () {
            setInterval(function () {
                moveRight();
            }, 3000);
        });

    var slideCount = $('#slider ul li')
        .length;
    var slideWidth = $('#slider ul li')
        .width();
    var slideHeight = $('#slider ul li')
        .height();
    var sliderUlWidth = slideCount * slideWidth;

    $('#slider')
        .css({
            width: slideWidth,
            height: slideHeight
        });

    $('#slider ul')
        .css({
            width: sliderUlWidth,
            marginLeft: -slideWidth
        });

    $('#slider ul li:last-child')
        .prependTo('#slider ul');

    function moveLeft() {
        $('#slider ul')
            .animate({
                left: +slideWidth
            }, 200, function () {
                $('#slider ul li:last-child')
                    .prependTo('#slider ul');
                $('#slider ul')
                    .css('left', '');
            });
    };

    function moveRight() {
        $('#slider ul')
            .animate({
                left: -slideWidth
            }, 200, function () {
                $('#slider ul li:first-child')
                    .appendTo('#slider ul');
                $('#slider ul')
                    .css('left', '');
            });
    };

    $('a.control_prev')
        .click(function () {
            moveLeft();
        });

    $('a.control_next')
        .click(function () {
            moveRight();
        });
});
//plotly graph
