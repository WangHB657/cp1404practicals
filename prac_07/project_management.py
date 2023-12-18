import datetime
from project import Project


def main():
    projects = []
    choice = input("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd "
                   "new project\n- (U)pdate project\n- (Q)uit\n>>> ").lower()
    while choice != 'q':
        if choice == 'l':
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'f':
            date_string = input("Show projects that start after date (dd/mm/yy): ")
            filter_projects_by_date(projects, date_string)
        choice = input(
            "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd "
            "new project\n- (U)pdate project\n- (Q)uit\n>>> ").lower()

    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    projects = []
    in_file = open(filename, 'r')
    next(in_file)
    for line in in_file:
        name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
        projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage)))
    in_file.close()
    return projects


def save_projects(filename, projects):
    out_file = open(filename, 'w')
    out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
    for project in projects:
        out_file.write(
            f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
    out_file.close()


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = int(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, percent_complete)
    projects.append(new_project)


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    completed_projects = [project for project in projects if project.completion_percentage == 100]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(completed_projects):
        print(f"  {project}")


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    choice = int(input("Project choice: "))
    project = projects[choice]

    new_percentage = input(f"New Percentage (current {project.completion_percentage}%): ")
    new_priority = input(f"New Priority (current {project.priority}): ")

    if new_percentage:
        project.completion_percentage = int(new_percentage)
    if new_priority:
        project.priority = int(new_priority)


def filter_projects_by_date(projects, date):
    date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > date]

    for project in sorted(filtered_projects):
        print(f"  {project}")


if __name__ == "__main__":
    main()
