import dearpygui.dearpygui as graphics
import comp151Colors
# ["Minnesota", "Alaska", "Oregon", "Wisconsin", "Ohio"]
bar_width = 100
next_bar_start = 50
states_info = open("Project4.txt", "r")
info = states_info.readlines()
graphics.create_context()
graphics.create_viewport(title="Income Graph", width=900, height=900)
with graphics.window(label="Info Graph", width=900, height=900):
    with graphics.drawlist(width=900, height=900):
        graphics.draw_arrow((30, 10), (30, 790), color=comp151Colors.LIGHT_BLUE, thickness=5)
        graphics.draw_arrow((790, 800), (30, 800), color=comp151Colors.TEAL, thickness=5)
        graphics.draw_text((0, 100), "800k", size=13)
        graphics.draw_text((0, 200), "700k", size=13)
        graphics.draw_text((0, 300), "600k", size=13)
        graphics.draw_text((0, 400), "500k", size=13)
        graphics.draw_text((0, 500), "400k", size=13)
        graphics.draw_text((0, 600), "300k", size=13)
        graphics.draw_text((0, 700), "200k", size=13)
        graphics.draw_text((0, 800), "100k", size=13)
    for line in info:
            line_info = line.split(";")
            median_house_price = float(line_info[5])
            bar_height = median_house_price/1000
            bar_color= comp151Colors.BLUE
            graphics.draw_rectangle((next_bar_start, 0), (next_bar_start+bar_width, bar_height),
                               fill=bar_color)
            next_bar_start += bar_width+30

graphics.setup_dearpygui()
graphics.show_viewport()
graphics.start_dearpygui()
graphics.destroy_context()