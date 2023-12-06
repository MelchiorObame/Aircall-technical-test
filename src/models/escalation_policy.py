

from src.models.target import Target


class EscalationPolicy:
    def __init__(self, service_id: str, levels: dict[int, set[Target]] = None):
        """
        Initialize an EscalationPolicy object with a service ID and a dictionary of levels.
        Each level maps to a set of Target objects, ensuring uniqueness.
        :param service_id: String representing the service ID.
        :param levels: Dictionary mapping integer levels to sets of Target objects.
        """
        self._service_id = service_id
        self._levels = levels if levels is not None else {}


    @property
    def service_id(self):
        return self._service_id


    def get_targets_by_level(self, level: int) ->set[Target]:
        return self._levels.get(level, set())


    def add_target(self, level: int, target: Target):
        """
        Add a target to a specific level. Creates the level if it does not exist.
        :param level: Integer representing the level.
        :param target: Target object to be added.
        """
        if level not in self._levels:
            self._levels[level] = set()
        self._levels[level].add(target)


    def remove_target(self, level: int, target: Target):
        """
        Remove a target from a specific level.
        :param level: Integer representing the level.
        :param target: Target object to be removed.
        """
        if level in self._levels and target in self._levels[level]:
            self._levels[level].remove(target)
            if not self._levels[level]:
                del self._levels[level]


    def remove_level(self, level: int):
        """
        Remove a specific level and its targets.
        :param level: Integer representing the level to be removed.
        """
        self._levels.pop(level, None)
