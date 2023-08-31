import csv
from dataclasses import dataclass
import re

import requests
from bs4 import BeautifulSoup, Tag
import config

BASE_URL = config.DJINNI_URL
Result_dict = dict.fromkeys(config.TECHNOLOGIES, 0)


@dataclass
class Job:
    description: str


def parse_single_job(course_container: Tag) -> Job:

    description = course_container.select_one(
        ".job-list-item__description"
    ).text.strip()

    return Job(
        description=description
    )


def get_num_pages(soup: BeautifulSoup) -> int:
    page_number = int(soup.select("li.page-item > a.page-link")[-2].text)
    return page_number if page_number else 1


def get_single_page_jobs(page_soup: BeautifulSoup) -> list[Job]:
    jobs = page_soup.select(".list-jobs__item.job-list__item")
    return [parse_single_job(job_soup) for job_soup in jobs]


def get_all_jobs() -> list[Job]:
    page = requests.get(BASE_URL).content
    first_page_soup = BeautifulSoup(page, "html.parser")

    pages_num = get_num_pages(first_page_soup)

    all_jobs = get_single_page_jobs(first_page_soup)

    for page_num in range(2, pages_num + 1):
        page = requests.get(BASE_URL, {"page": page_num}).content
        soup = BeautifulSoup(page, "html.parser")
        all_jobs.extend(get_single_page_jobs(soup))

    return all_jobs


def calculate_technologies(all_jobs: list[Job]) -> None:
    for job in all_jobs:
        job_description_lower = job.description.lower()
        for technology in config.TECHNOLOGIES:
            if re.findall(f"{technology.lower()}", job_description_lower):
                Result_dict[technology] += 1


def write_to_csv(result_dict: dict, output_csv_path: str) -> None:
    with open(output_csv_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(("Technology", "Frequency"))
        for technology, frequency in result_dict.items():
            writer.writerow((technology, frequency))


def main(output_csv_path: str) -> None:
    all_jobs = get_all_jobs()
    calculate_technologies(all_jobs)
    write_to_csv(Result_dict, output_csv_path)


if __name__ == "__main__":
    main("result.csv")
