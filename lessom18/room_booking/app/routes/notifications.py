from flask import Blueprint, jsonify, request, render_template
from app.models import db, Notification

notifications_bp = Blueprint('notifications', __name__, url_prefix='/api/notifications')

@notifications_bp.route('/', methods=['GET'])
def get_notifications():
    """Pobierz listę powiadomień (JSON) z opcjonalnymi filtrami."""
    query = Notification.query
    
    if user_id := request.args.get('user_id', type=int):
        query = query.filter(Notification.user_id == user_id)
        
    if is_read_str := request.args.get('is_read'):
        is_read_val = is_read_str.lower() in ['true', '1', 'yes']
        query = query.filter(Notification.is_read == is_read_val)
        
    notifications = query.order_by(Notification.created_at.desc()).all()
    return jsonify([n.to_dict() for n in notifications])


@notifications_bp.route('/<int:notification_id>/read', methods=['POST'])
def mark_as_read(notification_id):
    """Oznacz powiadomienie o danym ID jako przeczytane (API)."""
    notification = Notification.query.get_or_404(notification_id)
    try:
        notification.is_read = True
        db.session.commit()
        return jsonify({
            'success': True,
            'message': 'Powiadomienie oznaczone jako przeczytane',
            'notification': notification.to_dict()
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500