import csv
import matplotlib.pyplot as plt
from app.parse import main as parsing_main


def read_results_csv(csv_path):
    result_dict = {}
    with open(csv_path, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            technology = row[0]
            frequency = int(row[1])
            result_dict[technology] = frequency
    return result_dict


def create_bar_chart(result_dict, output_image_path):
    filtered_result_dict = {tech: freq for tech, freq in result_dict.items() if freq > 1}

    sorted_result_dict = dict(sorted(filtered_result_dict.items(), key=lambda item: item[1], reverse=True))

    technologies = list(sorted_result_dict.keys())
    frequencies = list(sorted_result_dict.values())

    plt.bar(technologies, frequencies)
    plt.xlabel("Technology")
    plt.ylabel("Frequency")
    plt.title("Most popular Python technologies on Djinni")
    plt.xticks(rotation=90)
    plt.tight_layout()

    plt.savefig(output_image_path)

    plt.show()
    plt.close()


def main():
    parsing_main("result.csv")
    output_image_path = "../chart/technologies_chart.png"
    result_dict = read_results_csv("result.csv")
    create_bar_chart(result_dict, output_image_path)


if __name__ == "__main__":
    main()
