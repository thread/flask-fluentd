from Queue import Empty, Queue

from flask import current_app, request
from fluent import sender

# Find the stack on which we want to store the database connection.
# Starting with Flask 0.9, the _app_ctx_stack is the correct one,
# before that we need to use the _request_ctx_stack.
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack

class Fluentd(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)
            # Send events after every request finishes
            app.after_request(self.send_events)

        # Unbounded queue for sent events
        self.queue = Queue()
        tag_label = app.config.get('EVENT_TAG_PREFIX', 'flask.fluentd')
        self._sender = sender.FluentSender(tag_label)

    def init_app(self, app):
        # Use the newstyle teardown_appcontext if it's available,
        # otherwise fall back to the request context
        if hasattr(app, 'teardown_appcontext'):
            app.teardown_appcontext(self.send_events)
        else:
            app.teardown_request(self.send_events)

    def event(self, pair):
        tag, evt = pair
        self.queue.put((tag, evt))

    def send_events(self, exception):
        """
        Makes a best-effort to send all the events that it pushed during a
        request but capable of missing some
        """
        pumping = True
        while pumping:
            try:
                tag, evt = self.queue.get()
                self._sender.emit(tag, evt)
                self.queue.task_done()
            except Empty:
                pumping = False
