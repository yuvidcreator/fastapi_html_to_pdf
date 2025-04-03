import matplotlib
import matplotlib.pyplot as plt



def generate_doughnut_chart(data):
    """Generate and save a doughnut chart from Excel data."""
    filename="static/chart.webp"
    if not data:
        raise ValueError("No data available for chart generation.")

    try:
        # print("@Graph ----> ", data)
        labels = [data_obj['Category'] for data_obj in data]
        sizes = [float(data_obj['Value']) for data_obj in data]
        # labels = list(data.keys())
        # sizes = list(data.values())
        # print(labels)
        # print(sizes)

        matplotlib.use('agg')
        fig, ax = plt.subplots(figsize=(4, 4), dpi=100)
        wedges, texts, autotexts = ax.pie(
            sizes, labels=labels, autopct="%1.1f%%", startangle=90,
            wedgeprops={"linewidth": 2, "edgecolor": "white"},
            pctdistance=0.85
        )

        for text in autotexts:
            text.set_color("white")

        ax.set_facecolor("white")
        ax.axis("equal")

        plt.savefig(filename, format="webp", pil_kwargs={"lossless": False})
        plt.close()
        print("Graph genereted successfully, --> ", filename)
        return filename
    except Exception as e:
        print(f"{e}")