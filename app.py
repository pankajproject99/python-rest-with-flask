from flask import Flask, jsonify

app = Flask(__name__)

db_courses = [
    {'name': "python", 'course_id': "0", 'Description': "Python Programming", 'price': "1.0"},
    {'name': "java", 'course_id': "1", 'Description': "Java Programming", 'price': "2.0"},
    {'name': "C", 'course_id': "2", 'Description': "C Programming", 'price': "3.0"},
    {'name': ".Net", 'course_id': "3", 'Description': ".Net Programming", 'price': "4.0"},
]


@app.route('/')
def index():
    return "Welcome To The Course API"


@app.route("/courses", methods=['GET'])
def get_courses():
    return jsonify({'Courses': db_courses})


@app.route("/courses/<int:course_id>", methods=['GET'])
def get_course_by_id(course_id):
    return jsonify({'course': db_courses[course_id]})


@app.route("/courses", methods=['POST'])
def create():
    course = {'name': ".Apache", 'course_id': "5", 'Description': "Apache Programming", 'price': "6.0"}
    db_courses.append(course);
    return jsonify({'Created': course})

if __name__ == "__main__":
    app.run(debug=True)
