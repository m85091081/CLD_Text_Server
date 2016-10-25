from flask import session
from flask_socketio import emit, join_room, leave_room
from . import socketio


@socketio.on('joined', namespace='/chat')
def joined(message):
    room = 'bj4'
    join_room(room)
    emit('status', {'msg': str(message['username']) + ' has entered the room.'}, room=room)

@socketio.on('text', namespace='/chat')
def text(message):
    room = 'bj4'
    emit('message', {'msg': str(message['username']) + ':' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    room = 'bj4'
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)


