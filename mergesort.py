"""MergeSort functions"""

# Landon Lamie
# CIS 226
# 11/1/24

# Imported from demonstrations in class

class MergeSort:
    """Merge Sort Class"""
    def __init__(self):
        self._aux = []

    # Main entry point to sort
    def sort(self, iterable):
        """Sort method"""
        self._aux = [None for i in range(len(iterable))]
        self._sort(iterable, 0, len(iterable) - 1)

    def _sort(self, iterable, lo, hi):
        """Recursive sort method"""
        if hi <= lo:
            return
        mid = lo + int((hi - lo) / 2)
        self._sort(iterable, lo, mid)
        self._sort(iterable, mid + 1, hi)
        self._merge(iterable, lo, mid, hi)

    def _merge(self, iterable, lo, mid, hi):
        """Merge method"""
        # Copy to aux[]
        for k in range(lo, hi + 1):
            self._aux[k] = iterable[k]

        # Merge back to iterable[]
        i = lo
        j = mid+1
        for k in range(lo, hi + 1):
            if i > mid: # Index past left subarray max index
                iterable[k] = self._aux[j]
                j += 1
            elif j > hi: # index past right subarray max index
                iterable[k] = self._aux[i]
                i += 1
            elif self._aux[j] < self._aux[i]:  # compare
                iterable[k] = self._aux[j]
                j += 1
            else:
                iterable[k] = self._aux[i]
                i += 1
        return