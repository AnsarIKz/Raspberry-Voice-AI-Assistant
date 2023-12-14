import threading
import
class MyAssistant(object):
    def __init__(self):
        self._task = threading.Thread(target=self._run_task)

def _run_task(self):
    credentials = aiy.assistant.auth_helpers.get_assistant_credentials()
    with Assistant(credentials) as assistant:
        # Save assistant as self._assistant, so later the button press handler can use
        # it.
        self._assistant = assistant
        for event in assistant.start():
            self._process_event(event)


def _process_event(self, event):

    if event.type == EventType.ON_START_FINISHED:
        # The Google Assistant is ready. Start the button trigger.
        aiy.voicehat.get_button().on_press(self._on_button_pressed)