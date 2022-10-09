
import heapq


class Solution:
    def minMeetingRooms(self, intervals):
        
        intervals.sort()
        rooms = []
        for i in intervals:
            if rooms and rooms[0] <= i[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, i[1])
        return len(rooms)

if __name__ == '__main__':
    s = Solution()
    print(s.minMeetingRooms([[0, 30],[5, 10],[15, 20]]))
    print(s.minMeetingRooms([[7,10],[2,4]]))
