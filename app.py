from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = [
    {
        'id' : 1,
        'title' : u'Do Homework',
        'description' : u'All school subject remaining HW',
        'done' : False
    },
    {
        'id' : 2,
        'title' : u'Exam Preparation',
        'description' : u'Revision',
        'done' : False
    },
]

@app.route('/')

def getData():
    return jsonify({
        'data' : tasks
    })

@app.route('/add-data', methods=['POST'])

def addTask():
    if not request.json:
        return jsonify({
            'status' : 'Error',
            'message' : 'Data not provided'
        })
    task = {
        'id' : tasks[-1]['id'] + 1,
        'title' : request.json['title'],
        'description' : request.json.get('description'),
        'done' : False
    }

    tasks.append(task)
    return jsonify({
            'status' : 'Successful',
            'message' : 'Task added successfully'
        })

if __name__ == '__main__':
    app.run(debug = True)