class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda point: point[0])
        m = -1
        n = len(points)
        for i in range(0, n-1):
            dist = abs(points[i][0] - points[i+1][0])
            if dist > m:
                m = dist
        return m