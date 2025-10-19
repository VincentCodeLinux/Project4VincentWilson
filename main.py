import dearpygui.dearpygui as graphics
import comp151Colors
bar_width = 100
next_bar_start = 50
states_info = open("Project4.txt", "r")
v_states = ["Minnesota", "Alaska", "Oregon", "Wisconsin", "Ohio"]
info = states_info.readlines()
graphics.create_context()
graphics.create_viewport(title="Income Graph", width=1000, height=1800)
with graphics.window(label="Info Graph", width=800, height=1000):
    with graphics.drawlist(width=800, height=1100):
        graphics.draw_arrow((30, 10), (30, 900), color=comp151Colors.TEAL, thickness=5)
        graphics.draw_arrow((790, 920), (30, 920), color=comp151Colors.TEAL, thickness=5)
        graphics.draw_text((0, 10), "900k", size=13)
        graphics.draw_text((0, 110), "800k", size=13)
        graphics.draw_text((0, 210), "700k", size=13)
        graphics.draw_text((0, 310), "600k", size=13)
        graphics.draw_text((0, 410), "500k", size=13)
        graphics.draw_text((0, 510), "400k", size=13)
        graphics.draw_text((0, 610), "300k", size=13)
        graphics.draw_text((0, 710), "200k", size=13)
        graphics.draw_text((0, 810), "100k", size=13)
        graphics.draw_text((0, 910), "0k", size=13)

    for state in v_states:
        for line in info:
            line_info = line.split(";")
            name_state = line_info[1].strip()
            if name_state == state:
                median_income = float(line_info[4])
                median_house_price = float(line_info[5])
                bar_height = median_house_price/1000
                if median_house_price <= 3 * median_income:
                    bar_color = comp151Colors.BLUE
                elif median_house_price <= 4 * median_income:
                    bar_color = comp151Colors.YELLOW
                else:
                    bar_color = comp151Colors.RED

                graphics.draw_rectangle((next_bar_start, 910-bar_height), (next_bar_start+bar_width, 910),
                               fill=bar_color)
                graphics.draw_text((next_bar_start + 10, 920), name_state, size=13)
                next_bar_start += bar_width+30

graphics.setup_dearpygui()
graphics.show_viewport()
graphics.start_dearpygui()
graphics.destroy_context()