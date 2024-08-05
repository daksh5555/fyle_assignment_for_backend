from flask import jsonify
from marshmallow.exceptions import ValidationError
from core import app
from core.apis.assignments import student_assignments_resources, teacher_assignments_resources, principal_resources
from core.libs import helpers
from core.libs.exceptions import FyleError
from sqlalchemy.exc import IntegrityError, OperationalError
from werkzeug.exceptions import HTTPException
from sqlalchemy import create_engine # Ensure to import create_engine for db connection if use

# Register blueprints on server
app.register_blueprint(student_assignments_resources, url_prefix='/student')
app.register_blueprint(teacher_assignments_resources, url_prefix='/teacher')
app.register_blueprint(principal_resources, url_prefix='/principal')

# Optional: Route to check database connection
# Uncomment if you want to use it
# @app.route('/check_db_connection', methods=['GET'])
# def check_db_connection():
#     try:
#         engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
#         with engine.connect() as connection:
#             return jsonify({
#                 'status': 'success',
#                 'message': 'Database connection successful.'
#             }), 200
#     except OperationalError as e:
#         return jsonify({
#             'status': 'error',
#             'message': f'Database connection failed: {str(e)}'
#         }), 500

@app.errorhandler(Exception)
def handle_error(err):
    if isinstance(err, FyleError):
        return jsonify(
            error=err.__class__.__name__, message=err.message
        ), err.status_code
    elif isinstance(err, ValidationError):
        return jsonify(
            error=err.__class__.__name__, message=err.messages
        ), 400
    elif isinstance(err, IntegrityError):
        return jsonify(
            error=err.__class__.__name__, message=str(err.orig)
        ), 400
    elif isinstance(err, HTTPException):
        return jsonify(
            error=err.__class__.__name__, message=str(err)
        ), err.code

    # Handle unexpected errors
    return jsonify(
        error='InternalServerError', message='An unexpected error occurred.'
    ), 500

if __name__ == '__main__':
    app.run(debug=True)
