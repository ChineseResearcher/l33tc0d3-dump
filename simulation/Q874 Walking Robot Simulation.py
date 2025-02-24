# simulation - medium
class Solution:
    def checkIfBlocked(self, body_position, curr_location, distance_to_travel):
        if body_position in [0, 2]:
            for i in range(1, distance_to_travel+1):
                sim_location = [curr_location[0], curr_location[1]+i if body_position == 0 else curr_location[1]-i]
                if tuple(sim_location) in self.obstacles: # O(1) check in hashset
                    return (True, sim_location)

        if body_position in [1, 3]:
            for i in range(1, distance_to_travel+1):
                sim_location = [curr_location[0]+i if body_position == 1 else curr_location[0]-i, curr_location[1]]
                if tuple(sim_location) in self.obstacles:
                    return (True, sim_location)

        return (False, [])

    def robotSim(self, commands, obstacles):
        self.obstacles = set(tuple(obs) for obs in obstacles) 
        normal_offset = [[1,1], [0,1], [1,-1], [0,-1]]
        obstacle_offset = [[1,-1], [0,-1], [1,1], [0,1]]

        body_position = 0 # north-facing
        curr_location = [0,0]
        getSquaredEuc = lambda coord: int(sum(x**2 for x in coord))

        max_euclidean = 0
        for c in commands:
            if c == -1:
                body_position = (body_position + 1) % 4
            elif c == -2:
                body_position = (body_position - 1) % 4
            else:
                block_sim = self.checkIfBlocked(body_position, curr_location, c)
                block_status, block_coord = block_sim[0], block_sim[1]
                
                if block_status:
                    offset_axis = obstacle_offset[body_position][0]
                    offset = obstacle_offset[body_position][1]
                    block_coord[offset_axis] += offset
                    curr_location = block_coord # updating
                else:
                    axis = normal_offset[body_position][0]
                    offset = normal_offset[body_position][1] * c
                    curr_location[axis] += offset

                max_euclidean = max(max_euclidean, getSquaredEuc(curr_location))

        return max_euclidean
    
commands, obstacles = [4,-1,3], []
commands, obstacles = [4,-1,4,-2,4], [[2,4]]
commands, obstacles = [6,-1,-1,6], [[0,0]]

Solution().robotSim(commands, obstacles)