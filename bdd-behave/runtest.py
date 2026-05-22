import subprocess
import os


if not os.path.exists("reports/allure-results"):
    os.makedirs("reports/allure-results")


subprocess.run(
    [
        "behave",
        "-f",
        "allure_behave.formatter:AllureFormatter",
        "-o",
        "reports/allure-results"
    ]
)