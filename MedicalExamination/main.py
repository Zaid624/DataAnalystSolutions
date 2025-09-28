from medical_data_visualizer import draw_cat_plot, draw_heat_map

if __name__ == "__main__":
    print("Drawing categorical plot...")
    cat_fig = draw_cat_plot()
    print("Saved catplot.png")

    print("Drawing heatmap...")
    heat_fig = draw_heat_map()
    print("Saved heatmap.png")
