# from flask import Blueprint, jsonify
#
# from db import db
#
# main_bp = Blueprint('main_bp', __name__)
#
#
# @main_bp.route('/test_db')
# def test_db():
#     result = db.session.execute(
#         '''
#         SELECT 1
#         '''
#     ).scalar()
#
#     return jsonify(
#         {
#             'result': result,
#         }
#
#     )