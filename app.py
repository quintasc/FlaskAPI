from flask import Flask, jsonify, request
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

STUDENTS = {
    '1': {'name': 'Carmen', 'age': 50, 'spec': 'M3'},
    '2': {'name': 'Txema', 'age': 51, 'spec': 'M12'},
    '3': {'name': 'Adri', 'age': 24, 'spec': 'M6'},
    '4': {'name': 'Jose', 'age': 52, 'spec': 'M9'}
}


@app.route('/api/students', methods=['GET'])
def get_users():
    return jsonify(STUDENTS)

@app.route('/api/student/<student_id>', methods=['GET'])
def get_student_by_id(student_id):
    student = STUDENTS.get(str(student_id))
    if student is None:
        return jsonify({"error": "Not Found"}), 404
    else:
        return jsonify(student)


@app.route('/api/student', methods=['POST'])
def post_student():
    student = request.get_json()
    student_id = str(int(max(STUDENTS.keys(), key=int)) + 1)
    STUDENTS[student_id] = student
    return jsonify(STUDENTS[student_id]), 201



@app.route('/api/student/<student_id>', methods=['PUT'])
def put_student(student_id):
    student = request.get_json()

    student_id = str(student_id)

    if student_id not in STUDENTS:
        return "Not Found", 404
    else:
        student_stored = STUDENTS[student_id]
        student_stored["name"] = student.get("name", student_stored["name"])
        student_stored["age"] = student.get("age", student_stored["age"])
        student_stored["spec"] = student.get("spec", student_stored["spec"])
        return jsonify(student_stored), 200


@app.route('/api/student/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    if student_id not in STUDENTS:
        return "Not Found", 404
    else:
        del STUDENTS[student_id]
        return '', 204


if __name__ == '__main__':
    app.run(debug=True)
