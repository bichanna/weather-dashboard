var ctx = document.getElementById("myChart-{{pk}}");
var myLineChart = new Chart(ctx, {
	type: "line",
	data: {
		labels: [{% for d in date %}
		"{{ d }}",
		{% endfor %}],


		datasets: [
			{
				type: "line",
				label: "最高気温(度)",
				data: {{ max_temp }},
				borderColor: "rgba(255,0,0,1)",
				backgroundColor: "rgba(0,0,0,0)",
				yAxisID: "y-axis-1",
			},
			
			{
				type: "line",
				label: "最低気温(度)",
				data: {{ min_temp }},
				borderColor: "rgba(0,0,255,1)",
				backgroundColor: "rgba(0,0,0,0)",
				yAxisID: "y-axis-1",
			},
			
			{
				type: "line",
				label: "湿度",
				data: {{ humidity }},
				borderColor: "rgba(0,255,0,1)",
				backgroundColor: "rgba(0,0,0,0)",
				yAxisID: "y-axis-2",
			},
		],
	},

	options: {
		title: {
			display: true,
			text: "気象データ",
		},
		scales: {
			yAxes: [{
				id: "y-axis-1",
				suggestedMax: 40,
				suggestedMin: 0,
				stepSize: 10,
			},

			{
				id: "y-axis-2",
				suggestedMax: 100,
				suggestedMin: 0,
				stepSize: 10,
				gridLines: {
					drowOnChartArea: false,
				},
			},
		]
		},
	},
});