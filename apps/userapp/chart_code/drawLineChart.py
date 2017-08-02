#__*__coding:utf-8__*__
import pygal


def lineChart(time_list, user_electricity):
    line_chart = pygal.Line()
    line_chart.title = '用电量走势图'
    line_chart.x_labels = time_list
    for k, v in user_electricity.items():
        line_chart.add(k, v)
    line_chart.render_to_file("static/chart/line.svg")

    return "static/chart/line.svg"
