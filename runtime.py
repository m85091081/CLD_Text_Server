#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 0muMDAU Server
from view import app
from conf import setting
from flask import session
from flask_socketio import SocketIO, emit, join_room, leave_room
socketio = SocketIO(app, async_mode='eventlet')

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


if __name__ == '__main__':
    socketio.run(app, debug=setting.debug, host=setting.host, port=setting.port)
