class GeographicService:
    @staticmethod
    def get_all_positions(size=25):
        positions = []
        for x in range(size):
            for y in range(size):
                positions.append((x, y))
        return positions
