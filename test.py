import pickle
def main():
    courses = [["Python", 3],
               ["Trig", 3],
               ["Physics", 4],
               ["Yoga", 2]]
    with open("classes.bin", "wb") as file:
        pickle.dump(courses, file)
    with open("classes.bin", "rb") as file:
        course_list = pickle.load(file)
    i = 0
    while i < len(course_list):
        course = course_list[i]
        print(course[0], str(course[1]), end=" ")
        i += 2

main()
