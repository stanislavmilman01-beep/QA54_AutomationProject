from pathlib import Path
def create_test_report(project_name,tester_name,passed,failed):

    project_folder = Path("reports") / project_name
    project_folder.mkdir(parents=True,exist_ok=True)
    total = passed + failed
    # if failed == 0:
    #     status = "passed"
    # else:
    #     status = "failed"

    file_path = project_folder / "reports.txt"
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f'''
Project:{project_name}
Tester:{tester_name}
Passed tests:{passed}
Failed tests:{failed}
Total tests:{total}
''')

create_test_report("Testlink", "Stas", 88, 22)

# from pathlib import Path
#
#
# def create_test_report(project_name, tester_name, passed, failed):
#     project_folder = Path("reports") / project_name
#     project_folder.mkdir(parents=True, exist_ok=True)
#
#     total = passed + failed
#     status = "passed" if failed == 0 else "failed"
#
#     file_path = project_folder / "report.txt"
#     with open(file_path, "w", encoding="utf-8") as file:
#         file.write(
#             f"Project: {project_name}\n"
#             f"Tester: {tester_name}\n"
#             f"Passed tests: {passed}\n"
#             f"Failed tests: {failed}\n"
#             f"Total tests: {total}\n"
#             f"Status: {status}\n"
#         )
#
#
# create_test_report("Testlink", "Stas", 88, 22)
#
# # Проверка
# with open(Path("reports") / "Testlink" / "report.txt", "r", encoding="utf-8") as file:
#     print(file.read())