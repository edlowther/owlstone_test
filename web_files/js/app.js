(function () {
    $(document).ready(function () {

        function drawChart(data, variableName) {
            var svg = d3.select("." + variableName),
                margin = {
                    top: 20,
                    right: 60,
                    bottom: 40,
                    left: 38
                },
                width = +svg.attr("width") - margin.left - margin.right,
                height = +svg.attr("height") - margin.top - margin.bottom,
                g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");
            console.log(svg);

            var x = d3.scaleLinear()
                .range([0, width])
                .domain([0, d3.max(data, function (d) {
                    return d[variableName];
                })]);

            var y = d3.scaleBand()
                .rangeRound([height, 0])
                .paddingInner(0.4)
                .domain(data.map(function (d) {
                    return d.publisher_name;
                }));

            //make y axis to show bar names
            var yAxis = d3.axisLeft(y)
                //no tick marks
                .tickSize(0);
            //
            var gy = g.append("g")
                .attr("class", "y axis")
                .call(yAxis)

            var bars = g.selectAll(".bar")
                .data(data)
                .enter()
                .append("g");

            //append rects
            bars.append("rect")
                .attr("class", "bar")
                .attr("y", function (d) {
                    return y(d.publisher_name);
                })
                .attr("height", '20px')
                .attr("x", 0)
                .attr("width", function (d) {
                    return x(d.average_word_count_by_article);
                })
                .attr('fill', '#007F7F');

            bars.append("text")
                .attr("class", "annotation")
                //y position of the label is halfway down the bar
                .attr("y", function (d) {
                    console.log(y(d.publisher_name));
                    return y(d.publisher_name) + y.bandwidth() / 2 + 4;
                })
                //x position is 3 pixels to the right of the bar
                .attr("x", function (d) {
                    return x(d.average_word_count_by_article) + 3;
                })
                .text(function (d) {
                    return d.average_word_count_by_article;
                });

        }

        $('svg').attr('width', $('.container').width());

        d3.json("../../owlstone_test/data/publisher_data.json", function (data) {
            data = data.sort(function (a, b) {
                return d3.ascending(a.average_word_count_by_article, b.average_word_count_by_article);
            })
            drawChart(data, 'average_word_count_by_article');
        });
    })
})();
