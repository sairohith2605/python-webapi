import flask
import uuid

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/ws/rest/v1/payroll/org', methods=['GET'])
def find_org_payroll():
    return flask.jsonify(get_payroll_data())

@app.route('/ws/rest/v1/payroll/staff/add', methods=['POST'])
def add_staff_payroll():
    form_data = flask.request.form
    staff_id = uuid.uuid4()
    existing_payrolld = get_payroll_data()
    existing_payrolld.append({
        'id': staff_id,
        'holderName': form_data.get('staffName'),
        'amount': float(form_data.get('salary')),
        'workTypeInd': form_data.get('workType')
    })
    return flask.jsonify(existing_payrolld)

def get_payroll_data():
    payroll_data = [
        {
            'id': '7d069aa1-79ff-4c84-9a20-21424b83607d',
            'holderName': 'Sam J. Curlings',
            'amount': 10000.00,
            'workTypeInd': 'r'
        },
        {
            'id': '2d4395fe-3268-4c40-afdc-3287581da9e6',
            'holderName': 'Charlie L. Podman',
            'amount': 18900.00,
            'workTypeInd': 'c'
        }
    ]
    return payroll_data

app.run()