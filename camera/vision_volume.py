import copy


class VolumeFilter:
    def __init__(self, solids, faces):
        self.solids = copy.deepcopy(solids)
        self.faces = copy.deepcopy(faces)

    def filter_solids(self):
        offset = 0
        for i in range(len(self.solids)):
            current = i - offset
            solid = self.solids[current]
            if not self.solid_in_volume(solid):
                self.solids.pop(current)
                self.faces.pop(current)
                offset += 1
        return self.solids, self.faces

    def solid_in_volume(self, solid):
        outside_x = [x for x in solid[0] if x < 0]
        outside_y = [y for y in solid[1] if y > 0]
        outside_z = [z for z in solid[2] if z > 0]
        length = len(outside_z) + len(outside_y) + len(outside_x)

        if length > 0:
            return False
        return True
