from couchpotato.core.logger import CPLog
from couchpotato.core.plugins.base import Plugin

log = CPLog(__name__)


class TVSearcher(Plugin):

    in_progress = False

    def __init__(self):
        pass
