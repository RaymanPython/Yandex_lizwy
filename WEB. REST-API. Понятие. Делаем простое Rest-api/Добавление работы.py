import flask
from flask import jsonify
from . import db_session
from .jobs import Job
from flask import request

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Job).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict()
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_one_jobs(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Job).get(job_id)
    if not job:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'job': job.to_dict()
        }
    )


@blueprint.route('/api/job', methods=['POST'])
def create_job():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'name']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    job = Job(
        id=request.json['id'],
        name=request.json['name'],
    )
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})
