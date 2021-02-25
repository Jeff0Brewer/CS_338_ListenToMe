from functions import *

commands = {
    'toggle my hand': toggle_hand,
    'toggle full screen': toggle_fullscreen,
    'unmute me': unmute,
    'mute me': mute,
    'start my video': start_video,
    'stop my video': stop_video,
    'share my screen': start_share,
    'stop sharing my screen': stop_share,
    'open the chat': open_chat,
    'close the chat': close_chat,
    'send this message': send_chat,
    'stop listening': quit
}

main_commands = commands.copy()

