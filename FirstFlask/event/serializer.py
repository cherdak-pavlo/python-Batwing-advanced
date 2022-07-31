from marshmallow import Schema, fields

from user.serializer import UserSerializer


class EventSerializer(Schema):
    id = fields.Integer(required=True, dump_only=True)
    name = fields.String(required=True)
    description = fields.String()
    starts_at = fields.DateTime()
    ends_at = fields.DateTime()
    users = fields.List(fields.Nested(UserSerializer))
    creator_id = fields.Integer()


class InvitationSerializer(Schema):
    user_id = fields.Integer(required=True)
    event_id = fields.Integer(required=True)
    invitation_status = fields.String()


class RespondSerializer(Schema):
    event_respond = fields.String(required=True)


class EventInvitationSerializer(Schema):
    users_id = fields.List(fields.Integer)


class EventIDSerializer(Schema):
    id = fields.Integer(dump_only=True)
