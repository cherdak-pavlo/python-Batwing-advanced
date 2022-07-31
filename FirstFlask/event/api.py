import marshmallow.exceptions
from flask import Blueprint, request, jsonify
from sqlalchemy import create_engine

from config import Config
from core.database import db
from core.models.user import User
from core.models.event import Event
from core.models.user_event import UserEvent
from event.serializer import EventSerializer, EventInvitationSerializer, EventIDSerializer, InvitationSerializer, \
    RespondSerializer

from core.auth import token_required

event_router = Blueprint("event", __name__, url_prefix="/event")


@event_router.route("")
@token_required
def get(user):
    schema = EventSerializer(many=True)
    events = Event.query.filter(Event.users.any(User.id == user.id))
    event_json = schema.dump(events)
    return jsonify(event_json)


@event_router.route("", methods=["POST"])
@token_required
def create(user):
    data = request.get_json()
    schema = EventSerializer()

    try:
        event_data = schema.load(data)
        event_obj = Event(name=event_data["name"],
                          description=event_data["description"],
                          starts_at=event_data["starts_at"],
                          ends_at=event_data["ends_at"],
                          creator_id=user.id)
        event_obj.users.append(user)
    except marshmallow.exceptions.ValidationError as message:
        return {"error": f"{message}"}

    db.session.add(event_obj)
    db.session.commit()
    event_json = EventSerializer().dump(event_obj)
    return event_json


@event_router.route("/<int:event_id>")
@token_required
def retrieve(user, event_id):
    schema = EventSerializer()
    if events := Event.query.filter(Event.users.any(User.id == user.id)).filter(Event.id == event_id).first():
        event_json = schema.dump(events)
        return jsonify(event_json)
    else:
        schema = EventIDSerializer()
        events_id = Event.query.filter(Event.users.any(User.id == user.id))
        event_json = schema.dump(events_id, many=True)
        return f"No event with this ID. You have events with these IDs: {event_json}", 400


@event_router.route("/<int:event_id>/invite", methods=["POST"])
@token_required
def invite(user, event_id):
    data = request.get_json()
    invitation_schema = EventInvitationSerializer()
    invitation_data = invitation_schema.load(data)
    if event := Event.query.filter(Event.users.any(User.id == user.id)).filter(Event.id == event_id,
                                                                               Event.creator_id == user.id).first():
        for user_id in invitation_data["users_id"]:
            invited_user = User.query.get(user_id)
            if invited_user:
                event.users.append(invited_user)
    else:
        return "You are not creator of this event", 401

    db.session.add(event)
    db.session.commit()
    event_json = EventSerializer().dump(event)

    for user_id in invitation_data["users_id"]:
        engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=False)
        engine.execute(
            f"UPDATE user_event SET invitation_status = 'pending' WHERE user_event.event_id = {event_json['id']}"
            f"AND user_event.user_id = {user_id}")
    return event_json


@event_router.route("/invitation", methods=["GET"])
@token_required
def invitation(user):
    schema = InvitationSerializer(many=True)
    events = UserEvent.query.filter(UserEvent.invitation_status == 'pending', UserEvent.user_id == user.id)
    events_json = schema.dump(events)
    return jsonify(events_json)


@event_router.route("/invitation/respond/<int:event_id>", methods=["POST"])
@token_required
def respond(user, event_id):
    data = request.get_json()
    schema = RespondSerializer()
    data_json = schema.load(data)
    if not UserEvent.query.filter(UserEvent.event_id == event_id, UserEvent.user_id == user.id).first():
        return {'error': 'No event found'}, 400

    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=False)

    if data_json['event_respond'] == 'accept':
        engine.execute(f"UPDATE user_event SET invitation_status = 'accepted' WHERE user_event.event_id = {event_id}"
                       f"AND user_event.user_id = {user.id}")
    elif data_json['event_respond'] == 'declined':
        engine.execute(f"UPDATE user_event SET invitation_status = 'decline' WHERE user_event.event_id = {event_id}"
                       f"AND user_event.user_id = {user.id}")
    else:
        return {"error": "Wrong command. Use 'accept or decline"}, 400

    db.session.commit()
    event = UserEvent.query.filter(UserEvent.event_id == event_id, UserEvent.user_id == user.id)
    events_json = InvitationSerializer(many=True).dump(event)
    return jsonify(events_json)


@event_router.route('/<int:event_id>', methods=["DELETE"])
@token_required
def delete(user, event_id):
    if Event.query.filter(Event.id == event_id, Event.creator_id == user.id).first():
        UserEvent.query.filter(UserEvent.event_id == event_id).delete()
        Event.query.filter(Event.id == event_id).delete()

        db.session.commit()
        return {'Success': 'The event was deleted'}
    else:
        return {'error': 'You are not a creator or event is not found'}, 401


@event_router.route('/<int:event_id>', methods=['PUT'])
@token_required
def edit(user, event_id):
    data = request.get_json()
    schema = EventSerializer()

    if event := Event.query.filter(Event.id == event_id, Event.creator_id == user.id).filter(
            Event.users.any(User.id == user.id)).first():
        try:
            schema_data = schema.load(data)

            event.name = schema_data["name"]
            event.description = schema_data["description"]
            event.starts_at = schema_data["starts_at"]
            event.ends_at = schema_data["ends_at"]

            db.session.add(event)
            db.session.commit()
            edited_event = schema.dump(event)
            return edited_event
        except marshmallow.exceptions.ValidationError as message:
            return {"error": f'{message}'}, 400
    else:
        return {'error': 'You are not creator'}, 401
