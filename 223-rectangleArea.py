class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        area1   = (C - A) * (D - B)
        area2   = (G - E) * (H - F)
        if area1 == 0 or area2 == 0 or A > G or B > H or E > C or B > H:
           overlap = 0
        else:
           overlap = (C - E) * (H - B)
        return area1 + area2 - overlap