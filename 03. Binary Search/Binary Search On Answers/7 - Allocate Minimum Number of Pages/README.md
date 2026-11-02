## Allocate Minimum Number of Pages

### Problem

There are n books with their page counts stored in an array arr. You need to allocate these books to m students so that each student gets a contiguous segment of books and each student must be assigned at least one book. The goal is to minimize the maximum number of pages assigned to a student.

### Examples

- Example 1:

  - Input: arr = [12, 34, 67, 90], m = 2
  - Output: 113

- Example 2:

  - Input: arr = [10, 20, 30, 40], m = 2
  - Output: 60

### Constraints

- 1 <= n <= 10^5
- 1 <= arr[i] <= 10^9
- 1 <= m <= n
