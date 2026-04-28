# Parent class
# All resources share these attributes
class Resource:

    def __init__(self, resource_id, location, max_capacity):
        self._resource_id = resource_id
        self._location = location
        self._max_capacity = max_capacity

    # Get method 
    def get_id(self):
        return self._resource_id

    def get_capacity(self):
        return self._max_capacity

    def display_details(self):
        return f"Resource {self._resource_id} at {self._location} (Capacity: {self._max_capacity})"


# LabSpace class inherits from Resource
class LabSpace(Resource):

    def __init__(self, resource_id, location, max_capacity, num_pcs, os_type):

        # Call the parent constructor
        super().__init__(resource_id, location, max_capacity)

        # Extra attributes specific to LabSpace
        self.num_pcs = num_pcs
        self.os_type = os_type

    # This overrides the parent method
    def display_details(self):
        return f"Lab {self._resource_id} | PCs: {self.num_pcs} | OS: {self.os_type}"


# MeetingRoom class inherits from Resource
class MeetingRoom(Resource):

    def __init__(self, resource_id, location, max_capacity, projector, layout):

        # Call the parent constructor
        super().__init__(resource_id, location, max_capacity)

        # Extra attributes for meeting rooms
        self.projector = projector
        self.layout = layout

    # polymorphism
    def display_details(self):
        return f"Meeting Room {self._resource_id} | Projector: {self.projector} | Layout: {self.layout}"