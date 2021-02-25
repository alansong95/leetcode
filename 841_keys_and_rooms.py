class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        seen = set([0])
        num_of_rooms = len(rooms)
        queue = [0]
        
        while queue:
            i = queue.pop(0)
            room = rooms[i]
            for key in room:
                if key not in seen:
                    queue.append(key)
            seen.add(i)
        
        return len(rooms) == len(seen)
            
        