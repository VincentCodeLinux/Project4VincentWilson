#This is where I import the interpretter and import the colors for the bars on the graph
import dearpygui.dearpygui as graphics
import comp151Colors
#This is where I define the lengths of the bars and how far apart they are
bar_width = 100
next_bar_start = 50
#This is where I open the file with the states to draw info for it
states_info = open("Project4.txt", "r")
#This is where I pull my states that I was assigned
v_states = ["Minnesota", "Alaska", "Oregon", "Wisconsin", "Ohio"]
info = states_info.readlines()
#This is where I make the context and the window that you can see the graph in
graphics.create_context()
graphics.create_viewport(title="Income Graph", width=1000, height=1800)
with graphics.window(label="Info Graph", width=800, height=1000):
#This is where I create the setup part of the graph such as the x and y axis and all the prices of the incomes on the y axis
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
#This is where I pull the info from each line specifically the name, median income and median household price
    for state in v_states:
        for line in info:
            line_info = line.split(";")
            name_state = line_info[1].strip()
            if name_state == state:
                median_income = float(line_info[4])
                median_house_price = float(line_info[5])
#This is where I divide the total price by 1000 so it can fit on the graph
                bar_height = median_house_price/1000
#This is where I assigned the colors of the states depending on the affordability of them
                if median_house_price <= 3 * median_income:
                    bar_color = comp151Colors.BLUE
                elif median_house_price <= 4 * median_income:
                    bar_color = comp151Colors.YELLOW
                else:
                    bar_color = comp151Colors.RED
#This is where I build the bars on the graph and place them specifically on the x axis of the graph
                graphics.draw_rectangle((next_bar_start, 910-bar_height), (next_bar_start+bar_width, 910),
                               fill=bar_color)
#This is where I place the names of the states by pulling it from a previous variable
                graphics.draw_text((next_bar_start + 10, 920), name_state, size=13)
                next_bar_start += bar_width+30
#This is where I closed the viewport to finish my code
graphics.setup_dearpygui()
graphics.show_viewport()
graphics.start_dearpygui()
graphics.destroy_context()